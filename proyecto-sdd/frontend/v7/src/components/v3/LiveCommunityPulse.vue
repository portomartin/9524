<script setup>
import {
  Users,
  Coins,
  Star,
  ArrowUpRight,
  ArrowRight,
  Maximize2,
  Minimize2,
  CheckCircle2,
  Sparkles
} from 'lucide-vue-next'
import { useSpatialStore } from '../../stores/spatialStore'
import { usePlatformStore } from '../../stores/platformStore'
import HandDrawnIcon from '../ui/HandDrawnIcon.vue'

const spatialStore = useSpatialStore()
const platformStore = usePlatformStore()

const liveExchanges = [
  {
    id: 1,
    title: 'Vue 3 & Frontend Reactivo 🔁 Inglés para IT',
    keyword: 'Vue',
    story: 'Juan necesitaba preparar una entrevista técnica en inglés y Elena quería modernizar su portfolio web en Vue 3. Coordinaron 1 hora de código por 1 hora de conversación técnica sin usar un centavo.',
    userA: { name: 'Juan Carlos', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80', badge: 'Frontend Dev', rep: 4.9 },
    userB: { name: 'Elena Rostova', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&auto=format&fit=crop&q=80', badge: 'Traductora & Coach', rep: 4.8 },
    category: 'Tecnología / Idiomas',
    status: 'Hoy 18:00 hs',
    credits: '1 Crédito transferido'
  },
  {
    id: 2,
    title: 'Docker & Linux en Servidores 🔁 Diseño UX con Figma',
    keyword: 'Docker',
    story: 'Carlos ayudó a Lucía a desplegar su propio entorno en contenedores Docker, y Lucía rediseñó en vivo el flujo de usuario del dashboard de Carlos en Figma.',
    userA: { name: 'Carlos Mendoza', avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80', badge: 'DevOps Senior', rep: 4.6 },
    userB: { name: 'Lucía Fernández', avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&auto=format&fit=crop&q=80', badge: 'Product Designer', rep: 4.9 },
    category: 'Infraestructura / Diseño',
    status: 'Confirmada',
    credits: '1 Crédito en garantía'
  },
  {
    id: 3,
    title: 'Python & FastAPI 🔁 Estrategia de Producto & Agile',
    keyword: 'Inglés',
    story: 'Martín compartió patrones limpios de APIs con FastAPI mientras Sofía lo guió en cómo estructurar el backlog y las métricas de su equipo.',
    userA: { name: 'Martín Gómez', avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80', badge: 'Backend Lead', rep: 4.8 },
    userB: { name: 'Sofía Valenzuela', avatar: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=150&auto=format&fit=crop&q=80', badge: 'Scrum Master', rep: 4.9 },
    category: 'Backend / Gestión',
    status: 'En curso ahora',
    credits: 'Intercambio activo'
  }
]

function handleJoinSimilarInPlace(keyword) {
  spatialStore.searchQuery = ''
  const matchingOffer = platformStore.offers.find(
    o => o.title.toLowerCase().includes(keyword.toLowerCase()) || o.category.toLowerCase().includes(keyword.toLowerCase())
  ) || platformStore.offers[0]

  if (matchingOffer) {
    spatialStore.expandSpecificItem('offer', matchingOffer.id)
    spatialStore.notify('Propuesta amplificada en tu lienzo', `Abrimos "${matchingOffer.title}" acá mismo para que puedas sumarte.`)
  } else {
    spatialStore.filterAndFocusCatalog(keyword)
  }
}
</script>

<template>
  <section class="relative rounded-3xl overflow-hidden border border-slate-800 bg-gradient-to-b from-slate-900 via-slate-900/95 to-slate-950 p-6 md:p-12 shadow-2xl space-y-8">
    <!-- Ambient Glow -->
    <div class="absolute -top-32 -left-32 w-96 h-96 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-500/15 rounded-full blur-3xl pointer-events-none"></div>

    <!-- Section Title -->
    <div class="relative z-10 flex flex-wrap items-end justify-between gap-4">
      <div class="space-y-2">
        <div class="flex items-start gap-4">
          <div
            class="w-12 h-12 sm:w-14 sm:h-14 rounded-2xl bg-emerald-500/15 border-2 border-dashed border-emerald-500/45 text-emerald-400 flex items-center justify-center shrink-0 shadow-inner -rotate-2"
            title="Bloque Principal · Intercambios en Vivo"
          >
            <HandDrawnIcon name="exchanges" size="lg" />
          </div>
          <h2 class="text-3xl sm:text-4xl font-black text-white tracking-tight leading-[1.12]">
            Intercambios que están pasando hoy.
            <span class="block bg-gradient-to-r from-emerald-400 via-teal-300 to-indigo-400 bg-clip-text text-transparent">
              Historias reales de par a par.
            </span>
          </h2>
        </div>
        <p class="text-slate-300 text-sm sm:text-base max-w-2xl leading-relaxed">
          Mirá cómo personas reales conectan sus habilidades sin dinero de por medio. Tocá una tarjeta para amplificar su historia acá adentro o sumarte a una propuesta similar.
        </p>
      </div>

      <button
        @click="spatialStore.filterAndFocusCatalog('')"
        class="inline-flex items-center gap-1.5 text-xs font-bold text-emerald-400 hover:text-emerald-300 transition-colors cursor-pointer bg-transparent border-none"
      >
        Ir al tablero interactivo de arriba
        <ArrowRight class="w-4 h-4" />
      </button>
    </div>

    <!-- 3 Highlighted Live Exchange Cards (Contained inside the Master Section Panel) -->
    <div class="relative z-10 grid grid-cols-1 md:grid-cols-3 gap-6 items-start">
      <div
        v-for="exchange in liveExchanges"
        :key="exchange.id"
        @click="spatialStore.toggleExchangeCard(exchange.id)"
        class="group relative rounded-2xl border transition-all duration-500 flex flex-col justify-between shadow-md cursor-pointer"
        :class="[
          spatialStore.expandedExchangeId === exchange.id
            ? 'md:col-span-3 border-emerald-500/60 bg-slate-950/90 p-6 md:p-8 ring-2 ring-emerald-500/20'
            : 'border-slate-800 bg-slate-950/75 p-5 hover:border-slate-700 hover:bg-slate-950',
          spatialStore.flashingKey === `exchange-${exchange.id}` ? 'spatial-flash-blink' : ''
        ]"
      >
        <!-- Top Status Bar -->
        <div>
          <div class="flex items-center justify-between text-xs mb-3">
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-slate-800 text-slate-300 font-semibold text-[11px]">
              <HandDrawnIcon name="exchanges" size="xs" class="text-emerald-400" />
              <span>{{ exchange.category }}</span>
            </span>
            <div class="flex items-center gap-2">
              <span class="flex items-center gap-1 text-[11px] font-semibold text-emerald-400 bg-emerald-500/10 px-2.5 py-0.5 rounded-full">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                {{ exchange.status }}
              </span>
              <span class="text-slate-400 hover:text-white">
                <Minimize2 v-if="spatialStore.expandedExchangeId === exchange.id" class="w-4 h-4 text-emerald-400" />
                <Maximize2 v-else class="w-3.5 h-3.5 opacity-60 group-hover:opacity-100" />
              </span>
            </div>
          </div>

          <!-- Exchange Title -->
          <h3
            class="font-extrabold text-white group-hover:text-emerald-300 transition-colors mb-4 leading-snug"
            :class="spatialStore.expandedExchangeId === exchange.id ? 'text-xl sm:text-2xl' : 'text-base line-clamp-2'"
          >
            {{ exchange.title }}
          </h3>

          <!-- Two Users Connected View -->
          <div
            class="bg-slate-950/70 p-4 rounded-xl border border-slate-800/80 mb-4"
            :class="spatialStore.expandedExchangeId === exchange.id ? 'grid grid-cols-1 md:grid-cols-3 gap-4 items-center' : 'space-y-3'"
          >
            <!-- User A -->
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2.5">
                <img :src="exchange.userA.avatar" :alt="exchange.userA.name" class="w-9 h-9 rounded-full object-cover border border-slate-700" />
                <div>
                  <div class="text-xs font-bold text-slate-200">{{ exchange.userA.name }}</div>
                  <div class="text-[10px] text-slate-400">{{ exchange.userA.badge }}</div>
                </div>
              </div>
              <span class="text-xs font-semibold text-amber-400 flex items-center gap-0.5">
                <Star class="w-3 h-3 fill-amber-400" /> {{ exchange.userA.rep }}
              </span>
            </div>

            <!-- Arrow divider -->
            <div class="flex items-center justify-center gap-2 text-[10px] text-emerald-400 font-bold uppercase tracking-wider bg-emerald-500/10 py-1.5 px-3 rounded-lg">
              <span class="inline-flex items-center gap-1 text-emerald-400" title="Enseña">
                <HandDrawnIcon name="teach" size="xs" />
              </span>
              <HandDrawnIcon name="exchanges" size="xs" />
              <span>Trueque 1 Hora = 1 Crédito</span>
              <span class="inline-flex items-center gap-1 text-indigo-400" title="Aprende">
                <HandDrawnIcon name="learn" size="xs" />
              </span>
            </div>

            <!-- User B -->
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2.5">
                <img :src="exchange.userB.avatar" :alt="exchange.userB.name" class="w-9 h-9 rounded-full object-cover border border-slate-700" />
                <div>
                  <div class="text-xs font-bold text-slate-200">{{ exchange.userB.name }}</div>
                  <div class="text-[10px] text-slate-400">{{ exchange.userB.badge }}</div>
                </div>
              </div>
              <span class="text-xs font-semibold text-amber-400 flex items-center gap-0.5">
                <Star class="w-3 h-3 fill-amber-400" /> {{ exchange.userB.rep }}
              </span>
            </div>
          </div>

          <!-- Expanded Story Details In-Place -->
          <div
            v-if="spatialStore.expandedExchangeId === exchange.id"
            class="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/25 mb-4 flex flex-wrap items-center justify-between gap-4"
            @click.stop
          >
            <div class="max-w-2xl space-y-1">
              <div class="text-xs font-bold text-emerald-300 flex items-center gap-1.5">
                <Sparkles class="w-3.5 h-3.5" /> Historia de este intercambio en vivo:
              </div>
              <p class="text-xs sm:text-sm text-slate-200 leading-relaxed">
                {{ exchange.story }}
              </p>
            </div>
            <button
              @click="handleJoinSimilarInPlace(exchange.keyword)"
              class="px-5 py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs cursor-pointer transition-all shadow-md"
            >
              Amplificar propuesta similar abajo →
            </button>
          </div>
        </div>

        <!-- Footer Card -->
        <div class="pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs">
          <div class="flex items-center gap-1.5 text-slate-400 text-[11px]">
            <Coins class="w-3.5 h-3.5 text-amber-400" />
            <span>{{ exchange.credits }}</span>
          </div>

          <button
            @click.stop="handleJoinSimilarInPlace(exchange.keyword)"
            class="text-xs font-bold text-emerald-400 hover:text-emerald-300 flex items-center gap-1 transition-colors cursor-pointer bg-transparent border-none"
          >
            <span>Sumarme aquí mismo</span>
            <ArrowUpRight class="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  </section>
</template>
