import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/authStore'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/explore',
    name: 'explore',
    component: () => import('../views/ExploreView.vue')
  },
  {
    path: '/offers/:id',
    name: 'offer-detail',
    component: () => import('../views/OfferDetailView.vue'),
    props: true
  },
  {
    path: '/needs/:id',
    name: 'need-detail',
    component: () => import('../views/NeedDetailView.vue'),
    props: true
  },
  {
    path: '/search',
    name: 'search',
    component: () => import('../views/SearchView.vue')
  },
  {
    path: '/trust',
    name: 'trust',
    component: () => import('../views/TrustView.vue')
  },
  {
    path: '/users/:id/availability',
    name: 'public-availability',
    component: () => import('../views/PublicAvailabilityView.vue'),
    props: true
  },
  {
    path: '/auth',
    name: 'auth',
    component: () => import('../views/AuthView.vue')
  },
  {
    path: '/workspace',
    name: 'workspace',
    component: () => import('../views/WorkspaceView.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/admin',
    name: 'admin',
    component: () => import('../views/AdminView.vue'),
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('../views/NotFoundView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    authStore.redirectAfterLogin = to.fullPath
    return next({ path: '/auth', query: { redirect: to.fullPath } })
  }

  if (to.meta.requiresAdmin && !authStore.isAdmin) {
    return next({ path: '/workspace' })
  }

  next()
})

export default router
