const apiUrl = (import.meta.env.VITE_API_URL || 'https://nine524-api-unificado.onrender.com').replace(/\/$/, '')

export const httpPublicOffersAdapter = {
  async listOffers() {
    try {
      const response = await fetch(`${apiUrl}/api/v1/public/offers`, {
        signal: AbortSignal.timeout(90000),
      })
      if (!response.ok) throw new Error(`HTTP ${response.status}`)
      const offers = await response.json()
      if (!Array.isArray(offers)) throw new Error('Respuesta inválida')
      return offers
    } catch {
      throw {
        code: 'PUBLIC_OFFERS_UNAVAILABLE',
        message: 'No pudimos cargar las propuestas desde el servidor. Intentá nuevamente.',
        fields: {},
      }
    }
  },
}
