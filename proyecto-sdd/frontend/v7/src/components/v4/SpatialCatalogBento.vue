<script setup>
import { ref, computed, watch } from 'vue'
import {
  Search,
  Sparkles,
  BookOpen,
  Compass,
  Clock,
  Star,
  Maximize2,
  Minimize2,
  CheckCircle2,
  Coins,
  Flag,
  Send,
  Calendar,
  X,
  UserCheck,
  Filter
} from 'lucide-vue-next'
import { useSpatialStore } from '../../stores/spatialStore'
import { usePlatformStore } from '../../stores/platformStore'
import { useAuthStore } from '../../stores/authStore'
import { mockStorage } from '../../services/mockStorage'
import HandDrawnIcon from '../ui/HandDrawnIcon.vue'

const spatialStore = useSpatialStore()
const platformStore = usePlatformStore()
const authStore = useAuthStore()

const categories = ['TODAS', 'Programación', 'Tecnología', 'Idiomas', 'Diseño', 'Infraestructura', 'Habilidades']

// Filtered offers & needs
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
    const matchMod =
      spatialStore.selectedModality === 'TODAS' ||
      o.modality === spatialStore.selectedModality
    return matchQ && matchCat && matchMod
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
    const matchMod =
      spatialStore.selectedModality === 'TODAS' ||
      n.modality === spatialStore.selectedModality
    return matchQ && matchCat && matchMod
  })
})

// In-place booking state when an offer or need card is expanded
const selectedSlotId = ref('')
const selectedModality = ref('VIRTUAL')
const exchangeType = ref('CREDITS')
const bookingError = ref('')
const bookingSuccess = ref(false)

// For teaching a need in-place
const teachNeedDate = ref('2026-10-21')
const teachNeedTime = ref('18:00')
const teachNeedSuccess = ref(false)

// In-place report mini-accordion
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

function getAuthor(userId) {
  return mockStorage.findUserById(userId) || {
    name: 'Miembro Verificado',
    bio: 'Entusiasta del aprendizaje colaborativo 1 a 1.',
    reputationScore: 4.9,
    reviewsCount: 8
  }
}

function getAvatarUrl(userId, userName = '') {
  const author = mockStorage.findUserById(userId)
  if (author && author.avatar) return author.avatar

  const nameKey = (userName || author?.name || '').toLowerCase()
  if (userId === 'usr-1' || nameKey.includes('juan')) {
    return 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80'
  }
  if (userId === 'usr-2' || nameKey.includes('elena')) {
    return 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&auto=format&fit=crop&q=80'
  }
  if (userId === 'usr-3' || nameKey.includes('carlos')) {
    return 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80'
  }
  if (nameKey.includes('lucía') || nameKey.includes('lucia')) {
    return 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&auto=format&fit=crop&q=80'
  }
  if (nameKey.includes('martín') || nameKey.includes('martin')) {
    return 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80'
  }
  if (nameKey.includes('sofía') || nameKey.includes('sofia')) {
    return 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=150&auto=format&fit=crop&q=80'
  }
  return 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150&auto=format&fit=crop&q=80'
}

function getFreeSlots(userId) {
  const slots = mockStorage.getPublicUserSlots(userId)
  if (slots && slots.length > 0) return slots
  // Fallback default slots so every expanded card is immediately interactive
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
    spatialStore.notify('Ingresá en 1 clic ahí arriba', 'Elegí un usuario demo o registrate para confirmar esta reserva sin salir de la página.', 'amber')
    return
  }

  if (offer.userId === authStore.currentUser.id) {
    bookingError.value = 'Esta es tu propia propuesta publicada.'
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
    spatialStore.triggerFlash(`offer-${offer.id}`, '⚡ ¡Reserva solicitada aquí mismo!')
    spatialStore.notify(
      '¡Reserva solicitada en el acto!',
      `Coordinaste "${offer.title}" para el ${chosenSlot.date} a las ${chosenSlot.startTime} hs.`
    )
  } catch (err) {
    bookingError.value = err.message
  }
}

async function handleOfferToTeachNeedInPlace(need) {
  bookingError.value = ''

  if (authStore.isGuest) {
    spatialStore.openCapsule('auth')
    spatialStore.notify('Ingresá en 1 clic ahí arriba', 'Elegí un perfil demo para ofrecer enseñar este tema y ganar +1 crédito.', 'amber')
    return
  }

  if (need.userId === authStore.currentUser.id) {
    bookingError.value = 'Este es tu propio pedido de aprendizaje.'
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
    spatialStore.triggerFlash(`need-${need.id}`, '⚡ ¡Propuesta de mentoría enviada!')
    spatialStore.notify(
      '¡Propuesta de mentoría enviada!',
      `Le ofreciste enseñar "${need.title}" a ${need.userName}. Ganarás +1 Crédito al completarla.`
    )
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
  spatialStore.triggerFlash(`${targetType.toLowerCase()}-${item.id}`, '⚡ Reporte registrado')
  spatialStore.notify('Reporte enviado a moderación', 'Gracias por cuidar la comunidad.', 'amber')
}
</script>

<template>
  <section
    id="spatial-catalog-section"
    class="scroll-mt-24 relative rounded-3xl overflow-hidden border border-slate-800 bg-gradient-to-b from-slate-900 via-slate-900/95 to-slate-950 p-6 md:p-12 shadow-2xl space-y-8 transition-all"
    :class="spatialStore.flashingKey === 'catalog-grid' ? 'spatial-flash-blink border-emerald-400' : ''"
  >
    <!-- Ambient Glow -->
    <div class="absolute -top-32 -left-32 w-96 h-96 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-500/15 rounded-full blur-3xl pointer-events-none"></div>

    <!-- Cabecera del Lienzo de Exploración & Búsqueda In-Place -->
    <div class="relative z-10 space-y-6">
      <div class="flex flex-wrap items-end justify-between gap-4">
        <div class="space-y-2">
          <div class="flex flex-wrap items-start gap-4">
            <div
              class="w-12 h-12 sm:w-14 sm:h-14 rounded-2xl bg-emerald-500/15 border-2 border-dashed border-emerald-500/45 text-emerald-400 flex items-center justify-center shrink-0 shadow-inner rotate-2"
              title="Bloque Principal · Explorar, Filtrar y Reservar"
            >
              <HandDrawnIcon name="explore" size="lg" />
            </div>
            <h2 class="text-3xl sm:text-4xl font-black text-white tracking-tight leading-[1.12]">
              Explorá, filtrá y reservá.
              <span class="block bg-gradient-to-r from-emerald-400 via-teal-300 to-indigo-400 bg-clip-text text-transparent">
                Todo en el mismo lugar.
              </span>
            </h2>
            <span
              v-if="spatialStore.flashingKey === 'catalog-grid' && spatialStore.flashLabel"
              class="px-3 py-1 rounded-full bg-amber-400 text-slate-950 text-xs font-black animate-bounce shadow-lg"
            >
              {{ spatialStore.flashLabel }}
            </span>
          </div>
          <p class="text-slate-300 text-sm sm:text-base max-w-2xl leading-relaxed">
            Sin páginas nuevas ni pestañas aparte. Tocá cualquier propuesta o pedido de aprendizaje acá adentro para que crezca frente a vos con sus horarios y detalles.
          </p>
        </div>

        <!-- Selector rápido Todo / Propuestas / Pedidos -->
        <div class="flex items-center gap-1.5 bg-slate-950 p-1.5 rounded-2xl border border-slate-800">
          <button
            @click="spatialStore.catalogMode = 'all'; spatialStore.triggerFlash('catalog-grid', '⚡ Mostrando todo el lienzo')"
            class="px-3.5 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center gap-2"
            :class="spatialStore.catalogMode === 'all' ? 'bg-emerald-500 text-slate-950 shadow-sm' : 'text-slate-400 hover:text-white'"
          >
            <HandDrawnIcon name="explore" size="sm" />
            <span>Todo ({{ filteredOffers.length + filteredNeeds.length }})</span>
          </button>
          <button
            @click="spatialStore.catalogMode = 'offers'; spatialStore.triggerFlash('catalog-grid', '⚡ Filtrado: Propuestas')"
            class="px-3.5 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center gap-2"
            :class="spatialStore.catalogMode === 'offers' ? 'bg-emerald-500 text-slate-950 shadow-sm' : 'text-emerald-400 hover:bg-emerald-500/15'"
          >
            <HandDrawnIcon name="teach" size="sm" />
            <span>Enseñar / Ofertas ({{ filteredOffers.length }})</span>
          </button>
          <button
            @click="spatialStore.catalogMode = 'needs'; spatialStore.triggerFlash('catalog-grid', '⚡ Filtrado: Buscan aprender')"
            class="px-3.5 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer flex items-center gap-2"
            :class="spatialStore.catalogMode === 'needs' ? 'bg-indigo-500 text-white shadow-sm' : 'text-indigo-400 hover:bg-indigo-500/15'"
          >
            <HandDrawnIcon name="learn" size="sm" />
            <span>Buscan Aprender ({{ filteredNeeds.length }})</span>
          </button>
        </div>
      </div>

      <!-- Barra de búsqueda en vivo + Chips de Categoría In-Place -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-center pt-4 border-t border-slate-800/80">
        <!-- Input instantáneo -->
        <div class="lg:col-span-5 relative">
          <Search class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
          <input
            v-model="spatialStore.searchQuery"
            type="text"
            placeholder="Filtrar en vivo por tema, habilidad o mentor (ej. Vue, Inglés, Docker)..."
            class="w-full pl-10 pr-9 py-2.5 rounded-xl bg-slate-950/90 border border-slate-700/80 text-xs sm:text-sm text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500 transition-colors"
          />
          <button
            v-if="spatialStore.searchQuery"
            @click="spatialStore.searchQuery = ''; spatialStore.triggerFlash('catalog-grid', '⚡ Búsqueda limpiada')"
            class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white cursor-pointer"
          >
            <X class="w-4 h-4" />
          </button>
        </div>

        <!-- Píldoras de Categoría -->
        <div class="lg:col-span-7 flex flex-wrap items-center gap-1.5">
          <button
            v-for="cat in categories"
            :key="cat"
            @click="spatialStore.selectedCategory = cat; spatialStore.triggerFlash('catalog-grid', `⚡ Categoría: ${cat}`)"
            class="px-3 py-1.5 rounded-xl text-xs font-semibold transition-all cursor-pointer border"
            :class="spatialStore.selectedCategory === cat
              ? 'bg-emerald-500/20 border-emerald-500/60 text-emerald-300 shadow-xs'
              : 'bg-slate-950/50 border-slate-800 text-slate-400 hover:text-slate-200 hover:border-slate-700'"
          >
            {{ cat }}
          </button>

          <button
            v-if="spatialStore.searchQuery || spatialStore.selectedCategory !== 'TODAS' || spatialStore.catalogMode !== 'all'"
            @click="spatialStore.clearFilters()"
            class="ml-auto px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-[11px] font-bold text-amber-300 cursor-pointer"
          >
            Limpiar filtros
          </button>
        </div>
      </div>
    </div>

    <!-- ======================================================================= -->
    <!-- GRILLA MORPHING BENTO CONTENIDA ADENTRO DEL MISMO PANEL DE LA SECCIÓN   -->
    <!-- ======================================================================= -->
    <div class="relative z-10 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 items-start pt-2">
      <!-- 1. TARJETAS DE OFERTAS (PROPUESTAS PARA APRENDER) -->
      <div
        v-for="offer in filteredOffers"
        :key="'offer-' + offer.id"
        :id="`bento-card-offer-${offer.id}`"
        class="rounded-3xl border transition-all duration-300 overflow-hidden scroll-mt-28"
        :class="[
          isExpanded('offer', offer.id)
            ? 'col-span-1 md:col-span-2 lg:col-span-3 border-emerald-500/70 bg-slate-950/90 p-6 md:p-8 shadow-2xl ring-2 ring-emerald-500/20'
            : 'bento-card-rollover-offer border-slate-800 bg-slate-950/75 p-6 shadow-md cursor-pointer group',
          (spatialStore.flashingKey === `offer-${offer.id}` || spatialStore.flashingKey === 'catalog-grid') ? 'spatial-flash-blink' : ''
        ]"
        @click="!isExpanded('offer', offer.id) && spatialStore.toggleExpandItem('offer', offer.id)"
      >
        <div
          v-if="spatialStore.flashingKey === `offer-${offer.id}`"
          class="mb-4 inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full bg-amber-400 text-slate-950 text-xs font-black shadow-lg animate-bounce"
        >
          <span>{{ spatialStore.flashLabel || '⚡ ¡Acá está el cambio!' }}</span>
        </div>

        <!-- ================= ESTADO COMPACTO (CERRADO) ================= -->
        <div v-if="!isExpanded('offer', offer.id)" class="flex flex-col justify-between h-full gap-5">
          <div>
            <div class="flex items-center justify-between gap-2 mb-3.5">
              <div class="flex items-center gap-2">
                <span
                  class="w-9 h-9 rounded-xl bg-emerald-500/15 border-2 border-emerald-500/45 text-emerald-400 group-hover:bg-emerald-500 group-hover:text-slate-950 group-hover:border-emerald-500 group-hover:scale-110 transition-all duration-300 flex items-center justify-center shrink-0 shadow-xs"
                  title="Entidad: Enseñar / Propuesta"
                >
                  <HandDrawnIcon name="teach" size="md" />
                </span>
                <span class="inline-flex items-center px-2.5 py-1 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-300 group-hover:bg-emerald-500 group-hover:text-slate-950 group-hover:border-emerald-500 transition-all duration-300 text-[11px] font-bold">
                  <span>Enseñar · {{ offer.category }}</span>
                </span>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[11px] text-slate-400 font-medium flex items-center gap-1">
                  <Clock class="w-3 h-3 text-emerald-400" />
                  {{ offer.durationMinutes || 60 }}m · {{ offer.modality }}
                </span>
                <span
                  class="w-6 h-6 rounded-lg bg-emerald-500/10 border border-dashed border-emerald-500/35 text-emerald-400 flex items-center justify-center shrink-0"
                  title="Sección: Explorar y Reservar"
                >
                  <HandDrawnIcon name="explore" size="xs" />
                </span>
              </div>
            </div>

            <h3 class="text-lg font-extrabold text-white group-hover:text-emerald-300 transition-colors leading-snug mb-2">
              {{ offer.title }}
            </h3>

            <p class="text-xs text-slate-400 line-clamp-3 leading-relaxed">
              {{ offer.description }}
            </p>
          </div>

          <div class="pt-4 border-t border-slate-800/80 group-hover:border-emerald-500/30 transition-colors flex items-center justify-between gap-3">
            <div class="flex items-center gap-2.5">
              <img
                :src="getAvatarUrl(offer.userId, offer.userName)"
                :alt="offer.userName"
                class="w-9 h-9 rounded-full object-cover border-2 border-emerald-500/40 group-hover:border-emerald-500 group-hover:scale-105 transition-all shadow-xs shrink-0"
              />
              <div>
                <div class="text-xs font-bold text-slate-200 group-hover:text-emerald-300 transition-colors">{{ offer.userName }}</div>
                <div class="text-[10px] text-amber-400 font-semibold flex items-center gap-0.5">
                  <Star class="w-2.5 h-2.5 fill-amber-400" />
                  <span>{{ getAuthor(offer.userId).reputationScore }} · Nivel {{ offer.level }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ================= ESTADO AMPLIFICADO (EXPANDIDO IN-PLACE) ================= -->
        <div v-else class="space-y-6" @click.stop>
          <!-- Barra superior de la tarjeta expandida -->
          <div class="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
            <div class="flex flex-wrap items-center gap-2.5">
              <span class="w-9 h-9 rounded-xl bg-emerald-500 text-slate-950 flex items-center justify-center shrink-0 shadow-sm">
                <HandDrawnIcon name="teach" size="md" />
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs font-black">
                <span>Enseñar · {{ offer.category }}</span>
              </span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-emerald-500/10 border border-dashed border-emerald-500/30 text-emerald-400 text-xs font-bold">
                <HandDrawnIcon name="explore" size="xs" />
                <span>Explorar</span>
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs font-semibold">
                Modalidad: {{ offer.modality }}
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs font-semibold">
                Nivel: {{ offer.level }}
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs font-semibold">
                Duración: {{ offer.durationMinutes || 60 }} minutos
              </span>
            </div>

            <div class="flex items-center gap-2">
              <button
                @click="showInlineReport = !showInlineReport"
                class="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-rose-500/15 text-slate-400 hover:text-rose-300 text-xs font-medium flex items-center gap-1 cursor-pointer transition-colors"
              >
                <Flag class="w-3.5 h-3.5" />
                <span>Denunciar</span>
              </button>

              <button
                @click="spatialStore.collapseItem()"
                class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold border border-slate-700 cursor-pointer transition-all"
              >
                <Minimize2 class="w-3.5 h-3.5 text-emerald-400" />
                <span>Achicar tarjeta</span>
              </button>
            </div>
          </div>

          <!-- Cuerpo de 2 columnas dentro de la tarjeta amplificada -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Columna Izquierda: Detalles de la Propuesta + Perfil del Mentor -->
            <div class="lg:col-span-7 space-y-5">
              <h3 class="text-2xl sm:text-3xl font-black text-white leading-tight">
                {{ offer.title }}
              </h3>

              <div class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800/90 space-y-2">
                <span class="text-[11px] uppercase font-bold tracking-wider text-emerald-400 block">
                  ¿Qué vas a aprender en esta sesión 1 a 1?
                </span>
                <p class="text-sm text-slate-200 leading-relaxed">
                  {{ offer.description }}
                </p>
              </div>

              <!-- Tarjeta Íntima del Mentor -->
              <div class="p-5 rounded-2xl bg-slate-950/50 border border-slate-800 flex flex-wrap items-center justify-between gap-4">
                <div class="flex items-center gap-3.5">
                  <img
                    :src="getAvatarUrl(offer.userId, offer.userName)"
                    :alt="offer.userName"
                    class="w-12 h-12 rounded-2xl object-cover border-2 border-emerald-500/50 shadow-md shrink-0"
                  />
                  <div>
                    <div class="flex items-center gap-2">
                      <span class="text-base font-bold text-white">{{ offer.userName }}</span>
                      <span class="px-2 py-0.5 rounded-md bg-amber-500/15 text-amber-300 text-xs font-bold flex items-center gap-1">
                        <Star class="w-3 h-3 fill-amber-400" />
                        {{ getAuthor(offer.userId).reputationScore }} ({{ getAuthor(offer.userId).reviewsCount || 6 }} reseñas)
                      </span>
                    </div>
                    <p class="text-xs text-slate-400 mt-1 max-w-md">
                      {{ getAuthor(offer.userId).bio || 'Miembro activo de la comunidad de intercambio.' }}
                    </p>
                  </div>
                </div>
              </div>

              <!-- Mini formulario de denuncia in-place si se activó -->
              <div v-if="showInlineReport" class="p-4 rounded-2xl bg-rose-950/30 border border-rose-500/30 space-y-3">
                <div v-if="reportSent" class="text-xs font-bold text-emerald-400">
                  ✓ Reporte registrado sin salir de la tarjeta.
                </div>
                <div v-else class="space-y-2.5">
                  <div class="text-xs font-bold text-rose-300">Reportar esta publicación a moderación</div>
                  <select v-model="reportReason" class="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-xs text-white">
                    <option value="Contenido inapropiado">Contenido inapropiado</option>
                    <option value="Spam / Publicidad comercial">Spam o intención de cobro con dinero</option>
                    <option value="Lenguaje ofensivo">Lenguaje ofensivo</option>
                  </select>
                  <input
                    v-model="reportDetails"
                    placeholder="Detalle opcional..."
                    class="w-full px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-xs text-white"
                  />
                  <div class="flex justify-end gap-2">
                    <button @click="showInlineReport = false" class="px-3 py-1 rounded-lg bg-slate-800 text-xs text-slate-300 cursor-pointer">Cancelar</button>
                    <button @click="handleSendInlineReport('OFFER', offer)" class="px-3 py-1 rounded-lg bg-rose-500 text-white text-xs font-bold cursor-pointer">Enviar Reporte</button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Columna Derecha: Reserva In-Place en 1 Clic -->
            <div
              class="lg:col-span-5 bg-slate-950/90 border border-slate-800 rounded-2xl p-5 sm:p-6 space-y-4 transition-all"
              :class="spatialStore.flashingKey === `booking-box-${offer.id}` ? 'spatial-flash-blink border-emerald-400' : ''"
            >
              <div v-if="bookingSuccess" class="py-6 text-center space-y-3">
                <div class="w-12 h-12 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center mx-auto">
                  <CheckCircle2 class="w-7 h-7" />
                </div>
                <h4 class="text-lg font-black text-white">¡Sesión Solicitada Aquí Mismo!</h4>
                <p class="text-xs text-slate-300 leading-relaxed">
                  Tu pedido para <strong>{{ offer.title }}</strong> ya quedó registrado. No tuviste que cambiar de página.
                </p>
                <div class="flex flex-wrap justify-center gap-2 pt-2">
                  <button
                    @click="spatialStore.openCapsule('sessions')"
                    class="px-4 py-2 rounded-xl bg-emerald-500 text-slate-950 font-black text-xs cursor-pointer"
                  >
                    Ver en Mis Sesiones Arriba
                  </button>
                  <button
                    @click="spatialStore.collapseItem()"
                    class="px-4 py-2 rounded-xl bg-slate-800 text-slate-200 font-bold text-xs cursor-pointer"
                  >
                    Achicar tarjeta
                  </button>
                </div>
              </div>

              <template v-else>
                <div class="flex items-center justify-between">
                  <span class="text-xs uppercase font-black tracking-wider text-emerald-400">
                    Coordinar Sesión Ahora
                  </span>
                  <span class="text-[11px] text-amber-300 font-semibold flex items-center gap-1">
                    <Coins class="w-3.5 h-3.5" /> 1 Hora = 1 Crédito
                  </span>
                </div>

                <div v-if="bookingError" class="p-3 rounded-xl bg-rose-500/15 border border-rose-500/30 text-xs text-rose-300">
                  {{ bookingError }}
                </div>

                <!-- Selección táctil de horario libre -->
                <div>
                  <label class="text-xs font-bold text-slate-300 block mb-2">
                    1. Elegí una franja horaria libre de {{ offer.userName }}:
                  </label>
                  <div class="grid grid-cols-1 gap-2">
                    <button
                      v-for="slot in getFreeSlots(offer.userId)"
                      :key="slot.id"
                      @click="selectedSlotId = slot.id; spatialStore.triggerFlash(`booking-box-${offer.id}`, `⚡ Horario elegido: ${slot.startTime} hs`)"
                      class="px-3.5 py-2.5 rounded-xl border text-xs font-bold flex items-center justify-between transition-all cursor-pointer"
                      :class="selectedSlotId === slot.id
                        ? 'bg-emerald-500/20 border-emerald-500 text-white shadow-xs'
                        : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white'"
                    >
                      <span class="flex items-center gap-2">
                        <Calendar class="w-3.5 h-3.5 text-emerald-400" />
                        {{ slot.date }} a las {{ slot.startTime }} hs
                      </span>
                      <span class="text-[10px] uppercase text-emerald-400">1h Libre</span>
                    </button>
                  </div>
                </div>

                <!-- Selección táctil de método de trueque -->
                <div>
                  <label class="text-xs font-bold text-slate-300 block mb-2">
                    2. ¿Cómo preferís intercambiar?
                  </label>
                  <div class="grid grid-cols-2 gap-2">
                    <button
                      @click="exchangeType = 'CREDITS'; spatialStore.triggerFlash(`booking-box-${offer.id}`, '⚡ Método: 1 Crédito')"
                      class="p-2.5 rounded-xl border text-left transition-all cursor-pointer"
                      :class="exchangeType === 'CREDITS'
                        ? 'bg-emerald-500/20 border-emerald-500 text-white'
                        : 'bg-slate-900 border-slate-800 text-slate-400'"
                    >
                      <div class="text-xs font-bold">Usar 1 Crédito</div>
                      <div class="text-[10px] text-slate-400">Saldo: {{ authStore.credits }}</div>
                    </button>
                    <button
                      @click="exchangeType = 'RECIPROCAL'; spatialStore.triggerFlash(`booking-box-${offer.id}`, '⚡ Método: Trueque 1 a 1')"
                      class="p-2.5 rounded-xl border text-left transition-all cursor-pointer"
                      :class="exchangeType === 'RECIPROCAL'
                        ? 'bg-indigo-500/20 border-indigo-500 text-white'
                        : 'bg-slate-900 border-slate-800 text-slate-400'"
                    >
                      <div class="text-xs font-bold">Trueque 1 a 1</div>
                      <div class="text-[10px] text-slate-400">Reciprocidad directa</div>
                    </button>
                  </div>
                </div>

                <button
                  @click="handleConfirmBookingInPlace(offer)"
                  class="w-full py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-sm shadow-lg shadow-emerald-500/20 transition-all cursor-pointer flex items-center justify-center gap-2"
                >
                  <Send class="w-4 h-4" />
                  <span>{{ authStore.isGuest ? 'Ingresar y Reservar Aquí Mismo' : 'Confirmar Reserva en 1 Clic' }}</span>
                </button>
              </template>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. TARJETAS DE NECESIDADES (APRENDIZAJES BUSCADOS) -->
      <div
        v-for="need in filteredNeeds"
        :key="'need-' + need.id"
        :id="`bento-card-need-${need.id}`"
        class="rounded-3xl border transition-all duration-300 overflow-hidden scroll-mt-28"
        :class="[
          isExpanded('need', need.id)
            ? 'col-span-1 md:col-span-2 lg:col-span-3 border-indigo-500/70 bg-slate-950/90 p-6 md:p-8 shadow-2xl ring-2 ring-indigo-500/20'
            : 'bento-card-rollover-need border-slate-800 bg-slate-950/75 p-6 shadow-md cursor-pointer group',
          (spatialStore.flashingKey === `need-${need.id}` || spatialStore.flashingKey === 'catalog-grid') ? 'spatial-flash-blink' : ''
        ]"
        @click="!isExpanded('need', need.id) && spatialStore.toggleExpandItem('need', need.id)"
      >
        <div
          v-if="spatialStore.flashingKey === `need-${need.id}`"
          class="mb-4 inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full bg-amber-400 text-slate-950 text-xs font-black shadow-lg animate-bounce"
        >
          <span>{{ spatialStore.flashLabel || '⚡ ¡Acá está el cambio!' }}</span>
        </div>

        <!-- ================= ESTADO COMPACTO (CERRADO) ================= -->
        <div v-if="!isExpanded('need', need.id)" class="flex flex-col justify-between h-full gap-5">
          <div>
            <div class="flex items-center justify-between gap-2 mb-3.5">
              <div class="flex items-center gap-2">
                <span
                  class="w-9 h-9 rounded-xl bg-indigo-500/15 border-2 border-indigo-500/45 text-indigo-400 group-hover:bg-indigo-500 group-hover:text-white group-hover:border-indigo-500 group-hover:scale-110 transition-all duration-300 flex items-center justify-center shrink-0 shadow-xs"
                  title="Entidad: Aprender / Pedido"
                >
                  <HandDrawnIcon name="learn" size="md" />
                </span>
                <span class="inline-flex items-center px-2.5 py-1 rounded-full bg-indigo-500/15 border border-indigo-500/30 text-indigo-300 group-hover:bg-indigo-500 group-hover:text-white group-hover:border-indigo-500 transition-all duration-300 text-[11px] font-bold">
                  <span>Aprender · {{ need.category }}</span>
                </span>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[11px] text-slate-400 font-medium">
                  {{ need.modality }}
                </span>
                <span
                  class="w-6 h-6 rounded-lg bg-indigo-500/10 border border-dashed border-indigo-500/35 text-indigo-400 flex items-center justify-center shrink-0"
                  title="Sección: Explorar y Reservar"
                >
                  <HandDrawnIcon name="explore" size="xs" />
                </span>
              </div>
            </div>

            <h3 class="text-lg font-extrabold text-white group-hover:text-indigo-300 transition-colors leading-snug mb-2">
              {{ need.title }}
            </h3>

            <p class="text-xs text-slate-400 line-clamp-3 leading-relaxed">
              {{ need.goal }}
            </p>
          </div>

          <div class="pt-4 border-t border-slate-800/80 group-hover:border-indigo-500/30 transition-colors flex items-center justify-between gap-3">
            <div class="flex items-center gap-2.5">
              <img
                :src="getAvatarUrl(need.userId, need.userName)"
                :alt="need.userName"
                class="w-9 h-9 rounded-full object-cover border-2 border-indigo-500/40 group-hover:border-indigo-500 group-hover:scale-105 transition-all shadow-xs shrink-0"
              />
              <div>
                <div class="text-xs font-bold text-slate-200 group-hover:text-indigo-300 transition-colors">{{ need.userName }}</div>
                <div class="text-[10px] text-indigo-300 font-semibold">
                  Ganá +1 Crédito enseñándole
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ================= ESTADO AMPLIFICADO (EXPANDIDO IN-PLACE) ================= -->
        <div v-else class="space-y-6" @click.stop>
          <div class="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
            <div class="flex flex-wrap items-center gap-2.5">
              <span class="w-9 h-9 rounded-xl bg-indigo-500 text-white flex items-center justify-center shrink-0 shadow-sm">
                <HandDrawnIcon name="learn" size="md" />
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 text-xs font-black">
                <span>Aprender · {{ need.category }}</span>
              </span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-indigo-500/10 border border-dashed border-indigo-500/30 text-indigo-400 text-xs font-bold">
                <HandDrawnIcon name="explore" size="xs" />
                <span>Explorar</span>
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs font-semibold">
                Modalidad preferida: {{ need.modality }}
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs font-semibold">
                Nivel actual: {{ need.level }}
              </span>
            </div>

            <button
              @click="spatialStore.collapseItem()"
              class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold border border-slate-700 cursor-pointer transition-all"
            >
              <Minimize2 class="w-3.5 h-3.5 text-indigo-400" />
              <span>Achicar tarjeta</span>
            </button>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <div class="lg:col-span-7 space-y-4">
              <div class="flex items-center gap-3">
                <img
                  :src="getAvatarUrl(need.userId, need.userName)"
                  :alt="need.userName"
                  class="w-11 h-11 rounded-2xl object-cover border-2 border-indigo-500/50 shadow-sm shrink-0"
                />
                <h3 class="text-2xl sm:text-3xl font-black text-white leading-tight">
                  {{ need.title }}
                </h3>
              </div>
              <div class="p-5 rounded-2xl bg-slate-950/70 border border-slate-800 space-y-2">
                <span class="text-[11px] uppercase font-bold tracking-wider text-indigo-400 block">
                  Objetivo concreto de {{ need.userName }}:
                </span>
                <p class="text-sm text-slate-200 leading-relaxed">
                  {{ need.goal }}
                </p>
              </div>
              <div class="p-4 rounded-2xl bg-indigo-500/10 border border-indigo-500/25 text-xs text-indigo-200">
                💡 <strong>¿Sabés sobre este tema?</strong> Si le dedicás 1 hora a {{ need.userName }}, sumás <strong>+1 Crédito</strong> a tu balance para aprender lo que vos quieras.
              </div>
            </div>

            <div class="lg:col-span-5 bg-slate-950/90 border border-slate-800 rounded-2xl p-5 sm:p-6 space-y-4">
              <div v-if="teachNeedSuccess" class="py-6 text-center space-y-3">
                <CheckCircle2 class="w-10 h-10 text-emerald-400 mx-auto" />
                <h4 class="text-lg font-black text-white">¡Ofrecimiento Enviado!</h4>
                <p class="text-xs text-slate-300">
                  Ya coordinamos tu propuesta con {{ need.userName }} sin salir del lienzo.
                </p>
                <button
                  @click="spatialStore.openCapsule('sessions')"
                  class="px-4 py-2 rounded-xl bg-emerald-500 text-slate-950 font-black text-xs cursor-pointer"
                >
                  Ver en Mis Sesiones
                </button>
              </div>

              <template v-else>
                <div class="text-xs uppercase font-black tracking-wider text-indigo-400">
                  Ofrecer Enseñar (+1 Crédito)
                </div>

                <div v-if="bookingError" class="p-3 rounded-xl bg-rose-500/15 text-xs text-rose-300">
                  {{ bookingError }}
                </div>

                <div class="grid grid-cols-2 gap-3">
                  <div>
                    <label class="text-[11px] text-slate-400 block mb-1">Fecha propuesta</label>
                    <input v-model="teachNeedDate" type="date" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
                  </div>
                  <div>
                    <label class="text-[11px] text-slate-400 block mb-1">Hora</label>
                    <input v-model="teachNeedTime" type="time" class="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white" />
                  </div>
                </div>

                <button
                  @click="handleOfferToTeachNeedInPlace(need)"
                  class="w-full py-3.5 rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-400 hover:to-purple-500 text-white font-black text-sm shadow-lg shadow-indigo-500/20 transition-all cursor-pointer flex items-center justify-center gap-2"
                >
                  <UserCheck class="w-4 h-4" />
                  <span>{{ authStore.isGuest ? 'Ingresar y Ofrecer Mentoría' : 'Ofrecer Enseñar en 1 Clic' }}</span>
                </button>
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
