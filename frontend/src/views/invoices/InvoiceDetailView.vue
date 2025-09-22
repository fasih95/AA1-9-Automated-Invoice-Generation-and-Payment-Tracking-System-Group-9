<template>
  <div class="min-h-screen bg-gray-50 p-8">
    <div class="max-w-7xl mx-auto">
      <h1 class="text-3xl font-bold text-gray-900 mb-8">Invoice Details</h1>
      <div class="bg-white shadow rounded-lg p-6">
        <p class="text-gray-600">Invoice details for ID: {{ id }}</p>
        <router-link to="/invoices" class="btn-primary mt-4">Back to Invoices</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  id: String
})
</script>
