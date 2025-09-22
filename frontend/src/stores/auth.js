import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { api } from '@/services/api'
import router from '@/router'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const token = ref(localStorage.getItem('token'))
  const refreshToken = ref(localStorage.getItem('refreshToken'))
  const loading = ref(false)
  const error = ref(null)

  // Computed
  const isAuthenticated = computed(() => !!token.value && !!user.value)
  const userRole = computed(() => user.value?.role || null)
  const userPermissions = computed(() => user.value?.permissions || [])

  // Actions
  async function login(credentials) {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.post('/auth/login/', credentials)
      const { access, refresh, user: userData } = response.data
      
      token.value = access
      refreshToken.value = refresh
      user.value = userData
      
      localStorage.setItem('token', access)
      localStorage.setItem('refreshToken', refresh)
      
      // Set API default header
      api.defaults.headers.common['Authorization'] = `Bearer ${access}`
      
      return { success: true }
    } catch (err) {
      error.value = err.response?.data?.message || 'Login failed'
      return { success: false, error: error.value }
    } finally {
      loading.value = false
    }
  }

  async function logout() {
    try {
      if (refreshToken.value) {
        await api.post('/auth/logout/', { refresh: refreshToken.value })
      }
    } catch (err) {
      console.error('Logout error:', err)
    } finally {
      // Clear all auth data
      user.value = null
      token.value = null
      refreshToken.value = null
      
      localStorage.removeItem('token')
      localStorage.removeItem('refreshToken')
      
      delete api.defaults.headers.common['Authorization']
      
      router.push('/login')
    }
  }

  async function refreshAccessToken() {
    if (!refreshToken.value) {
      throw new Error('No refresh token available')
    }

    try {
      const response = await api.post('/auth/refresh/', {
        refresh: refreshToken.value
      })
      
      const { access } = response.data
      token.value = access
      localStorage.setItem('token', access)
      api.defaults.headers.common['Authorization'] = `Bearer ${access}`
      
      return access
    } catch (err) {
      // Refresh token is invalid, logout user
      await logout()
      throw err
    }
  }

  async function fetchUser() {
    if (!token.value) return

    try {
      const response = await api.get('/auth/me/')
      user.value = response.data
    } catch (err) {
      console.error('Failed to fetch user:', err)
      await logout()
    }
  }

  async function updateProfile(profileData) {
    loading.value = true
    error.value = null

    try {
      const response = await api.patch('/auth/profile/', profileData)
      user.value = { ...user.value, ...response.data }
      return { success: true }
    } catch (err) {
      error.value = err.response?.data?.message || 'Profile update failed'
      return { success: false, error: error.value }
    } finally {
      loading.value = false
    }
  }

  function hasPermission(permission) {
    return userPermissions.value.includes(permission)
  }

  function hasPermissions(permissions) {
    return permissions.every(permission => hasPermission(permission))
  }

  function hasRole(roles) {
    if (Array.isArray(roles)) {
      return roles.includes(userRole.value)
    }
    return userRole.value === roles
  }

  // Initialize auth state
  function initialize() {
    if (token.value) {
      api.defaults.headers.common['Authorization'] = `Bearer ${token.value}`
      fetchUser()
    }
  }

  return {
    // State
    user,
    token,
    refreshToken,
    loading,
    error,
    
    // Computed
    isAuthenticated,
    userRole,
    userPermissions,
    
    // Actions
    login,
    logout,
    refreshAccessToken,
    fetchUser,
    updateProfile,
    hasPermission,
    hasPermissions,
    hasRole,
    initialize
  }
})
