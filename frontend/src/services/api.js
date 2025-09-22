import axios from 'axios'
import { useAuthStore } from '@/stores/auth'

// Create axios instance
const api = axios.create({
  baseURL: '/api/v1',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
})

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // Add timestamp to prevent caching
    if (config.method === 'get') {
      config.params = { ...config.params, _t: Date.now() }
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
api.interceptors.response.use(
  (response) => {
    return response
  },
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true

      try {
        const authStore = useAuthStore()
        await authStore.refreshAccessToken()
        
        // Retry the original request with new token
        return api(originalRequest)
      } catch (refreshError) {
        // Refresh failed, user will be logged out by auth store
        return Promise.reject(refreshError)
      }
    }

    return Promise.reject(error)
  }
)

// API methods
export const authAPI = {
  login: (credentials) => api.post('/auth/login/', credentials),
  logout: (refreshToken) => api.post('/auth/logout/', { refresh: refreshToken }),
  refresh: (refreshToken) => api.post('/auth/refresh/', { refresh: refreshToken }),
  me: () => api.get('/auth/me/'),
  profile: (data) => api.patch('/auth/profile/', data),
  changePassword: (data) => api.post('/auth/change-password/', data),
}

export const clientsAPI = {
  list: (params) => api.get('/clients/', { params }),
  create: (data) => api.post('/clients/', data),
  get: (id) => api.get(`/clients/${id}/`),
  update: (id, data) => api.patch(`/clients/${id}/`, data),
  delete: (id) => api.delete(`/clients/${id}/`),
}

export const invoicesAPI = {
  list: (params) => api.get('/invoices/', { params }),
  create: (data) => api.post('/invoices/', data),
  get: (id) => api.get(`/invoices/${id}/`),
  update: (id, data) => api.patch(`/invoices/${id}/`, data),
  delete: (id) => api.delete(`/invoices/${id}/`),
  generatePDF: (id) => api.get(`/invoices/${id}/pdf/`, { responseType: 'blob' }),
  sendEmail: (id, data) => api.post(`/invoices/${id}/send-email/`, data),
  markAsSent: (id) => api.post(`/invoices/${id}/mark-sent/`),
  markAsPaid: (id) => api.post(`/invoices/${id}/mark-paid/`),
}

export const paymentsAPI = {
  list: (params) => api.get('/payments/', { params }),
  create: (data) => api.post('/payments/', data),
  get: (id) => api.get(`/payments/${id}/`),
  update: (id, data) => api.patch(`/payments/${id}/`, data),
  delete: (id) => api.delete(`/payments/${id}/`),
}

export const usersAPI = {
  list: (params) => api.get('/users/', { params }),
  create: (data) => api.post('/users/', data),
  get: (id) => api.get(`/users/${id}/`),
  update: (id, data) => api.patch(`/users/${id}/`, data),
  delete: (id) => api.delete(`/users/${id}/`),
}

export const reportsAPI = {
  dashboard: () => api.get('/reports/dashboard/'),
  revenue: (params) => api.get('/reports/revenue/', { params }),
  invoices: (params) => api.get('/reports/invoices/', { params }),
  clients: (params) => api.get('/reports/clients/', { params }),
  payments: (params) => api.get('/reports/payments/', { params }),
}

export { api }
