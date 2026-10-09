<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from './stores/authStore'
import { usePlatformStore } from './stores/platformStore'

const router = useRouter()
const authStore = useAuthStore()
const platformStore = usePlatformStore()

const currentUser = computed(() => authStore.currentUser)
const wallet = computed(() => platformStore.userWallet(authStore.currentUserId))
const demoUsers = computed(() => authStore.demoUsers)

function handleSwitchUser(event) {
  const selectedId = event.target.value
  authStore.switchUser(selectedId)
  if (router.currentRoute.value.path === '/admin' && !authStore.isAdmin) {
    router.push('/workspace')
  }
}

function handleLogout() {
  authStore.logout()
  router.push('/auth')
}
</script>

<template>
  <div class="min-h-screen flex flex-column bg-slate-50">
    <!-- Barra superior de simulación de perfiles y roles -->
    <div class="bg-slate-900 text-slate-100 px-4 py-2 flex flex-wrap align-items-center justify-content-between text-xs border-bottom-1 border-slate-800">
      <div class="flex align-items-center gap-2">
        <span class="inline-block w-2rem h-2rem bg-indigo-500 border-circle text-center line-height-3 text-white font-bold">V1</span>
        <span class="font-semibold text-white">MVP V3 (PrimeVue 4)</span>
        <span class="text-slate-400 hidden sm:inline">· Simulación de roles y perfiles demo</span>
      </div>

      <div class="flex align-items-center gap-3">
        <div class="flex align-items-center gap-2">
          <label for="demo-switcher" class="text-slate-400">Perfil activo:</label>
          <select
            id="demo-switcher"
            :value="authStore.currentUserId || ''"
            @change="handleSwitchUser"
            class="bg-slate-800 text-white text-xs border-round border-1 border-slate-700 px-2 py-1 outline-none cursor-pointer"
          >
            <option value="" disabled>Seleccionar perfil...</option>
            <option v-for="user in demoUsers" :key="user.id" :value="user.id">
              {{ user.name }} ({{ user.role === 'ADMIN' ? 'ADMIN' : user.badge }})
            </option>
          </select>
        </div>

        <template v-if="authStore.isAuthenticated">
          <div class="flex align-items-center gap-2 bg-slate-800 border-round px-2 py-1">
            <i class="pi pi-wallet text-indigo-400"></i>
            <span class="font-medium text-white">{{ wallet.balance }} créditos</span>
            <span v-if="wallet.blockedBalance > 0" class="text-orange-400 font-semibold" title="Créditos retenidos en garantía">
              ({{ wallet.blockedBalance }} retenidos)
            </span>
          </div>

          <button
            @click="handleLogout"
            class="bg-transparent border-none text-slate-400 hover:text-white cursor-pointer text-xs p-1"
          >
            Cerrar sesión
          </button>
        </template>
        <template v-else>
          <router-link to="/auth" class="text-indigo-400 hover:underline">Iniciar sesión</router-link>
        </template>
      </div>
    </div>

    <!-- Navegación principal -->
    <header class="bg-white border-bottom-1 border-slate-200 sticky top-0 z-5 shadow-1">
      <div class="max-w-7xl mx-auto px-4 py-3 flex align-items-center justify-content-between">
        <router-link to="/" class="flex align-items-center gap-2 no-underline text-900">
          <span class="bg-indigo-600 text-white font-bold p-2 border-round">
            <i class="pi pi-sync"></i>
          </span>
          <div>
            <span class="font-bold text-lg text-slate-900">Intercambia</span>
            <span class="text-xs text-indigo-600 block font-medium">Aprender compartiendo</span>
          </div>
        </router-link>

        <nav class="flex align-items-center gap-2">
          <router-link
            to="/explore"
            class="px-3 py-2 border-round text-sm font-medium text-slate-700 hover:bg-slate-100 no-underline"
            active-class="bg-indigo-50 text-indigo-700 font-semibold"
          >
            <i class="pi pi-compass mr-1"></i> Explorar
          </router-link>

          <router-link
            to="/search"
            class="px-3 py-2 border-round text-sm font-medium text-slate-700 hover:bg-slate-100 no-underline"
            active-class="bg-indigo-50 text-indigo-700 font-semibold"
          >
            <i class="pi pi-search mr-1"></i> Buscar
          </router-link>

          <router-link
            to="/trust"
            class="px-3 py-2 border-round text-sm font-medium text-slate-700 hover:bg-slate-100 no-underline"
            active-class="bg-indigo-50 text-indigo-700 font-semibold"
          >
            <i class="pi pi-shield mr-1"></i> Confianza
          </router-link>

          <router-link
            v-if="authStore.isAuthenticated"
            to="/workspace"
            class="px-3 py-2 border-round text-sm font-medium text-slate-700 hover:bg-slate-100 no-underline"
            active-class="bg-indigo-50 text-indigo-700 font-semibold"
          >
            <i class="pi pi-user mr-1"></i> Mi Panel
          </router-link>

          <router-link
            v-if="authStore.isAdmin"
            to="/admin"
            class="px-3 py-2 border-round text-sm font-medium text-purple-700 bg-purple-50 hover:bg-purple-100 no-underline"
            active-class="bg-purple-100 font-bold"
          >
            <i class="pi pi-cog mr-1"></i> Administración
          </router-link>

          <router-link
            v-if="!authStore.isAuthenticated"
            to="/auth"
            class="ml-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white border-round text-sm font-medium no-underline shadow-1"
          >
            Entrar
          </router-link>
        </nav>
      </div>
    </header>

    <!-- Contenido principal -->
    <main class="flex-grow-1">
      <router-view />
    </main>

    <!-- Pie de página -->
    <footer class="bg-white border-top-1 border-slate-200 py-6 mt-8">
      <div class="max-w-7xl mx-auto px-4 flex flex-column sm:flex-row justify-content-between align-items-center gap-4 text-xs text-slate-500">
        <div>
          <span class="font-bold text-slate-700">Intercambia · MVP V3 (PrimeVue 4)</span>
          <p class="m-0 mt-1">Plataforma P2P de intercambio de habilidades basada en tiempo y créditos internos.</p>
        </div>
        <div class="flex gap-4">
          <router-link to="/explore" class="hover:text-indigo-600">Explorar</router-link>
          <router-link to="/search" class="hover:text-indigo-600">Búsqueda</router-link>
          <router-link to="/trust" class="hover:text-indigo-600">Modelo de confianza</router-link>
          <router-link to="/auth" class="hover:text-indigo-600">Acceso</router-link>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.max-w-7xl {
  max-width: 80rem;
}
.bg-slate-50 { background-color: #f8fafc; }
.bg-slate-100 { background-color: #f1f5f9; }
.bg-slate-200 { background-color: #e2e8f0; }
.bg-slate-700 { background-color: #334155; }
.bg-slate-800 { background-color: #1e293b; }
.bg-slate-900 { background-color: #0f172a; }
.text-slate-100 { color: #f1f5f9; }
.text-slate-400 { color: #94a3b8; }
.text-slate-500 { color: #64748b; }
.text-slate-700 { color: #334155; }
.text-slate-900 { color: #0f172a; }
.border-slate-200 { border-color: #e2e8f0; }
.border-slate-700 { border-color: #334155; }
.border-slate-800 { border-color: #1e293b; }
.bg-indigo-50 { background-color: #eef2ff; }
.bg-indigo-500 { background-color: #6366f1; }
.bg-indigo-600 { background-color: #4f46e5; }
.bg-indigo-700 { background-color: #4338ca; }
.text-indigo-400 { color: #818cf8; }
.text-indigo-600 { color: #4f46e5; }
.text-indigo-700 { color: #4338ca; }
</style>
