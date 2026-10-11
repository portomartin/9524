import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useSpatialStore = defineStore('spatial', () => {
  // Active top/floating capsule: null | 'sessions' | 'publish' | 'credits' | 'profile' | 'auth' | 'admin' | 'trust'
  const activeCapsule = ref(null)

  // Currently expanded card in the Bento Catalog: null | { type: 'offer' | 'need', id: string }
  const expandedItem = ref(null)

  // Currently expanded live exchange card in Community Pulse: null | number
  const expandedExchangeId = ref(null)

  // Live filter state on the single canvas
  const searchQuery = ref('')
  const selectedCategory = ref('TODAS')
  const selectedModality = ref('TODAS')
  const catalogMode = ref('all') // 'all' | 'offers' | 'needs'

  // Visual Flash / Blink state so the user clearly sees WHAT changed after an action/scroll
  const flashingKey = ref(null) // e.g. 'offer-off-1', 'catalog-grid', 'capsule-stage'
  const flashLabel = ref('')
  let flashTimer = null

  // Notification toast in-place
  const liveNotice = ref(null)
  let noticeTimer = null

  function triggerFlash(key, label = '⚡ ¡Acá está el cambio!') {
    if (flashTimer) clearTimeout(flashTimer)
    flashingKey.value = null
    setTimeout(() => {
      flashingKey.value = key
      flashLabel.value = label
    }, 30)
    flashTimer = setTimeout(() => {
      flashingKey.value = null
      flashLabel.value = ''
    }, 2800)
  }

  function toggleCapsule(capsuleName) {
    if (activeCapsule.value === capsuleName) {
      activeCapsule.value = null
    } else {
      activeCapsule.value = capsuleName
      setTimeout(() => {
        const el = document.getElementById('spatial-capsule-stage')
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'nearest' })
        }
        triggerFlash('capsule-stage', '⚡ Cápsula desplegada aquí mismo')
      }, 60)
    }
  }

  function openCapsule(capsuleName) {
    activeCapsule.value = capsuleName
    setTimeout(() => {
      const el = document.getElementById('spatial-capsule-stage')
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'nearest' })
      }
      triggerFlash('capsule-stage', '⚡ Acción lista acá arriba')
    }, 60)
  }

  function closeCapsule() {
    activeCapsule.value = null
  }

  function toggleExpandItem(type, id) {
    if (expandedItem.value && expandedItem.value.type === type && expandedItem.value.id === id) {
      expandedItem.value = null
    } else {
      expandedItem.value = { type, id }
      setTimeout(() => {
        const el = document.getElementById(`bento-card-${type}-${id}`)
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' })
        }
        triggerFlash(`${type}-${id}`, '⚡ Tarjeta amplificada')
      }, 80)
    }
  }

  function expandSpecificItem(type, id, customLabel = '⚡ ¡Acá está tu Match amplificado!') {
    expandedItem.value = { type, id }
    setTimeout(() => {
      const el = document.getElementById(`bento-card-${type}-${id}`)
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' })
      }
      triggerFlash(`${type}-${id}`, customLabel)
    }, 120)
  }

  function collapseItem() {
    expandedItem.value = null
  }

  function toggleExchangeCard(id) {
    if (expandedExchangeId.value === id) {
      expandedExchangeId.value = null
    } else {
      expandedExchangeId.value = id
      triggerFlash(`exchange-${id}`, '⚡ Historia amplificada')
    }
  }

  function filterAndFocusCatalog(query, mode = 'all') {
    searchQuery.value = query
    catalogMode.value = mode
    setTimeout(() => {
      const el = document.getElementById('spatial-catalog-section')
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' })
      }
      triggerFlash('catalog-grid', query ? `⚡ Filtrado en vivo: "${query}"` : '⚡ Tablero actualizado')
    }, 80)
  }

  function clearFilters() {
    searchQuery.value = ''
    selectedCategory.value = 'TODAS'
    selectedModality.value = 'TODAS'
    catalogMode.value = 'all'
    triggerFlash('catalog-grid', '⚡ Mostrando todas las propuestas')
  }

  function notify(title, subtitle = '', type = 'emerald') {
    if (noticeTimer) clearTimeout(noticeTimer)
    liveNotice.value = { title, subtitle, type }
    noticeTimer = setTimeout(() => {
      liveNotice.value = null
    }, 4500)
  }

  return {
    activeCapsule,
    expandedItem,
    expandedExchangeId,
    searchQuery,
    selectedCategory,
    selectedModality,
    catalogMode,
    flashingKey,
    flashLabel,
    liveNotice,
    triggerFlash,
    toggleCapsule,
    openCapsule,
    closeCapsule,
    toggleExpandItem,
    expandSpecificItem,
    collapseItem,
    toggleExchangeCard,
    filterAndFocusCatalog,
    clearFilters,
    notify
  }
})
