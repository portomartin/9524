<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import {
  Sparkles,
  Compass,
  Search,
  UserPlus,
  ArrowRight,
  Coins,
  ShieldCheck,
  CheckCircle2,
  Users2,
  BookOpen,
  Zap,
  TrendingUp,
  Star
} from 'lucide-vue-next'
import { usePlatformStore } from '../stores/platformStore'
import { useAuthStore } from '../stores/authStore'
import LiveActivityTicker from '../components/v3/LiveActivityTicker.vue'
import InteractiveMatchSimulator from '../components/v3/InteractiveMatchSimulator.vue'
import LiveCommunityPulse from '../components/v3/LiveCommunityPulse.vue'
import Button from '../components/ui/Button.vue'
import Badge from '../components/ui/Badge.vue'

const router = useRouter()
const platformStore = usePlatformStore()
const authStore = useAuthStore()

const popularTopics = [
  { name: 'Vue 3 & Frontend', category: 'Tecnología', count: '14 ofertas' },
  { name: 'Inglés para IT', category: 'Idiomas', count: '19 ofertas' },
  { name: 'Docker & DevOps', category: 'Infraestructura', count: '8 ofertas' },
  { name: 'Diseño UX/UI & Figma', category: 'Diseño', count: '11 ofertas' },
  { name: 'Python Backend', category: 'Programación', count: '15 ofertas' },
  { name: 'Liderazgo & Coaching', category: 'Habilidades', count: '6 ofertas' }
]

function handleSelectTopic(topicName) {
  router.push({ name: 'search', query: { q: topicName } })
}
</script>

<template>
  <div class="flex flex-col gap-12 pb-16">
    <!-- 1. Ticker en Vivo Superior -->
    <LiveActivityTicker />

    <!-- 2. Hero Cinematográfico de Alto Impacto -->
    <section class="relative rounded-3xl overflow-hidden border border-slate-800 bg-gradient-to-b from-slate-900 via-slate-900/95 to-slate-950 p-6 md:p-12 shadow-2xl">
      <!-- Background Ambient Glow -->
      <div class="absolute -top-32 -left-32 w-96 h-96 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-500/15 rounded-full blur-3xl pointer-events-none"></div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative z-10">
        <!-- Text Column -->
        <div class="lg:col-span-7 text-left space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/25 text-emerald-400 text-xs font-bold tracking-wide">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>Comunidad de Intercambio de Conocimiento · Sin Dinero</span>
          </div>

          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight leading-[1.1]">
            Aprender enseñando lo que sabés.
            <span class="block bg-gradient-to-r from-emerald-400 via-teal-300 to-indigo-400 bg-clip-text text-transparent">
              Tu tiempo es la única moneda.
            </span>
          </h1>

          <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-xl">
            Conectamos directamente a quien tiene una habilidad práctica con quien desea aprenderla.
            <strong>1 hora que compartís = 1 crédito que ganás</strong> para tomar cualquier otra sesión.
          </p>

          <!-- Quick Discovery Chips (Zero-Prompt / 1 Clic) -->
          <div class="pt-2">
            <span class="text-xs uppercase font-bold tracking-wider text-slate-400 block mb-2.5">
              Explorá por habilidades más solicitadas hoy:
            </span>
            <div class="flex flex-wrap gap-2">
              <button
                v-for="topic in popularTopics"
                :key="topic.name"
                @click="handleSelectTopic(topic.name)"
                class="px-3 py-1.5 rounded-xl bg-slate-800/80 hover:bg-emerald-500/20 hover:border-emerald-500/50 border border-slate-700/80 text-xs font-medium text-slate-200 hover:text-emerald-300 transition-all cursor-pointer flex items-center gap-1.5 shadow-xs"
              >
                <span>{{ topic.name }}</span>
                <span class="text-[10px] text-slate-400 font-normal">({{ topic.count }})</span>
              </button>
            </div>
          </div>

          <!-- CTAs -->
          <div class="flex flex-wrap items-center gap-3 pt-4">
            <button
              @click="router.push({ name: 'explore' })"
              class="px-6 py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 text-slate-950 font-black text-sm transition-all shadow-lg shadow-emerald-500/25 flex items-center gap-2 cursor-pointer"
            >
              <Compass class="w-4 h-4" />
              Explorar Catálogo Vivo
            </button>
            <button
              v-if="authStore.isGuest"
              @click="router.push({ name: 'auth' })"
              class="px-6 py-3.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm transition-all shadow-lg shadow-indigo-600/20 flex items-center gap-2 cursor-pointer"
            >
              <UserPlus class="w-4 h-4" />
              Reclamar mi Crédito de Bienvenida
            </button>
          </div>
        </div>

        <!-- Visual / Image Column -->
        <div class="lg:col-span-5 relative">
          <!-- Main Hero Image Frame -->
          <div class="relative rounded-2xl overflow-hidden border border-slate-700 shadow-2xl group">
            <img
              src="/src/assets/images/hero-community.jpg"
              alt="Colaboración y mentoría entre pares"
              class="w-full h-80 sm:h-96 object-cover object-center group-hover:scale-105 transition-transform duration-700"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/30 to-transparent"></div>

            <!-- Overlaid Badge Bottom -->
            <div class="absolute bottom-4 left-4 right-4 bg-slate-900/85 backdrop-blur-md p-4 rounded-xl border border-slate-700/80 flex items-center justify-between">
              <div>
                <div class="text-xs font-bold text-white flex items-center gap-1.5">
                  <Star class="w-4 h-4 fill-amber-400 text-amber-400" />
                  <span>Comunidad de Confianza Calificada</span>
                </div>
                <div class="text-[11px] text-slate-400 mt-0.5">
                  Todas las sesiones terminan con retroalimentación mutua.
                </div>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-emerald-500/15 text-emerald-400 border border-emerald-500/30 text-xs font-bold">
                100% Gratuito
              </span>
            </div>
          </div>

          <!-- Floating Metric Card -->
          <div class="absolute -top-4 -left-4 bg-slate-900/95 backdrop-blur-md border border-slate-700 px-3.5 py-2.5 rounded-xl shadow-xl hidden sm:flex items-center gap-3">
            <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold">
              <Zap class="w-4 h-4" />
            </div>
            <div>
              <div class="text-xs font-bold text-white">Match Inmediato</div>
              <div class="text-[10px] text-slate-400">Sin intermediarios</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. Intercambios que están pasando hoy (Vitalidad de Comunidad) -->
    <LiveCommunityPulse />

    <!-- 4. Simulador Interactivo de Matchmaking (Playground en 2 clics) -->
    <InteractiveMatchSimulator />

    <!-- 5. Métricas de Impacto y Garantía de Confianza -->
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="p-6 rounded-2xl border border-slate-800 bg-slate-900/40 text-center">
        <div class="text-3xl font-black text-emerald-400 mb-1">100%</div>
        <div class="text-xs uppercase font-bold text-white tracking-wider">Libre de Dinero</div>
        <div class="text-[11px] text-slate-400 mt-1">Intercambio de horas o créditos internos</div>
      </div>
      <div class="p-6 rounded-2xl border border-slate-800 bg-slate-900/40 text-center">
        <div class="text-3xl font-black text-indigo-400 mb-1">1 a 1</div>
        <div class="text-xs uppercase font-bold text-white tracking-wider">Sesiones Personalizadas</div>
        <div class="text-[11px] text-slate-400 mt-1">Aprendé a tu propio ritmo con alguien que sabe</div>
      </div>
      <div class="p-6 rounded-2xl border border-slate-800 bg-slate-900/40 text-center">
        <div class="text-3xl font-black text-amber-400 mb-1">4.8 ★</div>
        <div class="text-xs uppercase font-bold text-white tracking-wider">Reputación Verificada</div>
        <div class="text-[11px] text-slate-400 mt-1">Garantía por calificaciones posteriores</div>
      </div>
      <div class="p-6 rounded-2xl border border-slate-800 bg-slate-900/40 text-center">
        <div class="text-3xl font-black text-teal-400 mb-1">1 Crédito</div>
        <div class="text-xs uppercase font-bold text-white tracking-wider">Regalo de Bienvenida</div>
        <div class="text-[11px] text-slate-400 mt-1">Para que tomes tu primera clase hoy mismo</div>
      </div>
    </section>
  </div>
</template>
