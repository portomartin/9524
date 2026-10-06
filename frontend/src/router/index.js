import { createRouter, createWebHistory } from 'vue-router'
import { usePlatformStore } from '../stores/platformStore'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'explore', component: () => import('../views/ExploreView.vue') },
    { path: '/confianza', name: 'trust', component: () => import('../views/TrustView.vue') },
    { path: '/buscar', name: 'search', component: () => import('../views/SearchView.vue') },
    { path: '/acceso', name: 'auth', component: () => import('../views/AuthView.vue') },
    { path: '/propuestas/:offerId', name: 'public-offer-detail', component: () => import('../views/PublicOfferDetailView.vue'), props: true },
    { path: '/aprendizajes/:learningNeedId', name: 'public-learning-need-detail', component: () => import('../views/PublicLearningNeedDetailView.vue'), props: true },
    { path: '/mi-espacio/:section?', name: 'workspace', component: () => import('../views/WorkspaceView.vue'), props: true, meta: { requiresAuth: true } },
    { path: '/administracion', name: 'admin', component: () => import('../views/AdminView.vue'), meta: { requiresAuth: true, requiresAdmin: true } },
    { path: '/:pathMatch(.*)*', redirect: { name: 'explore' } },
  ],
  scrollBehavior: () => ({ top: 0 }),
})

router.beforeEach((to) => {
  const { isAuthenticated, isAdmin } = usePlatformStore()
  if (to.meta.requiresAuth && !isAuthenticated.value) return { name: 'auth', query: { redirect: to.fullPath } }
  if (to.meta.requiresAdmin && !isAdmin.value) return { name: 'workspace', query: { denied: 'admin' } }
  if (to.name === 'auth' && isAuthenticated.value) return { name: 'workspace' }
  return true
})

export default router
