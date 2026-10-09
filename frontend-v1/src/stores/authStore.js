import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { mockStorage } from '../services/mockStorage'

export const useAuthStore = defineStore('auth', () => {
  const currentUser = ref(null)
  const redirectAfterLogin = ref(null)

  const isGuest = computed(() => !currentUser.value)
  const isAuthenticated = computed(() => !!currentUser.value)
  const isAdmin = computed(() => currentUser.value?.role === 'ADMIN')
  const credits = computed(() => currentUser.value?.creditBalance || 0)

  function initAuth() {
    try {
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

  function login(email, password) {
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

  function register({ name, email, password }) {
    const newUser = mockStorage.registerUser({ name, email, password })
    currentUser.value = newUser
    localStorage.setItem('intercambia_logged_in_user_id', newUser.id)
    return newUser
  }

  function logout() {
    currentUser.value = null
    localStorage.removeItem('intercambia_logged_in_user_id')
  }

  function updateProfile(patch) {
    if (!currentUser.value) return
    const updated = mockStorage.updateProfile(currentUser.value.id, patch)
    currentUser.value = updated
    return updated
  }

  function switchUserQuick(userId) {
    const user = mockStorage.findUserById(userId)
    if (user) {
      currentUser.value = user
      localStorage.setItem('intercambia_logged_in_user_id', user.id)
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
