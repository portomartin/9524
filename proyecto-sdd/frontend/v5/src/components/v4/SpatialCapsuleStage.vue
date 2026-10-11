<script setup>
import { ref, computed, watch } from 'vue'
import {
  Minimize2,
  Coins,
  Plus,
  ShieldAlert,
  Sparkles,
  CheckCircle2,
  Clock,
  Star,
  Trash2,
  Play,
  Check,
  UserPlus,
  LogIn,
  Zap
} from 'lucide-vue-next'
import { useSpatialStore } from '../../stores/spatialStore'
import { useAuthStore } from '../../stores/authStore'
import { usePlatformStore } from '../../stores/platformStore'

const spatialStore = useSpatialStore()
const authStore = useAuthStore()
const platformStore = usePlatformStore()

// --- AUTH CAPSULE STATE ---
const authMode = ref('login') // 'login' | 'register'
const loginEmail = ref('juan@intercambia.org')
const loginPassword = ref('123456')
const regName = ref('')
const regEmail = ref('')
const regPassword = ref('')
const authError = ref('')

function switchAuthMode(mode) {
  authMode.value = mode
  spatialStore.triggerFlash('auth-form-box', mode === 'login' ? '⚡ Modo Ingreso' : '⚡ Modo Registro (+1 Crédito)')
}

async function handleQuickUserAccess(userId) {
  authError.value = ''
  await authStore.switchUserQuick(userId)
  await platformStore.refreshAll()
  spatialStore.notify(
    `¡Hola, ${authStore.currentUser?.name}!`,
    `Tenés ${authStore.credits} crédito(s) listo(s) para intercambiar sin salir de esta página.`
  )
  spatialStore.closeCapsule()
}

async function handleLoginSubmit() {
  authError.value = ''
  try {
    await authStore.login(loginEmail.value, loginPassword.value)
    await platformStore.refreshAll()
    spatialStore.notify(`¡Bienvenido de vuelta, ${authStore.currentUser?.name}!`, 'Todo tu espacio ya está activo en el lienzo.')
    spatialStore.closeCapsule()
  } catch (err) {
    authError.value = err.message
    spatialStore.triggerFlash('auth-form-box', '⚡ Revisá los datos ingresados')
  }
}

async function handleRegisterSubmit() {
  authError.value = ''
  if (!regName.value || !regEmail.value || !regPassword.value) {
    authError.value = 'Completá tu nombre, correo y contraseña.'
    spatialStore.triggerFlash('auth-form-box', '⚡ Faltan completar campos')
    return
  }
  try {
    await authStore.register({
      name: regName.value,
      email: regEmail.value,
      password: regPassword.value
    })
    await platformStore.refreshAll()
    spatialStore.notify(
      '¡Cuenta creada + 1 Crédito de Bienvenida!',
      'Ya podés tocar cualquier tarjeta abajo para reservar tu primera sesión.'
    )
    spatialStore.closeCapsule()
  } catch (err) {
    authError.value = err.message
    spatialStore.triggerFlash('auth-form-box', '⚡ Revisá los datos')
  }
}

// --- SESSIONS & AGENDA CAPSULE STATE ---
const sessionsSubTab = ref('sessions') // 'sessions' | 'agenda'
const expandedSessionChatId = ref(null)
const expandedSessionRateId = ref(null)
const chatMessageInput = ref('')
const sessionChatLog = ref({})
const ratingValue = ref(5)
const ratingComment = ref('')

const newSlotDate = ref('2026-10-22')
const newSlotTime = ref('18:00')
const slotError = ref('')

function switchSessionsSubTab(tab) {
  sessionsSubTab.value = tab
  spatialStore.triggerFlash(`sessions-subtab-${tab}`, tab === 'sessions' ? '⚡ Tus Sesiones en Vivo' : '⚡ Tu Agenda de Horarios')
}

function toggleSessionChat(sessionId) {
  if (expandedSessionChatId.value === sessionId) {
    expandedSessionChatId.value = null
  } else {
    expandedSessionChatId.value = sessionId
    spatialStore.triggerFlash(`session-chat-${sessionId}`, '⚡ Canal de chat abierto')
  }
}

function toggleSessionRate(sessionId) {
  if (expandedSessionRateId.value === sessionId) {
    expandedSessionRateId.value = null
  } else {
    expandedSessionRateId.value = sessionId
    spatialStore.triggerFlash(`session-rate-${sessionId}`, '⚡ Panel de calificación abierto')
  }
}

function sendChatMessage(sessionId) {
  if (!chatMessageInput.value.trim()) return
  if (!sessionChatLog.value[sessionId]) {
    sessionChatLog.value[sessionId] = []
  }
  sessionChatLog.value[sessionId].push({
    sender: authStore.currentUser?.name || 'Yo',
    text: chatMessageInput.value.trim(),
    time: 'Ahora'
  })
  chatMessageInput.value = ''
  // Trigger in-panel flash on the chat box and session card!
  spatialStore.triggerFlash(`session-chat-${sessionId}`, '⚡ ¡Mensaje enviado en vivo!')
  spatialStore.notify('💬 Mensaje enviado', 'Tu contraparte ya lo ve en su canal de coordinación.')
}

async function handleConfirmSession(session) {
  try {
    await platformStore.confirmSession(session.id)
    spatialStore.triggerFlash(`session-card-${session.id}`, '⚡ ¡Sesión CONFIRMADA!')
    spatialStore.notify('Sesión confirmada', `Confirmaste el encuentro sobre "${session.topic}".`)
  } catch (err) {
    alert(err.message)
  }
}

function handleStartSession(session) {
  try {
    platformStore.startSession(session.id)
    spatialStore.triggerFlash(`session-card-${session.id}`, '⚡ ¡Sesión EN CURSO ahora!')
    spatialStore.notify('Sesión en curso', `La sesión "${session.topic}" está activa ahora mismo.`)
  } catch (err) {
    alert(err.message)
  }
}

async function handleCompleteSession(session) {
  try {
    await platformStore.completeSession(session.id)
    expandedSessionRateId.value = session.id
    spatialStore.triggerFlash(`session-card-${session.id}`, '⚡ ¡Completada +1 Crédito!')
    spatialStore.notify('¡Intercambio completado! +1 Crédito', 'Sumaste 1 crédito por compartir tu conocimiento. Podés calificar la experiencia ahí mismo.')
  } catch (err) {
    alert(err.message)
  }
}

async function handleCancelSession(session) {
  try {
    await platformStore.cancelSession(session.id, 'Cancelación desde lienzo vivo')
    spatialStore.triggerFlash(`session-card-${session.id}`, '⚡ Sesión cancelada y saldo liberado')
    spatialStore.notify('Sesión cancelada', 'El horario y el crédito fueron liberados.', 'amber')
  } catch (err) {
    alert(err.message)
  }
}

async function handleRateSubmit(session) {
  const isTeacher = session.teacherId === authStore.currentUser?.id
  const toUserId = isTeacher ? session.studentId : session.teacherId
  try {
    await platformStore.submitRating({
      sessionId: session.id,
      toUserId,
      rating: ratingValue.value,
      comment: ratingComment.value || '¡Excelente intercambio 1 a 1!'
    })
    expandedSessionRateId.value = null
    ratingComment.value = ''
    spatialStore.triggerFlash(`session-card-${session.id}`, `⚡ ¡Calificada con ${ratingValue.value} ★!`)
    spatialStore.notify('¡Calificación enviada!', 'Gracias por fortalecer la confianza de la comunidad.')
  } catch (err) {
    alert(err.message)
  }
}

async function handleAddSlot() {
  slotError.value = ''
  try {
    await platformStore.addSlot({
      date: newSlotDate.value,
      startTime: newSlotTime.value
    })
    spatialStore.triggerFlash('agenda-slots-list', `⚡ Nuevo horario: ${newSlotDate.value} · ${newSlotTime.value} hs`)
    spatialStore.notify('Franja horaria agregada', `Disponible el ${newSlotDate.value} a las ${newSlotTime.value} hs.`)
  } catch (err) {
    slotError.value = err.message
    spatialStore.triggerFlash('agenda-form-box', '⚡ Horario duplicado o inválido')
  }
}

async function handleDeleteSlot(slotId) {
  await platformStore.deleteSlot(slotId)
  spatialStore.triggerFlash('agenda-slots-list', '⚡ Horario eliminado')
  spatialStore.notify('Franja eliminada', 'Se actualizó tu disponibilidad pública.')
}

// --- PUBLISH CAPSULE STATE ---
const publishType = ref('offer') // 'offer' | 'need'
const pubTitle = ref('')
const pubDesc = ref('')
const pubCategory = ref('Tecnología')
const pubLevel = ref('TODOS')
const pubModality = ref('VIRTUAL')

function switchPublishType(type) {
  publishType.value = type
  spatialStore.triggerFlash('publish-form-box', type === 'offer' ? '⚡ Modo: Quiero Enseñar' : '⚡ Modo: Quiero Aprender')
}

const myOffers = computed(() => {
  if (!authStore.currentUser) return []
  return platformStore.offers.filter(o => o.userId === authStore.currentUser.id)
})

const myNeeds = computed(() => {
  if (!authStore.currentUser) return []
  return platformStore.needs.filter(n => n.userId === authStore.currentUser.id)
})

async function handlePublishSubmit() {
  if (!pubTitle.value.trim() || !pubDesc.value.trim()) {
    spatialStore.triggerFlash('publish-form-box', '⚡ Completá título y descripción')
    return
  }

  if (publishType.value === 'offer') {
    const created = await platformStore.createOffer({
      title: pubTitle.value.trim(),
      description: pubDesc.value.trim(),
      category: pubCategory.value,
      level: pubLevel.value,
      modality: pubModality.value,
      status: 'PUBLICADA'
    })
    pubTitle.value = ''
    pubDesc.value = ''
    spatialStore.triggerFlash('my-publications-list', '⚡ ¡Nueva propuesta agregada!')
    spatialStore.notify('¡Propuesta publicada en vivo!', 'Ya aparece en el tablero y la amplificamos para que la veas.')
    if (created && created.id) {
      spatialStore.expandSpecificItem('offer', created.id, '⚡ ¡Tu nueva propuesta ya está publicada acá!')
    }
  } else {
    const created = await platformStore.createNeed({
      title: pubTitle.value.trim(),
      goal: pubDesc.value.trim(),
      category: pubCategory.value,
      level: pubLevel.value === 'TODOS' ? 'PRINCIPIANTE' : pubLevel.value,
      modality: pubModality.value
    })
    pubTitle.value = ''
    pubDesc.value = ''
    spatialStore.triggerFlash('my-publications-list', '⚡ ¡Nuevo pedido agregado!')
    spatialStore.notify('¡Búsqueda de aprendizaje publicada!', 'La comunidad ya puede ofrecerte mentoría.')
    if (created && created.id) {
      spatialStore.expandSpecificItem('need', created.id, '⚡ ¡Tu búsqueda ya está publicada acá!')
    }
  }
}

function handleDeleteMyOffer(id) {
  platformStore.deleteOffer(id)
  spatialStore.triggerFlash('my-publications-list', '⚡ Publicación eliminada')
}

function handleDeleteMyNeed(id) {
  platformStore.deleteNeed(id)
  spatialStore.triggerFlash('my-publications-list', '⚡ Pedido eliminado')
}

// --- PROFILE CAPSULE STATE ---
const profileName = ref('')
const profileBio = ref('')
const profileTeach = ref('')
const profileLearn = ref('')

watch(
  () => authStore.currentUser,
  (u) => {
    if (u) {
      profileName.value = u.name || ''
      profileBio.value = u.bio || ''
      profileTeach.value = (u.skillsToTeach || []).join(', ')
      profileLearn.value = (u.skillsToLearn || []).join(', ')
    }
  },
  { immediate: true }
)

async function handleSaveProfile() {
  await authStore.updateProfile({
    name: profileName.value,
    bio: profileBio.value,
    skillsToTeach: profileTeach.value.split(',').map(s => s.trim()).filter(Boolean),
    skillsToLearn: profileLearn.value.split(',').map(s => s.trim()).filter(Boolean)
  })
  await platformStore.refreshAll()
  spatialStore.triggerFlash('profile-box', '⚡ ¡Perfil y habilidades actualizados!')
  spatialStore.notify('Perfil actualizado en vivo', 'Tus habilidades y afinidades se recalcularon al instante.')
}

function handleAdminResolve(reportId, action) {
  platformStore.resolveReport(reportId, action)
  spatialStore.triggerFlash(`report-card-${reportId}`, `⚡ Reporte: ${action}`)
  spatialStore.notify('Moderación aplicada', `Estado actualizado a ${action}.`)
}
</script>

<template>
  <div id="spatial-capsule-stage" class="scroll-mt-24">
    <transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-4 scale-[0.98]"
      enter-to-class="opacity-100 translate-y-0 scale-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0 scale-100"
      leave-to-class="opacity-0 -translate-y-3 scale-[0.98]"
    >
      <section
        v-if="spatialStore.activeCapsule"
        class="relative rounded-3xl border border-emerald-500/40 bg-gradient-to-b from-slate-900/95 via-slate-900/98 to-slate-950 p-6 md:p-8 shadow-2xl shadow-emerald-950/50 backdrop-blur-xl mb-8 overflow-hidden"
        :class="spatialStore.flashingKey === 'capsule-stage' ? 'spatial-flash-blink' : ''"
      >
        <!-- Ambient glow -->
        <div class="absolute -top-24 -right-24 w-72 h-72 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute -bottom-24 -left-24 w-72 h-72 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <!-- Top Bar of Expanded Capsule -->
        <div class="flex flex-wrap items-center justify-between gap-4 pb-5 mb-6 border-b border-slate-800 relative z-10">
          <div class="flex items-center gap-2.5">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="text-xs uppercase font-black tracking-wider text-emerald-400">
              Cápsula Interactiva en Vivo · Sin salir del lienzo
            </span>
            <span
              v-if="spatialStore.flashingKey && spatialStore.flashLabel"
              class="px-3 py-0.5 rounded-full bg-amber-400 text-slate-950 text-[11px] font-black animate-bounce shadow-md"
            >
              {{ spatialStore.flashLabel }}
            </span>
          </div>

          <button
            @click="spatialStore.closeCapsule()"
            class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold border border-slate-700 transition-all cursor-pointer"
          >
            <Minimize2 class="w-3.5 h-3.5 text-emerald-400" />
            <span>Achicar cápsula</span>
          </button>
        </div>

        <!-- ========================================================== -->
        <!-- 1. CÁPSULA AUTH (INGRESO / REGISTRO RÁPIDO IN-PLACE)       -->
        <!-- ========================================================== -->
        <div v-if="spatialStore.activeCapsule === 'auth'" class="relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-6 space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/15 text-indigo-300 border border-indigo-500/30 text-xs font-bold">
              <Sparkles class="w-3.5 h-3.5" />
              <span>Acceso Íntimo en 1 Clic</span>
            </div>
            <h2 class="text-2xl sm:text-3xl font-black text-white tracking-tight">
              Sumate sin cambiar de pantalla y recibí <span class="text-emerald-400">1 Crédito de Regalo</span>
            </h2>
            <p class="text-slate-300 text-sm leading-relaxed">
              Elegí un perfil demostrativo con un toque o creá tu usuario ahí mismo. En cuanto entres, esta cápsula se pliega suavemente y seguís exactamente donde estabas.
            </p>

            <!-- Instant 1-Click Demo Profiles -->
            <div class="pt-2">
              <span class="text-[11px] uppercase font-bold tracking-wider text-slate-400 block mb-2.5">
                Entrar en 1 clic con cuenta activa de demostración:
              </span>
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                <button
                  @click="handleQuickUserAccess('usr-1')"
                  class="p-3 rounded-xl bg-slate-800/80 hover:bg-emerald-500/20 border border-slate-700 hover:border-emerald-500/50 text-left transition-all cursor-pointer"
                >
                  <div class="text-xs font-bold text-white">Juan Carlos</div>
                  <div class="text-[11px] text-emerald-400 font-medium">Enseña Vue 3 · ★ 4.9</div>
                </button>
                <button
                  @click="handleQuickUserAccess('usr-2')"
                  class="p-3 rounded-xl bg-slate-800/80 hover:bg-emerald-500/20 border border-slate-700 hover:border-emerald-500/50 text-left transition-all cursor-pointer"
                >
                  <div class="text-xs font-bold text-white">Elena Rostova</div>
                  <div class="text-[11px] text-indigo-300 font-medium">Inglés IT · ★ 4.8</div>
                </button>
                <button
                  @click="handleQuickUserAccess('usr-3')"
                  class="p-3 rounded-xl bg-slate-800/80 hover:bg-emerald-500/20 border border-slate-700 hover:border-emerald-500/50 text-left transition-all cursor-pointer"
                >
                  <div class="text-xs font-bold text-white">Carlos Mendoza</div>
                  <div class="text-[11px] text-amber-300 font-medium">Docker & Linux · ★ 4.6</div>
                </button>
              </div>
            </div>
          </div>

          <div
            class="lg:col-span-6 bg-slate-950/80 border border-slate-800 rounded-2xl p-6 transition-all"
            :class="spatialStore.flashingKey === 'auth-form-box' ? 'spatial-flash-blink' : ''"
          >
            <div class="flex items-center gap-2 mb-5 bg-slate-900 p-1 rounded-xl border border-slate-800">
              <button
                @click="switchAuthMode('login')"
                class="flex-1 py-2 rounded-lg text-xs font-bold transition-all cursor-pointer"
                :class="authMode === 'login' ? 'bg-emerald-500 text-slate-950' : 'text-slate-400 hover:text-white'"
              >
                Iniciar Sesión
              </button>
              <button
                @click="switchAuthMode('register')"
                class="flex-1 py-2 rounded-lg text-xs font-bold transition-all cursor-pointer"
                :class="authMode === 'register' ? 'bg-emerald-500 text-slate-950' : 'text-slate-400 hover:text-white'"
              >
                Crear Cuenta (+1 Crédito)
              </button>
            </div>

            <div v-if="authError" class="mb-4 p-3 rounded-xl bg-rose-500/15 border border-rose-500/30 text-xs text-rose-300">
              {{ authError }}
            </div>

            <form v-if="authMode === 'login'" @submit.prevent="handleLoginSubmit" class="space-y-3.5">
              <div>
                <label class="text-xs font-bold text-slate-300 block mb-1">Correo electrónico</label>
                <input
                  v-model="loginEmail"
                  type="email"
                  class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-sm text-white focus:outline-none focus:border-emerald-500"
                />
              </div>
              <div>
                <label class="text-xs font-bold text-slate-300 block mb-1">Contraseña</label>
                <input
                  v-model="loginPassword"
                  type="password"
                  class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-sm text-white focus:outline-none focus:border-emerald-500"
                />
              </div>
              <button
                type="submit"
                class="w-full py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-sm transition-all cursor-pointer flex items-center justify-center gap-2"
              >
                <LogIn class="w-4 h-4" />
                Entrar Aquí Mismo
              </button>
            </form>

            <form v-else @submit.prevent="handleRegisterSubmit" class="space-y-3.5">
              <div>
                <label class="text-xs font-bold text-slate-300 block mb-1">Tu Nombre</label>
                <input
                  v-model="regName"
                  type="text"
                  placeholder="Ej. Sofía Martínez"
                  class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-sm text-white focus:outline-none focus:border-emerald-500"
                />
              </div>
              <div>
                <label class="text-xs font-bold text-slate-300 block mb-1">Correo electrónico</label>
                <input
                  v-model="regEmail"
                  type="email"
                  placeholder="sofia@ejemplo.com"
                  class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-sm text-white focus:outline-none focus:border-emerald-500"
                />
              </div>
              <div>
                <label class="text-xs font-bold text-slate-300 block mb-1">Contraseña</label>
                <input
                  v-model="regPassword"
                  type="password"
                  placeholder="Mínimo 6 caracteres"
                  class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-sm text-white focus:outline-none focus:border-emerald-500"
                />
              </div>
              <button
                type="submit"
                class="w-full py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-sm transition-all cursor-pointer flex items-center justify-center gap-2"
              >
                <UserPlus class="w-4 h-4" />
                Registrarme y Recibir 1 Crédito
              </button>
            </form>
          </div>
        </div>

        <!-- ========================================================== -->
        <!-- 2. CÁPSULA MIS SESIONES & AGENDA EN VIVO                   -->
        <!-- ========================================================== -->
        <div v-else-if="spatialStore.activeCapsule === 'sessions'" class="relative z-10 space-y-6">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <h2 class="text-2xl font-black text-white tracking-tight">
                Mis Sesiones & Agenda Viva
              </h2>
              <p class="text-xs text-slate-400 mt-0.5">
                Confirmá encuentros, iniciá sesiones, chateá o calificá con estrellas sin salir de esta vista.
              </p>
            </div>

            <div class="flex items-center gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
              <button
                @click="switchSessionsSubTab('sessions')"
                class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer"
                :class="sessionsSubTab === 'sessions' ? 'bg-emerald-500 text-slate-950' : 'text-slate-400 hover:text-white'"
              >
                Sesiones ({{ platformStore.sessions.length }})
              </button>
              <button
                @click="switchSessionsSubTab('agenda')"
                class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer"
                :class="sessionsSubTab === 'agenda' ? 'bg-emerald-500 text-slate-950' : 'text-slate-400 hover:text-white'"
              >
                Mis Horarios Libres ({{ platformStore.slots.length }})
              </button>
            </div>
          </div>

          <!-- Sub-vista: Sesiones -->
          <div
            v-if="sessionsSubTab === 'sessions'"
            :class="spatialStore.flashingKey === 'sessions-subtab-sessions' ? 'spatial-flash-blink rounded-2xl' : ''"
          >
            <div v-if="platformStore.sessions.length === 0" class="rounded-2xl border border-dashed border-slate-800 p-8 text-center">
              <p class="text-sm font-bold text-slate-300">Todavía no tenés sesiones activas</p>
              <p class="text-xs text-slate-400 mt-1">Tocá cualquier tarjeta de propuesta abajo para ampliarla y reservar en 1 clic.</p>
            </div>

            <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div
                v-for="s in platformStore.sessions"
                :key="s.id"
                class="rounded-2xl border border-slate-800 bg-slate-950/80 p-5 flex flex-col justify-between gap-4 hover:border-slate-700 transition-all"
                :class="spatialStore.flashingKey === `session-card-${s.id}` ? 'spatial-flash-blink border-emerald-400' : ''"
              >
                <div>
                  <div class="flex items-center justify-between gap-2 mb-2">
                    <span
                      class="px-2.5 py-0.5 rounded-full text-[11px] font-bold"
                      :class="{
                        'bg-amber-500/15 text-amber-300 border border-amber-500/30': s.status === 'SOLICITADA',
                        'bg-indigo-500/15 text-indigo-300 border border-indigo-500/30': s.status === 'CONFIRMADA',
                        'bg-emerald-500/15 text-emerald-300 border border-emerald-500/30': s.status === 'EN_CURSO' || s.status === 'COMPLETADA',
                        'bg-rose-500/15 text-rose-300 border border-rose-500/30': s.status === 'CANCELADA'
                      }"
                    >
                      {{ s.status }}
                    </span>
                    <span class="text-xs text-slate-400 flex items-center gap-1">
                      <Clock class="w-3.5 h-3.5" /> {{ s.date }} · {{ s.time }} hs
                    </span>
                  </div>

                  <h3 class="text-base font-bold text-white leading-snug">{{ s.topic }}</h3>
                  <p class="text-xs text-slate-400 mt-1">
                    Rol:
                    <strong class="text-slate-200">
                      {{ s.teacherId === authStore.currentUser?.id ? 'Enseñás (Recibís +1 Crédito)' : 'Aprendés (Con ' + s.teacherName + ')' }}
                    </strong>
                  </p>
                </div>

                <!-- Botones de Acción In-Place -->
                <div class="flex flex-wrap items-center gap-2 pt-3 border-t border-slate-800/80">
                  <button
                    v-if="s.status === 'SOLICITADA' && s.teacherId === authStore.currentUser?.id"
                    @click="handleConfirmSession(s)"
                    class="px-3 py-1.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs cursor-pointer flex items-center gap-1"
                  >
                    <Check class="w-3.5 h-3.5" /> Confirmar Pedido
                  </button>

                  <button
                    v-if="s.status === 'CONFIRMADA'"
                    @click="handleStartSession(s)"
                    class="px-3 py-1.5 rounded-xl bg-indigo-500 hover:bg-indigo-400 text-white font-bold text-xs cursor-pointer flex items-center gap-1"
                  >
                    <Play class="w-3.5 h-3.5" /> Iniciar Ahora
                  </button>

                  <button
                    v-if="s.status === 'CONFIRMADA' || s.status === 'EN_CURSO'"
                    @click="handleCompleteSession(s)"
                    class="px-3 py-1.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs cursor-pointer flex items-center gap-1"
                  >
                    <CheckCircle2 class="w-3.5 h-3.5" /> Marcar Completada
                  </button>

                  <button
                    v-if="s.status === 'SOLICITADA' || s.status === 'CONFIRMADA'"
                    @click="handleCancelSession(s)"
                    class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-rose-500/20 text-slate-300 hover:text-rose-300 text-xs font-medium cursor-pointer"
                  >
                    Cancelar
                  </button>

                  <button
                    @click="toggleSessionChat(s.id)"
                    class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold cursor-pointer ml-auto"
                  >
                    {{ expandedSessionChatId === s.id ? 'Cerrar Chat' : '💬 Coordinar' }}
                  </button>

                  <button
                    v-if="s.status === 'COMPLETADA'"
                    @click="toggleSessionRate(s.id)"
                    class="px-3 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/30 text-xs font-bold cursor-pointer"
                  >
                    ★ Calificar
                  </button>
                </div>

                <!-- Sub-acordeón: Chat in-place con Flash al enviar mensaje -->
                <div
                  v-if="expandedSessionChatId === s.id"
                  class="mt-2 p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2.5 transition-all"
                  :class="spatialStore.flashingKey === `session-chat-${s.id}` ? 'spatial-flash-blink border-emerald-400' : ''"
                >
                  <div class="flex items-center justify-between">
                    <span class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Mensajes de coordinación</span>
                    <span
                      v-if="spatialStore.flashingKey === `session-chat-${s.id}`"
                      class="px-2 py-0.5 rounded-full bg-amber-400 text-slate-950 text-[10px] font-black animate-bounce"
                    >
                      {{ spatialStore.flashLabel || '⚡ ¡Mensaje enviado!' }}
                    </span>
                  </div>
                  <div class="space-y-1.5 max-h-36 overflow-y-auto text-xs">
                    <div class="p-2 rounded-lg bg-slate-800/70 text-slate-300">
                      <strong>Sistema:</strong> Canal directo habilitado para coordinar el link o punto de encuentro.
                    </div>
                    <div
                      v-for="(msg, idx) in (sessionChatLog[s.id] || [])"
                      :key="idx"
                      class="p-2.5 rounded-lg bg-emerald-500/20 border border-emerald-500/40 text-emerald-200 flex items-center justify-between"
                    >
                      <span><strong>{{ msg.sender }}:</strong> {{ msg.text }}</span>
                      <span class="text-[10px] text-emerald-400 font-bold ml-2">✓ Enviado</span>
                    </div>
                  </div>
                  <div class="flex gap-2">
                    <input
                      v-model="chatMessageInput"
                      @keyup.enter="sendChatMessage(s.id)"
                      placeholder="Escribí un mensaje rápido..."
                      class="flex-1 px-3 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-xs text-white focus:outline-none focus:border-emerald-500"
                    />
                    <button
                      @click="sendChatMessage(s.id)"
                      class="px-3.5 py-1.5 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs cursor-pointer"
                    >
                      Enviar
                    </button>
                  </div>
                </div>

                <!-- Sub-acordeón: Calificar con estrellas in-place -->
                <div
                  v-if="expandedSessionRateId === s.id"
                  class="mt-2 p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 space-y-3 transition-all"
                  :class="spatialStore.flashingKey === `session-rate-${s.id}` ? 'spatial-flash-blink' : ''"
                >
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-amber-300">Calificá el intercambio (1 a 5 ★)</span>
                    <div class="flex items-center gap-1">
                      <button
                        v-for="star in 5"
                        :key="star"
                        @click="ratingValue = star; spatialStore.triggerFlash(`session-rate-${s.id}`, `⚡ Elegiste ${star} ★`)"
                        class="text-lg cursor-pointer transition-transform hover:scale-125"
                        :class="star <= ratingValue ? 'text-amber-400' : 'text-slate-600'"
                      >
                        ★
                      </button>
                    </div>
                  </div>
                  <input
                    v-model="ratingComment"
                    placeholder="¿Qué fue lo mejor de esta sesión?"
                    class="w-full px-3 py-2 rounded-lg bg-slate-950 border border-slate-700 text-xs text-white"
                  />
                  <button
                    @click="handleRateSubmit(s)"
                    class="w-full py-2 rounded-lg bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs cursor-pointer"
                  >
                    Publicar Calificación Verificada
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Sub-vista: Agenda y Horarios Libres -->
          <div
            v-else
            class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start"
            :class="spatialStore.flashingKey === 'sessions-subtab-agenda' ? 'spatial-flash-blink rounded-2xl' : ''"
          >
            <div
              class="lg:col-span-5 bg-slate-950/80 border border-slate-800 p-5 rounded-2xl space-y-3.5"
              :class="spatialStore.flashingKey === 'agenda-form-box' ? 'spatial-flash-blink' : ''"
            >
              <h3 class="text-sm font-bold text-white">Agregar Franja Horaria de 1 Hora</h3>
              <div v-if="slotError" class="text-xs text-rose-400">{{ slotError }}</div>
              <div class="grid grid-cols-2 gap-3">
                <div>
                  <label class="text-[11px] text-slate-400 block mb-1">Fecha</label>
                  <input v-model="newSlotDate" type="date" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
                </div>
                <div>
                  <label class="text-[11px] text-slate-400 block mb-1">Hora de inicio</label>
                  <input v-model="newSlotTime" type="time" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
                </div>
              </div>
              <button
                @click="handleAddSlot"
                class="w-full py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs cursor-pointer"
              >
                + Sumar Horario Disponible
              </button>
            </div>

            <div
              class="lg:col-span-7 flex flex-wrap gap-2.5 p-2 rounded-2xl transition-all"
              :class="spatialStore.flashingKey === 'agenda-slots-list' ? 'spatial-flash-blink bg-emerald-500/10' : ''"
            >
              <div
                v-for="slot in platformStore.slots"
                :key="slot.id"
                class="px-3.5 py-2.5 rounded-xl border border-slate-800 bg-slate-950/80 flex items-center gap-3 text-xs"
              >
                <Clock class="w-3.5 h-3.5 text-emerald-400" />
                <span class="font-bold text-white">{{ slot.date }} · {{ slot.startTime }} hs</span>
                <span class="px-2 py-0.5 rounded-full text-[10px] font-bold" :class="slot.status === 'LIBRE' ? 'bg-emerald-500/15 text-emerald-300' : 'bg-amber-500/15 text-amber-300'">
                  {{ slot.status }}
                </span>
                <button
                  v-if="slot.status === 'LIBRE'"
                  @click="handleDeleteSlot(slot.id)"
                  class="text-slate-500 hover:text-rose-400 cursor-pointer"
                >
                  <Trash2 class="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- ========================================================== -->
        <!-- 3. CÁPSULA PUBLICAR EN 10 SEGUNDOS / MIS PROPUESTAS        -->
        <!-- ========================================================== -->
        <div v-else-if="spatialStore.activeCapsule === 'publish'" class="relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-8">
          <div class="lg:col-span-6 space-y-4">
            <h2 class="text-2xl font-black text-white tracking-tight">
              Publicá en el Lienzo en 10 Segundos
            </h2>
            <p class="text-xs text-slate-400">
              Lo que publiques aparece al instante en el tablero interactivo de abajo sin recargar la página.
            </p>

            <div class="flex gap-2 bg-slate-950 p-1 rounded-xl border border-slate-800">
              <button
                @click="switchPublishType('offer')"
                class="flex-1 py-2 rounded-lg text-xs font-bold transition-all cursor-pointer"
                :class="publishType === 'offer' ? 'bg-emerald-500 text-slate-950' : 'text-slate-400 hover:text-white'"
              >
                📚 Quiero Enseñar (Oferta)
              </button>
              <button
                @click="switchPublishType('need')"
                class="flex-1 py-2 rounded-lg text-xs font-bold transition-all cursor-pointer"
                :class="publishType === 'need' ? 'bg-indigo-500 text-white' : 'text-slate-400 hover:text-white'"
              >
                🎯 Quiero Aprender (Pedido)
              </button>
            </div>

            <div
              class="space-y-3 bg-slate-950/70 p-5 rounded-2xl border border-slate-800 transition-all"
              :class="spatialStore.flashingKey === 'publish-form-box' ? 'spatial-flash-blink' : ''"
            >
              <div>
                <label class="text-xs font-bold text-slate-300 block mb-1">Título claro y atractivo</label>
                <input
                  v-model="pubTitle"
                  :placeholder="publishType === 'offer' ? 'Ej. Mentoría práctica de Vue 3 desde cero' : 'Ej. Busco practicar conversación en Inglés IT'"
                  class="w-full px-3.5 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-sm text-white focus:outline-none focus:border-emerald-500"
                />
              </div>
              <div class="grid grid-cols-2 gap-3">
                <div>
                  <label class="text-xs font-bold text-slate-300 block mb-1">Categoría</label>
                  <select v-model="pubCategory" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white">
                    <option value="Tecnología">Tecnología</option>
                    <option value="Programación">Programación</option>
                    <option value="Idiomas">Idiomas</option>
                    <option value="Diseño">Diseño</option>
                    <option value="Infraestructura">Infraestructura</option>
                    <option value="Habilidades">Habilidades</option>
                  </select>
                </div>
                <div>
                  <label class="text-xs font-bold text-slate-300 block mb-1">Modalidad</label>
                  <select v-model="pubModality" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white">
                    <option value="VIRTUAL">Virtual</option>
                    <option value="PRESENCIAL">Presencial</option>
                    <option value="HIBRIDA">Híbrida</option>
                  </select>
                </div>
              </div>
              <div>
                <label class="text-xs font-bold text-slate-300 block mb-1">
                  {{ publishType === 'offer' ? '¿Qué van a lograr en 1 hora con vos?' : '¿Cuál es tu objetivo de aprendizaje?' }}
                </label>
                <textarea
                  v-model="pubDesc"
                  rows="3"
                  placeholder="Contalo de forma cercana y concreta..."
                  class="w-full px-3.5 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white focus:outline-none focus:border-emerald-500"
                ></textarea>
              </div>
              <button
                @click="handlePublishSubmit"
                class="w-full py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-sm cursor-pointer transition-all"
              >
                + Publicar y Amplificar en el Lienzo
              </button>
            </div>
          </div>

          <div
            class="lg:col-span-6 space-y-4 p-3 rounded-2xl transition-all"
            :class="spatialStore.flashingKey === 'my-publications-list' ? 'spatial-flash-blink bg-emerald-500/10' : ''"
          >
            <h3 class="text-sm font-bold text-slate-300 uppercase tracking-wider">
              Tus Publicaciones Activas ({{ myOffers.length + myNeeds.length }})
            </h3>
            <div class="space-y-2.5 max-h-80 overflow-y-auto pr-1">
              <div
                v-for="o in myOffers"
                :key="o.id"
                class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 flex items-center justify-between gap-3"
              >
                <div>
                  <span class="text-[10px] font-bold uppercase text-emerald-400">Enseñás · {{ o.category }}</span>
                  <div class="text-xs font-bold text-white">{{ o.title }}</div>
                </div>
                <div class="flex items-center gap-2">
                  <button
                    @click="spatialStore.expandSpecificItem('offer', o.id)"
                    class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-[11px] text-emerald-300 font-semibold cursor-pointer"
                  >
                    Ver en Lienzo
                  </button>
                  <button
                    @click="handleDeleteMyOffer(o.id)"
                    class="p-1.5 rounded-lg bg-slate-900 hover:bg-rose-500/20 text-slate-400 hover:text-rose-400 cursor-pointer"
                  >
                    <Trash2 class="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>

              <div
                v-for="n in myNeeds"
                :key="n.id"
                class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 flex items-center justify-between gap-3"
              >
                <div>
                  <span class="text-[10px] font-bold uppercase text-indigo-400">Buscás aprender · {{ n.category }}</span>
                  <div class="text-xs font-bold text-white">{{ n.title }}</div>
                </div>
                <div class="flex items-center gap-2">
                  <button
                    @click="spatialStore.expandSpecificItem('need', n.id)"
                    class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-[11px] text-indigo-300 font-semibold cursor-pointer"
                  >
                    Ver en Lienzo
                  </button>
                  <button
                    @click="handleDeleteMyNeed(n.id)"
                    class="p-1.5 rounded-lg bg-slate-900 hover:bg-rose-500/20 text-slate-400 hover:text-rose-400 cursor-pointer"
                  >
                    <Trash2 class="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ========================================================== -->
        <!-- 4. CÁPSULA CRÉDITOS & ECONOMÍA DE TIEMPO                   -->
        <!-- ========================================================== -->
        <div v-else-if="spatialStore.activeCapsule === 'credits'" class="relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-5 bg-gradient-to-br from-amber-500/15 via-slate-900 to-slate-950 border border-amber-500/30 p-6 rounded-2xl space-y-3">
            <div class="inline-flex items-center gap-1.5 text-amber-400 text-xs font-bold uppercase tracking-wider">
              <Coins class="w-4 h-4" /> Balance Interno de Tiempo
            </div>
            <div class="text-4xl font-black text-white">
              {{ authStore.credits }} <span class="text-xl text-amber-400 font-bold">Crédito(s)</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              Cada crédito equivale exactamente a <strong>1 hora de aprendizaje</strong>. No son dinero, no se compran ni se venden: se ganan compartiendo lo que sabés con otra persona de la comunidad.
            </p>
          </div>

          <div class="lg:col-span-7 space-y-3">
            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Historial de Movimientos en Vivo</h3>
            <div v-if="platformStore.creditMovements.length === 0" class="text-xs text-slate-400 p-4 rounded-xl bg-slate-950/60 border border-slate-800">
              Aún no tenés movimientos adicionales registrados.
            </div>
            <div v-else class="space-y-2 max-h-60 overflow-y-auto pr-1">
              <div
                v-for="mov in platformStore.creditMovements"
                :key="mov.id"
                class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800 flex items-center justify-between text-xs"
              >
                <div>
                  <div class="font-bold text-white">{{ mov.description || mov.reason || 'Movimiento de crédito de sesión' }}</div>
                  <div class="text-[11px] text-slate-400">{{ mov.date || mov.created_at || 'Reciente' }}</div>
                </div>
                <span
                  class="px-2.5 py-1 rounded-full font-black"
                  :class="(mov.amount > 0) ? 'bg-emerald-500/15 text-emerald-400' : 'bg-amber-500/15 text-amber-300'"
                >
                  {{ mov.amount > 0 ? `+${mov.amount}` : mov.amount }} Crédito
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- ========================================================== -->
        <!-- 5. CÁPSULA MI PERFIL & AFINIDADES                          -->
        <!-- ========================================================== -->
        <div v-else-if="spatialStore.activeCapsule === 'profile'" class="relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-8">
          <div class="lg:col-span-5 space-y-3">
            <h2 class="text-2xl font-black text-white">{{ authStore.currentUser?.name }}</h2>
            <p class="text-xs text-slate-400">{{ authStore.currentUser?.email }}</p>
            <div class="flex items-center gap-2 text-amber-400 font-bold text-sm">
              <Star class="w-4 h-4 fill-amber-400" />
              <span>{{ authStore.currentUser?.reputationScore || 5.0 }} Reputación Comunitaria</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed pt-2">
              Actualizá tus intereses acá mismo y el lienzo recalculará tus matches recíprocos sin cambiar de página.
            </p>
          </div>

          <div
            class="lg:col-span-7 space-y-3 bg-slate-950/80 p-5 rounded-2xl border border-slate-800 transition-all"
            :class="spatialStore.flashingKey === 'profile-box' ? 'spatial-flash-blink border-emerald-400' : ''"
          >
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label class="text-xs font-bold text-slate-300 block mb-1">Nombre visible</label>
                <input v-model="profileName" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
              </div>
              <div>
                <label class="text-xs font-bold text-slate-300 block mb-1">Bio corta</label>
                <input v-model="profileBio" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
              </div>
            </div>
            <div>
              <label class="text-xs font-bold text-emerald-400 block mb-1">Habilidades que puedo enseñar (separadas por coma)</label>
              <input v-model="profileTeach" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
            </div>
            <div>
              <label class="text-xs font-bold text-indigo-400 block mb-1">Habilidades que busco aprender (separadas por coma)</label>
              <input v-model="profileLearn" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
            </div>
            <button
              @click="handleSaveProfile"
              class="px-5 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs cursor-pointer"
            >
              Guardar Cambios en Vivo
            </button>
          </div>
        </div>

        <!-- ========================================================== -->
        <!-- 6. CÁPSULA DE MODERACIÓN ADMIN IN-PLACE                    -->
        <!-- ========================================================== -->
        <div v-else-if="spatialStore.activeCapsule === 'admin'" class="relative z-10 space-y-4">
          <h2 class="text-2xl font-black text-white flex items-center gap-2">
            <ShieldAlert class="w-6 h-6 text-rose-400" />
            Moderación Comunitaria en Vivo
          </h2>
          <div v-if="platformStore.reports.length === 0" class="text-xs text-slate-400">
            No hay denuncias registradas.
          </div>
          <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div
              v-for="rep in platformStore.reports"
              :key="rep.id"
              class="p-4 rounded-2xl bg-slate-950/90 border border-slate-800 flex flex-col justify-between gap-3 transition-all"
              :class="spatialStore.flashingKey === `report-card-${rep.id}` ? 'spatial-flash-blink' : ''"
            >
              <div>
                <div class="flex items-center justify-between text-xs mb-1">
                  <span class="font-bold text-rose-400">{{ rep.reason }}</span>
                  <span class="px-2 py-0.5 rounded-full bg-slate-800 text-[10px] font-bold text-slate-300">{{ rep.status }}</span>
                </div>
                <div class="text-sm font-bold text-white">{{ rep.targetTitle }}</div>
                <p class="text-xs text-slate-400 mt-1">{{ rep.details }}</p>
              </div>
              <div v-if="rep.status === 'PENDIENTE'" class="flex gap-2 pt-2 border-t border-slate-800">
                <button
                  @click="handleAdminResolve(rep.id, 'DESESTIMADA')"
                  class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 cursor-pointer"
                >
                  Desestimar
                </button>
                <button
                  @click="handleAdminResolve(rep.id, 'CONTENIDO_OCULTO')"
                  class="px-3 py-1.5 rounded-lg bg-rose-500/20 hover:bg-rose-500/30 text-rose-300 border border-rose-500/30 text-xs font-bold cursor-pointer"
                >
                  Ocultar Publicación
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </transition>
  </div>
</template>
