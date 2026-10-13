<script setup>
import { ref, computed } from 'vue'
import {
  Sparkles,
  ArrowRight,
  RefreshCw,
  Clock,
  Coins,
  ShieldCheck,
  CheckCircle2
} from 'lucide-vue-next'
import { useSpatialStore } from '../../stores/spatialStore'
import { usePlatformStore } from '../../stores/platformStore'
import HandDrawnIcon from '../ui/HandDrawnIcon.vue'

const spatialStore = useSpatialStore()
const platformStore = usePlatformStore()

const mySkills = [
  { id: 'web', name: 'Desarrollo Web / Vue', icon: '💻', category: 'Tecnología' },
  { id: 'design', name: 'Diseño UX/UI & Figma', icon: '🎨', category: 'Diseño' },
  { id: 'devops', name: 'Docker & Linux', icon: '🐳', category: 'Infraestructura' },
  { id: 'git', name: 'Git & Trabajo Colaborativo', icon: '🐙', category: 'Herramientas' },
  { id: 'biz', name: 'Gestión Ágil & Scrum', icon: '📊', category: 'Negocios' }
]

const wantSkills = [
  { id: 'english', name: 'Inglés para IT & Conversación', keyword: 'Inglés', icon: '🗣️', partner: 'Elena Rostova', badge: 'Instructora Nativa', rep: 4.8 },
  { id: 'python', name: 'Vue 3 & Frontend Reactivo', keyword: 'Vue', icon: '⚡', partner: 'Juan Carlos', badge: 'Dev Senior', rep: 4.9 },
  { id: 'devops_learn', name: 'Docker & Contenedores', keyword: 'Docker', icon: '🐳', partner: 'Carlos Mendoza', badge: 'DevOps Lead', rep: 4.7 },
  { id: 'soft', name: 'Oratoria & Liderazgo', keyword: 'Inglés', icon: '🎯', partner: 'Elena Rostova', badge: 'Coach', rep: 4.8 }
]

const selectedMySkill = ref(mySkills[0])
const selectedWantSkill = ref(wantSkills[0])

const matchScore = computed(() => {
  if (selectedMySkill.value.id === 'web' && selectedWantSkill.value.id === 'english') return 96
  if (selectedMySkill.value.id === 'design' && selectedWantSkill.value.id === 'soft') return 92
  if (selectedMySkill.value.id === 'devops' && selectedWantSkill.value.id === 'python') return 94
  return 89
})

function handleGoToExploreInPlace() {
  spatialStore.clearFilters()
  spatialStore.filterAndFocusCatalog('')
}

function handleStartExchangeInPlace() {
  spatialStore.clearFilters()
  const keyword = selectedWantSkill.value.keyword || selectedWantSkill.value.name
  const matchedOffer = platformStore.offers.find(
    o =>
      o.title.toLowerCase().includes(keyword.toLowerCase()) ||
      (o.userName && o.userName.toLowerCase().includes(selectedWantSkill.value.partner.split(' ')[0].toLowerCase()))
  ) || platformStore.offers[0]

  if (matchedOffer) {
    spatialStore.expandSpecificItem('offer', matchedOffer.id)
    spatialStore.notify(
      `¡Match ${matchScore.value}% amplificado!`,
      `Desplegamos la propuesta de ${matchedOffer.userName} acá mismo para que elijas horario en 1 clic.`
    )
  } else {
    spatialStore.filterAndFocusCatalog(keyword)
  }
}
</script>

<template>
  <section id="spatial-simulator-section" class="scroll-mt-24 relative rounded-3xl overflow-hidden border border-slate-800 bg-gradient-to-b from-slate-900 via-slate-900/95 to-slate-950 p-6 md:p-12 shadow-2xl space-y-8">
    <!-- Ambient Glow -->
    <div class="absolute -top-32 -left-32 w-96 h-96 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-500/15 rounded-full blur-3xl pointer-events-none"></div>

    <!-- Header bar -->
    <div class="relative z-10 flex flex-wrap items-end justify-between gap-4">
      <div class="space-y-2">
        <div class="flex items-start gap-4">
          <div
            class="w-12 h-12 sm:w-14 sm:h-14 rounded-2xl bg-indigo-500/15 border-2 border-dashed border-indigo-500/45 text-indigo-400 flex items-center justify-center shrink-0 shadow-inner rotate-2"
            title="Bloque Principal · Simulador de Afinidad 1 a 1"
          >
            <HandDrawnIcon name="simulator" size="lg" />
          </div>
          <h2 class="text-3xl sm:text-4xl font-black text-white tracking-tight leading-[1.12]">
            Simulá tu intercambio en 2 clics.
            <span class="block bg-gradient-to-r from-emerald-400 via-teal-300 to-indigo-400 bg-clip-text text-transparent">
              Descubrí tu afinidad al instante.
            </span>
          </h2>
        </div>
        <p class="text-slate-300 text-sm sm:text-base max-w-2xl leading-relaxed">
          Elegí lo que podés enseñar y lo que buscás aprender. Al tocar "Amplificar propuesta", la tarjeta del mentor se despliega directamente en tu lienzo.
        </p>
      </div>

      <div class="flex items-center gap-2 bg-slate-950/80 px-4 py-2 rounded-xl border border-slate-800 text-xs text-slate-300">
        <HandDrawnIcon name="simulator" size="xs" class="text-indigo-400" />
        <Coins class="w-4 h-4 text-amber-400" />
        <span><strong>1 Hora</strong> compartida = <strong>1 Crédito</strong> ganado</span>
      </div>
    </div>

    <!-- Interactive Two-Column Selector -->
    <div class="relative z-10 grid grid-cols-1 lg:grid-cols-11 gap-6 items-center">
      <!-- Left: Lo que enseño -->
      <div class="lg:col-span-5 bg-slate-950/75 border border-slate-800 p-5 rounded-2xl">
        <div class="flex items-center justify-between mb-3.5">
          <span class="inline-flex items-center gap-2 text-xs uppercase font-black tracking-wider text-emerald-400">
            <span class="w-8 h-8 rounded-xl bg-emerald-500/15 border-2 border-emerald-500/45 text-emerald-400 flex items-center justify-center shrink-0">
              <HandDrawnIcon name="teach" size="sm" />
            </span>
            <span>Paso 1 · Lo que vos enseñás</span>
          </span>
          <span class="inline-flex items-center gap-1 text-[11px] text-slate-400">
            <HandDrawnIcon name="simulator" size="xs" class="text-emerald-400/80" />
            <span>Hacé clic para cambiar</span>
          </span>
        </div>

        <div class="space-y-2">
          <button
            v-for="skill in mySkills"
            :key="skill.id"
            @click="selectedMySkill = skill; spatialStore.triggerFlash('simulator-result', '⚡ ¡Match recalculado!')"
            class="w-full text-left px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all flex items-center justify-between border cursor-pointer"
            :class="selectedMySkill.id === skill.id
              ? 'bg-emerald-500/15 border-emerald-500/60 text-white shadow-sm'
              : 'bg-slate-950/40 border-slate-800/80 text-slate-300 hover:bg-slate-800/50 hover:border-slate-700'"
          >
            <div class="flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-emerald-500/15 border border-emerald-500/45 text-emerald-400 flex items-center justify-center shrink-0">
                <HandDrawnIcon name="teach" size="sm" />
              </span>
              <span>{{ skill.name }}</span>
            </div>
            <span class="text-[10px] text-slate-400 font-normal uppercase flex items-center gap-1">
              <span>{{ skill.category }}</span>
              <HandDrawnIcon name="simulator" size="xs" class="text-emerald-400/70" />
            </span>
          </button>
        </div>
      </div>

      <!-- Center: Connector Animation -->
      <div class="lg:col-span-1 flex flex-col items-center justify-center gap-2">
        <div class="w-11 h-11 rounded-2xl bg-indigo-500/15 border-2 border-dashed border-indigo-500/50 flex items-center justify-center text-indigo-400 shadow-sm">
          <HandDrawnIcon name="simulator" size="md" />
        </div>
        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 text-center">Trueque 1:1</span>
      </div>

      <!-- Right: Lo que busco -->
      <div class="lg:col-span-5 bg-slate-950/75 border border-slate-800 p-5 rounded-2xl">
        <div class="flex items-center justify-between mb-3.5">
          <span class="inline-flex items-center gap-2 text-xs uppercase font-black tracking-wider text-indigo-400">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/15 border-2 border-indigo-500/45 text-indigo-400 flex items-center justify-center shrink-0">
              <HandDrawnIcon name="learn" size="sm" />
            </span>
            <span>Paso 2 · Lo que querés aprender</span>
          </span>
          <span class="inline-flex items-center gap-1 text-[11px] text-slate-400">
            <HandDrawnIcon name="simulator" size="xs" class="text-indigo-400/80" />
            <span>Hacé clic para cambiar</span>
          </span>
        </div>

        <div class="space-y-2">
          <button
            v-for="skill in wantSkills"
            :key="skill.id"
            @click="selectedWantSkill = skill; spatialStore.triggerFlash('simulator-result', '⚡ ¡Match recalculado!')"
            class="w-full text-left px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all flex items-center justify-between border cursor-pointer"
            :class="selectedWantSkill.id === skill.id
              ? 'bg-indigo-500/15 border-indigo-500/60 text-white shadow-sm'
              : 'bg-slate-950/40 border-slate-800/80 text-slate-300 hover:bg-slate-800/50 hover:border-slate-700'"
          >
            <div class="flex items-center gap-2.5">
              <span class="w-7 h-7 rounded-lg bg-indigo-500/15 border border-indigo-500/45 text-indigo-400 flex items-center justify-center shrink-0">
                <HandDrawnIcon name="learn" size="sm" />
              </span>
              <div>
                <div class="leading-tight">{{ skill.name }}</div>
                <div class="text-[11px] text-slate-400 font-normal">con {{ skill.partner }}</div>
              </div>
            </div>
            <div class="text-right flex items-center gap-1.5">
              <span class="text-xs font-bold text-amber-400">★ {{ skill.rep }}</span>
              <HandDrawnIcon name="simulator" size="xs" class="text-indigo-400/70" />
            </div>
          </button>
        </div>
      </div>
    </div>

    <!-- Match Result Banner -->
    <div
      class="relative z-10 pt-6 border-t border-slate-800/80 bg-slate-950/80 rounded-2xl p-5 flex flex-wrap items-center justify-between gap-6 transition-all"
      :class="spatialStore.flashingKey === 'simulator-result' ? 'spatial-flash-blink border border-emerald-400' : ''"
    >
      <div class="flex items-center gap-4">
        <!-- Circular Score Badge -->
        <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-700 flex flex-col items-center justify-center text-white shadow-lg shadow-emerald-500/25 shrink-0">
          <span class="text-2xl font-black leading-none">{{ matchScore }}%</span>
          <span class="text-[9px] uppercase tracking-wider font-semibold opacity-90">Afinidad</span>
        </div>

        <div>
          <h4 class="text-lg font-bold text-white flex items-center gap-2">
            <HandDrawnIcon name="simulator" size="sm" class="text-emerald-400" />
            <span>¡Match Recíproco Detectado!</span>
            <CheckCircle2 class="w-4 h-4 text-emerald-400 inline" />
          </h4>
          <p class="text-xs text-slate-300 mt-0.5">
            <strong>{{ selectedWantSkill.partner }}</strong> busca tus conocimientos en <span class="text-emerald-400 font-semibold">{{ selectedMySkill.name }}</span> y ofrece <span class="text-indigo-300 font-semibold">{{ selectedWantSkill.name }}</span>.
          </p>
          <div class="flex items-center gap-4 text-[11px] text-slate-400 mt-2">
            <span class="flex items-center gap-1"><Clock class="w-3.5 h-3.5 text-slate-500" /> Sesión 1 hora recomendada</span>
            <span class="flex items-center gap-1"><ShieldCheck class="w-3.5 h-3.5 text-emerald-400" /> Saldo garantizado</span>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center gap-3 w-full sm:w-auto">
        <button
          @click="handleStartExchangeInPlace"
          class="flex-1 sm:flex-none px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 text-slate-950 font-black text-sm transition-all shadow-lg shadow-emerald-500/25 flex items-center justify-center gap-2 cursor-pointer"
        >
          Amplificar propuesta acá mismo
          <ArrowRight class="w-4 h-4" />
        </button>
        <button
          @click="handleGoToExploreInPlace"
          class="px-4 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-medium text-xs transition-all border border-slate-700 cursor-pointer"
        >
          Ver tablero
        </button>
      </div>
    </div>
  </section>
</template>

<style scoped>
@keyframes spin-slow {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.animate-spin-slow {
  animation: spin-slow 12s linear infinite;
}
</style>
