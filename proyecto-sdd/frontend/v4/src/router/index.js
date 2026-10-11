import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

// En V4 (Spatial Canvas / Lienzo Único), absolutamente todo sucede en la misma vista sin cambiar de página
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
