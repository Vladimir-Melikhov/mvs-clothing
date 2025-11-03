<template>
    <div class="min-h-screen bg-gray-50">
      <AppHeader variant="dark" />
      <div class="max-w-7xl mx-auto px-6 py-12 mt-20">
        <div class="mb-8">
          <h1 class="text-3xl font-light tracking-[0.3em] text-gray-900" style="font-family: Georgia, serif;">
            Checkout
          </h1>
          <p class="mt-2 text-sm text-gray-600 tracking-wide">
            Complete your order
          </p>
        </div>
  
        <div class="grid lg:grid-cols-3 gap-8">
          <!-- Checkout Form -->
          <div class="lg:col-span-2">
            <form @submit.prevent="handleSubmit" class="space-y-6">
              <!-- Shipping Information -->
              <div class="bg-white border border-gray-200 p-6">
                <h2 class="text-lg font-medium text-gray-900 mb-6 tracking-wide">
                  SHIPPING INFORMATION
                </h2>
  
                <div class="grid md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">First Name</label>
                    <input
                      v-model="formData.shipping_first_name"
                      type="text"
                      required
                      class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                    />
                  </div>
  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Last Name</label>
                    <input
                      v-model="formData.shipping_last_name"
                      type="text"
                      required
                      class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                    />
                  </div>
  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                    <input
                      v-model="formData.shipping_email"
                      type="email"
                      required
                      class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                    />
                  </div>
  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Phone</label>
                    <input
                      v-model="formData.shipping_phone"
                      type="tel"
                      required
                      class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                    />
                  </div>
  
                  <div class="md:col-span-2">
                    <label class="block text-sm font-medium text-gray-700 mb-2">Address</label>
                    <input
                      v-model="formData.shipping_address"
                      type="text"
                      required
                      class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                    />
                  </div>
  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">City</label>
                    <input
                      v-model="formData.shipping_city"
                      type="text"
                      required
                      class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                    />
                  </div>
  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">State/Province</label>
                    <input
                      v-model="formData.shipping_state"
                      type="text"
                      required
                      class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                    />
                  </div>
  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Postal Code</label>
                    <input
                      v-model="formData.shipping_postal_code"
                      type="text"
                      required
                      class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                    />
                  </div>
  
                  <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">Country</label>
                    <input
                      v-model="formData.shipping_country"
                      type="text"
                      required
                      class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                    />
                  </div>
                </div>
              </div>
  
              <!-- Order Notes -->
              <div class="bg-white border border-gray-200 p-6">
                <h2 class="text-lg font-medium text-gray-900 mb-4 tracking-wide">
                  ORDER NOTES (OPTIONAL)
                </h2>
                <textarea
                  v-model="formData.notes"
                  rows="3"
                  placeholder="Any special instructions for your order"
                  class="w-full px-4 py-3 border border-gray-300 focus:outline-none focus:border-black"
                ></textarea>
              </div>
  
              <!-- Error Message -->
              <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-800 px-4 py-3 text-sm">
                <p>{{ errorMessage }}</p>
              </div>
  
              <!-- Submit Button -->
              <button
                type="submit"
                :disabled="submitting || cartStore.isEmpty"
                class="w-full px-6 py-4 border border-black text-sm font-medium tracking-widest transition-all"
                :class="
                  submitting || cartStore.isEmpty
                    ? 'text-gray-400 bg-gray-100 border-gray-300 cursor-not-allowed'
                    : 'text-white bg-black hover:bg-gray-900'
                "
              >
                <span v-if="submitting">PLACING ORDER...</span>
                <span v-else>PLACE ORDER</span>
              </button>
            </form>
          </div>
  
          <!-- Order Summary -->
          <div class="lg:col-span-1">
            <div class="bg-white border border-gray-200 p-6 sticky top-24">
              <h2 class="text-lg font-medium text-gray-900 mb-4 tracking-wide">
                ORDER SUMMARY
              </h2>
  
              <!-- Cart Items -->
              <div class="space-y-4 mb-6">
                <div
                  v-for="item in cartStore.items"
                  :key="item.id"
                  class="flex gap-4 pb-4 border-b border-gray-200"
                >
                  <div class="w-16 h-20 bg-gray-100 flex-shrink-0">
                    <img
                      v-if="item.product.primary_image"
                      :src="getImageUrl(item.product.primary_image)"
                      :alt="item.product.name"
                      class="w-full h-full object-cover"
                    />
                  </div>
                  <div class="flex-1">
                    <p class="text-sm font-medium text-gray-900">{{ item.product.name }}</p>
                    <p class="text-xs text-gray-600 mt-1">Qty: {{ item.quantity }}</p>
                    <p class="text-sm font-medium text-gray-900 mt-1">${{ item.total_price }}</p>
                  </div>
                </div>
              </div>
  
              <!-- Price Breakdown -->
              <div class="space-y-3 mb-6">
                <div class="flex justify-between text-sm">
                  <span class="text-gray-600">Subtotal</span>
                  <span class="text-gray-900 font-medium">${{ cartStore.subtotal }}</span>
                </div>
                <div class="flex justify-between text-sm">
                  <span class="text-gray-600">Shipping</span>
                  <span class="text-gray-900 font-medium">$0.00</span>
                </div>
              </div>
  
              <div class="border-t border-gray-200 pt-4">
                <div class="flex justify-between">
                  <span class="text-base font-medium text-gray-900">Total</span>
                  <span class="text-lg font-medium text-gray-900">${{ cartStore.subtotal }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive, computed, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import { useCartStore } from '@/stores/cart'
  import { useOrdersStore } from '@/stores/orders'
  import { useAuthStore } from '@/stores/auth'
  import AppHeader from '@/components/layout/AppHeader.vue'
  
  const router = useRouter()
  const cartStore = useCartStore()
  const ordersStore = useOrdersStore()
  const authStore = useAuthStore()
  
  const submitting = ref(false)
  const errorMessage = ref('')
  
  const user = computed(() => authStore.user)
  
  const formData = reactive({
    shipping_first_name: '',
    shipping_last_name: '',
    shipping_email: '',
    shipping_phone: '',
    shipping_address: '',
    shipping_city: '',
    shipping_state: '',
    shipping_postal_code: '',
    shipping_country: '',
    notes: '',
  })
  
  const getImageUrl = (url) => {
    if (url && url.startsWith('http')) {
      return url
    }
    return `http://localhost:8002${url || ''}`
  }
  
  const handleSubmit = async () => {
    if (cartStore.isEmpty) {
      errorMessage.value = 'Your cart is empty'
      return
    }
  
    submitting.value = true
    errorMessage.value = ''
  
    try {
      // Prepare order data
      const orderData = {
        ...formData,
        items: cartStore.items.map((item) => ({
          product_id: item.product.id,
          variant_id: item.variant_details?.id || null,
          quantity: item.quantity,
          price: item.price,
        })),
        shipping_cost: 0,
      }
  
      const result = await ordersStore.createOrder(orderData)
  
      if (result.success) {
        // Clear cart
        await cartStore.clearCart()
  
        // Redirect to order confirmation
        router.push(`/orders/${result.order.id}`)
      } else {
        errorMessage.value = result.message
      }
    } catch (error) {
      errorMessage.value = 'An unexpected error occurred. Please try again.'
    } finally {
      submitting.value = false
    }
  }
  
  onMounted(async () => {
    // Pre-fill form with user data
    if (user.value) {
      formData.shipping_first_name = user.value.first_name || ''
      formData.shipping_last_name = user.value.last_name || ''
      formData.shipping_email = user.value.email || ''
      formData.shipping_phone = user.value.phone_number || ''
    }
  
    // Fetch cart
    await cartStore.fetchCart()
  
    // Redirect if cart is empty
    if (cartStore.isEmpty) {
      router.push('/cart')
    }
  })
  </script>