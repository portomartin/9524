<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import {
  Sparkles,
  ArrowRight,
  RefreshCw,
  Clock,
  Coins,
  ShieldCheck,
  CheckCircle2,
  Users2
} from 'lucide-vue-next'

const router = useRouter()

const mySkills = [
  { id: 'web', name: 'Desarrollo Web / Vue', icon: '💻', category: 'Tecnología' },
  { id: 'design', name: 'Diseño UX/UI & Figma', icon: '🎨', category: 'Diseño' },
  { id: 'devops', name: 'Docker & Linux', icon: '🐳', category: 'Infraestructura' },
  { id: 'git', name: 'Git & Trabajo Colaborativo', icon: '🐙', category: 'Herramientas' },
  { id: 'biz', name: 'Gestión Ágil & Scrum', icon: '📊', category: 'Negocios' }
]

const wantSkills = [
  { id: 'english', name: 'Inglés para IT & Conversación', icon: '🗣️', partner: 'Elena Rostova', badge: 'Instructora Nativa', rep: 4.8 },
  { id: 'python', name: 'Python Backend & APIs', icon: '🐍', partner: 'Martín Gómez', badge: 'Dev Senior', rep: 4.9 },
  { id: 'crypto', name: 'Finanzas & Cripto Básico', icon: '📈', partner: 'Lucía Fernández', badge: 'Analista', rep: 4.7 },
  { id: 'soft', name: 'Oratoria & Liderazgo', icon: '🎯', partner: 'Carlos Mendoza', badge: 'Coach', rep: 4.6 }
]

const selectedMySkill = ref(mySkills[0])
const selectedWantSkill = ref(wantSkills[0])
const isSimulating = ref(false)

const matchScore = computed(() => {
  if (selectedMySkill.value.id === 'web' && selectedWantSkill.value.id === 'english') return 96
  if (selectedMySkill.value.id === 'design' && selectedWantSkill.value.id === 'soft') return 92
  if (selectedMySkill.value.id === 'devops' && selectedWantSkill.value.id === 'python') return 94
  return 88
})

function handleGoToExplore() {
  router.push({ name: 'explore' })
}

function handleStartExchange() {
  router.push({
    name: 'search',
    query: { q: selectedWantSkill.value.name }
  })
}
</script>

<template>
  <div class="rounded-3xl border border-slate-700/60 bg-gradient-to-b from-slate-900/90 to-slate-950/95 p-6 md:p-8 shadow-2xl backdrop-blur-xl relative overflow-hidden">
    <!-- Glow effect in background -->
    <div class="absolute -top-24 -right-24 w-72 h-72 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-24 -left-24 w-72 h-72 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none"></div>

    <!-- Header bar -->
    <div class="flex flex-wrap items-center justify-between gap-4 mb-8">
      <div>
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 mb-2">
          <Sparkles class="w-3.5 h-3.5" />
          Playground Interactivo de Trueque
        </div>
        <h3 class="text-2xl font-black text-white tracking-tight">
          Simulá tu intercambio en 2 clics
        </h3>
        <p class="text-slate-400 text-sm mt-1">
          Elegí lo que podés enseñar y lo que buscás aprender. La plataforma calcula tu match recíproco al instante.
        </p>
      </div>

      <div class="flex items-center gap-2 bg-slate-800/80 px-3.5 py-1.5 rounded-xl border border-slate-700/60 text-xs text-slate-300">
        <Coins class="w-4 h-4 text-amber-400" />
        <span><strong>1 Hora</strong> compartida = <strong>1 Crédito</strong> ganado</span>
      </div>
    </div>

    <!-- Interactive Two-Column Selector -->
    <div class="grid grid-cols-1 lg:grid-cols-11 gap-6 items-center">
      <!-- Left: Lo que enseño -->
      <div class="lg:col-span-5 bg-slate-900/70 border border-slate-800 p-5 rounded-2xl">
        <div class="flex items-center justify-between mb-3">
          <span class="text-xs uppercase font-bold tracking-wider text-emerald-400">Paso 1 · Lo que vos ofrecés</span>
          <span class="text-[11px] text-slate-400">Hacé clic para cambiar</span>
        </div>

        <div class="space-y-2">
          <button
            v-for="skill in mySkills"
            :key="skill.id"
            @click="selectedMySkill = skill"
            class="w-full text-left px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all flex items-center justify-between border"
            :class="selectedMySkill.id === skill.id
              ? 'bg-emerald-500/15 border-emerald-500/60 text-white shadow-sm'
              : 'bg-slate-950/40 border-slate-800/80 text-slate-300 hover:bg-slate-800/50 hover:border-slate-700'"
          >
            <div class="flex items-center gap-2.5">
              <span class="text-lg">{{ skill.icon }}</span>
              <span>{{ skill.name }}</span>
            </div>
            <span class="text-[10px] text-slate-400 font-normal uppercase">{{ skill.category }}</span>
          </button>
        </div>
      </div>

      <!-- Center: Connector Animation -->
      <div class="lg:col-span-1 flex flex-col items-center justify-center gap-2">
        <div class="w-10 h-10 rounded-full bg-gradient-to-r from-emerald-500 to-indigo-600 flex items-center justify-center text-white shadow-lg shadow-emerald-500/20">
          <RefreshCw class="w-5 h-5 animate-spin-slow" />
        </div>
        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 text-center">Trueque 1:1</span>
      </div>

      <!-- Right: Lo que busco -->
      <div class="lg:col-span-5 bg-slate-900/70 border border-slate-800 p-5 rounded-2xl">
        <div class="flex items-center justify-between mb-3">
          <span class="text-xs uppercase font-bold tracking-wider text-indigo-400">Paso 2 · Lo que querés aprender</span>
          <span class="text-[11px] text-slate-400">Hacé clic para cambiar</span>
        </div>

        <div class="space-y-2">
          <button
            v-for="skill in wantSkills"
            :key="skill.id"
            @click="selectedWantSkill = skill"
            class="w-full text-left px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all flex items-center justify-between border"
            :class="selectedWantSkill.id === skill.id
              ? 'bg-indigo-500/15 border-indigo-500/60 text-white shadow-sm'
              : 'bg-slate-950/40 border-slate-800/80 text-slate-300 hover:bg-slate-800/50 hover:border-slate-700'"
          >
            <div class="flex items-center gap-2.5">
              <span class="text-lg">{{ skill.icon }}</span>
              <div>
                <div class="leading-tight">{{ skill.name }}</div>
                <div class="text-[11px] text-slate-400 font-normal">con {{ skill.partner }}</div>
              </div>
            </div>
            <div class="text-right">
              <span class="text-xs font-bold text-amber-400">★ {{ skill.rep }}</span>
            </div>
          </button>
        </div>
      </div>
    </div>

    <!-- Match Result Banner -->
    <div class="mt-8 pt-6 border-t border-slate-800/80 bg-slate-950/60 rounded-2xl p-5 flex flex-wrap items-center justify-between gap-6">
      <div class="flex items-center gap-4">
        <!-- Circular Score Badge -->
        <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-700 flex flex-col items-center justify-center text-white shadow-lg shadow-emerald-500/25 shrink-0">
          <span class="text-2xl font-black leading-none">{{ matchScore }}%</span>
          <span class="text-[9px] uppercase tracking-wider font-semibold opacity-90">Afinidad</span>
        </div>

        <div>
          <h4 class="text-lg font-bold text-white flex items-center gap-2">
            ¡Match Recíproco Detectado!
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
          @click="handleStartExchange"
          class="flex-1 sm:flex-none px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 text-slate-950 font-black text-sm transition-all shadow-lg shadow-emerald-500/25 flex items-center justify-center gap-2 cursor-pointer"
        >
          Proponer este intercambio
          <ArrowRight class="w-4 h-4" />
        </button>
        <button
          @click="handleGoToExplore"
          class="px-4 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-medium text-xs transition-all border border-slate-700 cursor-pointer"
        >
          Explorar todo
        </button>
      </div>
    </div>
  </div>
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
