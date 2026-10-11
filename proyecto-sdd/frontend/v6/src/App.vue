<script setup>
import { computed } from 'vue'
import {
  Compass,
  Calendar,
  Plus,
  User,
  ShieldAlert,
  Coins,
  LogOut,
  Sparkles,
  UserPlus
} from 'lucide-vue-next'
import { useAuthStore } from './stores/authStore'
import { usePlatformStore } from './stores/platformStore'
import { useSpatialStore } from './stores/spatialStore'
import Button from './components/ui/Button.vue'
import Badge from './components/ui/Badge.vue'

const authStore = useAuthStore()
const platformStore = usePlatformStore()
const spatialStore = useSpatialStore()

const pendingReportsCount = computed(() => {
  return platformStore.reports.filter(r => r.status === 'PENDIENTE').length
})

function handleLogout() {
  authStore.logout()
  platformStore.refreshAll()
  spatialStore.closeCapsule()
  spatialStore.notify('Sesión cerrada', 'Seguís explorando el lienzo como visitante.')
}

function handleQuickSwitch(userId) {
  if (userId === 'guest') {
    authStore.logout()
    spatialStore.closeCapsule()
  } else {
    authStore.switchUserQuick(userId)
  }
  platformStore.refreshAll()
  spatialStore.notify(
    userId === 'guest' ? 'Modo Visitante Activo' : `Simulando a ${authStore.currentUser?.name}`,
    'El lienzo se adaptó en vivo sin cambiar de página.'
  )
}

function handleScrollTop() {
  spatialStore.closeCapsule()
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function handleFocusSimulator() {
  const el = document.getElementById('spatial-simulator-section')
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' })
}

function handleResetData() {
  if (confirm('¿Restablecer todos los datos del MVP a los valores iniciales?')) {
    platformStore.resetAllData()
    authStore.initAuth()
    spatialStore.closeCapsule()
    spatialStore.collapseItem()
    spatialStore.notify('Datos restablecidos', 'Todo el lienzo volvió a su estado inicial.')
  }
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background text-foreground antialiased">
    <!-- Top Simulator Banner -->
    <header class="border-b border-border/80 bg-muted/50 px-4 py-2 text-xs">
      <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
        <div class="flex items-center gap-2">
          <Badge variant="outline" class="bg-emerald-500/15 text-emerald-400 border-emerald-500/40 font-bold">
            Frontend V6 · Warm Light Canvas
          </Badge>
          <span class="text-muted-foreground hidden sm:inline">
            Tema Claro Cálido (Solarized Light) · Basado en V4 · Lienzo único con Flash en cada acción.
          </span>
        </div>

        <div class="flex items-center gap-1.5 overflow-x-auto">
          <span class="text-muted-foreground text-[11px] mr-1 hidden md:inline">Simular en vivo:</span>
          <button
            class="px-2.5 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.isGuest ? 'bg-card text-foreground shadow-xs border-border font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('guest')"
          >
            GUEST
          </button>
          <button
            class="px-2.5 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.currentUser?.id === 'usr-1' ? 'bg-card text-foreground shadow-xs border-border font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('usr-1')"
          >
            Juan (Vue)
          </button>
          <button
            class="px-2.5 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.currentUser?.id === 'usr-2' ? 'bg-card text-foreground shadow-xs border-border font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('usr-2')"
          >
            Elena (Inglés)
          </button>
          <button
            class="px-2.5 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.currentUser?.id === 'usr-3' ? 'bg-card text-foreground shadow-xs border-border font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('usr-3')"
          >
            Carlos (DevOps)
          </button>
          <button
            class="px-2.5 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.isAdmin ? 'bg-destructive/10 text-destructive border-destructive/20 font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('usr-admin')"
          >
            Admin
          </button>
        </div>
      </div>
    </header>

    <!-- Main Spatial Dock Bar (Zero URL Changes — Only In-Place Capsules & Focus) -->
    <nav class="sticky top-0 z-40 w-full border-b border-border/80 bg-background/95 backdrop-blur-md">
      <div class="max-w-7xl mx-auto flex h-16 items-center justify-between px-4 sm:px-6 gap-2">
        <!-- Logo (Scrolls smoothly to top of canvas) -->
        <button
          @click="handleScrollTop"
          class="flex items-center gap-2.5 text-left bg-transparent border-none cursor-pointer text-foreground"
        >
          <div class="h-9 w-9 rounded-xl bg-emerald-500 flex items-center justify-center text-slate-950 font-black text-sm shadow-sm">
            95
          </div>
          <div class="flex flex-col">
            <span class="font-extrabold text-base tracking-tight leading-none">Intercambia</span>
            <span class="text-[11px] text-emerald-400 font-semibold mt-0.5">Warm Light V6</span>
          </div>
        </button>

        <!-- Interactive Capsules Bar (Expands in-place instead of changing routes) -->
        <div class="hidden md:flex items-center gap-1.5 text-xs font-semibold">
          <button
            @click="spatialStore.filterAndFocusCatalog('')"
            class="px-3.5 py-2 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer text-muted-foreground hover:text-foreground hover:bg-muted/60"
          >
            <Compass class="h-4 w-4 text-emerald-400" />
            <span>Tablero Expandible</span>
          </button>

          <button
            @click="handleFocusSimulator"
            class="px-3.5 py-2 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer text-muted-foreground hover:text-foreground hover:bg-muted/60"
          >
            <Sparkles class="h-4 w-4 text-indigo-400" />
            <span>Simulador 1:1</span>
          </button>

          <template v-if="authStore.isAuthenticated">
            <button
              @click="spatialStore.toggleCapsule('sessions')"
              class="px-3.5 py-2 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer border"
              :class="spatialStore.activeCapsule === 'sessions'
                ? 'bg-emerald-500/20 border-emerald-500/50 text-emerald-300 font-bold'
                : 'border-transparent text-muted-foreground hover:text-foreground hover:bg-muted/60'"
            >
              <Calendar class="h-4 w-4" />
              <span>Mis Sesiones ({{ platformStore.sessions.length }})</span>
            </button>

            <button
              @click="spatialStore.toggleCapsule('publish')"
              class="px-3.5 py-2 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer border"
              :class="spatialStore.activeCapsule === 'publish'
                ? 'bg-indigo-500/20 border-indigo-500/50 text-indigo-300 font-bold'
                : 'border-transparent text-muted-foreground hover:text-foreground hover:bg-muted/60'"
            >
              <Plus class="h-4 w-4" />
              <span>Publicar / Mis Temas</span>
            </button>
          </template>

          <button
            v-if="authStore.isAdmin"
            @click="spatialStore.toggleCapsule('admin')"
            class="px-3.5 py-2 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer text-destructive hover:bg-destructive/10"
            :class="spatialStore.activeCapsule === 'admin' ? 'bg-destructive/15 font-bold' : ''"
          >
            <ShieldAlert class="h-4 w-4" />
            <span>Moderación</span>
            <span v-if="pendingReportsCount > 0" class="h-2 w-2 rounded-full bg-destructive animate-pulse"></span>
          </button>
        </div>

        <!-- Right Area: Credits Capsule + Profile Capsule / In-Place Auth -->
        <div class="flex items-center gap-2.5">
          <template v-if="authStore.isAuthenticated">
            <!-- Expandable Credits Capsule -->
            <button
              class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full border transition-all cursor-pointer text-xs font-bold"
              :class="spatialStore.activeCapsule === 'credits'
                ? 'border-amber-400 bg-amber-500/25 text-amber-200 scale-105'
                : 'border-amber-500/30 bg-amber-500/10 text-amber-300 hover:bg-amber-500/20'"
              title="Tocar para desplegar detalle de créditos en el lugar"
              @click="spatialStore.toggleCapsule('credits')"
            >
              <Coins class="h-3.5 w-3.5 text-amber-400" />
              <span>{{ authStore.credits }} Créditos</span>
            </button>

            <!-- Expandable Profile Capsule -->
            <button
              @click="spatialStore.toggleCapsule('profile')"
              class="px-3 py-1.5 rounded-xl border text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5"
              :class="spatialStore.activeCapsule === 'profile'
                ? 'border-emerald-500/50 bg-emerald-500/15 text-emerald-300'
                : 'border-border bg-card/80 text-foreground hover:border-slate-600'"
            >
              <User class="h-3.5 w-3.5 text-emerald-400" />
              <span class="hidden sm:inline">{{ authStore.currentUser.name }}</span>
            </button>

            <Button
              variant="ghost"
              size="icon"
              title="Salir a modo visitante"
              @click="handleLogout"
            >
              <LogOut class="h-4 w-4 text-muted-foreground hover:text-foreground" />
            </Button>
          </template>

          <template v-else>
            <button
              @click="spatialStore.toggleCapsule('auth')"
              class="px-4 py-2 rounded-xl text-xs font-black transition-all cursor-pointer flex items-center gap-1.5 shadow-md"
              :class="spatialStore.activeCapsule === 'auth'
                ? 'bg-slate-800 text-emerald-300 border border-emerald-500/50'
                : 'bg-emerald-500 hover:bg-emerald-400 text-slate-950'"
            >
              <UserPlus class="w-3.5 h-3.5" />
              <span>{{ spatialStore.activeCapsule === 'auth' ? 'Achicar Acceso' : 'Ingresar Aquí Mismo' }}</span>
            </button>
          </template>
        </div>
      </div>
    </nav>

    <!-- Single-Canvas Main Area -->
    <main class="flex-1 py-8 px-4 sm:px-6">
      <router-view />
    </main>

    <!-- Footer (Zero External Links — All Actions Stay On Canvas) -->
    <footer class="border-t border-border bg-card py-8 text-sm text-muted-foreground mt-auto">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="text-center md:text-left">
          <div class="font-bold text-foreground">Plataforma de Intercambio de Aprendizajes · V6 Warm Light Spatial Canvas</div>
          <p class="text-xs mt-1 max-w-md">
            Todo ocurre en el mismo lugar sin perder contexto. Los créditos son una unidad interna de tiempo sin equivalencia monetaria.
          </p>
        </div>

        <div class="flex items-center gap-4 text-xs">
          <button
            class="hover:text-foreground transition-colors bg-transparent border-none cursor-pointer text-muted-foreground"
            @click="spatialStore.filterAndFocusCatalog('', 'offers')"
          >
            Propuestas
          </button>
          <button
            class="hover:text-foreground transition-colors bg-transparent border-none cursor-pointer text-muted-foreground"
            @click="spatialStore.filterAndFocusCatalog('', 'needs')"
          >
            Pedidos
          </button>
          <button
            class="hover:text-foreground transition-colors bg-transparent border-none cursor-pointer text-muted-foreground"
            @click="handleFocusSimulator"
          >
            Simulador 1:1
          </button>
          <button
            class="text-xs text-muted-foreground hover:text-destructive underline bg-transparent border-none cursor-pointer"
            @click="handleResetData"
          >
            Reiniciar datos demo
          </button>
        </div>
      </div>
    </footer>
  </div>
</template>
