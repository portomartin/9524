<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import {
  Compass,
  Search,
  ShieldCheck,
  User,
  ShieldAlert,
  Coins,
  LogOut,
  Sparkles,
  BookOpen
} from '@lucide/vue'
import { useAuthStore } from './stores/authStore'
import { usePlatformStore } from './stores/platformStore'
import Button from './components/ui/Button.vue'
import Badge from './components/ui/Badge.vue'

const authStore = useAuthStore()
const platformStore = usePlatformStore()
const router = useRouter()
const route = useRoute()

const pendingReportsCount = computed(() => {
  return platformStore.reports.filter(r => r.status === 'PENDIENTE').length
})

function handleLogout() {
  authStore.logout()
  platformStore.refreshAll()
  router.push({ name: 'home' })
}

function handleQuickSwitch(userId) {
  if (userId === 'guest') {
    authStore.logout()
  } else {
    authStore.switchUserQuick(userId)
  }
  platformStore.refreshAll()
}

function handleResetData() {
  if (confirm('¿Restablecer todos los datos del MVP a los valores iniciales?')) {
    platformStore.resetAllData()
    authStore.initAuth()
    alert('Datos restablecidos exitosamente.')
  }
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-background text-foreground antialiased">
    <!-- Top Simulator Banner (Shadcn Minimalist) -->
    <header class="border-b border-border/80 bg-muted/50 px-4 py-2 text-xs">
      <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
        <div class="flex items-center gap-2">
          <Badge variant="outline" class="bg-background text-primary font-bold">MVP V3</Badge>
          <span class="text-muted-foreground hidden sm:inline">
            Aprende enseñando · Los créditos son internos y no representan dinero.
          </span>
        </div>

        <div class="flex items-center gap-1.5 overflow-x-auto">
          <span class="text-muted-foreground text-[11px] mr-1 hidden md:inline">Simular usuario:</span>
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

    <!-- Main Navigation Bar -->
    <nav class="sticky top-0 z-40 w-full border-b border-border/80 bg-background/95 backdrop-blur-md">
      <div class="max-w-7xl mx-auto flex h-16 items-center justify-between px-4 sm:px-6">
        <!-- Logo -->
        <router-link to="/" class="flex items-center gap-2.5 no-underline text-foreground">
          <div class="h-9 w-9 rounded-xl bg-primary flex items-center justify-center text-primary-foreground font-black text-sm shadow-sm">
            95
          </div>
          <div class="flex flex-col">
            <span class="font-extrabold text-base tracking-tight leading-none">Intercambia</span>
            <span class="text-[11px] text-muted-foreground font-medium mt-0.5">Plataforma de Aprendizaje</span>
          </div>
        </router-link>

        <!-- Navigation Links -->
        <div class="hidden md:flex items-center gap-1 text-sm font-medium">
          <router-link
            to="/explore"
            class="px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1.5 no-underline"
            :class="route.name === 'explore' ? 'bg-muted text-foreground font-semibold' : 'text-muted-foreground hover:text-foreground hover:bg-muted/50'"
          >
            <Compass class="h-4 w-4" />
            <span>Explorar</span>
          </router-link>

          <router-link
            to="/search"
            class="px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1.5 no-underline"
            :class="route.name === 'search' ? 'bg-muted text-foreground font-semibold' : 'text-muted-foreground hover:text-foreground hover:bg-muted/50'"
          >
            <Search class="h-4 w-4" />
            <span>Buscar</span>
          </router-link>

          <router-link
            to="/trust"
            class="px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1.5 no-underline"
            :class="route.name === 'trust' ? 'bg-muted text-foreground font-semibold' : 'text-muted-foreground hover:text-foreground hover:bg-muted/50'"
          >
            <ShieldCheck class="h-4 w-4" />
            <span>Confianza</span>
          </router-link>

          <router-link
            v-if="authStore.isAuthenticated"
            to="/workspace"
            class="px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1.5 no-underline"
            :class="route.name === 'workspace' ? 'bg-primary/10 text-primary font-semibold' : 'text-muted-foreground hover:text-foreground hover:bg-muted/50'"
          >
            <User class="h-4 w-4" />
            <span>Mi Espacio</span>
          </router-link>

          <router-link
            v-if="authStore.isAdmin"
            to="/admin"
            class="px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1.5 no-underline text-destructive hover:bg-destructive/10"
            :class="route.name === 'admin' ? 'bg-destructive/15 font-semibold' : ''"
          >
            <ShieldAlert class="h-4 w-4" />
            <span>Admin</span>
            <span v-if="pendingReportsCount > 0" class="h-2 w-2 rounded-full bg-destructive animate-pulse"></span>
          </router-link>
        </div>

        <!-- Auth / Action Area -->
        <div class="flex items-center gap-3">
          <template v-if="authStore.isAuthenticated">
            <!-- Credits Badge -->
            <button
              class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full border border-amber-300 bg-amber-50 text-amber-800 text-xs font-semibold cursor-pointer transition-all hover:bg-amber-100"
              title="1 crédito = 1 hora de sesión. No son dinero."
              @click="router.push({ name: 'workspace', query: { tab: 'credits' } })"
            >
              <Coins class="h-3.5 w-3.5 text-amber-600" />
              <span>{{ authStore.credits }} Créditos</span>
            </button>

            <!-- Profile & Logout -->
            <div class="flex items-center gap-2">
              <span class="text-xs font-semibold text-foreground hidden sm:inline">
                {{ authStore.currentUser.name }}
              </span>
              <Button
                variant="ghost"
                size="icon"
                title="Cerrar sesión"
                @click="handleLogout"
              >
                <LogOut class="h-4 w-4 text-muted-foreground hover:text-foreground" />
              </Button>
            </div>
          </template>

          <template v-else>
            <Button size="sm" @click="router.push({ name: 'auth' })">
              Ingresar
            </Button>
          </template>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-1 py-8 px-4 sm:px-6">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="border-t border-border bg-card py-8 text-sm text-muted-foreground mt-auto">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col md:flex-row items-center justify-between gap-4">
        <div class="text-center md:text-left">
          <div class="font-bold text-foreground">Plataforma de Intercambio de Aprendizajes</div>
          <p class="text-xs mt-1 max-w-md">
            Enseña lo que sabes, aprende lo que necesitas. Los créditos son una unidad interna de coordinación sin equivalencia monetaria.
          </p>
        </div>

        <div class="flex items-center gap-4 text-xs">
          <router-link to="/explore" class="hover:text-foreground transition-colors no-underline">Propuestas</router-link>
          <router-link to="/search" class="hover:text-foreground transition-colors no-underline">Buscador</router-link>
          <router-link to="/trust" class="hover:text-foreground transition-colors no-underline">Confianza</router-link>
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
