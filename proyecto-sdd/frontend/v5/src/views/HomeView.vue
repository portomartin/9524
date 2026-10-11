<script setup>
import { ref } from 'vue'
import {
  Compass,
  UserPlus,
  Zap,
  Star,
  Sparkles,
  Plus,
  Calendar,
  Minimize2,
  ShieldCheck,
  ArrowRight,
  ArrowLeftRight
} from 'lucide-vue-next'
import { usePlatformStore } from '../stores/platformStore'
import { useAuthStore } from '../stores/authStore'
import { useSpatialStore } from '../stores/spatialStore'
import LiveActivityTicker from '../components/v3/LiveActivityTicker.vue'
import InteractiveMatchSimulator from '../components/v3/InteractiveMatchSimulator.vue'
import LiveCommunityPulse from '../components/v3/LiveCommunityPulse.vue'
import SpatialCapsuleStage from '../components/v4/SpatialCapsuleStage.vue'
import SpatialCatalogBento from '../components/v4/SpatialCatalogBento.vue'

const platformStore = usePlatformStore()
const authStore = useAuthStore()
const spatialStore = useSpatialStore()

const popularTopics = [
  { name: 'Vue 3', keyword: 'Vue', icon: '💻', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&auto=format&fit=crop&q=80' },
  { name: 'Inglés IT', keyword: 'Inglés', icon: '🗣️', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=80&auto=format&fit=crop&q=80' },
  { name: 'Docker', keyword: 'Docker', icon: '🐳', avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=80&auto=format&fit=crop&q=80' },
  { name: 'Diseño UX', keyword: 'Diseño', icon: '🎨', avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=80&auto=format&fit=crop&q=80' },
  { name: 'Python', keyword: 'Programación', icon: '🐍', avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&auto=format&fit=crop&q=80' }
]

const expandedTrustCard = ref(null)

function handleSelectTopicInPlace(keyword) {
  spatialStore.filterAndFocusCatalog(keyword)
  spatialStore.notify(`⚡ ${keyword}`, 'Filtrado en el tablero.')
}

function toggleTrustDetail(key) {
  expandedTrustCard.value = expandedTrustCard.value === key ? null : key
  if (expandedTrustCard.value) {
    spatialStore.triggerFlash('trust-detail', '⚡ Regla destacada')
  }
}
</script>

<template>
  <div class="max-w-7xl mx-auto flex flex-col gap-8 pb-16">
    <!-- Notificación Flotante Íntima -->
    <transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="opacity-0 translate-y-2 scale-95"
      enter-to-class="opacity-100 translate-y-0 scale-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0 scale-100"
      leave-to-class="opacity-0 translate-y-2 scale-95"
    >
      <div
        v-if="spatialStore.liveNotice"
        class="fixed bottom-6 right-6 z-50 max-w-xs rounded-2xl border border-emerald-500/50 bg-slate-900/95 backdrop-blur-xl p-3.5 shadow-2xl flex items-center gap-3"
      >
        <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0">
          <Sparkles class="w-4 h-4" />
        </div>
        <div>
          <div class="text-xs font-black text-white">{{ spatialStore.liveNotice.title }}</div>
          <p v-if="spatialStore.liveNotice.subtitle" class="text-[11px] text-slate-300">
            {{ spatialStore.liveNotice.subtitle }}
          </p>
        </div>
      </div>
    </transition>

    <!-- 1. Ticker en Vivo -->
    <LiveActivityTicker />

    <!-- 2. Escenario de Cápsulas Vivas -->
    <SpatialCapsuleStage />

    <!-- 3. Hero Visual Cognitivo ("Entra por los ojos en 1 segundo") -->
    <section class="relative rounded-3xl overflow-hidden border border-slate-800 bg-gradient-to-b from-slate-900 via-slate-900/95 to-slate-950 p-6 md:p-10 shadow-2xl">
      <div class="absolute -top-32 -left-32 w-96 h-96 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-500/15 rounded-full blur-3xl pointer-events-none"></div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative z-10">
        <!-- Columna Visual-Cognitiva -->
        <div class="lg:col-span-7 text-left space-y-5">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/25 text-emerald-400 text-xs font-bold">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>Personas reales · Trueque 1 a 1 · $0 Dinero</span>
          </div>

          <h1 class="text-4xl sm:text-5xl font-black text-white tracking-tight leading-[1.08]">
            Enseñás lo que sabés.
            <span class="block bg-gradient-to-r from-emerald-400 via-teal-300 to-indigo-400 bg-clip-text text-transparent">
              Aprendés lo que necesitás.
            </span>
          </h1>

          <!-- Infografía Visual de 3 Pasos (Reemplaza el párrafo largo) -->
          <div class="grid grid-cols-3 gap-2 sm:gap-3 pt-1">
            <div class="p-3 rounded-2xl bg-slate-950/75 border border-emerald-500/30 flex items-center gap-2.5">
              <span class="text-2xl">🎓</span>
              <div>
                <div class="text-xs font-black text-emerald-400">1. Enseñás</div>
                <div class="text-[11px] text-slate-300 font-semibold">1 hora tuya</div>
              </div>
            </div>

            <div class="p-3 rounded-2xl bg-slate-950/75 border border-amber-500/30 flex items-center gap-2.5">
              <span class="text-2xl">🪙</span>
              <div>
                <div class="text-xs font-black text-amber-400">2. Sumás</div>
                <div class="text-[11px] text-slate-300 font-semibold">+1 Crédito</div>
              </div>
            </div>

            <div class="p-3 rounded-2xl bg-slate-950/75 border border-indigo-500/30 flex items-center gap-2.5">
              <span class="text-2xl">🚀</span>
              <div>
                <div class="text-xs font-black text-indigo-400">3. Aprendés</div>
                <div class="text-[11px] text-slate-300 font-semibold">Con otro par</div>
              </div>
            </div>
          </div>

          <!-- Píldoras con Rostros Humanos + Íconos -->
          <div class="pt-1">
            <div class="flex flex-wrap items-center gap-2">
              <button
                v-for="topic in popularTopics"
                :key="topic.name"
                @click="handleSelectTopicInPlace(topic.keyword)"
                class="pl-1.5 pr-3 py-1.5 rounded-full border text-xs font-bold transition-all cursor-pointer flex items-center gap-2 shadow-xs"
                :class="spatialStore.searchQuery.toLowerCase() === topic.keyword.toLowerCase()
                  ? 'bg-emerald-500 text-slate-950 border-emerald-400 scale-105'
                  : 'bg-slate-800/90 hover:bg-slate-800 border-slate-700 text-white hover:border-emerald-500/50'"
              >
                <img :src="topic.avatar" :alt="topic.name" class="w-6 h-6 rounded-full object-cover" />
                <span>{{ topic.icon }} {{ topic.name }}</span>
              </button>
            </div>
          </div>

          <!-- Botones directos -->
          <div class="flex flex-wrap items-center gap-3 pt-2">
            <button
              @click="spatialStore.filterAndFocusCatalog('')"
              class="px-5 py-3 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-sm transition-all shadow-lg shadow-emerald-500/20 flex items-center gap-2 cursor-pointer"
            >
              <ArrowLeftRight class="w-4 h-4" />
              Ver Conexiones Abajo
            </button>

            <button
              v-if="authStore.isGuest"
              @click="spatialStore.toggleCapsule('auth')"
              class="px-5 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm transition-all flex items-center gap-2 cursor-pointer"
            >
              <UserPlus class="w-4 h-4" />
              Recibir +1 🪙 Gratis
            </button>

            <template v-else>
              <button
                @click="spatialStore.toggleCapsule('sessions')"
                class="px-4 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-white font-bold text-xs flex items-center gap-2 cursor-pointer"
              >
                📅 Mis Sesiones ({{ platformStore.sessions.length }})
              </button>
              <button
                @click="spatialStore.toggleCapsule('publish')"
                class="px-4 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs flex items-center gap-1.5 cursor-pointer"
              >
                ➕ Publicar
              </button>
            </template>
          </div>
        </div>

        <!-- Columna Derecha: Foto Humana + Puente Visual Enseño ⇄ Aprendo sobre la imagen -->
        <div class="lg:col-span-5 relative">
          <div
            @click="spatialStore.filterAndFocusCatalog('')"
            class="relative rounded-2xl overflow-hidden border border-slate-700 shadow-2xl group cursor-pointer"
          >
            <img
              src="/src/assets/images/hero-community.jpg"
              alt="Colaboración y mentoría entre pares"
              class="w-full h-72 sm:h-80 object-cover object-center group-hover:scale-105 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/95 via-slate-950/25 to-transparent"></div>

            <!-- Tarjeta Visual Superpuesta: Ejemplo real de Enseño ⇄ Aprendo -->
            <div class="absolute bottom-3 left-3 right-3 bg-slate-900/90 backdrop-blur-md p-3.5 rounded-xl border border-slate-700/80 flex items-center justify-between gap-2">
              <div class="flex items-center gap-2">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&auto=format&fit=crop&q=80" class="w-9 h-9 rounded-full object-cover border border-emerald-400" />
                <div>
                  <div class="text-[11px] font-black text-emerald-400">🎓 Enseña Vue 3</div>
                  <div class="text-[10px] text-slate-300">Juan · ★ 4.9</div>
                </div>
              </div>

              <div class="px-2 py-1 rounded-lg bg-slate-800 text-amber-300 text-xs font-black">
                ⇄ 1h
              </div>

              <div class="flex items-center gap-2 text-right">
                <div>
                  <div class="text-[11px] font-black text-indigo-300">🗣️ Enseña Inglés</div>
                  <div class="text-[10px] text-slate-300">Elena · ★ 4.8</div>
                </div>
                <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=80&auto=format&fit=crop&q=80" class="w-9 h-9 rounded-full object-cover border border-indigo-400" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Tablero Humano Enseño ⇄ Aprendo (Bento Expandible) -->
    <SpatialCatalogBento />

    <!-- 5. Simulador Visual "¿Esto me sirve?" (En 2 toques) -->
    <InteractiveMatchSimulator />

    <!-- 6. Trueques Reales de Hoy (Rostros Conectados) -->
    <LiveCommunityPulse />

    <!-- 7. Píldoras de Confianza con Íconos -->
    <section class="space-y-3">
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3">
        <button
          @click="toggleTrustDetail('money')"
          class="p-4 rounded-2xl border transition-all flex items-center gap-3.5 text-left cursor-pointer"
          :class="expandedTrustCard === 'money' ? 'border-emerald-500 bg-emerald-500/10' : 'border-slate-800 bg-slate-900/50 hover:border-slate-700'"
        >
          <span class="text-2xl">🚫💵</span>
          <div>
            <div class="text-sm font-black text-white">$0 Dinero</div>
            <div class="text-[11px] text-emerald-400 font-semibold">100% Tiempo</div>
          </div>
        </button>

        <button
          @click="toggleTrustDetail('one2one')"
          class="p-4 rounded-2xl border transition-all flex items-center gap-3.5 text-left cursor-pointer"
          :class="expandedTrustCard === 'one2one' ? 'border-indigo-500 bg-indigo-500/10' : 'border-slate-800 bg-slate-900/50 hover:border-slate-700'"
        >
          <span class="text-2xl">🤝</span>
          <div>
            <div class="text-sm font-black text-white">1 a 1 En Vivo</div>
            <div class="text-[11px] text-indigo-400 font-semibold">Entre pares</div>
          </div>
        </button>

        <button
          @click="toggleTrustDetail('rep')"
          class="p-4 rounded-2xl border transition-all flex items-center gap-3.5 text-left cursor-pointer"
          :class="expandedTrustCard === 'rep' ? 'border-amber-500 bg-amber-500/10' : 'border-slate-800 bg-slate-900/50 hover:border-slate-700'"
        >
          <span class="text-2xl">⭐</span>
          <div>
            <div class="text-sm font-black text-white">4.8 ★ Confianza</div>
            <div class="text-[11px] text-amber-400 font-semibold">Verificada</div>
          </div>
        </button>

        <button
          @click="toggleTrustDetail('gift')"
          class="p-4 rounded-2xl border transition-all flex items-center gap-3.5 text-left cursor-pointer"
          :class="expandedTrustCard === 'gift' ? 'border-teal-500 bg-teal-500/10' : 'border-slate-800 bg-slate-900/50 hover:border-slate-700'"
        >
          <span class="text-2xl">🎁</span>
          <div>
            <div class="text-sm font-black text-white">+1 🪙 Regalo</div>
            <div class="text-[11px] text-teal-400 font-semibold">Al sumarte</div>
          </div>
        </button>
      </div>

      <transition
        enter-active-class="transition duration-200 ease-out"
        enter-from-class="opacity-0 -translate-y-1"
        enter-to-class="opacity-100 translate-y-0"
      >
        <div
          v-if="expandedTrustCard"
          class="p-4 rounded-2xl border border-slate-700 bg-slate-900/90 flex items-center justify-between gap-4 text-xs text-slate-200 transition-all"
          :class="spatialStore.flashingKey === 'trust-detail' ? 'spatial-flash-blink' : ''"
        >
          <span>
            <strong v-if="expandedTrustCard === 'money'" class="text-emerald-400">Sin plata:</strong>
            <strong v-else-if="expandedTrustCard === 'one2one'" class="text-indigo-400">Rol único humano:</strong>
            <strong v-else-if="expandedTrustCard === 'rep'" class="text-amber-400">Calificación mutua:</strong>
            <strong v-else class="text-teal-400">Crédito inicial:</strong>
            {{
              expandedTrustCard === 'money'
                ? ' Los créditos nunca se compran ni se cambian por dinero. Solo se ganan enseñando 1 hora.'
                : expandedTrustCard === 'one2one'
                  ? ' Todos somos pares (USER): hoy enseñás lo que dominás y mañana aprendés lo que necesitás.'
                  : expandedTrustCard === 'rep'
                    ? ' Cada sesión completada suma estrellas y reseñas reales al perfil.'
                    : ' Te regalamos tu primer crédito al registrarte para que destrabes tu primera clase hoy mismo.'
            }}
          </span>
          <button @click="expandedTrustCard = null" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold cursor-pointer shrink-0">✕</button>
        </div>
      </transition>
    </section>
  </div>
</template>
