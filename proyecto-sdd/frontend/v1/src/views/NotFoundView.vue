<script setup>
import { useRouter } from 'vue-router'
import { Compass, Home } from '@lucide/vue'
import Button from '../components/ui/Button.vue'
import Card from '../components/ui/Card.vue'

const router = useRouter()
</script>

<template>
  <div class="max-w-md mx-auto py-16 text-center">
    <Card class="p-8 shadow-xs">
      <div class="h-14 w-14 rounded-2xl bg-primary/10 text-primary flex items-center justify-center mx-auto mb-4">
        <Compass class="h-7 w-7" />
      </div>
      <h1 class="text-4xl font-black text-foreground mb-1">404</h1>
      <h2 class="text-base font-bold text-muted-foreground mb-3">Página no encontrada</h2>
      <p class="text-xs text-muted-foreground mb-6">
        La ruta a la que intentas acceder no existe o fue movida.
      </p>
      <Button @click="router.push({ name: 'home' })">
        <Home class="h-4 w-4 mr-1.5" />
        Volver al Inicio
      </Button>
    </Card>
  </div>
</template>
