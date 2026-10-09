<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {
  User,
  BookOpen,
  Compass,
  Calendar,
  MessageSquare,
  Sparkles,
  Coins,
  LayoutDashboard,
  Plus,
  Pencil,
  Trash2,
  Pause,
  Play,
  Clock,
  Lock,
  CheckCircle2,
  XCircle,
  PlayCircle,
  Star,
  Check,
  RefreshCw,
  Zap,
  ArrowRight
} from '@lucide/vue'
import { useAuthStore } from '../stores/authStore'
import { usePlatformStore } from '../stores/platformStore'
import Button from '../components/ui/Button.vue'
import Badge from '../components/ui/Badge.vue'
import Card from '../components/ui/Card.vue'
import Dialog from '../components/ui/Dialog.vue'
import Input from '../components/ui/Input.vue'
import Textarea from '../components/ui/Textarea.vue'
import RatingStars from '../components/ui/RatingStars.vue'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const platformStore = usePlatformStore()

const currentTab = ref(route.query.tab || 'overview')

onMounted(() => {
  platformStore.refreshAll()
})

const currentUser = computed(() => authStore.currentUser)

// Perfil Editable (Subtarea 2.1.2)
const profileForm = ref({
  name: currentUser.value?.name || '',
  bio: currentUser.value?.bio || '',
  level: currentUser.value?.level || 'PRINCIPIANTE',
  modality: currentUser.value?.modality || 'VIRTUAL',
  teachInput: (currentUser.value?.skillsToTeach || []).join(', '),
  learnInput: (currentUser.value?.skillsToLearn || []).join(', '),
  agendaPublic: currentUser.value?.agendaPublic ?? true
})
const profileSaved = ref(false)

function saveProfile() {
  const teachArray = profileForm.value.teachInput
    .split(',')
    .map(s => s.trim())
    .filter(Boolean)
  const learnArray = profileForm.value.learnInput
    .split(',')
    .map(s => s.trim())
    .filter(Boolean)

  authStore.updateProfile({
    name: profileForm.value.name,
    bio: profileForm.value.bio,
    level: profileForm.value.level,
    modality: profileForm.value.modality,
    skillsToTeach: teachArray,
    skillsToLearn: learnArray,
    agendaPublic: profileForm.value.agendaPublic
  })
  platformStore.refreshAll()
  profileSaved.value = true
  setTimeout(() => (profileSaved.value = false), 2000)
}

// Propuestas CRUD (Subtarea 2.2.2)
const showOfferDialog = ref(false)
const editingOfferId = ref(null)
const offerForm = ref({
  title: '',
  description: '',
  category: 'Programación',
  level: 'TODOS',
  modality: 'VIRTUAL',
  status: 'PUBLICADA'
})

function openNewOfferDialog() {
  editingOfferId.value = null
  offerForm.value = {
    title: '',
    description: '',
    category: 'Programación',
    level: 'TODOS',
    modality: 'VIRTUAL',
    status: 'PUBLICADA'
  }
  showOfferDialog.value = true
}

function openEditOfferDialog(offer) {
  editingOfferId.value = offer.id
  offerForm.value = {
    title: offer.title,
    description: offer.description,
    category: offer.category,
    level: offer.level,
    modality: offer.modality,
    status: offer.status
  }
  showOfferDialog.value = true
}

function saveOffer() {
  if (!offerForm.value.title || !offerForm.value.description) {
    alert('Ingresa título y descripción.')
    return
  }
  if (editingOfferId.value) {
    platformStore.updateOffer(editingOfferId.value, offerForm.value)
  } else {
    platformStore.createOffer(offerForm.value)
  }
  showOfferDialog.value = false
}

function deleteOffer(id) {
  if (confirm('¿Eliminar esta propuesta?')) {
    platformStore.deleteOffer(id)
  }
}

// Necesidades CRUD (Subtarea 2.3.2)
const showNeedDialog = ref(false)
const editingNeedId = ref(null)
const needForm = ref({
  title: '',
  goal: '',
  category: 'Programación',
  level: 'PRINCIPIANTE',
  modality: 'VIRTUAL'
})

function openNewNeedDialog() {
  editingNeedId.value = null
  needForm.value = {
    title: '',
    goal: '',
    category: 'Programación',
    level: 'PRINCIPIANTE',
    modality: 'VIRTUAL'
  }
  showNeedDialog.value = true
}

function openEditNeedDialog(need) {
  editingNeedId.value = need.id
  needForm.value = {
    title: need.title,
    goal: need.goal,
    category: need.category,
    level: need.level,
    modality: need.modality
  }
  showNeedDialog.value = true
}

function saveNeed() {
  if (!needForm.value.title || !needForm.value.goal) {
    alert('Ingresa título y objetivo.')
    return
  }
  if (editingNeedId.value) {
    platformStore.updateNeed(editingNeedId.value, needForm.value)
  } else {
    platformStore.createNeed(needForm.value)
  }
  showNeedDialog.value = false
}

function togglePauseNeed(need) {
  const newStatus = need.status === 'ACTIVA' ? 'PAUSADA' : 'ACTIVA'
  platformStore.updateNeed(need.id, { status: newStatus })
}

function deleteNeed(id) {
  if (confirm('¿Eliminar este aprendizaje buscado?')) {
    platformStore.deleteNeed(id)
  }
}

// Agenda y Franjas (Subtareas 4.1.3 & 4.2.3)
const newSlotDate = ref('2026-10-20')
const newSlotTime = ref('10:00')
const slotError = ref('')

function handleAddSingleSlot() {
  slotError.value = ''
  try {
    platformStore.addSlot({
      date: newSlotDate.value,
      startTime: newSlotTime.value
    })
  } catch (err) {
    slotError.value = err.message
  }
}

// Asistente en Lote (sin recurrencia persistida)
const showBatchDialog = ref(false)
const batchStartDate = ref('2026-10-21')
const batchEndDate = ref('2026-10-23')
const batchHour1 = ref(true)
const batchHour2 = ref(true)
const batchHour3 = ref(false)
const batchHour4 = ref(false)

function handleBatchAddSlots() {
  const dates = []
  let current = new Date(batchStartDate.value)
  const end = new Date(batchEndDate.value)

  while (current <= end) {
    dates.push(current.toISOString().split('T')[0])
    current.setDate(current.getDate() + 1)
  }

  const hours = []
  if (batchHour1.value) hours.push('10:00')
  if (batchHour2.value) hours.push('11:00')
  if (batchHour3.value) hours.push('15:00')
  if (batchHour4.value) hours.push('16:00')

  if (hours.length === 0) {
    alert('Selecciona al menos una hora diaria.')
    return
  }

  const added = platformStore.batchAddSlots({ dates, hours })
  alert(`Se agregaron ${added} franjas horarias concretas a tu agenda.`)
  showBatchDialog.value = false
}

// Sesiones y Estados (Subtarea 4.4.5 & 4.5.2)
const sessionFilter = ref('ALL')
const filteredSessions = computed(() => {
  if (sessionFilter.value === 'ALL') return platformStore.sessions
  return platformStore.sessions.filter(s => s.status === sessionFilter.value)
})

function handleConfirmSession(id) {
  platformStore.confirmSession(id)
}

function handleStartSession(id) {
  platformStore.startSession(id)
}

function handleCompleteSession(id) {
  platformStore.completeSession(id)
  alert('¡Sesión finalizada! Créditos transferidos exitosamente. Ahora puedes calificar al participante.')
}

const showCancelDialog = ref(false)
const cancelingSessionId = ref(null)
const cancelReason = ref('')

function openCancelDialog(id) {
  cancelingSessionId.value = id
  cancelReason.value = 'Imprevisto de agenda'
  showCancelDialog.value = true
}

function submitCancelSession() {
  platformStore.cancelSession(cancelingSessionId.value, cancelReason.value)
  showCancelDialog.value = false
}

// Calificación (Subtarea 5.3.3)
const showRatingDialog = ref(false)
const ratingSession = ref(null)
const ratingStars = ref(5)
const ratingComment = ref('')

function openRatingDialog(session) {
  ratingSession.value = session
  ratingStars.value = 5
  ratingComment.value = ''
  showRatingDialog.value = true
}

function submitRating() {
  if (!ratingSession.value) return
  const isTeacher = ratingSession.value.teacherId === currentUser.value.id
  const targetUserId = isTeacher ? ratingSession.value.studentId : ratingSession.value.teacherId

  platformStore.submitRating({
    sessionId: ratingSession.value.id,
    toUserId: targetUserId,
    rating: ratingStars.value,
    comment: ratingComment.value
  })
  showRatingDialog.value = false
  alert('¡Calificación enviada! La reputación del participante fue actualizada.')
}

const myOffers = computed(() => platformStore.offers.filter(o => o.userId === currentUser.value?.id))
const myNeeds = computed(() => platformStore.needs.filter(n => n.userId === currentUser.value?.id))
</script>

<template>
  <div class="max-w-7xl mx-auto flex flex-col gap-8 pb-12">
    <!-- Top Workspace Card -->
    <div class="rounded-3xl border border-border bg-card p-6 md:p-8 shadow-xs flex flex-wrap items-center justify-between gap-6">
      <div>
        <div class="flex items-center gap-2 mb-1">
          <h1 class="text-2xl sm:text-3xl font-black tracking-tight text-foreground">Mi Espacio</h1>
          <Badge variant="secondary">{{ currentUser?.role }}</Badge>
        </div>
        <p class="text-xs text-muted-foreground">
          Hola, <strong>{{ currentUser?.name }}</strong> · Administra tus temas, agenda de disponibilidad y sesiones.
        </p>
      </div>

      <!-- Quick Metrics -->
      <div class="flex items-center gap-3">
        <div class="rounded-2xl border border-border bg-muted/40 p-4 text-center min-w-[120px]">
          <span class="text-[10px] font-bold uppercase tracking-wider text-muted-foreground block">Saldo Interno</span>
          <span class="text-2xl font-black text-foreground block my-0.5">{{ currentUser?.creditBalance }}</span>
          <span class="text-[10px] text-muted-foreground">Créditos (horas)</span>
        </div>

        <div class="rounded-2xl border border-border bg-muted/40 p-4 text-center min-w-[120px]">
          <span class="text-[10px] font-bold uppercase tracking-wider text-muted-foreground block">Reputación</span>
          <div class="flex items-center justify-center gap-1 my-0.5">
            <Star class="h-4 w-4 fill-amber-400 text-amber-400" />
            <span class="text-2xl font-black text-foreground">{{ currentUser?.reputationScore }}</span>
          </div>
          <span class="text-[10px] text-muted-foreground">{{ currentUser?.reviewsCount }} reseñas</span>
        </div>
      </div>
    </div>

    <!-- Shadcn Navigation Tabs -->
    <div class="flex gap-1.5 overflow-x-auto pb-2 border-b border-border">
      <button
        v-for="tab in [
          { key: 'overview', label: 'Resumen', icon: LayoutDashboard },
          { key: 'profile', label: 'Perfil y Temas', icon: User },
          { key: 'offers', label: 'Mis Propuestas', icon: BookOpen },
          { key: 'needs', label: 'Mis Aprendizajes', icon: Compass },
          { key: 'agenda', label: 'Mi Agenda', icon: Calendar },
          { key: 'sessions', label: 'Mis Sesiones', icon: MessageSquare },
          { key: 'compatibilities', label: 'Compatibilidades', icon: Sparkles },
          { key: 'credits', label: 'Créditos e Historial', icon: Coins }
        ]"
        :key="tab.key"
        class="flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all cursor-pointer border border-transparent"
        :class="currentTab === tab.key ? 'bg-primary text-primary-foreground shadow-xs font-bold' : 'bg-muted/60 text-muted-foreground hover:text-foreground hover:bg-muted'"
        @click="currentTab = tab.key"
      >
        <component :is="tab.icon" class="h-3.5 w-3.5" />
        <span>{{ tab.label }}</span>
      </button>
    </div>

    <!-- TAB 1: OVERVIEW -->
    <div v-if="currentTab === 'overview'" class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <Card class="p-6">
        <h2 class="text-base font-bold text-foreground mb-4 flex items-center gap-2">
          <Zap class="h-4 w-4 text-primary" />
          Acciones Rápidas
        </h2>
        <div class="flex flex-col gap-2.5">
          <Button variant="outline" class="justify-start text-xs h-10" @click="currentTab = 'offers'; openNewOfferDialog()">
            <Plus class="h-3.5 w-3.5 mr-2" />
            Publicar nueva propuesta de enseñanza
          </Button>
          <Button variant="outline" class="justify-start text-xs h-10" @click="currentTab = 'needs'; openNewNeedDialog()">
            <Plus class="h-3.5 w-3.5 mr-2 text-amber-500" />
            Publicar qué deseo aprender
          </Button>
          <Button variant="outline" class="justify-start text-xs h-10" @click="currentTab = 'agenda'">
            <Calendar class="h-3.5 w-3.5 mr-2 text-emerald-500" />
            Cargar franjas horarias en mi agenda
          </Button>
          <Button variant="outline" class="justify-start text-xs h-10" @click="currentTab = 'compatibilities'">
            <Sparkles class="h-3.5 w-3.5 mr-2 text-blue-500" />
            Ver sugerencias de compatibilidad
          </Button>
        </div>
      </Card>

      <Card class="p-6">
        <h2 class="text-base font-bold text-foreground mb-4 flex items-center gap-2">
          <Clock class="h-4 w-4 text-blue-500" />
          Sesiones Recientes
        </h2>
        <div v-if="platformStore.sessions.length > 0" class="flex flex-col gap-2.5">
          <div
            v-for="s in platformStore.sessions.slice(0, 3)"
            :key="s.id"
            class="p-3 rounded-xl border border-border/60 bg-muted/20 flex items-center justify-between text-xs"
          >
            <div>
              <span class="font-bold text-foreground block">{{ s.topic }}</span>
              <span class="text-muted-foreground">{{ s.date }} · {{ s.time }} hs · Estado: <strong>{{ s.status }}</strong></span>
            </div>
            <Button variant="ghost" size="sm" @click="currentTab = 'sessions'">Gestionar</Button>
          </div>
        </div>
        <div v-else class="text-center p-8 text-xs text-muted-foreground">
          No tienes sesiones activas registradas.
        </div>
      </Card>
    </div>

    <!-- TAB 2: PERFIL (Subtarea 2.1.2) -->
    <div v-if="currentTab === 'profile'" class="max-w-xl mx-auto w-full">
      <Card class="p-6 sm:p-8">
        <h2 class="text-xl font-bold tracking-tight text-foreground mb-1">Editar Perfil</h2>
        <p class="text-xs text-muted-foreground mb-6">
          Configura tus habilidades y preferencias para que el motor de compatibilidad encuentre mejores coincidencias.
        </p>

        <div v-if="profileSaved" class="rounded-lg bg-emerald-50 border border-emerald-200 p-3 text-xs text-emerald-800 font-medium mb-4 flex items-center gap-2">
          <CheckCircle2 class="h-4 w-4 shrink-0" />
          <span>Perfil actualizado con éxito.</span>
        </div>

        <form @submit.prevent="saveProfile" class="flex flex-col gap-4">
          <div class="flex flex-col gap-1.5">
            <label class="text-xs font-bold text-foreground">Nombre público</label>
            <Input v-model="profileForm.name" />
          </div>

          <div class="flex flex-col gap-1.5">
            <label class="text-xs font-bold text-foreground">Biografía</label>
            <Textarea v-model="profileForm.bio" rows="2" />
          </div>

          <div class="flex flex-col gap-1.5">
            <label class="text-xs font-bold text-foreground">Temas que puedo enseñar (separados por coma)</label>
            <Input v-model="profileForm.teachInput" placeholder="Ej: Vue 3, CSS, Python, Guitarra" />
          </div>

          <div class="flex flex-col gap-1.5">
            <label class="text-xs font-bold text-foreground">Temas que deseo aprender (separados por coma)</label>
            <Input v-model="profileForm.learnInput" placeholder="Ej: Inglés técnico, Docker, Finanzas" />
          </div>

          <div class="grid grid-cols-2 gap-3">
            <div class="flex flex-col gap-1.5">
              <label class="text-xs font-bold text-foreground">Nivel preferido</label>
              <select v-model="profileForm.level" class="h-9 w-full rounded-lg border border-input bg-card px-2 text-xs text-foreground">
                <option value="PRINCIPIANTE">Principiante</option>
                <option value="INTERMEDIO">Intermedio</option>
                <option value="AVANZADO">Avanzado</option>
              </select>
            </div>
            <div class="flex flex-col gap-1.5">
              <label class="text-xs font-bold text-foreground">Modalidad preferida</label>
              <select v-model="profileForm.modality" class="h-9 w-full rounded-lg border border-input bg-card px-2 text-xs text-foreground">
                <option value="VIRTUAL">Virtual</option>
                <option value="PRESENCIAL">Presencial</option>
                <option value="HIBRIDA">Híbrida</option>
              </select>
            </div>
          </div>

          <div class="rounded-xl border border-border bg-muted/40 p-3.5 flex items-center gap-2.5 mt-2">
            <input type="checkbox" id="agendaCheck" v-model="profileForm.agendaPublic" class="h-4 w-4 rounded accent-primary cursor-pointer" />
            <label for="agendaCheck" class="text-xs text-foreground cursor-pointer leading-relaxed">
              <strong>Permitir que otros consulten mi agenda pública</strong> (solo se expondrán horarios libres de 1 hora, sin datos de acuerdos privados).
            </label>
          </div>

          <Button type="submit" class="mt-2">Guardar Cambios</Button>
        </form>
      </Card>
    </div>

    <!-- TAB 3: MIS PROPUESTAS (Subtarea 2.2.2) -->
    <div v-if="currentTab === 'offers'" class="flex flex-col gap-6">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-xl font-bold tracking-tight text-foreground">Mis Propuestas de Enseñanza</h2>
          <p class="text-xs text-muted-foreground">Conocimientos que compartes con la comunidad</p>
        </div>
        <Button size="sm" @click="openNewOfferDialog">
          <Plus class="h-3.5 w-3.5 mr-1" />
          Crear Propuesta
        </Button>
      </div>

      <div v-if="myOffers.length > 0" class="grid grid-cols-1 md:grid-cols-2 gap-5">
        <Card v-for="offer in myOffers" :key="offer.id" class="p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <Badge variant="info">{{ offer.category }}</Badge>
              <Badge :variant="offer.status === 'PUBLICADA' ? 'success' : 'secondary'">{{ offer.status }}</Badge>
            </div>
            <h3 class="text-base font-bold text-foreground mb-2">{{ offer.title }}</h3>
            <p class="text-xs text-muted-foreground line-clamp-3 mb-4 leading-relaxed">{{ offer.description }}</p>
          </div>

          <div class="pt-4 border-t border-border flex items-center justify-end gap-2">
            <Button variant="ghost" size="sm" @click="openEditOfferDialog(offer)">
              <Pencil class="h-3.5 w-3.5 mr-1" />
              Editar
            </Button>
            <Button variant="ghost" size="sm" class="text-destructive hover:bg-destructive/10" @click="deleteOffer(offer.id)">
              <Trash2 class="h-3.5 w-3.5 mr-1" />
              Eliminar
            </Button>
          </div>
        </Card>
      </div>

      <div v-else class="rounded-2xl border border-dashed border-border p-12 text-center text-xs text-muted-foreground">
        No has creado propuestas de enseñanza todavía.
      </div>
    </div>

    <!-- TAB 4: MIS APRENDIZAJES (Subtarea 2.3.2) -->
    <div v-if="currentTab === 'needs'" class="flex flex-col gap-6">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-xl font-bold tracking-tight text-foreground">Mis Aprendizajes Buscados</h2>
          <p class="text-xs text-muted-foreground">Lo que deseas aprender de otros participantes</p>
        </div>
        <Button size="sm" @click="openNewNeedDialog">
          <Plus class="h-3.5 w-3.5 mr-1" />
          Publicar Aprendizaje
        </Button>
      </div>

      <div v-if="myNeeds.length > 0" class="grid grid-cols-1 md:grid-cols-2 gap-5">
        <Card v-for="need in myNeeds" :key="need.id" class="p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <Badge variant="warning">{{ need.category }}</Badge>
              <Badge :variant="need.status === 'ACTIVA' ? 'success' : 'secondary'">{{ need.status }}</Badge>
            </div>
            <h3 class="text-base font-bold text-foreground mb-2">{{ need.title }}</h3>
            <p class="text-xs text-muted-foreground line-clamp-3 mb-4 leading-relaxed">{{ need.goal }}</p>
          </div>

          <div class="pt-4 border-t border-border flex items-center justify-end gap-2">
            <Button variant="ghost" size="sm" @click="togglePauseNeed(need)">
              <component :is="need.status === 'ACTIVA' ? Pause : Play" class="h-3.5 w-3.5 mr-1" />
              {{ need.status === 'ACTIVA' ? 'Pausar' : 'Reactivar' }}
            </Button>
            <Button variant="ghost" size="sm" @click="openEditNeedDialog(need)">
              <Pencil class="h-3.5 w-3.5 mr-1" />
              Editar
            </Button>
            <Button variant="ghost" size="sm" class="text-destructive hover:bg-destructive/10" @click="deleteNeed(need.id)">
              <Trash2 class="h-3.5 w-3.5 mr-1" />
              Eliminar
            </Button>
          </div>
        </Card>
      </div>

      <div v-else class="rounded-2xl border border-dashed border-border p-12 text-center text-xs text-muted-foreground">
        No tienes pedidos de aprendizaje registrados actualmente.
      </div>
    </div>

    <!-- TAB 5: MI AGENDA (Subtareas 4.1.3 & 4.2.3) -->
    <div v-if="currentTab === 'agenda'" class="flex flex-col gap-6">
      <Card class="p-6 sm:p-8">
        <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
          <div>
            <h2 class="text-xl font-bold tracking-tight text-foreground">Mi Agenda de Disponibilidad Concreta</h2>
            <p class="text-xs text-muted-foreground mt-0.5">
              Franjas horarias concretas por fecha y hora (unidad de 1 hora). No existen recurrencias automáticas persistidas.
            </p>
          </div>
          <Button variant="outline" size="sm" @click="showBatchDialog = true">
            <Zap class="h-3.5 w-3.5 mr-1.5" />
            Asistente de Carga Rápida
          </Button>
        </div>

        <!-- Add Single Slot -->
        <div class="rounded-xl border border-border bg-muted/40 p-4 mb-6 flex flex-wrap items-end gap-3">
          <div>
            <label class="text-[11px] font-bold text-muted-foreground uppercase tracking-wider block mb-1">Fecha</label>
            <input type="date" v-model="newSlotDate" class="h-9 rounded-lg border border-input bg-card px-3 text-xs text-foreground" />
          </div>
          <div>
            <label class="text-[11px] font-bold text-muted-foreground uppercase tracking-wider block mb-1">Hora Inicio</label>
            <input type="time" v-model="newSlotTime" class="h-9 rounded-lg border border-input bg-card px-3 text-xs text-foreground" />
          </div>
          <Button size="sm" class="h-9" @click="handleAddSingleSlot">
            <Plus class="h-3.5 w-3.5 mr-1" />
            Agregar Franja (1 hora)
          </Button>
        </div>

        <div v-if="slotError" class="rounded-lg bg-destructive/10 p-3 text-xs text-destructive font-medium mb-4">
          {{ slotError }}
        </div>

        <!-- Slots List -->
        <h3 class="text-xs font-bold uppercase tracking-wider text-muted-foreground mb-3">Mis Franjas Horarias</h3>
        <div v-if="platformStore.slots.length > 0" class="flex flex-col gap-2.5">
          <div
            v-for="slot in platformStore.slots"
            :key="slot.id"
            class="p-3.5 rounded-xl border border-border flex items-center justify-between text-xs"
            :class="slot.isCommitted ? 'bg-amber-50/50 border-amber-200' : 'bg-card'"
          >
            <div class="flex items-center gap-3">
              <component :is="slot.isCommitted ? Lock : Clock" class="h-4 w-4" :class="slot.isCommitted ? 'text-amber-600' : 'text-primary'" />
              <div>
                <span class="font-bold text-foreground block">{{ slot.date }} — {{ slot.startTime }} hs</span>
                <span class="text-muted-foreground text-[11px]">
                  {{ slot.isCommitted ? 'Comprometida con una sesión activa' : 'Libre para reservas' }}
                </span>
              </div>
            </div>

            <Button
              v-if="!slot.isCommitted"
              variant="ghost"
              size="icon"
              class="text-destructive hover:bg-destructive/10"
              @click="platformStore.deleteSlot(slot.id)"
            >
              <Trash2 class="h-4 w-4" />
            </Button>
          </div>
        </div>

        <div v-else class="text-center p-8 text-xs text-muted-foreground">
          No tienes franjas horarias cargadas.
        </div>
      </Card>
    </div>

    <!-- TAB 6: MIS SESIONES (Subtareas 4.4.5 & 4.5.2) -->
    <div v-if="currentTab === 'sessions'" class="flex flex-col gap-6">
      <div class="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 class="text-xl font-bold tracking-tight text-foreground">Ciclo de Vida de Sesiones</h2>
          <p class="text-xs text-muted-foreground">
            Transiciones: Solicitada → Confirmada → En curso → Finalizada / Cancelada
          </p>
        </div>

        <div class="flex items-center gap-1 bg-muted p-1 rounded-xl text-xs font-medium">
          <button
            v-for="st in ['ALL', 'SOLICITADA', 'CONFIRMADA', 'EN_CURSO', 'FINALIZADA', 'CANCELADA']"
            :key="st"
            class="px-2.5 py-1 rounded-lg border-none cursor-pointer transition-colors"
            :class="sessionFilter === st ? 'bg-card text-foreground shadow-xs font-bold' : 'bg-transparent text-muted-foreground'"
            @click="sessionFilter = st"
          >
            {{ st === 'ALL' ? 'Todas' : st }}
          </button>
        </div>
      </div>

      <div v-if="filteredSessions.length > 0" class="flex flex-col gap-4">
        <Card
          v-for="session in filteredSessions"
          :key="session.id"
          class="p-5 flex flex-col justify-between gap-4"
        >
          <div class="flex flex-wrap items-start justify-between gap-3">
            <div>
              <div class="flex items-center gap-2 mb-1.5">
                <Badge
                  :variant="
                    session.status === 'FINALIZADA' ? 'success' :
                    session.status === 'EN_CURSO' ? 'info' :
                    session.status === 'CONFIRMADA' ? 'warning' :
                    session.status === 'CANCELADA' ? 'destructive' : 'secondary'
                  "
                >
                  {{ session.status }}
                </Badge>
                <span class="text-xs font-semibold text-muted-foreground">
                  {{ session.exchangeType === 'CREDITS' ? '1 Crédito' : 'Intercambio Recíproco' }}
                </span>
              </div>
              <h3 class="text-base font-bold text-foreground">{{ session.topic }}</h3>
              <p class="text-xs text-muted-foreground mt-0.5">
                Profesor: <strong>{{ session.teacherName }}</strong> · Alumno: <strong>{{ session.studentName }}</strong>
              </p>
            </div>

            <div class="text-right">
              <span class="text-xs font-bold text-foreground block">{{ session.date }} · {{ session.time }} hs</span>
              <span class="text-[11px] text-muted-foreground">{{ session.durationMinutes }} min · {{ session.modality }}</span>
            </div>
          </div>

          <div v-if="session.status === 'CANCELADA'" class="rounded-lg bg-destructive/10 p-3 text-xs text-destructive">
            <strong>Motivo de cancelación:</strong> {{ session.cancellationReason || 'Cancelada' }}
          </div>

          <!-- Actions Bar according to State -->
          <div class="pt-4 border-t border-border flex flex-wrap items-center justify-between gap-3">
            <!-- Solicitada -->
            <template v-if="session.status === 'SOLICITADA'">
              <span class="text-xs text-muted-foreground">Esperando confirmación del receptor.</span>
              <div class="flex items-center gap-2">
                <Button
                  v-if="session.teacherId === currentUser.id"
                  size="sm"
                  @click="handleConfirmSession(session.id)"
                >
                  <Check class="h-3.5 w-3.5 mr-1" />
                  Confirmar Sesión
                </Button>
                <Button
                  variant="outline"
                  size="sm"
                  class="text-destructive hover:bg-destructive/10"
                  @click="openCancelDialog(session.id)"
                >
                  <XCircle class="h-3.5 w-3.5 mr-1" />
                  Rechazar
                </Button>
              </div>
            </template>

            <!-- Confirmada -->
            <template v-if="session.status === 'CONFIRMADA'">
              <span class="text-xs text-muted-foreground">Sesión acordada. Al llegar la hora, inicia la sesión.</span>
              <div class="flex items-center gap-2">
                <Button size="sm" @click="handleStartSession(session.id)">
                  <PlayCircle class="h-3.5 w-3.5 mr-1" />
                  Iniciar Sesión (En curso)
                </Button>
                <Button
                  variant="outline"
                  size="sm"
                  class="text-destructive hover:bg-destructive/10"
                  @click="openCancelDialog(session.id)"
                >
                  Cancelar
                </Button>
              </div>
            </template>

            <!-- En curso -->
            <template v-if="session.status === 'EN_CURSO'">
              <span class="text-xs text-primary font-semibold flex items-center gap-1.5">
                <RefreshCw class="h-3.5 w-3.5 animate-spin" />
                Sesión en desarrollo actualmente.
              </span>
              <Button size="sm" @click="handleCompleteSession(session.id)">
                <CheckCircle2 class="h-3.5 w-3.5 mr-1" />
                Finalizar Sesión
              </Button>
            </template>

            <!-- Finalizada -->
            <template v-if="session.status === 'FINALIZADA'">
              <span class="text-xs text-emerald-700 font-semibold flex items-center gap-1">
                <CheckCircle2 class="h-3.5 w-3.5 text-emerald-600" />
                Sesión completada y liquidada.
              </span>
              <Button
                v-if="!session.isRated"
                variant="outline"
                size="sm"
                @click="openRatingDialog(session.id)"
              >
                <Star class="h-3.5 w-3.5 mr-1 text-amber-500" />
                Calificar Participante
              </Button>
              <span v-else class="text-xs text-muted-foreground italic">Ya calificada</span>
            </template>
          </div>
        </Card>
      </div>

      <div v-else class="rounded-2xl border border-dashed border-border p-12 text-center text-xs text-muted-foreground">
        No hay sesiones en el estado seleccionado.
      </div>
    </div>

    <!-- TAB 7: COMPATIBILIDADES (Subtarea 3.3.2) -->
    <div v-if="currentTab === 'compatibilities'" class="flex flex-col gap-6">
      <Card class="p-6">
        <h2 class="text-lg font-bold tracking-tight text-foreground mb-1">Cálculo Inteligente de Compatibilidades</h2>
        <p class="text-xs text-muted-foreground">
          Cruzamos lo que puedes enseñar ({{ currentUser?.skillsToTeach.join(', ') || 'sin definir' }})
          con lo que buscas aprender ({{ currentUser?.skillsToLearn.join(', ') || 'sin definir' }}) contra el catálogo de la comunidad.
        </p>
      </Card>

      <div v-if="platformStore.compatibilities.length > 0" class="flex flex-col gap-4">
        <Card
          v-for="match in platformStore.compatibilities"
          :key="match.offer.id"
          class="p-5 flex flex-col md:flex-row items-start md:items-center justify-between gap-4"
        >
          <div class="flex-1">
            <div class="flex items-center gap-2 mb-2">
              <Badge :variant="match.score > 80 ? 'success' : 'info'">
                {{ match.score }}% Compatibilidad
              </Badge>
              <Badge v-if="match.isReciprocal" variant="warning" class="bg-amber-100 text-amber-800 font-bold border-amber-300">
                ¡Reciprocidad Directa!
              </Badge>
            </div>

            <h3 class="text-base font-bold text-foreground mb-1">{{ match.offer.title }}</h3>
            <p class="text-xs text-muted-foreground mb-3">Enseña: {{ match.author?.name }} · {{ match.offer.category }}</p>

            <div class="flex flex-col gap-1">
              <span v-for="(reason, idx) in match.reasons" :key="idx" class="text-xs text-muted-foreground flex items-center gap-1.5">
                <Check class="h-3.5 w-3.5 text-emerald-600 shrink-0" />
                {{ reason }}
              </span>
            </div>
          </div>

          <Button size="sm" @click="router.push({ name: 'offer-detail', params: { id: match.offer.id } })">
            Solicitar Sesión
            <ArrowRight class="h-3.5 w-3.5 ml-1" />
          </Button>
        </Card>
      </div>

      <div v-else class="rounded-2xl border border-dashed border-border p-12 text-center text-xs text-muted-foreground">
        No se encontraron coincidencias directas. Agrega más temas en la pestaña Perfil para mejorar los resultados.
      </div>
    </div>

    <!-- TAB 8: CRÉDITOS E HISTORIAL (Subtareas 5.1.3 & 5.2.2) -->
    <div v-if="currentTab === 'credits'" class="grid grid-cols-1 md:grid-cols-12 gap-6">
      <Card class="p-6 md:col-span-5 flex flex-col justify-between">
        <div>
          <h2 class="text-base font-bold text-foreground mb-4">Balance de Créditos</h2>
          <div class="rounded-2xl border border-border bg-muted/40 p-6 text-center mb-6">
            <span class="text-[11px] font-bold uppercase tracking-wider text-muted-foreground block">Saldo Disponible</span>
            <span class="text-4xl font-black text-foreground block my-1">{{ currentUser?.creditBalance }}</span>
            <span class="text-xs text-muted-foreground">Créditos de Intercambio</span>
          </div>
        </div>

        <div class="rounded-xl border border-blue-200/60 bg-blue-50/50 p-4 text-xs text-blue-900 leading-relaxed">
          <strong>Regla de Producto (MVP V3):</strong> Los créditos son una unidad interna de coordinación.
          <strong>No representan dinero</strong> ni pueden cambiarse por dinero en ningún caso.
        </div>
      </Card>

      <Card class="p-6 md:col-span-7">
        <h2 class="text-base font-bold text-foreground mb-4">Libro de Movimientos de Créditos</h2>

        <div v-if="platformStore.creditMovements.length > 0" class="flex flex-col gap-2.5">
          <div
            v-for="cm in platformStore.creditMovements"
            :key="cm.id"
            class="p-3.5 rounded-xl border border-border/60 bg-muted/20 flex items-center justify-between text-xs"
          >
            <div>
              <span class="font-bold text-foreground block">{{ cm.description }}</span>
              <span class="text-[11px] text-muted-foreground">{{ new Date(cm.date).toLocaleDateString() }} · {{ cm.type }}</span>
            </div>
            <span
              class="font-black px-2 py-0.5 rounded-md text-xs"
              :class="cm.amount > 0 ? 'bg-emerald-100 text-emerald-800' : 'bg-destructive/10 text-destructive'"
            >
              {{ cm.amount > 0 ? `+${cm.amount}` : cm.amount }}
            </span>
          </div>
        </div>
        <div v-else class="text-center p-8 text-xs text-muted-foreground">
          No hay movimientos registrados.
        </div>
      </Card>
    </div>

    <!-- DIALOGS -->

    <!-- Dialog Oferta -->
    <Dialog
      :open="showOfferDialog"
      :title="editingOfferId ? 'Editar Propuesta' : 'Nueva Propuesta de Enseñanza'"
      description="Ingresa los detalles del conocimiento a compartir."
      @update:open="showOfferDialog = $event"
    >
      <div class="flex flex-col gap-3">
        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Título</label>
          <Input v-model="offerForm.title" />
        </div>
        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Descripción detallada</label>
          <Textarea v-model="offerForm.description" rows="3" />
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div class="flex flex-col gap-1.5">
            <label class="text-xs font-bold text-foreground">Categoría</label>
            <select v-model="offerForm.category" class="h-9 w-full rounded-lg border border-input bg-card px-2 text-xs text-foreground">
              <option value="Programación">Programación</option>
              <option value="Idiomas">Idiomas</option>
              <option value="Diseño">Diseño</option>
              <option value="DevOps">DevOps</option>
              <option value="Música">Música</option>
              <option value="Negocios">Negocios</option>
            </select>
          </div>
          <div class="flex flex-col gap-1.5">
            <label class="text-xs font-bold text-foreground">Nivel</label>
            <select v-model="offerForm.level" class="h-9 w-full rounded-lg border border-input bg-card px-2 text-xs text-foreground">
              <option value="TODOS">Todos</option>
              <option value="PRINCIPIANTE">Principiante</option>
              <option value="INTERMEDIO">Intermedio</option>
              <option value="AVANZADO">Avanzado</option>
            </select>
          </div>
        </div>
        <div class="flex justify-end gap-2 pt-2 border-t border-border mt-2">
          <Button variant="ghost" size="sm" @click="showOfferDialog = false">Cancelar</Button>
          <Button size="sm" @click="saveOffer">Guardar</Button>
        </div>
      </div>
    </Dialog>

    <!-- Dialog Necesidad -->
    <Dialog
      :open="showNeedDialog"
      :title="editingNeedId ? 'Editar Aprendizaje' : 'Nuevo Aprendizaje Buscado'"
      description="Describe lo que quieres aprender."
      @update:open="showNeedDialog = $event"
    >
      <div class="flex flex-col gap-3">
        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Título del tema</label>
          <Input v-model="needForm.title" />
        </div>
        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Objetivo de aprendizaje</label>
          <Textarea v-model="needForm.goal" rows="3" />
        </div>
        <div class="flex justify-end gap-2 pt-2 border-t border-border mt-2">
          <Button variant="ghost" size="sm" @click="showNeedDialog = false">Cancelar</Button>
          <Button size="sm" @click="saveNeed">Guardar</Button>
        </div>
      </div>
    </Dialog>

    <!-- Dialog Asistente Carga Múltiple (Subtarea 4.1.3) -->
    <Dialog
      :open="showBatchDialog"
      title="Asistente de Carga Múltiple de Franjas"
      description="Genera múltiples franjas horarias concretas sin persistir recurrencias."
      @update:open="showBatchDialog = $event"
    >
      <div class="flex flex-col gap-4">
        <div class="grid grid-cols-2 gap-3">
          <div class="flex flex-col gap-1.5">
            <label class="text-xs font-bold text-foreground">Desde</label>
            <input type="date" v-model="batchStartDate" class="h-9 rounded-lg border border-input bg-card px-2 text-xs text-foreground" />
          </div>
          <div class="flex flex-col gap-1.5">
            <label class="text-xs font-bold text-foreground">Hasta</label>
            <input type="date" v-model="batchEndDate" class="h-9 rounded-lg border border-input bg-card px-2 text-xs text-foreground" />
          </div>
        </div>

        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Horarios a generar diariamente:</label>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" v-model="batchHour1" class="accent-primary" /> 10:00 a 11:00 hs
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" v-model="batchHour2" class="accent-primary" /> 11:00 a 12:00 hs
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" v-model="batchHour3" class="accent-primary" /> 15:00 a 16:00 hs
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input type="checkbox" v-model="batchHour4" class="accent-primary" /> 16:00 a 17:00 hs
            </label>
          </div>
        </div>

        <div class="flex justify-end gap-2 pt-2 border-t border-border mt-2">
          <Button variant="ghost" size="sm" @click="showBatchDialog = false">Cancelar</Button>
          <Button size="sm" @click="handleBatchAddSlots">Generar Franjas</Button>
        </div>
      </div>
    </Dialog>

    <!-- Dialog Cancelar Sesión -->
    <Dialog
      :open="showCancelDialog"
      title="Cancelar Sesión de Intercambio"
      description="Ingresa el motivo de la cancelación."
      @update:open="showCancelDialog = $event"
    >
      <div class="flex flex-col gap-3">
        <Input v-model="cancelReason" placeholder="Motivo de cancelación..." />
        <div class="flex justify-end gap-2 pt-2 border-t border-border">
          <Button variant="ghost" size="sm" @click="showCancelDialog = false">Volver</Button>
          <Button variant="destructive" size="sm" @click="submitCancelSession">Confirmar Cancelación</Button>
        </div>
      </div>
    </Dialog>

    <!-- Dialog Calificar Sesión (Subtarea 5.3.3) -->
    <Dialog
      :open="showRatingDialog"
      title="Calificar Sesión Realizada"
      description="Evalúa tu experiencia con el participante para la reputación comunitaria."
      @update:open="showRatingDialog = $event"
    >
      <div class="flex flex-col gap-4 text-center">
        <div class="flex justify-center py-2">
          <RatingStars v-model="ratingStars" />
        </div>
        <div class="text-left flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Comentario opcional</label>
          <Textarea v-model="ratingComment" rows="3" placeholder="¿Cómo resultó la sesión de aprendizaje?" />
        </div>
        <div class="flex justify-end gap-2 pt-2 border-t border-border">
          <Button variant="ghost" size="sm" @click="showRatingDialog = false">Omitir</Button>
          <Button size="sm" @click="submitRating">Enviar Calificación</Button>
        </div>
      </div>
    </Dialog>
  </div>
</template>
