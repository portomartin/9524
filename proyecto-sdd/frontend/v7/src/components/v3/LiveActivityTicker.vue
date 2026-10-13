<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { Sparkles, ArrowRight, Zap, CheckCircle2 } from 'lucide-vue-next'

const props = defineProps({
  activities: {
    type: Array,
    default: () => [
      { id: 1, userA: 'Juan Carlos', skillA: 'Vue 3', userB: 'Elena', skillB: 'Inglés para IT', time: 'Hace 3 min', type: 'match' },
      { id: 2, userA: 'Carlos M.', skillA: 'Docker & Linux', userB: 'Comunidad', skillB: 'Nueva oferta', time: 'Hace 8 min', type: 'offer' },
      { id: 3, userA: 'Lucía F.', skillA: 'Diseño UX/UI', userB: 'Martín', skillB: 'Python Backend', time: 'Hace 14 min', type: 'match' },
      { id: 4, userA: 'Mariana G.', skillA: 'Sesión Finalizada', userB: 'Crédito transferido', skillB: '5★ Calificación', time: 'Hace 22 min', type: 'success' },
      { id: 5, userA: 'Diego S.', skillA: 'Git Avanzado', userB: 'Comunidad', skillB: 'Agenda abierta hoy', time: 'Hace 30 min', type: 'availability' }
    ]
  }
})

const currentIndex = ref(0)
let timer = null

onMounted(() => {
  timer = setInterval(() => {
    currentIndex.value = (currentIndex.value + 1) % props.activities.length
  }, 4000)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})
</script>

<template>
  <div class="w-full bg-gradient-to-r from-emerald-950/80 via-slate-900 to-indigo-950/80 border-y border-emerald-500/20 px-4 py-2 text-xs text-slate-200 overflow-hidden relative backdrop-blur-md">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <!-- Live Indicator Badge -->
      <div class="flex items-center gap-2 shrink-0">
        <span class="relative flex h-2.5 w-2.5">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
        </span>
        <span class="font-bold uppercase tracking-wider text-[11px] text-emerald-400 flex items-center gap-1">
          <Zap class="w-3 h-3 inline" />
          En Vivo
        </span>
        <span class="text-slate-500 hidden sm:inline">|</span>
        <span class="text-slate-400 hidden sm:inline">Pulso de Intercambios</span>
      </div>

      <!-- Ticker Transition Item -->
      <div class="flex-1 overflow-hidden relative h-5 flex items-center">
        <transition name="fade" mode="out-in">
          <div :key="currentIndex" class="flex items-center gap-2 text-xs truncate">
            <template v-if="activities[currentIndex]?.type === 'match'">
              <span class="font-semibold text-white">{{ activities[currentIndex].userA }}</span>
              <span class="text-emerald-400 font-medium">({{ activities[currentIndex].skillA }})</span>
              <span class="text-slate-400">intercambió con</span>
              <span class="font-semibold text-white">{{ activities[currentIndex].userB }}</span>
              <span class="text-indigo-300 font-medium">({{ activities[currentIndex].skillB }})</span>
            </template>
            <template v-else-if="activities[currentIndex]?.type === 'offer'">
              <span class="font-semibold text-white">{{ activities[currentIndex].userA }}</span>
              <span class="text-slate-300">publicó nueva propuesta:</span>
              <span class="text-amber-300 font-medium underline underline-offset-2">{{ activities[currentIndex].skillA }}</span>
            </template>
            <template v-else>
              <CheckCircle2 class="w-3.5 h-3.5 text-emerald-400 shrink-0" />
              <span class="font-semibold text-white">{{ activities[currentIndex]?.userA }}</span>
              <span class="text-slate-300">·</span>
              <span class="text-emerald-300 font-medium">{{ activities[currentIndex]?.skillB }}</span>
            </template>

            <span class="text-[10px] bg-slate-800/90 text-slate-400 px-1.5 py-0.5 rounded ml-2 shrink-0">
              {{ activities[currentIndex]?.time }}
            </span>
          </div>
        </transition>
      </div>

      <!-- Live Community Count Pill -->
      <div class="hidden md:flex items-center gap-2 shrink-0 text-slate-300 text-[11px]">
        <span class="inline-block w-1.5 h-1.5 rounded-full bg-indigo-400"></span>
        <span><strong>148+ h</strong> transferidas hoy</span>
        <span class="text-slate-600">·</span>
        <span class="text-emerald-400 font-semibold">$0 gastados</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.35s ease, transform 0.35s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(6px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>
