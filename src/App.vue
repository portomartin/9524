<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import Menubar from 'primevue/menubar'
import Button from 'primevue/button'
import Avatar from 'primevue/avatar'
import { usePlatformStore } from './stores/platformStore'

const router = useRouter()
const { currentUser, isAuthenticated, isAdmin, logout } = usePlatformStore()

const items = computed(() => {
  const publicItems = [
    { label: 'Explorar', icon: 'pi pi-compass', command: () => router.push({ name: 'explore' }) },
    { label: 'Buscar', icon: 'pi pi-search', command: () => router.push({ name: 'search' }) },
    { label: 'Confianza', icon: 'pi pi-star', command: () => router.push({ name: 'trust' }) },
  ]
  if (isAuthenticated.value) publicItems.push({ label: 'Mi espacio', icon: 'pi pi-user', command: () => router.push({ name: 'workspace' }) })
  if (isAdmin.value) publicItems.push({ label: 'Administración', icon: 'pi pi-shield', command: () => router.push({ name: 'admin' }) })
  return publicItems
})

function signOut() {
  logout()
  router.push({ name: 'explore' })
}
</script>

<template>
  <div class="min-h-screen surface-ground">
    <Menubar :model="items" class="border-noround border-x-none border-top-none shadow-1 sticky top-0 z-5 px-3 md:px-5">
      <template #start>
        <Button text severity="contrast" aria-label="Ir al inicio" class="mr-2" @click="router.push({ name: 'explore' })">
          <Avatar icon="pi pi-sparkles" shape="circle" class="bg-primary text-primary-contrast mr-2" />
          <span class="font-bold text-lg">Intercambia</span>
        </Button>
      </template>
      <template #end>
        <div class="flex align-items-center gap-2">
          <Avatar v-if="currentUser" :label="currentUser.name.slice(0, 1).toUpperCase()" shape="circle" class="hidden md:flex" />
          <span v-if="currentUser" class="hidden lg:inline text-sm font-medium">{{ currentUser.name }}</span>
          <Button v-if="isAuthenticated" label="Salir" icon="pi pi-sign-out" text size="small" @click="signOut" />
          <Button v-else label="Ingresar" icon="pi pi-sign-in" size="small" @click="router.push({ name: 'auth' })" />
        </div>
      </template>
    </Menubar>
    <main class="w-full lg:w-10 xl:w-9 mx-auto p-3 md:p-5 lg:py-6">
      <RouterView />
    </main>
  </div>
</template>
