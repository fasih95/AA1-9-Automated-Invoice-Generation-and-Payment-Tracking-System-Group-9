<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Navigation placeholder -->
    <nav class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <h1 class="text-xl font-semibold text-gray-900">Invoice System</h1>
          </div>
          <div class="flex items-center space-x-4">
            <span class="text-sm text-gray-700">Welcome, {{ authStore.user?.first_name || 'User' }}</span>
            <button
              @click="handleLogout"
              class="text-sm text-gray-500 hover:text-gray-700"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>

    <!-- Main content -->
    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <div class="border-4 border-dashed border-gray-200 rounded-lg h-96 flex items-center justify-center">
          <div class="text-center">
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Dashboard</h2>
            <p class="text-gray-600 mb-8">Welcome to the AA1-9 Invoice System</p>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-3xl mx-auto">
              <div class="bg-white p-6 rounded-lg shadow">
                <h3 class="text-lg font-semibold text-gray-900 mb-2">Invoices</h3>
                <p class="text-gray-600">Manage your invoices</p>
                <router-link to="/invoices" class="btn-primary mt-4">
                  View Invoices
                </router-link>
              </div>
              
              <div class="bg-white p-6 rounded-lg shadow">
                <h3 class="text-lg font-semibold text-gray-900 mb-2">Clients</h3>
                <p class="text-gray-600">Manage your clients</p>
                <router-link to="/clients" class="btn-primary mt-4">
                  View Clients
                </router-link>
              </div>
              
              <div class="bg-white p-6 rounded-lg shadow">
                <h3 class="text-lg font-semibold text-gray-900 mb-2">Payments</h3>
                <p class="text-gray-600">Track payments</p>
                <router-link to="/payments" class="btn-primary mt-4">
                  View Payments
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { useToast } from 'vue-toastification'

const authStore = useAuthStore()
const toast = useToast()

const handleLogout = async () => {
  await authStore.logout()
  toast.success('Successfully logged out')
}
</script>
