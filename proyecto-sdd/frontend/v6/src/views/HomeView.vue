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
  ShieldCheck
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
  { name: 'Vue 3 & Frontend', keyword: 'Vue', count: 'En vivo' },
  { name: 'Inglés para IT', keyword: 'Inglés', count: 'Alta demanda' },
  { name: 'Docker & DevOps', keyword: 'Docker', count: 'Práctico' },
  { name: 'Diseño UX/UI & Figma', keyword: 'Diseño', count: 'Creativo' },
  { name: 'Python & Backend', keyword: 'Programación', count: 'Mentoría' }
]

const expandedTrustCard = ref(null) // null | 'money' | 'one2one' | 'rep' | 'gift'

function handleSelectTopicInPlace(keyword) {
  spatialStore.filterAndFocusCatalog(keyword)
  spatialStore.notify(`Filtro "${keyword}" activado en vivo`, 'Las tarjetas del tablero se acomodaron sin cambiar de página.')
}

function toggleTrustDetail(key) {
  expandedTrustCard.value = expandedTrustCard.value === key ? null : key
  if (expandedTrustCard.value) {
    spatialStore.triggerFlash('trust-detail', '⚡ Regla destacada')
  }
}
</script>

<template>
  <div class="max-w-7xl mx-auto flex flex-col gap-10 pb-16">
    <!-- Notificación Flotante Íntima In-Place -->
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
        class="fixed bottom-6 right-6 z-50 max-w-sm rounded-2xl border border-emerald-500/50 bg-slate-900/95 backdrop-blur-xl p-4 shadow-2xl shadow-emerald-950/80 flex items-start gap-3"
      >
        <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0 mt-0.5">
          <Sparkles class="w-4 h-4" />
        </div>
        <div class="flex-1">
          <div class="text-xs font-black text-white">{{ spatialStore.liveNotice.title }}</div>
          <p v-if="spatialStore.liveNotice.subtitle" class="text-[11px] text-slate-300 mt-0.5 leading-relaxed">
            {{ spatialStore.liveNotice.subtitle }}
          </p>
        </div>
      </div>
    </transition>

    <!-- 1. Ticker en Vivo Superior -->
    <LiveActivityTicker />

    <!-- 2. Escenario de Cápsulas Vivas (Se despliega y pliega aquí mismo) -->
    <SpatialCapsuleStage />

    <!-- 3. Hero Cinematográfico de Alto Impacto (100% In-Place) -->
    <section class="relative rounded-3xl overflow-hidden border border-slate-800 bg-gradient-to-b from-slate-900 via-slate-900/95 to-slate-950 p-6 md:p-12 shadow-2xl">
      <!-- Background Ambient Glow -->
      <div class="absolute -top-32 -left-32 w-96 h-96 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-500/15 rounded-full blur-3xl pointer-events-none"></div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative z-10">
        <!-- Text Column -->
        <div class="lg:col-span-7 text-left space-y-6">
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight leading-[1.1]">
            Aprender enseñando lo que sabés.
            <span class="block bg-gradient-to-r from-emerald-400 via-teal-300 to-indigo-400 bg-clip-text text-transparent">
              Todo sucede frente a vos.
            </span>
          </h1>

          <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-xl">
            Tocá cualquier habilidad, tarjeta o cápsula: se amplifica suavemente en su lugar para que explores, coordines horarios y reserves sin perder jamás tu contexto.
            <strong>1 hora que compartís = 1 crédito que ganás.</strong>
          </p>

          <!-- Quick Discovery Chips (Zero-Navigation / Filtran en Vivo) -->
          <div class="pt-2">
            <span class="text-xs uppercase font-bold tracking-wider text-slate-400 block mb-2.5">
              Tocá un tema para iluminarlo en vivo en el tablero:
            </span>
            <div class="flex flex-wrap gap-2">
              <button
                v-for="topic in popularTopics"
                :key="topic.name"
                @click="handleSelectTopicInPlace(topic.keyword)"
                class="px-3.5 py-2 rounded-xl border text-xs font-semibold transition-all cursor-pointer flex items-center gap-1.5 shadow-xs"
                :class="spatialStore.searchQuery.toLowerCase() === topic.keyword.toLowerCase()
                  ? 'bg-emerald-500 text-slate-950 border-emerald-400 font-black scale-105'
                  : 'bg-slate-800/80 hover:bg-emerald-500/20 hover:border-emerald-500/50 border-slate-700/80 text-slate-200 hover:text-emerald-300'"
              >
                <span>{{ topic.name }}</span>
                <span class="text-[10px] opacity-75 font-normal">({{ topic.count }})</span>
              </button>
            </div>
          </div>

          <!-- CTAs In-Place -->
          <div class="flex flex-wrap items-center gap-3 pt-4">
            <button
              @click="spatialStore.filterAndFocusCatalog('')"
              class="px-6 py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 text-slate-950 font-black text-sm transition-all shadow-lg shadow-emerald-500/25 flex items-center gap-2 cursor-pointer"
            >
              <Compass class="w-4 h-4" />
              Ir al Tablero Expandible
            </button>

            <button
              v-if="authStore.isGuest"
              @click="spatialStore.toggleCapsule('auth')"
              class="px-6 py-3.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm transition-all shadow-lg shadow-indigo-600/20 flex items-center gap-2 cursor-pointer"
            >
              <UserPlus class="w-4 h-4" />
              Reclamar mi Crédito Aquí Mismo
            </button>

            <template v-else>
              <button
                @click="spatialStore.toggleCapsule('sessions')"
                class="px-5 py-3.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-white font-bold text-sm transition-all flex items-center gap-2 cursor-pointer"
              >
                <Calendar class="w-4 h-4 text-emerald-400" />
                Abrir Mis Sesiones ({{ platformStore.sessions.length }})
              </button>
              <button
                @click="spatialStore.toggleCapsule('publish')"
                class="px-5 py-3.5 rounded-xl bg-indigo-600/90 hover:bg-indigo-500 text-white font-bold text-sm transition-all flex items-center gap-2 cursor-pointer"
              >
                <Plus class="w-4 h-4" />
                Publicar en 10 seg
              </button>
            </template>
          </div>
        </div>

        <!-- Visual / Image Column -->
        <div class="lg:col-span-5 relative">
          <!-- Main Hero Image Frame -->
          <div
            @click="spatialStore.filterAndFocusCatalog('')"
            class="relative rounded-2xl overflow-hidden border border-slate-700 shadow-2xl group cursor-pointer"
          >
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
                  Tocá cualquier propuesta abajo para agrandarla en el lugar.
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
              <div class="text-xs font-bold text-white">Cero Saltos de Página</div>
              <div class="text-[10px] text-slate-400">Todo se expande in-situ</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Tablero Espacial Interactivo (Contenido íntegramente en su propio Panel) -->
    <SpatialCatalogBento />

    <!-- 5. Intercambios que están pasando hoy (Contenido íntegramente en su propio Panel) -->
    <LiveCommunityPulse />

    <!-- 6. Simulador Interactivo de Matchmaking (Contenido íntegramente en su propio Panel) -->
    <InteractiveMatchSimulator />

    <!-- 7. Garantías y Reglas de Confianza (Contenido íntegramente en su propio Panel) -->
    <section class="relative rounded-3xl overflow-hidden border border-slate-800 bg-gradient-to-b from-slate-900 via-slate-900/95 to-slate-950 p-6 md:p-12 shadow-2xl space-y-8">
      <div class="absolute -top-32 -left-32 w-96 h-96 bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-500/15 rounded-full blur-3xl pointer-events-none"></div>

      <div class="relative z-10 space-y-6">
        <div class="max-w-2xl space-y-2">
          <h2 class="text-3xl sm:text-4xl font-black text-white tracking-tight leading-[1.12]">
            Comunidad libre de dinero.
            <span class="block bg-gradient-to-r from-emerald-400 via-teal-300 to-indigo-400 bg-clip-text text-transparent">
              Confianza mutua en cada sesión.
            </span>
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            Tocá cualquiera de los cuatro pilares para desplegar acá mismo cómo cuidamos la equidad y la reputación en cada intercambio.
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <button
            @click="toggleTrustDetail('money')"
            class="p-6 rounded-2xl border transition-all text-center cursor-pointer"
            :class="expandedTrustCard === 'money' ? 'border-emerald-500 bg-emerald-500/10 scale-[1.02]' : 'border-slate-800 bg-slate-950/65 hover:border-slate-700'"
          >
            <div class="text-3xl font-black text-emerald-400 mb-1">100%</div>
            <div class="text-xs uppercase font-bold text-white tracking-wider">Libre de Dinero</div>
            <div class="text-[11px] text-slate-400 mt-1">Tocá para ver la regla de oro ⤢</div>
          </button>

          <button
            @click="toggleTrustDetail('one2one')"
            class="p-6 rounded-2xl border transition-all text-center cursor-pointer"
            :class="expandedTrustCard === 'one2one' ? 'border-indigo-500 bg-indigo-500/10 scale-[1.02]' : 'border-slate-800 bg-slate-950/65 hover:border-slate-700'"
          >
            <div class="text-3xl font-black text-indigo-400 mb-1">1 a 1</div>
            <div class="text-xs uppercase font-bold text-white tracking-wider">Sesiones Personalizadas</div>
            <div class="text-[11px] text-slate-400 mt-1">Tocá para ver cómo funcionan ⤢</div>
          </button>

          <button
            @click="toggleTrustDetail('rep')"
            class="p-6 rounded-2xl border transition-all text-center cursor-pointer"
            :class="expandedTrustCard === 'rep' ? 'border-amber-500 bg-amber-500/10 scale-[1.02]' : 'border-slate-800 bg-slate-950/65 hover:border-slate-700'"
          >
            <div class="text-3xl font-black text-amber-400 mb-1">4.8 ★</div>
            <div class="text-xs uppercase font-bold text-white tracking-wider">Reputación Verificada</div>
            <div class="text-[11px] text-slate-400 mt-1">Tocá para ver reseñas reales ⤢</div>
          </button>

          <button
            @click="toggleTrustDetail('gift')"
            class="p-6 rounded-2xl border transition-all text-center cursor-pointer"
            :class="expandedTrustCard === 'gift' ? 'border-teal-500 bg-teal-500/10 scale-[1.02]' : 'border-slate-800 bg-slate-950/65 hover:border-slate-700'"
          >
            <div class="text-3xl font-black text-teal-400 mb-1">1 Crédito</div>
            <div class="text-xs uppercase font-bold text-white tracking-wider">Regalo de Bienvenida</div>
            <div class="text-[11px] text-slate-400 mt-1">Tocá para ver cómo usarlo ⤢</div>
          </button>
        </div>

        <!-- Detalle expandido de Confianza In-Place (Contenido dentro del mismo panel) -->
        <transition
          enter-active-class="transition duration-300 ease-out"
          enter-from-class="opacity-0 -translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition duration-150 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 -translate-y-2"
        >
          <div
            v-if="expandedTrustCard"
            class="p-6 rounded-2xl border border-slate-700 bg-slate-950/85 flex flex-wrap items-center justify-between gap-4 transition-all"
            :class="spatialStore.flashingKey === 'trust-detail' ? 'spatial-flash-blink' : ''"
          >
            <div class="max-w-3xl space-y-1">
              <div class="text-xs font-black uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                <ShieldCheck class="w-4 h-4" />
                <span v-if="expandedTrustCard === 'money'">Garantía de Economía No Monetaria</span>
                <span v-else-if="expandedTrustCard === 'one2one'">Aprendizaje Humano Directo 1 a 1</span>
                <span v-else-if="expandedTrustCard === 'rep'">Calificaciones Cruzadas Verificadas</span>
                <span v-else>Tu Primer Aprendizaje Empieza Hoy</span>
              </div>
              <p class="text-xs sm:text-sm text-slate-200 leading-relaxed">
                <span v-if="expandedTrustCard === 'money'">
                  En Intercambia los créditos no se compran con tarjeta ni se retiran por dinero. La única forma de sumar créditos es dedicándole 1 hora de tu tiempo a enseñar algo que sabés.
                </span>
                <span v-else-if="expandedTrustCard === 'one2one'">
                  Todas las sesiones duran 60 minutos y conectan directamente a dos miembros de la comunidad (rol único USER: todos podemos enseñar y aprender).
                </span>
                <span v-else-if="expandedTrustCard === 'rep'">
                  Al finalizar cada encuentro de 1 hora, ambas personas califican la sesión de 1 a 5 estrellas, construyendo un historial público transparente.
                </span>
                <span v-else>
                  Al crear tu cuenta recibís 1 Crédito de Bienvenida automáticamente para que puedas reservar tu primera clase antes incluso de dar tu primera mentoría.
                </span>
              </p>
            </div>
            <button
              @click="expandedTrustCard = null"
              class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 flex items-center gap-1.5 cursor-pointer"
            >
              <Minimize2 class="w-3.5 h-3.5 text-emerald-400" />
              <span>Achicar</span>
            </button>
          </div>
        </transition>
      </div>
    </section>
  </div>
</template>
