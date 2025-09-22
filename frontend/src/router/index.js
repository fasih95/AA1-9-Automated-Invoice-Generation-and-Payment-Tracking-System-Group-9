import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Import views
import LoginView from '@/views/auth/LoginView.vue'
import DashboardView from '@/views/DashboardView.vue'
import InvoicesView from '@/views/invoices/InvoicesView.vue'
import InvoiceCreateView from '@/views/invoices/InvoiceCreateView.vue'
import InvoiceDetailView from '@/views/invoices/InvoiceDetailView.vue'
import ClientsView from '@/views/clients/ClientsView.vue'
import ClientCreateView from '@/views/clients/ClientCreateView.vue'
import ClientDetailView from '@/views/clients/ClientDetailView.vue'
import PaymentsView from '@/views/payments/PaymentsView.vue'
import PaymentDetailView from '@/views/payments/PaymentDetailView.vue'
import ReportsView from '@/views/reports/ReportsView.vue'
import UsersView from '@/views/users/UsersView.vue'
import UserCreateView from '@/views/users/UserCreateView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SettingsView from '@/views/SettingsView.vue'
import NotFoundView from '@/views/NotFoundView.vue'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: { requiresGuest: true }
  },
  {
    path: '/',
    name: 'dashboard',
    component: DashboardView,
    meta: { requiresAuth: true }
  },
  {
    path: '/invoices',
    name: 'invoices',
    component: InvoicesView,
    meta: { requiresAuth: true, permissions: ['view_invoice'] }
  },
  {
    path: '/invoices/create',
    name: 'invoice-create',
    component: InvoiceCreateView,
    meta: { requiresAuth: true, permissions: ['add_invoice'] }
  },
  {
    path: '/invoices/:id',
    name: 'invoice-detail',
    component: InvoiceDetailView,
    meta: { requiresAuth: true, permissions: ['view_invoice'] },
    props: true
  },
  {
    path: '/clients',
    name: 'clients',
    component: ClientsView,
    meta: { requiresAuth: true, permissions: ['view_client'] }
  },
  {
    path: '/clients/create',
    name: 'client-create',
    component: ClientCreateView,
    meta: { requiresAuth: true, permissions: ['add_client'] }
  },
  {
    path: '/clients/:id',
    name: 'client-detail',
    component: ClientDetailView,
    meta: { requiresAuth: true, permissions: ['view_client'] },
    props: true
  },
  {
    path: '/payments',
    name: 'payments',
    component: PaymentsView,
    meta: { requiresAuth: true, permissions: ['view_payment'] }
  },
  {
    path: '/payments/:id',
    name: 'payment-detail',
    component: PaymentDetailView,
    meta: { requiresAuth: true, permissions: ['view_payment'] },
    props: true
  },
  {
    path: '/reports',
    name: 'reports',
    component: ReportsView,
    meta: { requiresAuth: true, permissions: ['view_reports'] }
  },
  {
    path: '/users',
    name: 'users',
    component: UsersView,
    meta: { requiresAuth: true, permissions: ['view_user'], roles: ['admin'] }
  },
  {
    path: '/users/create',
    name: 'user-create',
    component: UserCreateView,
    meta: { requiresAuth: true, permissions: ['add_user'], roles: ['admin'] }
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    meta: { requiresAuth: true }
  },
  {
    path: '/settings',
    name: 'settings',
    component: SettingsView,
    meta: { requiresAuth: true, roles: ['admin'] }
  },
  {
    path: '/404',
    name: 'not-found',
    component: NotFoundView
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/404'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// Navigation guards
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  
  // Check if route requires authentication
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login')
    return
  }
  
  // Check if route requires guest (not authenticated)
  if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next('/')
    return
  }
  
  // Check permissions
  if (to.meta.permissions && !authStore.hasPermissions(to.meta.permissions)) {
    next('/404')
    return
  }
  
  // Check roles
  if (to.meta.roles && !authStore.hasRole(to.meta.roles)) {
    next('/404')
    return
  }
  
  next()
})

export default router
