<script setup>
import { ref, computed } from 'vue'
import {
  Sparkles,
  ArrowRight,
  RefreshCw,
  Coins,
  CheckCircle2,
  Star
} from 'lucide-vue-next'
import { useSpatialStore } from '../../stores/spatialStore'
import { usePlatformStore } from '../../stores/platformStore'

const spatialStore = useSpatialStore()
const platformStore = usePlatformStore()

const mySkills = [
  { id: 'web', name: 'Vue 3 & Web', icon: '💻' },
  { id: 'design', name: 'Figma & UX/UI', icon: '🎨' },
  { id: 'devops', name: 'Docker & Linux', icon: '🐳' },
  { id: 'git', name: 'Git & Equipos', icon: '🐙' },
  { id: 'biz', name: 'Scrum & Agile', icon: '📊' }
]

const wantSkills = [
  { id: 'english', name: 'Inglés para IT', keyword: 'Inglés', icon: '🗣️', partner: 'Elena Rostova', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=120&auto=format&fit=crop&q=80', rep: 4.8 },
  { id: 'python', name: 'Vue 3 Avanzado', keyword: 'Vue', icon: '⚡', partner: 'Juan Carlos', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&auto=format&fit=crop&q=80', rep: 4.9 },
  { id: 'devops_learn', name: 'Docker desde Cero', keyword: 'Docker', icon: '🐳', partner: 'Carlos Mendoza', avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&auto=format&fit=crop&q=80', rep: 4.7 },
  { id: 'soft', name: 'Oratoria & Pitch', keyword: 'Inglés', icon: '🎯', partner: 'Elena Rostova', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=120&auto=format&fit=crop&q=80', rep: 4.8 }
]

const selectedMySkill = ref(mySkills[0])
const selectedWantSkill = ref(wantSkills[0])

const matchScore = computed(() => {
  if (selectedMySkill.value.id === 'web' && selectedWantSkill.value.id === 'english') return 96
  if (selectedMySkill.value.id === 'design' && selectedWantSkill.value.id === 'soft') return 92
  if (selectedMySkill.value.id === 'devops' && selectedWantSkill.value.id === 'python') return 94
  return 91
})

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
      `⚡ Match ${matchScore.value}% con ${matchedOffer.userName}`,
      'Elegí horario ahí mismo.'
    )
  } else {
    spatialStore.filterAndFocusCatalog(keyword)
  }
}
</script>

<template>
  <div id="spatial-simulator-section" class="scroll-mt-24 rounded-3xl border border-slate-700/60 bg-gradient-to-b from-slate-900/90 to-slate-950/95 p-5 sm:p-7 shadow-2xl backdrop-blur-xl relative overflow-hidden">
    <!-- Cabecera compacta sin párrafo largo -->
    <div class="flex flex-wrap items-center justify-between gap-3 mb-5">
      <div class="flex items-center gap-2.5">
        <span class="text-2xl">⚡</span>
        <div>
          <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight leading-none">
            Probá tu Match: Enseño ⇄ Aprendo
          </h3>
          <span class="text-[11px] text-slate-400">Tocá qué das y qué buscás para ver con quién conectás hoy</span>
        </div>
      </div>

      <div class="flex items-center gap-1.5 bg-amber-500/10 px-3 py-1.5 rounded-xl border border-amber-500/25 text-xs font-black text-amber-300">
        <Coins class="w-3.5 h-3.5 text-amber-400" />
        <span>1h = 1 🪙</span>
      </div>
    </div>

    <!-- Selector Visual de 2 Columnas con Chips Rápidos -->
    <div class="grid grid-cols-1 lg:grid-cols-11 gap-4 items-center">
      <!-- Lo que enseño -->
      <div class="lg:col-span-5 bg-slate-950/70 border border-slate-800 p-4 rounded-2xl">
        <div class="text-xs font-black uppercase text-emerald-400 mb-3 flex items-center gap-1.5">
          <span>🎓 1. Yo puedo enseñar:</span>
        </div>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="skill in mySkills"
            :key="skill.id"
            @click="selectedMySkill = skill; spatialStore.triggerFlash('simulator-result', '⚡ ¡Match recalculado!')"
            class="px-3.5 py-2.5 rounded-xl text-xs font-bold transition-all flex items-center gap-2 border cursor-pointer"
            :class="selectedMySkill.id === skill.id
              ? 'bg-emerald-500 text-slate-950 border-emerald-400 font-black scale-105 shadow-md'
              : 'bg-slate-900 border-slate-800 text-slate-300 hover:text-white'"
          >
            <span class="text-base">{{ skill.icon }}</span>
            <span>{{ skill.name }}</span>
          </button>
        </div>
      </div>

      <!-- Conector -->
      <div class="lg:col-span-1 flex flex-col items-center justify-center">
        <div class="w-10 h-10 rounded-full bg-gradient-to-r from-emerald-500 to-indigo-600 flex items-center justify-center text-white font-black text-sm shadow-lg">
          ⇄
        </div>
      </div>

      <!-- Lo que quiero aprender -->
      <div class="lg:col-span-5 bg-slate-950/70 border border-slate-800 p-4 rounded-2xl">
        <div class="text-xs font-black uppercase text-indigo-400 mb-3 flex items-center gap-1.5">
          <span>🚀 2. Quiero aprender:</span>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
          <button
            v-for="skill in wantSkills"
            :key="skill.id"
            @click="selectedWantSkill = skill; spatialStore.triggerFlash('simulator-result', '⚡ ¡Match recalculado!')"
            class="p-2.5 rounded-xl text-left transition-all flex items-center gap-2.5 border cursor-pointer"
            :class="selectedWantSkill.id === skill.id
              ? 'bg-indigo-500/25 border-indigo-400 text-white shadow-sm'
              : 'bg-slate-900 border-slate-800 text-slate-300 hover:text-white'"
          >
            <img :src="skill.avatar" class="w-8 h-8 rounded-full object-cover border border-indigo-400/50 shrink-0" />
            <div class="min-w-0">
              <div class="text-xs font-bold truncate">{{ skill.icon }} {{ skill.name }}</div>
              <div class="text-[10px] text-amber-400 font-semibold">★ {{ skill.rep }} · {{ skill.partner.split(' ')[0] }}</div>
            </div>
          </button>
        </div>
      </div>
    </div>

    <!-- Resultado Humano Instantáneo -->
    <div
      class="mt-5 bg-slate-950/90 border border-emerald-500/30 rounded-2xl p-4 flex flex-wrap items-center justify-between gap-4 transition-all"
      :class="spatialStore.flashingKey === 'simulator-result' ? 'spatial-flash-blink border-emerald-400' : ''"
    >
      <div class="flex items-center gap-3.5">
        <img :src="selectedWantSkill.avatar" class="w-12 h-12 rounded-2xl object-cover border-2 border-emerald-400 shadow-md" />
        <div>
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded-md bg-emerald-500 text-slate-950 text-xs font-black">
              {{ matchScore }}% Match
            </span>
            <span class="text-sm font-black text-white">{{ selectedWantSkill.partner }}</span>
            <span class="text-xs font-bold text-amber-400">★ {{ selectedWantSkill.rep }}</span>
          </div>
          <div class="flex flex-wrap items-center gap-2 text-xs text-slate-300 mt-1">
            <span class="text-emerald-400 font-bold">🎓 Vos das: {{ selectedMySkill.name }}</span>
            <span>⇄</span>
            <span class="text-indigo-300 font-bold">🚀 Recibís: {{ selectedWantSkill.name }}</span>
          </div>
        </div>
      </div>

      <button
        @click="handleStartExchangeInPlace"
        class="w-full sm:w-auto px-5 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-xs sm:text-sm transition-all shadow-lg flex items-center justify-center gap-2 cursor-pointer"
      >
        <span>Conectar con {{ selectedWantSkill.partner.split(' ')[0] }} arriba</span>
        <ArrowRight class="w-4 h-4" />
      </button>
    </div>
  </div>
</template>
