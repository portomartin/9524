<script setup>
import {
  Star,
  ArrowUpRight,
  Maximize2,
  Minimize2
} from 'lucide-vue-next'
import { useSpatialStore } from '../../stores/spatialStore'
import { usePlatformStore } from '../../stores/platformStore'

const spatialStore = useSpatialStore()
const platformStore = usePlatformStore()

const liveExchanges = [
  {
    id: 1,
    skillA: '💻 Vue 3',
    skillB: '🗣️ Inglés IT',
    keyword: 'Vue',
    story: 'Juan preparó su entrevista en inglés con Elena y a cambio la ayudó a armar su web en Vue 3.',
    userA: { name: 'Juan', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80', rep: 4.9 },
    userB: { name: 'Elena', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&auto=format&fit=crop&q=80', rep: 4.8 },
    status: 'Hoy 18:00'
  },
  {
    id: 2,
    skillA: '🐳 Docker',
    skillB: '🎨 Figma UX',
    keyword: 'Docker',
    story: 'Carlos configuró los contenedores de Lucía y ella diseñó el flujo visual del sistema de Carlos.',
    userA: { name: 'Carlos', avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80', rep: 4.6 },
    userB: { name: 'Lucía', avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&auto=format&fit=crop&q=80', rep: 4.9 },
    status: 'Confirmado'
  },
  {
    id: 3,
    skillA: '🐍 FastAPI',
    skillB: '📊 Agile',
    keyword: 'Inglés',
    story: 'Martín enseñó arquitectura de APIs en Python y Sofía lo ayudó a organizar su roadmap.',
    userA: { name: 'Martín', avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80', rep: 4.8 },
    userB: { name: 'Sofía', avatar: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=150&auto=format&fit=crop&q=80', rep: 4.9 },
    status: 'En vivo'
  }
]

function handleJoinSimilarInPlace(keyword) {
  spatialStore.searchQuery = ''
  const matchingOffer = platformStore.offers.find(
    o => o.title.toLowerCase().includes(keyword.toLowerCase()) || o.category.toLowerCase().includes(keyword.toLowerCase())
  ) || platformStore.offers[0]

  if (matchingOffer) {
    spatialStore.expandSpecificItem('offer', matchingOffer.id)
    spatialStore.notify(`⚡ ${matchingOffer.title}`, 'Amplificado en el tablero.')
  }
}
</script>

<template>
  <div class="my-4">
    <!-- Cabecera directa sin párrafo largo -->
    <div class="flex items-center justify-between gap-4 mb-4">
      <div class="flex items-center gap-2.5">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
        <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight">
          Trueques Humanos de Hoy
        </h2>
      </div>
      <span class="text-xs text-slate-400 hidden sm:inline">Tocá para ver historia ⤢</span>
    </div>

    <!-- 3 Tarjetas Cara a Cara (Se entienden en 0.5 seg) -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-start">
      <div
        v-for="ex in liveExchanges"
        :key="ex.id"
        @click="spatialStore.toggleExchangeCard(ex.id)"
        class="group rounded-2xl border transition-all duration-300 p-4 cursor-pointer"
        :class="[
          spatialStore.expandedExchangeId === ex.id
            ? 'md:col-span-3 border-emerald-500/60 bg-slate-900 p-6'
            : 'border-slate-800 bg-slate-900/60 hover:border-slate-700',
          spatialStore.flashingKey === `exchange-${ex.id}` ? 'spatial-flash-blink' : ''
        ]"
      >
        <div class="flex items-center justify-between mb-3">
          <span class="text-[11px] font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-0.5 rounded-full">
            ● {{ ex.status }}
          </span>
          <span class="text-xs font-bold text-amber-300">🪙 1h ⇄ 1h</span>
        </div>

        <!-- Cara a Cara Visual -->
        <div class="flex items-center justify-between gap-2 bg-slate-950/80 p-3 rounded-xl border border-slate-800">
          <div class="flex items-center gap-2">
            <img :src="ex.userA.avatar" class="w-10 h-10 rounded-full object-cover border border-emerald-400" />
            <div>
              <div class="text-xs font-black text-white">{{ ex.userA.name }}</div>
              <div class="text-[11px] font-bold text-emerald-400">{{ ex.skillA }}</div>
            </div>
          </div>

          <div class="px-2 py-1 rounded-lg bg-slate-900 text-slate-300 font-black text-xs">
            ⇄
          </div>

          <div class="flex items-center gap-2 text-right">
            <div>
              <div class="text-xs font-black text-white">{{ ex.userB.name }}</div>
              <div class="text-[11px] font-bold text-indigo-300">{{ ex.skillB }}</div>
            </div>
            <img :src="ex.userB.avatar" class="w-10 h-10 rounded-full object-cover border border-indigo-400" />
          </div>
        </div>

        <!-- Historia expandida solo al tocar -->
        <div
          v-if="spatialStore.expandedExchangeId === ex.id"
          class="mt-4 pt-3 border-t border-slate-800 flex flex-wrap items-center justify-between gap-3"
          @click.stop
        >
          <p class="text-xs text-slate-200">{{ ex.story }}</p>
          <button
            @click="handleJoinSimilarInPlace(ex.keyword)"
            class="px-4 py-2 rounded-xl bg-emerald-500 text-slate-950 font-black text-xs cursor-pointer"
          >
            Sumarme a uno similar ↑
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
