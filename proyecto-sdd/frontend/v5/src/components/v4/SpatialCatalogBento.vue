<script setup>
import { ref, computed, watch } from 'vue'
import {
  Search,
  Star,
  Maximize2,
  Minimize2,
  CheckCircle2,
  Coins,
  Flag,
  Send,
  X,
  UserCheck,
  Globe,
  MapPin,
  ArrowLeftRight,
  Zap
} from 'lucide-vue-next'
import { useSpatialStore } from '../../stores/spatialStore'
import { usePlatformStore } from '../../stores/platformStore'
import { useAuthStore } from '../../stores/authStore'
import { mockStorage } from '../../services/mockStorage'

const spatialStore = useSpatialStore()
const platformStore = usePlatformStore()
const authStore = useAuthStore()

const categories = [
  { id: 'TODAS', label: 'Todo', icon: '✨' },
  { id: 'Programación', label: 'Código', icon: '💻' },
  { id: 'Tecnología', label: 'Tech', icon: '⚡' },
  { id: 'Idiomas', label: 'Idiomas', icon: '🗣️' },
  { id: 'Diseño', label: 'Diseño', icon: '🎨' },
  { id: 'Infraestructura', label: 'DevOps', icon: '🐳' }
]

const userAvatars = {
  'usr-1': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=180&auto=format&fit=crop&q=80',
  'usr-2': 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=180&auto=format&fit=crop&q=80',
  'usr-3': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=180&auto=format&fit=crop&q=80',
  'usr-4': 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=180&auto=format&fit=crop&q=80'
}

function getAvatar(userId) {
  return userAvatars[userId] || 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=180&auto=format&fit=crop&q=80'
}

function getCategoryEmoji(cat = '') {
  const c = cat.toLowerCase()
  if (c.includes('idiom')) return '🗣️'
  if (c.includes('diseñ')) return '🎨'
  if (c.includes('infra') || c.includes('devops')) return '🐳'
  if (c.includes('progr') || c.includes('tecno')) return '💻'
  return '🚀'
}

function getAuthor(userId) {
  return mockStorage.findUserById(userId) || {
    name: 'Miembro Activo',
    bio: 'Entusiasta del aprendizaje 1 a 1.',
    reputationScore: 4.9,
    reviewsCount: 8,
    skillsToTeach: ['Mentoría práctica'],
    skillsToLearn: ['Nuevas tecnologías']
  }
}

function getAuthorWantsToLearn(userId) {
  const u = getAuthor(userId)
  if (u.skillsToLearn && u.skillsToLearn.length > 0) {
    return u.skillsToLearn.slice(0, 2).join(' · ')
  }
  const userNeed = platformStore.needs.find(n => n.userId === userId)
  if (userNeed) return userNeed.title
  return 'Abierto a aprender de vos'
}

function getAuthorCanTeach(userId) {
  const u = getAuthor(userId)
  if (u.skillsToTeach && u.skillsToTeach.length > 0) {
    return u.skillsToTeach.slice(0, 2).join(' · ')
  }
  const userOffer = platformStore.offers.find(o => o.userId === userId)
  if (userOffer) return userOffer.title
  return 'Te transfiere +1 Crédito'
}

const filteredOffers = computed(() => {
  if (spatialStore.catalogMode === 'needs') return []
  const q = spatialStore.searchQuery.trim().toLowerCase()
  return platformStore.offers.filter(o => {
    const matchQ =
      !q ||
      o.title.toLowerCase().includes(q) ||
      o.description.toLowerCase().includes(q) ||
      o.category.toLowerCase().includes(q) ||
      (o.userName && o.userName.toLowerCase().includes(q))
    const matchCat =
      spatialStore.selectedCategory === 'TODAS' ||
      o.category.toLowerCase() === spatialStore.selectedCategory.toLowerCase()
    return matchQ && matchCat
  })
})

const filteredNeeds = computed(() => {
  if (spatialStore.catalogMode === 'offers') return []
  const q = spatialStore.searchQuery.trim().toLowerCase()
  return platformStore.needs.filter(n => {
    const matchQ =
      !q ||
      n.title.toLowerCase().includes(q) ||
      n.goal.toLowerCase().includes(q) ||
      n.category.toLowerCase().includes(q) ||
      (n.userName && n.userName.toLowerCase().includes(q))
    const matchCat =
      spatialStore.selectedCategory === 'TODAS' ||
      n.category.toLowerCase() === spatialStore.selectedCategory.toLowerCase()
    return matchQ && matchCat
  })
})

const selectedSlotId = ref('')
const selectedModality = ref('VIRTUAL')
const exchangeType = ref('CREDITS')
const bookingError = ref('')
const bookingSuccess = ref(false)

const teachNeedDate = ref('2026-10-21')
const teachNeedTime = ref('18:00')
const teachNeedSuccess = ref(false)

const showInlineReport = ref(false)
const reportReason = ref('Contenido inapropiado')
const reportDetails = ref('')
const reportSent = ref(false)

function isExpanded(type, id) {
  return (
    spatialStore.expandedItem &&
    spatialStore.expandedItem.type === type &&
    spatialStore.expandedItem.id === id
  )
}

function isCardFlashing(type, id) {
  return (
    spatialStore.flashingKey === `${type}-${id}` ||
    spatialStore.flashingKey === 'catalog-grid'
  )
}

function getFreeSlots(userId) {
  const slots = mockStorage.getPublicUserSlots(userId)
  if (slots && slots.length > 0) return slots
  return [
    { id: `fallback-${userId}-1`, date: '2026-10-20', startTime: '18:00', status: 'LIBRE' },
    { id: `fallback-${userId}-2`, date: '2026-10-22', startTime: '19:00', status: 'LIBRE' }
  ]
}

watch(
  () => spatialStore.expandedItem,
  (item) => {
    bookingError.value = ''
    bookingSuccess.value = false
    teachNeedSuccess.value = false
    showInlineReport.value = false
    reportSent.value = false

    if (item && item.type === 'offer') {
      const offer = platformStore.offers.find(o => o.id === item.id)
      if (offer) {
        selectedModality.value = offer.modality || 'VIRTUAL'
        const slots = getFreeSlots(offer.userId)
        selectedSlotId.value = slots.length > 0 ? slots[0].id : ''
      }
    }
  }
)

async function handleConfirmBookingInPlace(offer) {
  bookingError.value = ''
  if (authStore.isGuest) {
    spatialStore.openCapsule('auth')
    spatialStore.notify('Tocá un usuario arriba para entrar', 'Elegí un perfil en 1 clic y reservá acá mismo.', 'amber')
    return
  }
  if (offer.userId === authStore.currentUser.id) {
    bookingError.value = 'Esta es tu propia propuesta.'
    return
  }
  const slots = getFreeSlots(offer.userId)
  const chosenSlot = slots.find(s => s.id === selectedSlotId.value) || slots[0]

  try {
    await platformStore.requestSession({
      teacherId: offer.userId,
      offerId: offer.id,
      topic: offer.title,
      date: chosenSlot.date,
      time: chosenSlot.startTime,
      modality: selectedModality.value,
      exchangeType: exchangeType.value
    })
    bookingSuccess.value = true
    spatialStore.triggerFlash(`offer-${offer.id}`, '⚡ ¡Reserva confirmada aquí mismo!')
    spatialStore.notify(
      '¡Sesión reservada!',
      `${offer.title} · ${chosenSlot.date} (${chosenSlot.startTime} hs).`
    )
  } catch (err) {
    bookingError.value = err.message
  }
}

async function handleOfferToTeachNeedInPlace(need) {
  bookingError.value = ''
  if (authStore.isGuest) {
    spatialStore.openCapsule('auth')
    spatialStore.notify('Tocá un usuario arriba para entrar', 'Elegí un perfil en 1 clic para ofrecer enseñar.', 'amber')
    return
  }
  if (need.userId === authStore.currentUser.id) {
    bookingError.value = 'Este es tu propio pedido.'
    return
  }
  try {
    await platformStore.requestSession({
      teacherId: authStore.currentUser.id,
      studentId: need.userId,
      offerId: need.id,
      topic: need.title,
      date: teachNeedDate.value,
      time: teachNeedTime.value,
      modality: need.modality || 'VIRTUAL',
      exchangeType: 'CREDITS'
    })
    teachNeedSuccess.value = true
    spatialStore.triggerFlash(`need-${need.id}`, '⚡ ¡Ofrecimiento enviado aquí mismo!')
    spatialStore.notify('¡Mentoría ofrecida!', `Vas a sumar +1 Crédito con ${need.userName}.`)
  } catch (err) {
    bookingError.value = err.message
  }
}

function handleSendInlineReport(targetType, item) {
  platformStore.submitReport({
    targetType,
    targetId: item.id,
    targetTitle: item.title,
    reason: reportReason.value,
    details: reportDetails.value
  })
  reportSent.value = true
  spatialStore.notify('Reporte enviado', 'Moderación revisará el caso.', 'amber')
}
</script>

<template>
  <section id="spatial-catalog-section" class="scroll-mt-24 space-y-6">
    <!-- Barra de Control Unificada -->
    <div
      class="rounded-3xl border border-slate-800 bg-slate-900/80 backdrop-blur-xl p-5 shadow-xl flex flex-col gap-4 transition-all"
      :class="spatialStore.flashingKey === 'catalog-grid' ? 'spatial-flash-blink border-emerald-400' : ''"
    >
      <div class="flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight">
            Personas para Intercambiar
          </h2>
          <span
            v-if="spatialStore.flashingKey === 'catalog-grid' && spatialStore.flashLabel"
            class="px-3 py-1 rounded-full bg-amber-400 text-slate-950 text-xs font-black animate-bounce shadow-lg"
          >
            {{ spatialStore.flashLabel }}
          </span>
        </div>

        <div class="flex items-center gap-1 bg-slate-950 p-1 rounded-2xl border border-slate-800">
          <button
            @click="spatialStore.catalogMode = 'all'; spatialStore.triggerFlash('catalog-grid', '⚡ Mostrando todo')"
            class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer"
            :class="spatialStore.catalogMode === 'all' ? 'bg-emerald-500 text-slate-950' : 'text-slate-400 hover:text-white'"
          >
            Todo ({{ filteredOffers.length + filteredNeeds.length }})
          </button>
          <button
            @click="spatialStore.catalogMode = 'offers'; spatialStore.triggerFlash('catalog-grid', '⚡ Quienes enseñan')"
            class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer"
            :class="spatialStore.catalogMode === 'offers' ? 'bg-emerald-500 text-slate-950' : 'text-slate-400 hover:text-white'"
          >
            🎓 Enseñan ({{ filteredOffers.length }})
          </button>
          <button
            @click="spatialStore.catalogMode = 'needs'; spatialStore.triggerFlash('catalog-grid', '⚡ Quienes buscan')"
            class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer"
            :class="spatialStore.catalogMode === 'needs' ? 'bg-indigo-500 text-white' : 'text-slate-400 hover:text-white'"
          >
            🎯 Buscan ({{ filteredNeeds.length }})
          </button>
        </div>
      </div>

      <div class="flex flex-wrap items-center gap-2 pt-3 border-t border-slate-800/80">
        <div class="relative flex-1 min-w-[200px]">
          <Search class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
          <input
            v-model="spatialStore.searchQuery"
            type="text"
            placeholder="Filtrar persona o habilidad..."
            class="w-full pl-9 pr-8 py-2 rounded-xl bg-slate-950/90 border border-slate-800 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500"
          />
          <button
            v-if="spatialStore.searchQuery"
            @click="spatialStore.searchQuery = ''"
            class="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white cursor-pointer"
          >
            <X class="w-3.5 h-3.5" />
          </button>
        </div>

        <div class="flex flex-wrap items-center gap-1.5">
          <button
            v-for="cat in categories"
            :key="cat.id"
            @click="spatialStore.selectedCategory = cat.id; spatialStore.triggerFlash('catalog-grid', `⚡ Categoría: ${cat.label}`)"
            class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer border flex items-center gap-1.5"
            :class="spatialStore.selectedCategory === cat.id
              ? 'bg-emerald-500/20 border-emerald-500/60 text-emerald-300'
              : 'bg-slate-950/60 border-slate-800 text-slate-400 hover:text-white'"
          >
            <span>{{ cat.icon }}</span>
            <span>{{ cat.label }}</span>
          </button>
        </div>
      </div>
    </div>

    <!-- ======================================================================= -->
    <!-- GRILLA UNIFICADA (SIN SUB-CAJAS FRAGMENTADAS + CON FLASH DE IMPACTO)    -->
    <!-- ======================================================================= -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 items-start">
      <!-- 1. TARJETAS DE OFERTAS -->
      <div
        v-for="offer in filteredOffers"
        :key="'offer-' + offer.id"
        :id="`bento-card-offer-${offer.id}`"
        class="rounded-3xl border transition-all duration-500 overflow-hidden scroll-mt-28 relative"
        :class="[
          isExpanded('offer', offer.id)
            ? 'col-span-1 md:col-span-2 lg:col-span-3 border-emerald-500/80 bg-gradient-to-b from-slate-900 via-slate-900/98 to-slate-950 p-6 md:p-8 shadow-2xl ring-2 ring-emerald-500/30'
            : 'border-slate-800/90 bg-slate-900/70 hover:bg-slate-900 hover:border-emerald-500/50 p-6 shadow-lg cursor-pointer group',
          isCardFlashing('offer', offer.id) ? 'spatial-flash-blink' : ''
        ]"
        @click="!isExpanded('offer', offer.id) && spatialStore.toggleExpandItem('offer', offer.id)"
      >
        <!-- Badge de Flash cuando esta tarjeta acaba de cambiar -->
        <div
          v-if="spatialStore.flashingKey === `offer-${offer.id}`"
          class="mb-4 inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full bg-amber-400 text-slate-950 text-xs font-black shadow-lg animate-bounce"
        >
          <Zap class="w-3.5 h-3.5 fill-slate-950" />
          <span>{{ spatialStore.flashLabel || '⚡ ¡Acá está el cambio!' }}</span>
        </div>

        <!-- ESTADO COMPACTO: UNA SOLA SUPERFICIE LIMPIA (SIN CAJAS ANIDADAS) -->
        <div v-if="!isExpanded('offer', offer.id)" class="flex flex-col justify-between gap-5">
          <!-- Rostro + Nombre + Estrella -->
          <div class="flex items-center justify-between gap-3">
            <div class="flex items-center gap-3">
              <img
                :src="getAvatar(offer.userId)"
                :alt="offer.userName"
                class="w-12 h-12 rounded-full object-cover border-2 border-emerald-500/60"
              />
              <div>
                <div class="text-sm font-black text-white flex items-center gap-1.5">
                  <span>{{ offer.userName }}</span>
                  <span class="text-xs font-bold text-amber-400">★ {{ getAuthor(offer.userId).reputationScore }}</span>
                </div>
                <div class="text-[11px] text-slate-400">
                  {{ offer.modality === 'VIRTUAL' ? '🌐 Online · 1h' : '📍 ' + offer.modality + ' · 1h' }}
                </div>
              </div>
            </div>

            <Maximize2 class="w-4 h-4 text-slate-500 group-hover:text-emerald-400 transition-colors" />
          </div>

          <!-- Enseña ⇄ Busca directo sobre el lienzo de la tarjeta -->
          <div class="space-y-2.5 pt-2 border-t border-slate-800/70">
            <div>
              <span class="text-[10px] font-black uppercase tracking-wider text-emerald-400 block">
                🎓 Enseña
              </span>
              <h3 class="text-base font-extrabold text-white group-hover:text-emerald-300 transition-colors leading-snug mt-0.5">
                {{ getCategoryEmoji(offer.category) }} {{ offer.title }}
              </h3>
            </div>

            <div class="flex items-center justify-between text-xs pt-1 text-slate-400">
              <span class="truncate">
                <strong class="text-indigo-400">🎯 Busca:</strong> {{ getAuthorWantsToLearn(offer.userId) }}
              </span>
              <span class="text-amber-300 font-black shrink-0 ml-2">🪙 1</span>
            </div>
          </div>
        </div>

        <!-- ESTADO AMPLIFICADO -->
        <div v-else class="space-y-6" @click.stop>
          <div class="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
            <div class="flex items-center gap-3">
              <img
                :src="getAvatar(offer.userId)"
                :alt="offer.userName"
                class="w-12 h-12 rounded-full object-cover border-2 border-emerald-400"
              />
              <div>
                <div class="flex items-center gap-2">
                  <span class="text-lg font-black text-white">{{ offer.userName }}</span>
                  <span class="text-xs font-bold text-amber-400">★ {{ getAuthor(offer.userId).reputationScore }}</span>
                </div>
                <div class="text-xs text-slate-400">{{ getAuthor(offer.userId).bio }}</div>
              </div>
            </div>

            <div class="flex items-center gap-2">
              <button
                @click="showInlineReport = !showInlineReport"
                class="p-2 rounded-xl bg-slate-900 hover:bg-rose-500/15 text-slate-400 hover:text-rose-300 cursor-pointer"
                title="Denunciar publicación"
              >
                <Flag class="w-4 h-4" />
              </button>
              <button
                @click="spatialStore.collapseItem()"
                class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold border border-slate-700 cursor-pointer"
              >
                <Minimize2 class="w-3.5 h-3.5 text-emerald-400" />
                <span>Achicar</span>
              </button>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <div class="lg:col-span-7 space-y-4">
              <h3 class="text-2xl sm:text-3xl font-black text-white leading-tight">
                {{ getCategoryEmoji(offer.category) }} {{ offer.title }}
              </h3>

              <p class="text-sm text-slate-200 leading-relaxed">
                {{ offer.description }}
              </p>

              <div class="flex flex-wrap items-center gap-4 pt-2 text-xs text-slate-300">
                <span><strong class="text-emerald-400">🎓 Enseña:</strong> {{ offer.title }}</span>
                <span>⇄</span>
                <span><strong class="text-indigo-400">🎯 Busca:</strong> {{ getAuthorWantsToLearn(offer.userId) }}</span>
              </div>

              <div v-if="showInlineReport" class="p-4 rounded-2xl bg-rose-950/30 border border-rose-500/30 space-y-2.5">
                <div v-if="reportSent" class="text-xs font-bold text-emerald-400">✓ Reporte enviado.</div>
                <div v-else class="flex flex-wrap items-center gap-2">
                  <select v-model="reportReason" class="px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-xs text-white">
                    <option value="Contenido inapropiado">Contenido inapropiado</option>
                    <option value="Spam / Publicidad comercial">Spam comercial</option>
                  </select>
                  <input v-model="reportDetails" placeholder="Detalle..." class="flex-1 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-xs text-white" />
                  <button @click="handleSendInlineReport('OFFER', offer)" class="px-3 py-1.5 rounded-lg bg-rose-500 text-white text-xs font-bold cursor-pointer">Reportar</button>
                </div>
              </div>
            </div>

            <div
              class="lg:col-span-5 bg-slate-950/90 border border-slate-800 rounded-2xl p-5 space-y-4 transition-all"
              :class="spatialStore.flashingKey === `booking-box-${offer.id}` ? 'spatial-flash-blink border-emerald-400' : ''"
            >
              <div v-if="bookingSuccess" class="py-6 text-center space-y-3">
                <CheckCircle2 class="w-10 h-10 text-emerald-400 mx-auto" />
                <h4 class="text-base font-black text-white">¡Conectados!</h4>
                <div class="flex justify-center gap-2">
                  <button @click="spatialStore.openCapsule('sessions')" class="px-4 py-2 rounded-xl bg-emerald-500 text-slate-950 font-black text-xs cursor-pointer">
                    📅 Ver Mis Sesiones
                  </button>
                  <button @click="spatialStore.collapseItem()" class="px-4 py-2 rounded-xl bg-slate-800 text-slate-200 font-bold text-xs cursor-pointer">
                    Achicar
                  </button>
                </div>
              </div>

              <template v-else>
                <div class="flex items-center justify-between">
                  <span class="text-xs uppercase font-black text-emerald-400">📅 Elegí Horario (1h)</span>
                  <span class="text-xs font-bold text-amber-300">🪙 1 Crédito</span>
                </div>

                <div v-if="bookingError" class="p-2.5 rounded-xl bg-rose-500/15 text-xs text-rose-300">
                  {{ bookingError }}
                </div>

                <div class="grid grid-cols-1 gap-2">
                  <button
                    v-for="slot in getFreeSlots(offer.userId)"
                    :key="slot.id"
                    @click="selectedSlotId = slot.id; spatialStore.triggerFlash(`booking-box-${offer.id}`, `⚡ Horario elegido: ${slot.startTime} hs`)"
                    class="px-3.5 py-2.5 rounded-xl border text-xs font-bold flex items-center justify-between cursor-pointer transition-all"
                    :class="selectedSlotId === slot.id
                      ? 'bg-emerald-500/20 border-emerald-500 text-white'
                      : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white'"
                  >
                    <span>🗓️ {{ slot.date }} · {{ slot.startTime }} hs</span>
                    <span class="text-[10px] text-emerald-400">Disponible</span>
                  </button>
                </div>

                <button
                  @click="handleConfirmBookingInPlace(offer)"
                  class="w-full py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-sm shadow-lg shadow-emerald-500/20 cursor-pointer flex items-center justify-center gap-2"
                >
                  <Send class="w-4 h-4" />
                  <span>{{ authStore.isGuest ? 'Entrar y Reservar' : 'Reservar en 1 Clic' }}</span>
                </button>
              </template>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. TARJETAS DE NECESIDADES -->
      <div
        v-for="need in filteredNeeds"
        :key="'need-' + need.id"
        :id="`bento-card-need-${need.id}`"
        class="rounded-3xl border transition-all duration-500 overflow-hidden scroll-mt-28 relative"
        :class="[
          isExpanded('need', need.id)
            ? 'col-span-1 md:col-span-2 lg:col-span-3 border-indigo-500/80 bg-gradient-to-b from-slate-900 via-slate-900/98 to-slate-950 p-6 md:p-8 shadow-2xl ring-2 ring-indigo-500/30'
            : 'border-slate-800/90 bg-slate-900/70 hover:bg-slate-900 hover:border-indigo-500/50 p-6 shadow-lg cursor-pointer group',
          isCardFlashing('need', need.id) ? 'spatial-flash-blink' : ''
        ]"
        @click="!isExpanded('need', need.id) && spatialStore.toggleExpandItem('need', need.id)"
      >
        <div
          v-if="spatialStore.flashingKey === `need-${need.id}`"
          class="mb-4 inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full bg-amber-400 text-slate-950 text-xs font-black shadow-lg animate-bounce"
        >
          <Zap class="w-3.5 h-3.5 fill-slate-950" />
          <span>{{ spatialStore.flashLabel || '⚡ ¡Acá está el cambio!' }}</span>
        </div>

        <div v-if="!isExpanded('need', need.id)" class="flex flex-col justify-between gap-5">
          <div class="flex items-center justify-between gap-3">
            <div class="flex items-center gap-3">
              <img
                :src="getAvatar(need.userId)"
                :alt="need.userName"
                class="w-12 h-12 rounded-full object-cover border-2 border-indigo-500/60"
              />
              <div>
                <div class="text-sm font-black text-white flex items-center gap-1.5">
                  <span>{{ need.userName }}</span>
                  <span class="text-xs font-bold text-amber-400">★ {{ getAuthor(need.userId).reputationScore }}</span>
                </div>
                <div class="text-[11px] text-slate-400">
                  {{ need.modality === 'VIRTUAL' ? '🌐 Online · 1h' : '📍 ' + need.modality + ' · 1h' }}
                </div>
              </div>
            </div>

            <Maximize2 class="w-4 h-4 text-slate-500 group-hover:text-indigo-400 transition-colors" />
          </div>

          <div class="space-y-2.5 pt-2 border-t border-slate-800/70">
            <div>
              <span class="text-[10px] font-black uppercase tracking-wider text-indigo-400 block">
                🎯 Busca Aprender
              </span>
              <h3 class="text-base font-extrabold text-white group-hover:text-indigo-300 transition-colors leading-snug mt-0.5">
                {{ getCategoryEmoji(need.category) }} {{ need.title }}
              </h3>
            </div>

            <div class="flex items-center justify-between text-xs pt-1 text-slate-400">
              <span class="truncate">
                <strong class="text-emerald-400">🎓 Enseña:</strong> {{ getAuthorCanTeach(need.userId) }}
              </span>
              <span class="text-emerald-300 font-black shrink-0 ml-2">+1 🪙</span>
            </div>
          </div>
        </div>

        <div v-else class="space-y-6" @click.stop>
          <div class="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
            <div class="flex items-center gap-3">
              <img
                :src="getAvatar(need.userId)"
                :alt="need.userName"
                class="w-12 h-12 rounded-full object-cover border-2 border-indigo-400"
              />
              <div>
                <div class="text-lg font-black text-white">{{ need.userName }}</div>
                <div class="text-xs text-indigo-300 font-semibold">Te transfiere +1 Crédito si le enseñás</div>
              </div>
            </div>

            <button
              @click="spatialStore.collapseItem()"
              class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold border border-slate-700 cursor-pointer"
            >
              <Minimize2 class="w-3.5 h-3.5 text-indigo-400" />
              <span>Achicar</span>
            </button>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <div class="lg:col-span-7 space-y-4">
              <h3 class="text-2xl font-black text-white leading-tight">
                {{ getCategoryEmoji(need.category) }} {{ need.title }}
              </h3>
              <p class="text-sm text-slate-200 leading-relaxed">
                {{ need.goal }}
              </p>
            </div>

            <div class="lg:col-span-5 bg-slate-950/90 border border-slate-800 rounded-2xl p-5 space-y-4">
              <div v-if="teachNeedSuccess" class="py-6 text-center space-y-3">
                <CheckCircle2 class="w-10 h-10 text-emerald-400 mx-auto" />
                <h4 class="text-base font-black text-white">¡Ofrecimiento Enviado!</h4>
                <button @click="spatialStore.openCapsule('sessions')" class="px-4 py-2 rounded-xl bg-emerald-500 text-slate-950 font-black text-xs cursor-pointer">
                  📅 Ver Mis Sesiones
                </button>
              </div>

              <template v-else>
                <div class="text-xs uppercase font-black text-indigo-400">
                  🤝 Ofrecerle 1 Hora (+1 🪙)
                </div>
                <div v-if="bookingError" class="p-2.5 rounded-xl bg-rose-500/15 text-xs text-rose-300">
                  {{ bookingError }}
                </div>
                <div class="grid grid-cols-2 gap-2.5">
                  <input v-model="teachNeedDate" type="date" class="px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
                  <input v-model="teachNeedTime" type="time" class="px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
                </div>
                <button
                  @click="handleOfferToTeachNeedInPlace(need)"
                  class="w-full py-3.5 rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-400 hover:to-purple-500 text-white font-black text-sm cursor-pointer flex items-center justify-center gap-2"
                >
                  <UserCheck class="w-4 h-4" />
                  <span>¡Yo le enseño! (+1 Crédito)</span>
                </button>
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
