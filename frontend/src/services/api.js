import axios from 'axios'
import router from '@/router'

const API_BASE_URL = 'http://localhost:8002/api/v1'

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor to add auth token
apiClient.interceptors.request.use(
  (config) => {
    const token = getAccessToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor to handle token refresh
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    // If error is 401 and we haven't tried to refresh token yet
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true

      try {
        const refreshToken = getRefreshToken()
        if (refreshToken) {
          const response = await axios.post(`${API_BASE_URL}/auth/token/refresh/`, {
            refresh: refreshToken,
          })

          if (response.data.access) {
            setAccessToken(response.data.access)
            originalRequest.headers.Authorization = `Bearer ${response.data.access}`
            return apiClient(originalRequest)
          }
        }
      } catch (refreshError) {
        clearTokens()
        router.push({ name: 'login' })
        return Promise.reject(refreshError)
      }
    }

    return Promise.reject(error)
  }
)

// Token management functions (using memory storage as per requirements)
let accessToken = null
let refreshToken = null
let currentUser = null

export const setAccessToken = (token) => {
  accessToken = token
  window.accessToken = token
}

export const setRefreshToken = (token) => {
  refreshToken = token
  window.refreshToken = token
}

export const setCurrentUser = (user) => {
  currentUser = user
  window.currentUser = user
}

export const getAccessToken = () => {
  return accessToken || window.accessToken
}

export const getRefreshToken = () => {
  return refreshToken || window.refreshToken
}

export const getCurrentUser = () => {
  return currentUser || window.currentUser
}

export const clearTokens = () => {
  accessToken = null
  refreshToken = null
  currentUser = null
  window.accessToken = null
  window.refreshToken = null
  window.currentUser = null
}

// API methods
export const authAPI = {
  register: (userData) => apiClient.post('/auth/register/', userData),
  login: (credentials) => apiClient.post('/auth/login/', credentials),
  logout: () => {
    clearTokens()
    return Promise.resolve()
  },
  getProfile: () => apiClient.get('/auth/profile/'),
  updateProfile: (userData) => apiClient.put('/auth/profile/update/', userData),
  changePassword: (passwordData) => apiClient.post('/auth/password/change/', passwordData),
  requestPasswordReset: (email) =>
    apiClient.post('/auth/password/reset/request/', { email }),
  confirmPasswordReset: (data) => apiClient.post('/auth/password/reset/confirm/', data),
  verifyEmail: (token) => apiClient.post('/auth/email/verify/', { token }),
  resendVerificationEmail: () => apiClient.post('/auth/email/resend/'),
}

export default apiClient
