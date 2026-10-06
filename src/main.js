import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'
import './assets/base.css'
import App from './App.vue'
import router from './router'
import { IntercambiaPreset } from './theme'

createApp(App)
  .use(PrimeVue, {
    theme: {
      preset: IntercambiaPreset,
      options: { darkModeSelector: false },
    },
  })
  .use(router)
  .mount('#app')
