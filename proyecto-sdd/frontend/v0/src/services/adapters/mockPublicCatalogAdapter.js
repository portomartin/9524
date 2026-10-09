import { usePlatformStore } from '../../stores/platformStore'

const wait = (milliseconds = 450) => new Promise((resolve) => setTimeout(resolve, milliseconds))
const scenario = import.meta.env.VITE_MOCK_SCENARIO || 'success'

const failWhenRequested = () => {
  if (scenario === 'error') {
    throw { code: 'MOCK_PUBLIC_CATALOG_UNAVAILABLE', message: 'No pudimos cargar el contenido público. Intentá nuevamente.', fields: {} }
  }
}

const newestFirst = (items) => [...items].sort((a, b) => new Date(b.publishedAt) - new Date(a.publishedAt))
const listOrEmpty = (items) => (scenario === 'empty' ? [] : newestFirst(items))

export const mockPublicCatalogAdapter = {
  async listOffers() {
    await wait(); failWhenRequested(); return listOrEmpty(usePlatformStore().state.offers)
  },
  async listLearningNeeds() {
    await wait(); failWhenRequested(); return listOrEmpty(usePlatformStore().state.learningNeeds)
  },
  async getOffer(offerId) {
    await wait(); failWhenRequested()
    const offer = usePlatformStore().state.offers.find(({ id }) => id === offerId)
    if (!offer) throw { code: 'PUBLIC_OFFER_NOT_FOUND', message: 'La propuesta no existe o ya no es pública.', fields: {} }
    return { ...offer }
  },
  async getLearningNeed(learningNeedId) {
    await wait(); failWhenRequested()
    const item = usePlatformStore().state.learningNeeds.find(({ id }) => id === learningNeedId)
    if (!item) throw { code: 'PUBLIC_LEARNING_NEED_NOT_FOUND', message: 'El aprendizaje buscado no existe o ya no es público.', fields: {} }
    return { ...item }
  },
}
