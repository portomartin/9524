import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './assets/main.css'

import App from './App.vue'
import router from './router'
import { useAuthStore } from './stores/authStore'
import { usePlatformStore } from './stores/platformStore'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)

// Initialize state
const authStore = useAuthStore()
const platformStore = usePlatformStore()
authStore.initAuth()
platformStore.refreshAll()

app.mount('#app')
