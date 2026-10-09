<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Card from 'primevue/card'
import Tabs from 'primevue/tabs'
import TabList from 'primevue/tablist'
import Tab from 'primevue/tab'
import TabPanels from 'primevue/tabpanels'
import TabPanel from 'primevue/tabpanel'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Message from 'primevue/message'
import { usePlatformStore } from '../stores/platformStore'

const route = useRoute()
const router = useRouter()
const { login, register } = usePlatformStore()
const loginForm = ref({ email: 'demo@9524.test', password: 'demo1234' })
const registerForm = ref({ email: '', password: '' })
const error = ref('')
const isLoading = ref(false)

async function submit(mode) {
  error.value = ''
  isLoading.value = true
  try {
    const form = mode === 'login' ? loginForm.value : registerForm.value
    if (!form.email || form.password.length < 8) throw new Error('Ingresá un correo válido y una contraseña de al menos 8 caracteres.')
    if (mode === 'login') await login(form.email, form.password)
    else await register(form.email, form.password)
    router.push(typeof route.query.redirect === 'string' ? route.query.redirect : { name: 'workspace' })
  } catch (submitError) {
    error.value = submitError.message
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="flex justify-content-center py-4">
    <Card class="w-full md:w-8 lg:w-6">
      <template #title>Ingresá cuando quieras participar</template>
      <template #subtitle>La exploración sigue siendo pública. Solo pedimos acceso para acciones protegidas.</template>
      <template #content>
        <Message v-if="error" severity="error" :closable="false" class="mb-3">{{ error }}</Message>
        <Tabs value="login">
          <TabList><Tab value="login">Iniciar sesión</Tab><Tab value="register">Crear cuenta</Tab></TabList>
          <TabPanels>
            <TabPanel value="login">
              <form class="flex flex-column gap-3" @submit.prevent="submit('login')">
                <label for="login-email">Correo</label>
                <InputText id="login-email" v-model="loginForm.email" type="email" autocomplete="email" />
                <label for="login-password">Contraseña</label>
                <Password id="login-password" v-model="loginForm.password" :feedback="false" toggle-mask autocomplete="current-password" />
                <Button type="submit" label="Ingresar" icon="pi pi-sign-in" :loading="isLoading" />
                <Message severity="secondary" :closable="false">Demo: demo@9524.test / demo1234</Message>
              </form>
            </TabPanel>
            <TabPanel value="register">
              <form class="flex flex-column gap-3" @submit.prevent="submit('register')">
                <label for="register-email">Correo</label>
                <InputText id="register-email" v-model="registerForm.email" type="email" autocomplete="email" />
                <label for="register-password">Contraseña</label>
                <Password id="register-password" v-model="registerForm.password" toggle-mask autocomplete="new-password" />
                <Button type="submit" label="Crear cuenta" icon="pi pi-user-plus" :loading="isLoading" />
              </form>
            </TabPanel>
          </TabPanels>
        </Tabs>
      </template>
    </Card>
  </div>
</template>
