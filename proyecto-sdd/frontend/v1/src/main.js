import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'
import './assets/main.css'

import App from './App.vue'
import router from './router'
import { IntercambiaPreset } from './theme'
import { useAuthStore } from './stores/authStore'
import { usePlatformStore } from './stores/platformStore'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(PrimeVue, {
  theme: {
    preset: IntercambiaPreset,
    options: { darkModeSelector: false },
  },
})
app.use(router)

const authStore = useAuthStore()
const platformStore = usePlatformStore()
authStore.initAuth()
platformStore.refreshAll()

app.mount('#app')
