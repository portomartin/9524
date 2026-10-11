import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { mockStorage } from '../services/mockStorage'
import { useAuthStore } from './authStore'
import { apiClient } from '../services/apiClient'

export const usePlatformStore = defineStore('platform', () => {
  const authStore = useAuthStore()

  // Estado reactivo
  const offers = ref([])
  const needs = ref([])
  const sessions = ref([])
  const slots = ref([])
  const creditMovements = ref([])
  const reviews = ref([])
  const reports = ref([])
  const rankings = ref([])
  const trending = ref([])

  // Carga inicial y refresco integrado (FastAPI + Fallback Mock)
  async function refreshAll() {
    // 1. Cargar ofertas públicas desde backend o fallback
    try {
      const backendOffers = await apiClient.get('/api/v1/public/offers')
      if (Array.isArray(backendOffers) && backendOffers.length > 0) {
        offers.value = backendOffers
      } else {
        offers.value = mockStorage.getPublicOffers()
      }
    } catch {
      offers.value = mockStorage.getPublicOffers()
    }

    // 2. Cargar necesidades públicas
    try {
      const backendNeeds = await apiClient.get('/api/v1/public/learning-needs')
      if (Array.isArray(backendNeeds) && backendNeeds.length > 0) {
        needs.value = backendNeeds
      } else {
        needs.value = mockStorage.getPublicNeeds()
      }
    } catch {
      needs.value = mockStorage.getPublicNeeds()
    }

    // 3. Cargar rankings
    try {
      const backendRankings = await apiClient.get('/api/v1/public/rankings')
      if (Array.isArray(backendRankings) && backendRankings.length > 0) {
        rankings.value = backendRankings
      } else {
        rankings.value = mockStorage.getCommunityRankings()
      }
    } catch {
      rankings.value = mockStorage.getCommunityRankings()
    }

    // 4. Trending topics
    trending.value = mockStorage.getTrendingTopics()

    // 5. Cargar datos del usuario autenticado si existe
    if (authStore.currentUser) {
      const uid = authStore.currentUser.id

      // Sesiones
      try {
        if (apiClient.getToken()) {
          const backendSessions = await apiClient.get('/api/v1/sessions')
          if (Array.isArray(backendSessions)) {
            sessions.value = backendSessions
          } else {
            sessions.value = mockStorage.getUserSessions(uid)
          }
        } else {
          sessions.value = mockStorage.getUserSessions(uid)
        }
      } catch {
        sessions.value = mockStorage.getUserSessions(uid)
      }

      // Disponibilidad / Slots
      try {
        if (apiClient.getToken()) {
          const backendSlots = await apiClient.get('/api/v1/me/availability')
          if (Array.isArray(backendSlots)) {
            slots.value = backendSlots
          } else {
            slots.value = mockStorage.getUserSlots(uid)
          }
        } else {
          slots.value = mockStorage.getUserSlots(uid)
        }
      } catch {
        slots.value = mockStorage.getUserSlots(uid)
      }

      // Movimientos de créditos
      try {
        if (apiClient.getToken()) {
          const res = await apiClient.get('/api/v1/me/credit-movements')
          if (res && Array.isArray(res.items)) {
            creditMovements.value = res.items
          } else {
            creditMovements.value = mockStorage.credits.filter(c => c.userId === uid)
          }
        } else {
          creditMovements.value = mockStorage.credits.filter(c => c.userId === uid)
        }
      } catch {
        creditMovements.value = mockStorage.credits.filter(c => c.userId === uid)
      }

      reviews.value = mockStorage.getUserReviews(uid)

      // Refrescar datos del usuario actual
      try {
        if (apiClient.getToken()) {
          const freshBackendUser = await apiClient.get('/api/v1/me/profile')
          if (freshBackendUser && freshBackendUser.id) {
            authStore.currentUser = freshBackendUser
          }
        } else {
          const freshUser = mockStorage.findUserById(uid)
          if (freshUser) authStore.currentUser = freshUser
        }
      } catch {
        const freshUser = mockStorage.findUserById(uid)
        if (freshUser) authStore.currentUser = freshUser
      }
    } else {
      sessions.value = []
      slots.value = []
      creditMovements.value = []
      reviews.value = []
    }

    if (authStore.isAdmin) {
      reports.value = mockStorage.getAllReports()
    }
  }

  // Compatibilidades
  const compatibilities = computed(() => {
    if (!authStore.currentUser) return []
    return mockStorage.calculateCompatibilities(authStore.currentUser.id)
  })

  // Agendas públicas
  async function getPublicUserSlots(userId) {
    try {
      const publicSlots = await apiClient.get(`/api/v1/public/users/${userId}/availability`)
      if (Array.isArray(publicSlots)) return publicSlots
    } catch {
      // Fallback
    }
    return mockStorage.getPublicUserSlots(userId)
  }

  // Acciones de Ofertas
  async function createOffer(data) {
    try {
      if (apiClient.getToken()) {
        const created = await apiClient.post('/api/v1/teaching-offers', data)
        await refreshAll()
        return created
      }
    } catch (e) {
      console.warn('Backend createOffer falló, usando fallback:', e.message)
    }
    const res = mockStorage.createOffer(authStore.currentUser.id, data)
    await refreshAll()
    return res
  }

  async function updateOffer(offerId, patch) {
    try {
      if (apiClient.getToken()) {
        const updated = await apiClient.patch(`/api/v1/teaching-offers/${offerId}`, patch)
        await refreshAll()
        return updated
      }
    } catch (e) {
      console.warn('Backend updateOffer falló, usando fallback:', e.message)
    }
    const res = mockStorage.updateOffer(offerId, patch)
    await refreshAll()
    return res
  }

  function deleteOffer(offerId) {
    mockStorage.deleteOffer(offerId)
    refreshAll()
  }

  // Acciones de Necesidades
  async function createNeed(data) {
    try {
      if (apiClient.getToken()) {
        const created = await apiClient.post('/api/v1/learning-needs', data)
        await refreshAll()
        return created
      }
    } catch (e) {
      console.warn('Backend createNeed falló, usando fallback:', e.message)
    }
    const res = mockStorage.createNeed(authStore.currentUser.id, data)
    await refreshAll()
    return res
  }

  async function updateNeed(needId, patch) {
    try {
      if (apiClient.getToken()) {
        const updated = await apiClient.patch(`/api/v1/learning-needs/${needId}`, patch)
        await refreshAll()
        return updated
      }
    } catch (e) {
      console.warn('Backend updateNeed falló, usando fallback:', e.message)
    }
    const res = mockStorage.updateNeed(needId, patch)
    await refreshAll()
    return res
  }

  function deleteNeed(needId) {
    mockStorage.deleteNeed(needId)
    refreshAll()
  }

  // Acciones de Disponibilidad
  async function addSlot(slotData) {
    try {
      if (apiClient.getToken()) {
        const created = await apiClient.post('/api/v1/me/availability', slotData)
        await refreshAll()
        return created
      }
    } catch (e) {
      console.warn('Backend addSlot falló, usando fallback:', e.message)
    }
    const res = mockStorage.addSlot(authStore.currentUser.id, slotData)
    await refreshAll()
    return res
  }

  function batchAddSlots(batchData) {
    const res = mockStorage.batchAddSlots(authStore.currentUser.id, batchData)
    refreshAll()
    return res
  }

  async function deleteSlot(slotId) {
    try {
      if (apiClient.getToken()) {
        await apiClient.delete(`/api/v1/me/availability/${slotId}`)
        await refreshAll()
        return
      }
    } catch (e) {
      console.warn('Backend deleteSlot falló, usando fallback:', e.message)
    }
    mockStorage.deleteSlot(slotId)
    await refreshAll()
  }

  async function toggleAgendaVisibility(isPublic) {
    try {
      if (apiClient.getToken()) {
        await apiClient.put('/api/v1/me/availability-visibility', { public: isPublic })
        await refreshAll()
        return
      }
    } catch (e) {
      console.warn('Backend toggleAgendaVisibility falló:', e.message)
    }
    mockStorage.toggleAgendaVisibility(authStore.currentUser.id, isPublic)
    await refreshAll()
  }

  // Acciones de Sesiones
  async function requestSession(payload) {
    try {
      if (apiClient.getToken()) {
        const created = await apiClient.post('/api/v1/sessions', payload)
        await refreshAll()
        return created
      }
    } catch (e) {
      console.warn('Backend requestSession falló, usando fallback:', e.message)
    }
    const res = mockStorage.createSessionRequest({
      ...payload,
      studentId: authStore.currentUser.id
    })
    await refreshAll()
    return res
  }

  async function confirmSession(sessionId) {
    try {
      if (apiClient.getToken()) {
        const confirmed = await apiClient.post(`/api/v1/sessions/${sessionId}/confirm`, {})
        await refreshAll()
        return confirmed
      }
    } catch (e) {
      console.warn('Backend confirmSession falló:', e.message)
    }
    const res = mockStorage.confirmSession(sessionId)
    await refreshAll()
    return res
  }

  function startSession(sessionId) {
    const res = mockStorage.startSession(sessionId)
    refreshAll()
    return res
  }

  async function completeSession(sessionId) {
    try {
      if (apiClient.getToken()) {
        const completed = await apiClient.post(`/api/v1/sessions/${sessionId}/complete`, {})
        await refreshAll()
        return completed
      }
    } catch (e) {
      console.warn('Backend completeSession falló:', e.message)
    }
    const res = mockStorage.completeSession(sessionId)
    await refreshAll()
    return res
  }

  async function cancelSession(sessionId, reason) {
    try {
      if (apiClient.getToken()) {
        const canceled = await apiClient.post(`/api/v1/sessions/${sessionId}/cancel`, { reason })
        await refreshAll()
        return canceled
      }
    } catch (e) {
      console.warn('Backend cancelSession falló:', e.message)
    }
    const res = mockStorage.cancelSession(sessionId, reason)
    await refreshAll()
    return res
  }

  // Calificaciones
  async function submitRating({ sessionId, toUserId, rating, comment }) {
    try {
      if (apiClient.getToken()) {
        const rated = await apiClient.post(`/api/v1/sessions/${sessionId}/ratings`, {
          rating,
          comment
        })
        await refreshAll()
        return rated
      }
    } catch (e) {
      console.warn('Backend submitRating falló:', e.message)
    }
    const res = mockStorage.submitRating({
      sessionId,
      fromUserId: authStore.currentUser.id,
      toUserId,
      rating,
      comment
    })
    await refreshAll()
    return res
  }

  // Denuncias
  function submitReport(reportData) {
    const reporterId = authStore.currentUser ? authStore.currentUser.id : 'anon'
    const res = mockStorage.submitReport({
      reporterId,
      ...reportData
    })
    if (authStore.isAdmin) reports.value = mockStorage.getAllReports()
    return res
  }

  // Moderación Admin
  function resolveReport(reportId, action) {
    const res = mockStorage.resolveReport(reportId, action)
    refreshAll()
    return res
  }

  function toggleUserSuspension(userId) {
    const res = mockStorage.toggleUserSuspension(userId)
    refreshAll()
    return res
  }

  function hideOffer(offerId) {
    const res = mockStorage.hideOffer(offerId)
    refreshAll()
    return res
  }

  function resetAllData() {
    mockStorage.resetToDefaults()
    refreshAll()
  }

  return {
    offers,
    needs,
    sessions,
    slots,
    creditMovements,
    reviews,
    reports,
    rankings,
    trending,
    compatibilities,
    refreshAll,
    getPublicUserSlots,
    createOffer,
    updateOffer,
    deleteOffer,
    createNeed,
    updateNeed,
    deleteNeed,
    addSlot,
    batchAddSlots,
    deleteSlot,
    toggleAgendaVisibility,
    requestSession,
    confirmSession,
    startSession,
    completeSession,
    cancelSession,
    submitRating,
    submitReport,
    resolveReport,
    toggleUserSuspension,
    hideOffer,
    resetAllData
  }
})
