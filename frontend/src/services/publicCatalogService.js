import { mockPublicCatalogAdapter } from './adapters/mockPublicCatalogAdapter'

const apiMode = import.meta.env.VITE_API_MODE || 'mock'
const adapters = { mock: mockPublicCatalogAdapter }
const adapter = adapters[apiMode]

if (!adapter) throw new Error(`VITE_API_MODE=${apiMode} todavía no tiene un adaptador configurado.`)

export const publicCatalogService = {
  listOffers: () => adapter.listOffers(),
  listLearningNeeds: () => adapter.listLearningNeeds(),
  getOffer: (offerId) => adapter.getOffer(offerId),
  getLearningNeed: (learningNeedId) => adapter.getLearningNeed(learningNeedId),
}
