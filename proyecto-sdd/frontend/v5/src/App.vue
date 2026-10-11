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
  UserPlus,
  ArrowLeftRight
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
  spatialStore.notify('Modo Visitante', 'Seguís en el lienzo.')
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
    userId === 'guest' ? '👀 Visitante' : `👋 Hola, ${authStore.currentUser?.name}`
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
  if (confirm('¿Restablecer datos demo?')) {
    platformStore.resetAllData()
    authStore.initAuth()
    spatialStore.closeCapsule()
    spatialStore.collapseItem()
    spatialStore.notify('Datos reiniciados')
  }
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background text-foreground antialiased">
    <!-- Top Simulator Banner (Compacto y Visual) -->
    <header class="border-b border-border/80 bg-muted/50 px-4 py-1.5 text-xs">
      <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
        <div class="flex items-center gap-2">
          <Badge variant="outline" class="bg-emerald-500/15 text-emerald-400 border-emerald-500/40 font-bold">
            V5 · Human Visual
          </Badge>
          <span class="text-muted-foreground hidden sm:inline">
            🎓 Enseño ⇄ 🚀 Aprendo · Golpe de vista en 1 lienzo
          </span>
        </div>

        <div class="flex items-center gap-1 overflow-x-auto">
          <button
            class="px-2 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.isGuest ? 'bg-card text-foreground shadow-xs border-border font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('guest')"
          >
            👀 Guest
          </button>
          <button
            class="px-2 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.currentUser?.id === 'usr-1' ? 'bg-card text-foreground shadow-xs border-border font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('usr-1')"
          >
            💻 Juan
          </button>
          <button
            class="px-2 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.currentUser?.id === 'usr-2' ? 'bg-card text-foreground shadow-xs border-border font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('usr-2')"
          >
            🗣️ Elena
          </button>
          <button
            class="px-2 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.currentUser?.id === 'usr-3' ? 'bg-card text-foreground shadow-xs border-border font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('usr-3')"
          >
            🐳 Carlos
          </button>
          <button
            class="px-2 py-1 rounded-md text-xs font-medium transition-all cursor-pointer border border-transparent"
            :class="authStore.isAdmin ? 'bg-destructive/10 text-destructive border-destructive/20 font-bold' : 'text-muted-foreground hover:text-foreground'"
            @click="handleQuickSwitch('usr-admin')"
          >
            🛡️ Admin
          </button>
        </div>
      </div>
    </header>

    <!-- Main Dock Bar (Íconos Directos) -->
    <nav class="sticky top-0 z-40 w-full border-b border-border/80 bg-background/95 backdrop-blur-md">
      <div class="max-w-7xl mx-auto flex h-15 items-center justify-between px-4 sm:px-6 gap-2">
        <button
          @click="handleScrollTop"
          class="flex items-center gap-2 text-left bg-transparent border-none cursor-pointer text-foreground"
        >
          <div class="h-8 w-8 rounded-xl bg-emerald-500 flex items-center justify-center text-slate-950 font-black text-xs shadow-sm">
            95
          </div>
          <span class="font-black text-base tracking-tight">Intercambia</span>
        </button>

        <div class="hidden md:flex items-center gap-1.5 text-xs font-bold">
          <button
            @click="spatialStore.filterAndFocusCatalog('')"
            class="px-3 py-1.5 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer text-muted-foreground hover:text-foreground hover:bg-muted/60"
          >
            <ArrowLeftRight class="h-4 w-4 text-emerald-400" />
            <span>Conexiones</span>
          </button>

          <button
            @click="handleFocusSimulator"
            class="px-3 py-1.5 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer text-muted-foreground hover:text-foreground hover:bg-muted/60"
          >
            <Sparkles class="h-4 w-4 text-indigo-400" />
            <span>Match 1:1</span>
          </button>

          <template v-if="authStore.isAuthenticated">
            <button
              @click="spatialStore.toggleCapsule('sessions')"
              class="px-3 py-1.5 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer border"
              :class="spatialStore.activeCapsule === 'sessions'
                ? 'bg-emerald-500/20 border-emerald-500/50 text-emerald-300'
                : 'border-transparent text-muted-foreground hover:text-foreground hover:bg-muted/60'"
            >
              <Calendar class="h-4 w-4" />
              <span>Sesiones ({{ platformStore.sessions.length }})</span>
            </button>

            <button
              @click="spatialStore.toggleCapsule('publish')"
              class="px-3 py-1.5 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer border"
              :class="spatialStore.activeCapsule === 'publish'
                ? 'bg-indigo-500/20 border-indigo-500/50 text-indigo-300'
                : 'border-transparent text-muted-foreground hover:text-foreground hover:bg-muted/60'"
            >
              <Plus class="h-4 w-4" />
              <span>Publicar</span>
            </button>
          </template>

          <button
            v-if="authStore.isAdmin"
            @click="spatialStore.toggleCapsule('admin')"
            class="px-3 py-1.5 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer text-destructive hover:bg-destructive/10"
          >
            <ShieldAlert class="h-4 w-4" />
            <span>Admin</span>
            <span v-if="pendingReportsCount > 0" class="h-2 w-2 rounded-full bg-destructive animate-pulse"></span>
          </button>
        </div>

        <div class="flex items-center gap-2">
          <template v-if="authStore.isAuthenticated">
            <button
              class="inline-flex items-center gap-1 px-3 py-1.5 rounded-full border transition-all cursor-pointer text-xs font-black"
              :class="spatialStore.activeCapsule === 'credits'
                ? 'border-amber-400 bg-amber-500/25 text-amber-200 scale-105'
                : 'border-amber-500/30 bg-amber-500/10 text-amber-300 hover:bg-amber-500/20'"
              @click="spatialStore.toggleCapsule('credits')"
            >
              <span>🪙 {{ authStore.credits }}</span>
            </button>

            <button
              @click="spatialStore.toggleCapsule('profile')"
              class="px-2.5 py-1.5 rounded-xl border text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5"
              :class="spatialStore.activeCapsule === 'profile'
                ? 'border-emerald-500/50 bg-emerald-500/15 text-emerald-300'
                : 'border-border bg-card/80 text-foreground'"
            >
              <User class="h-3.5 w-3.5 text-emerald-400" />
              <span class="hidden sm:inline">{{ authStore.currentUser.name.split(' ')[0] }}</span>
            </button>

            <Button variant="ghost" size="icon" title="Salir" @click="handleLogout">
              <LogOut class="h-4 w-4 text-muted-foreground hover:text-foreground" />
            </Button>
          </template>

          <template v-else>
            <button
              @click="spatialStore.toggleCapsule('auth')"
              class="px-3.5 py-1.5 rounded-xl text-xs font-black transition-all cursor-pointer flex items-center gap-1.5"
              :class="spatialStore.activeCapsule === 'auth'
                ? 'bg-slate-800 text-emerald-300 border border-emerald-500/50'
                : 'bg-emerald-500 hover:bg-emerald-400 text-slate-950'"
            >
              <UserPlus class="w-3.5 h-3.5" />
              <span>{{ spatialStore.activeCapsule === 'auth' ? 'Cerrar' : 'Entrar (+1 🪙)' }}</span>
            </button>
          </template>
        </div>
      </div>
    </nav>

    <main class="flex-1 py-6 px-4 sm:px-6">
      <router-view />
    </main>

    <footer class="border-t border-border bg-card py-6 text-xs text-muted-foreground mt-auto">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-wrap items-center justify-between gap-4">
        <div class="font-bold text-foreground">
          Intercambia V5 · 🎓 Enseño ⇄ 🚀 Aprendo · $0 Dinero
        </div>
        <button
          class="text-xs text-muted-foreground hover:text-destructive underline bg-transparent border-none cursor-pointer"
          @click="handleResetData"
        >
          Reiniciar demo
        </button>
      </div>
    </footer>
  </div>
</template>
