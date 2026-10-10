<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import {
  Users,
  Clock,
  Coins,
  ShieldCheck,
  Star,
  ArrowUpRight,
  Sparkles,
  ArrowRight
} from 'lucide-vue-next'

const router = useRouter()

const liveExchanges = [
  {
    id: 1,
    title: 'Vue 3 & Frontend Reactivo 🔁 Inglés para IT',
    userA: { name: 'Juan Carlos', avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80', badge: 'Frontend Dev', rep: 4.9 },
    userB: { name: 'Elena Rostova', avatar: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&auto=format&fit=crop&q=80', badge: 'Traductora & Coach', rep: 4.8 },
    category: 'Tecnología / Idiomas',
    status: 'Hoy 18:00 hs',
    credits: '1 Crédito transferido'
  },
  {
    id: 2,
    title: 'Docker & Linux en Servidores 🔁 Diseño UX con Figma',
    userA: { name: 'Carlos Mendoza', avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80', badge: 'DevOps Senior', rep: 4.6 },
    userB: { name: 'Lucía Fernández', avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=150&auto=format&fit=crop&q=80', badge: 'Product Designer', rep: 4.9 },
    category: 'Infraestructura / Diseño',
    status: 'Confirmada',
    credits: '1 Crédito en garantía'
  },
  {
    id: 3,
    title: 'Python & FastAPI 🔁 Estrategia de Producto & Agile',
    userA: { name: 'Martín Gómez', avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80', badge: 'Backend Lead', rep: 4.8 },
    userB: { name: 'Sofía Valenzuela', avatar: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=150&auto=format&fit=crop&q=80', badge: 'Scrum Master', rep: 4.9 },
    category: 'Backend / Gestión',
    status: 'En curso ahora',
    credits: 'Intercambio activo'
  }
]

function handleViewOffer(query) {
  router.push({ name: 'search', query: { q: query } })
}
</script>

<template>
  <div class="my-16">
    <!-- Section Title -->
    <div class="flex flex-wrap items-end justify-between gap-4 mb-8">
      <div>
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 mb-2">
          <Users class="w-3.5 h-3.5" />
          Comunidad Activa
        </div>
        <h2 class="text-3xl font-black text-white tracking-tight">
          Intercambios que están pasando hoy
        </h2>
        <p class="text-slate-400 text-sm mt-1 max-w-xl">
          Mirá cómo personas reales conectan sus habilidades sin dinero de por medio. Una hora enseñada equivale a una hora aprendida.
        </p>
      </div>

      <router-link
        to="/explore"
        class="inline-flex items-center gap-1.5 text-xs font-bold text-emerald-400 hover:text-emerald-300 transition-colors"
      >
        Ver catálogo de 40+ ofertas y necesidades
        <ArrowRight class="w-4 h-4" />
      </router-link>
    </div>

    <!-- 3 Highlighted Live Exchange Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div
        v-for="exchange in liveExchanges"
        :key="exchange.id"
        class="group relative rounded-2xl border border-slate-800 bg-slate-900/60 p-5 hover:border-slate-700 hover:bg-slate-900/90 transition-all duration-300 flex flex-col justify-between shadow-lg"
      >
        <!-- Top Status Bar -->
        <div>
          <div class="flex items-center justify-between text-xs mb-3">
            <span class="px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 font-medium text-[11px]">
              {{ exchange.category }}
            </span>
            <span class="flex items-center gap-1 text-[11px] font-semibold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
              {{ exchange.status }}
            </span>
          </div>

          <!-- Exchange Title -->
          <h3 class="text-base font-bold text-white group-hover:text-emerald-300 transition-colors line-clamp-2 mb-4 leading-snug">
            {{ exchange.title }}
          </h3>

          <!-- Two Users Connected View -->
          <div class="space-y-3 bg-slate-950/60 p-3.5 rounded-xl border border-slate-800/80 mb-4">
            <!-- User A -->
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2.5">
                <img :src="exchange.userA.avatar" :alt="exchange.userA.name" class="w-8 h-8 rounded-full object-cover border border-slate-700" />
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
            <div class="flex items-center justify-center text-[10px] text-slate-500 font-bold uppercase tracking-wider">
              <span>↕ Intercambio recíproco 1 a 1</span>
            </div>

            <!-- User B -->
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2.5">
                <img :src="exchange.userB.avatar" :alt="exchange.userB.name" class="w-8 h-8 rounded-full object-cover border border-slate-700" />
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
        </div>

        <!-- Footer Card -->
        <div class="pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs">
          <div class="flex items-center gap-1.5 text-slate-400 text-[11px]">
            <Coins class="w-3.5 h-3.5 text-amber-400" />
            <span>{{ exchange.credits }}</span>
          </div>

          <button
            @click="handleViewOffer(exchange.title)"
            class="text-xs font-bold text-white hover:text-emerald-400 flex items-center gap-1 transition-colors cursor-pointer"
          >
            Sumarme
            <ArrowUpRight class="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
