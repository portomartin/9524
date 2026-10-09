<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import {
  LogIn,
  UserPlus,
  Info,
  CheckCircle2,
  AlertCircle
} from '@lucide/vue'
import { useAuthStore } from '../stores/authStore'
import { usePlatformStore } from '../stores/platformStore'
import Button from '../components/ui/Button.vue'
import Card from '../components/ui/Card.vue'
import Input from '../components/ui/Input.vue'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()
const platformStore = usePlatformStore()

const isRegisterMode = ref(false)
const name = ref('')
const email = ref('')
const password = ref('')
const errorMessage = ref('')
const isSubmitting = ref(false)

const redirectTarget = route.query.redirect || authStore.redirectAfterLogin || '/workspace'

function handleSubmit() {
  errorMessage.value = ''
  isSubmitting.value = true

  try {
    if (isRegisterMode.value) {
      if (!name.value || !email.value || !password.value) {
        throw new Error('Por favor completa todos los campos del registro.')
      }
      authStore.register({
        name: name.value,
        email: email.value,
        password: password.value
      })
    } else {
      if (!email.value || !password.value) {
        throw new Error('Ingresa tu email y contraseña.')
      }
      authStore.login(email.value, password.value)
    }

    platformStore.refreshAll()
    authStore.redirectAfterLogin = null
    router.push(redirectTarget)
  } catch (err) {
    errorMessage.value = err.message
  } finally {
    isSubmitting.value = false
  }
}

function handleFillDemo(demoEmail, demoPass) {
  isRegisterMode.value = false
  email.value = demoEmail
  password.value = demoPass
}
</script>

<template>
  <div class="max-w-md mx-auto py-6">
    <Card class="p-6 sm:p-8 shadow-sm">
      <!-- Title -->
      <div class="text-center mb-6">
        <div class="h-11 w-11 rounded-2xl bg-primary/10 text-primary flex items-center justify-center mx-auto mb-3">
          <component :is="isRegisterMode ? UserPlus : LogIn" class="h-5 w-5" />
        </div>
        <h1 class="text-2xl font-black tracking-tight text-foreground">
          {{ isRegisterMode ? 'Crear Cuenta Breve' : 'Iniciar Sesión' }}
        </h1>
        <p class="text-xs text-muted-foreground mt-1">
          {{ isRegisterMode ? 'Solo lo imprescindible para comenzar a intercambiar' : 'Accede a tu agenda, sesiones y créditos' }}
        </p>
      </div>

      <!-- Context preservation banner -->
      <div v-if="route.query.redirect" class="rounded-xl border border-blue-200/60 bg-blue-50/50 p-3 text-xs text-blue-900 flex items-center gap-2 mb-4">
        <Info class="h-4 w-4 shrink-0 text-blue-600" />
        <span>Inicia sesión o regístrate para continuar con la acción solicitada.</span>
      </div>

      <!-- Error alert -->
      <div v-if="errorMessage" class="rounded-xl border border-destructive/20 bg-destructive/10 p-3 text-xs text-destructive flex items-center gap-2 mb-4 font-medium">
        <AlertCircle class="h-4 w-4 shrink-0" />
        <span>{{ errorMessage }}</span>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleSubmit" class="flex flex-col gap-3.5">
        <div v-if="isRegisterMode" class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Nombre público</label>
          <Input v-model="name" placeholder="Tu nombre o apodo" />
        </div>

        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Correo Electrónico</label>
          <Input v-model="email" type="email" placeholder="ejemplo@correo.com" />
        </div>

        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-bold text-foreground">Contraseña</label>
          <Input v-model="password" type="password" placeholder="Tu contraseña" />
        </div>

        <Button
          type="submit"
          class="w-full mt-2"
          :disabled="isSubmitting"
        >
          {{ isRegisterMode ? 'Registrarme y Obtener 3 Créditos' : 'Entrar a la Plataforma' }}
        </Button>
      </form>

      <!-- Toggle mode -->
      <div class="text-center mt-6 pt-4 border-t border-border">
        <button
          type="button"
          class="border-none bg-transparent text-primary text-xs font-semibold cursor-pointer hover:underline"
          @click="isRegisterMode = !isRegisterMode; errorMessage = ''"
        >
          {{ isRegisterMode ? '¿Ya tienes una cuenta? Iniciar Sesión' : '¿No tienes cuenta? Regístrate en 1 minuto' }}
        </button>
      </div>

      <!-- Demo Accounts Picker -->
      <div class="mt-6 rounded-xl bg-muted/50 p-3.5 border border-border/60">
        <span class="text-[11px] font-bold uppercase tracking-wider text-muted-foreground block mb-2">
          Cuentas demo para probar:
        </span>
        <div class="flex flex-wrap gap-1.5">
          <button
            type="button"
            class="text-xs bg-card border border-border px-2.5 py-1 rounded-md cursor-pointer hover:bg-muted font-medium text-foreground transition-colors"
            @click="handleFillDemo('juancarlos@example.com', 'password123')"
          >
            Juan (Vue)
          </button>
          <button
            type="button"
            class="text-xs bg-card border border-border px-2.5 py-1 rounded-md cursor-pointer hover:bg-muted font-medium text-foreground transition-colors"
            @click="handleFillDemo('elena@example.com', 'password123')"
          >
            Elena (Inglés)
          </button>
          <button
            type="button"
            class="text-xs bg-card border border-border px-2.5 py-1 rounded-md cursor-pointer hover:bg-muted font-medium text-foreground transition-colors"
            @click="handleFillDemo('carlos@example.com', 'password123')"
          >
            Carlos (DevOps)
          </button>
          <button
            type="button"
            class="text-xs bg-destructive/10 border border-destructive/20 text-destructive px-2.5 py-1 rounded-md cursor-pointer hover:bg-destructive/20 font-medium transition-colors"
            @click="handleFillDemo('admin@example.com', 'adminpassword')"
          >
            Admin
          </button>
        </div>
      </div>
    </Card>
  </div>
</template>
