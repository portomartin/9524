import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { mockStorage } from '../services/mockStorage'
import { useAuthStore } from './authStore'

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

  // Carga inicial
  function refreshAll() {
    offers.value = mockStorage.getPublicOffers()
    needs.value = mockStorage.getPublicNeeds()
    rankings.value = mockStorage.getCommunityRankings()
    trending.value = mockStorage.getTrendingTopics()

    if (authStore.currentUser) {
      const uid = authStore.currentUser.id
      sessions.value = mockStorage.getUserSessions(uid)
      slots.value = mockStorage.getUserSlots(uid)
      creditMovements.value = mockStorage.credits.filter(c => c.userId === uid)
      reviews.value = mockStorage.getUserReviews(uid)
      // Refrescar datos del usuario actual (balance de créditos, reputación)
      const freshUser = mockStorage.findUserById(uid)
      if (freshUser) authStore.currentUser = freshUser
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
  function getPublicUserSlots(userId) {
    return mockStorage.getPublicUserSlots(userId)
  }

  // Acciones de Ofertas
  function createOffer(data) {
    const res = mockStorage.createOffer(authStore.currentUser.id, data)
    refreshAll()
    return res
  }

  function updateOffer(offerId, patch) {
    const res = mockStorage.updateOffer(offerId, patch)
    refreshAll()
    return res
  }

  function deleteOffer(offerId) {
    mockStorage.deleteOffer(offerId)
    refreshAll()
  }

  // Acciones de Necesidades
  function createNeed(data) {
    const res = mockStorage.createNeed(authStore.currentUser.id, data)
    refreshAll()
    return res
  }

  function updateNeed(needId, patch) {
    const res = mockStorage.updateNeed(needId, patch)
    refreshAll()
    return res
  }

  function deleteNeed(needId) {
    mockStorage.deleteNeed(needId)
    refreshAll()
  }

  // Acciones de Disponibilidad
  function addSlot(slotData) {
    const res = mockStorage.addSlot(authStore.currentUser.id, slotData)
    refreshAll()
    return res
  }

  function batchAddSlots(batchData) {
    const res = mockStorage.batchAddSlots(authStore.currentUser.id, batchData)
    refreshAll()
    return res
  }

  function deleteSlot(slotId) {
    mockStorage.deleteSlot(slotId)
    refreshAll()
  }

  function toggleAgendaVisibility(isPublic) {
    mockStorage.toggleAgendaVisibility(authStore.currentUser.id, isPublic)
    refreshAll()
  }

  // Acciones de Sesiones
  function requestSession(payload) {
    const res = mockStorage.createSessionRequest({
      ...payload,
      studentId: authStore.currentUser.id
    })
    refreshAll()
    return res
  }

  function confirmSession(sessionId) {
    const res = mockStorage.confirmSession(sessionId)
    refreshAll()
    return res
  }

  function startSession(sessionId) {
    const res = mockStorage.startSession(sessionId)
    refreshAll()
    return res
  }

  function completeSession(sessionId) {
    const res = mockStorage.completeSession(sessionId)
    refreshAll()
    return res
  }

  function cancelSession(sessionId, reason) {
    const res = mockStorage.cancelSession(sessionId, reason)
    refreshAll()
    return res
  }

  // Calificaciones
  function submitRating({ sessionId, toUserId, rating, comment }) {
    const res = mockStorage.submitRating({
      sessionId,
      fromUserId: authStore.currentUser.id,
      toUserId,
      rating,
      comment
    })
    refreshAll()
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
