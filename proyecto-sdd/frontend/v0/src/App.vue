<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { Compass, LogIn, LogOut, Menu, Search, Shield, Sparkles, Star, User, X } from '@lucide/vue'
import UiButton from './components/ui/Button.vue'
import { usePlatformStore } from './stores/platformStore'

const router = useRouter()
const { currentUser, isAuthenticated, isAdmin, logout } = usePlatformStore()
const mobileOpen = ref(false)

const items = computed(() => {
  const publicItems = [
    { label: 'Explorar', icon: Compass, route: { name: 'explore' } },
    { label: 'Buscar', icon: Search, route: { name: 'search' } },
    { label: 'Confianza', icon: Star, route: { name: 'trust' } },
  ]
  if (isAuthenticated.value) publicItems.push({ label: 'Mi espacio', icon: User, route: { name: 'workspace' } })
  if (isAdmin.value) publicItems.push({ label: 'Administración', icon: Shield, route: { name: 'admin' } })
  return publicItems
})

function navigate(route) {
  mobileOpen.value = false
  router.push(route)
}

function signOut() {
  logout()
  mobileOpen.value = false
  router.push({ name: 'explore' })
}
</script>

<template>
  <div class="min-h-screen bg-background text-foreground">
    <header class="sticky top-0 z-50 border-b bg-background/90 backdrop-blur-xl">
      <div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 lg:px-6">
        <button class="flex items-center gap-3 rounded-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring" aria-label="Ir al inicio" @click="navigate({ name: 'explore' })">
          <span class="grid size-9 place-items-center rounded-xl bg-primary text-primary-foreground shadow-sm"><Sparkles :size="18" /></span>
          <span class="text-lg font-bold tracking-tight">Intercambia</span>
        </button>

        <nav class="hidden items-center gap-1 md:flex" aria-label="Navegación principal">
          <UiButton v-for="item in items" :key="item.label" variant="ghost" @click="navigate(item.route)">
            <component :is="item.icon" :size="16" />{{ item.label }}
          </UiButton>
        </nav>

        <div class="hidden items-center gap-2 md:flex">
          <div v-if="currentUser" class="flex items-center gap-2 rounded-full bg-muted px-3 py-1.5 text-sm font-medium">
            <span class="grid size-6 place-items-center rounded-full bg-primary/10 text-xs text-primary">{{ currentUser.name.slice(0, 1).toUpperCase() }}</span>
            <span class="hidden lg:inline">{{ currentUser.name }}</span>
          </div>
          <UiButton v-if="isAuthenticated" variant="ghost" size="sm" @click="signOut"><LogOut :size="16" />Salir</UiButton>
          <UiButton v-else size="sm" @click="navigate({ name: 'auth' })"><LogIn :size="16" />Ingresar</UiButton>
        </div>

        <UiButton class="md:hidden" variant="ghost" size="icon" aria-label="Abrir menú" @click="mobileOpen = !mobileOpen">
          <X v-if="mobileOpen" :size="20" /><Menu v-else :size="20" />
        </UiButton>
      </div>

      <nav v-if="mobileOpen" class="border-t bg-background p-3 md:hidden" aria-label="Navegación móvil">
        <div class="mx-auto flex max-w-7xl flex-col gap-1">
          <UiButton v-for="item in items" :key="item.label" variant="ghost" class="justify-start" @click="navigate(item.route)"><component :is="item.icon" :size="17" />{{ item.label }}</UiButton>
          <UiButton v-if="isAuthenticated" variant="ghost" class="justify-start" @click="signOut"><LogOut :size="17" />Salir</UiButton>
          <UiButton v-else class="justify-start" @click="navigate({ name: 'auth' })"><LogIn :size="17" />Ingresar</UiButton>
        </div>
      </nav>
    </header>

    <main class="mx-auto w-full max-w-7xl px-4 py-6 lg:px-6 lg:py-8">
      <RouterView />
    </main>
  </div>
</template>
