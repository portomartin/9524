import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { mockStorage } from '../services/mockStorage'
import { apiClient } from '../services/apiClient'

export const useAuthStore = defineStore('auth', () => {
  const currentUser = ref(null)
  const redirectAfterLogin = ref(null)

  const isGuest = computed(() => !currentUser.value)
  const isAuthenticated = computed(() => !!currentUser.value)
  const isAdmin = computed(() => currentUser.value?.role === 'ADMIN')
  const credits = computed(() => currentUser.value?.creditBalance ?? currentUser.value?.credit_balance ?? 0)

  async function initAuth() {
    try {
      const savedToken = apiClient.getToken()
      if (savedToken) {
        try {
          // Intentar validar sesión con backend FastAPI
          const backendProfile = await apiClient.get('/api/v1/me/profile')
          if (backendProfile && backendProfile.id) {
            currentUser.value = backendProfile
            localStorage.setItem('intercambia_logged_in_user_id', backendProfile.id)
            return
          }
        } catch (e) {
          // Si el token expiró o el backend no responde, intentar fallback
          console.warn('Sesión remota expirada o backend inaccesible:', e.message)
        }
      }

      const savedUserId = localStorage.getItem('intercambia_logged_in_user_id')
      if (savedUserId) {
        const found = mockStorage.findUserById(savedUserId)
        if (found && found.status !== 'SUSPENDIDO') {
          currentUser.value = found
          return
        }
      }
    } catch {
      // Local storage disabled or error
    }
    // Default to GUEST on initial load
    currentUser.value = null
  }

  async function login(email, password) {
    try {
      // Intentar primero autenticar contra el backend FastAPI
      const res = await apiClient.post('/api/v1/auth/login', { email, password })
      if (res && res.access_token) {
        apiClient.setToken(res.access_token)
        currentUser.value = res.user
        localStorage.setItem('intercambia_logged_in_user_id', res.user.id)
        return res.user
      }
    } catch (apiErr) {
      // Si el backend da error de credenciales explícito, lanzarlo
      if (apiErr.status === 401 || apiErr.status === 403 || apiErr.status === 422) {
        throw apiErr
      }
      console.warn('Backend inaccesible en login, probando fallback local:', apiErr.message)
    }

    // Fallback a mockStorage
    const user = mockStorage.findUserByEmail(email)
    if (!user) {
      throw new Error('Credenciales inválidas. Revisa el correo electrónico.')
    }
    if (user.password !== password) {
      throw new Error('Contraseña incorrecta.')
    }
    if (user.status === 'SUSPENDIDO') {
      throw new Error('Esta cuenta ha sido suspendida por administración por infracción de normas.')
    }

    currentUser.value = user
    localStorage.setItem('intercambia_logged_in_user_id', user.id)
    return user
  }

  async function register({ name, email, password }) {
    try {
      // Intentar registrar en backend FastAPI
      const res = await apiClient.post('/api/v1/users', { name, email, password })
      if (res && res.access_token) {
        apiClient.setToken(res.access_token)
        currentUser.value = res.user
        localStorage.setItem('intercambia_logged_in_user_id', res.user.id)
        return res.user
      }
    } catch (apiErr) {
      if (apiErr.status === 409 || apiErr.status === 422) {
        throw apiErr
      }
      console.warn('Backend inaccesible en registro, probando fallback local:', apiErr.message)
    }

    // Fallback a mockStorage
    const newUser = mockStorage.registerUser({ name, email, password })
    currentUser.value = newUser
    localStorage.setItem('intercambia_logged_in_user_id', newUser.id)
    return newUser
  }

  async function logout() {
    try {
      if (apiClient.getToken()) {
        await apiClient.post('/api/v1/auth/logout', {}).catch(() => {})
      }
    } catch {
      // Ignorar errores al desloguear
    }
    currentUser.value = null
    apiClient.setToken('')
    localStorage.removeItem('intercambia_logged_in_user_id')
  }

  async function updateProfile(patch) {
    if (!currentUser.value) return
    try {
      if (apiClient.getToken()) {
        const updated = await apiClient.patch('/api/v1/me/profile', patch)
        if (updated) {
          currentUser.value = { ...currentUser.value, ...updated }
          return currentUser.value
        }
      }
    } catch (e) {
      console.warn('No se pudo actualizar en backend, aplicando fallback local:', e.message)
    }

    const updated = mockStorage.updateProfile(currentUser.value.id, patch)
    currentUser.value = updated
    return updated
  }

  function switchUserQuick(userId) {
    const user = mockStorage.findUserById(userId)
    if (user) {
      currentUser.value = user
      localStorage.setItem('intercambia_logged_in_user_id', user.id)
      // Limpiar token JWT en simulador rápido para no generar desajustes con el backend
      apiClient.setToken('')
    }
  }

  return {
    currentUser,
    redirectAfterLogin,
    isGuest,
    isAuthenticated,
    isAdmin,
    credits,
    initAuth,
    login,
    register,
    logout,
    updateProfile,
    switchUserQuick
  }
})
