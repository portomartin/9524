import { ref } from 'vue'
import { publicCatalogService } from '../services/publicCatalogService'

export function usePublicCatalog() {
  const offers = ref([])
  const learningNeeds = ref([])
  const isLoading = ref(false)
  const error = ref(null)

  async function loadCatalog() {
    isLoading.value = true
    error.value = null
    try {
      const [offerResults, learningNeedResults] = await Promise.all([
        publicCatalogService.listOffers(), publicCatalogService.listLearningNeeds(),
      ])
      offers.value = offerResults
      learningNeeds.value = learningNeedResults
    } catch (catalogError) {
      error.value = catalogError
      offers.value = []
      learningNeeds.value = []
    } finally {
      isLoading.value = false
    }
  }

  return { offers, learningNeeds, isLoading, error, loadCatalog }
}
