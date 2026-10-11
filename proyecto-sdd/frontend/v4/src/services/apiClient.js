// Cliente HTTP para conectar el frontend v2 con el backend FastAPI
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || ''

class ApiClient {
  getToken() {
    try {
      return localStorage.getItem('intercambia_auth_token') || ''
    } catch {
      return ''
    }
  }

  setToken(token) {
    try {
      if (token) {
        localStorage.setItem('intercambia_auth_token', token)
      } else {
        localStorage.removeItem('intercambia_auth_token')
      }
    } catch (e) {
      console.warn('No se pudo guardar el token en localStorage:', e)
    }
  }

  async request(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`
    const headers = {
      'Content-Type': 'application/json',
      ...(options.headers || {})
    }

    const token = this.getToken()
    if (token && !headers['Authorization']) {
      headers['Authorization'] = `Bearer ${token}`
    }

    const config = {
      ...options,
      headers
    }

    try {
      const response = await fetch(url, config)

      if (response.status === 204) {
        return null
      }

      const contentType = response.headers.get('content-type')
      const isJson = contentType && contentType.includes('application/json')
      const data = isJson ? await response.json() : await response.text()

      if (!response.ok) {
        const errorMsg =
          (data && data.detail && (data.detail.message || data.detail)) ||
          (data && data.message) ||
          `Error HTTP ${response.status}`
        const error = new Error(typeof errorMsg === 'string' ? errorMsg : JSON.stringify(errorMsg))
        error.status = response.status
        error.data = data
        throw error
      }

      return data
    } catch (error) {
      throw error
    }
  }

  get(endpoint, options = {}) {
    return this.request(endpoint, { ...options, method: 'GET' })
  }

  post(endpoint, body, options = {}) {
    return this.request(endpoint, {
      ...options,
      method: 'POST',
      body: JSON.stringify(body)
    })
  }

  patch(endpoint, body, options = {}) {
    return this.request(endpoint, {
      ...options,
      method: 'PATCH',
      body: JSON.stringify(body)
    })
  }

  put(endpoint, body, options = {}) {
    return this.request(endpoint, {
      ...options,
      method: 'PUT',
      body: JSON.stringify(body)
    })
  }

  delete(endpoint, options = {}) {
    return this.request(endpoint, { ...options, method: 'DELETE' })
  }
}

export const apiClient = new ApiClient()
