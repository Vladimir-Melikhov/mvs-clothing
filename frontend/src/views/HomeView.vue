<template>
  <div class="min-h-screen bg-white">
    <!-- Navigation -->
    <nav class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-gray-200 shadow-sm">
      <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
          <!-- Logo -->
          <div class="text-2xl font-bold tracking-wider">
            <router-link to="/" class="hover:text-gray-600 transition-colors" style="font-family: 'Times New Roman', Georgia, serif;">
              VMC
            </router-link>
          </div>

          <!-- Desktop Navigation -->
          <div class="hidden md:flex items-center space-x-8 text-sm font-medium tracking-wide">
            <a href="#" class="nav-link hover:text-gray-600">COLLECTION</a>
            <a href="#" class="nav-link hover:text-gray-600">MEN</a>
            <a href="#" class="nav-link hover:text-gray-600">WOMEN</a>
            <a href="#" class="nav-link hover:text-gray-600">ATELIER</a>
            <a href="#" class="nav-link hover:text-gray-600">SEARCH</a>
          </div>

          <!-- Right Navigation -->
          <div class="hidden md:flex items-center space-x-6 text-sm">
            <router-link v-if="!isAuthenticated" to="/login" class="nav-link hover:text-gray-600">
              SIGN IN
            </router-link>
            <router-link v-if="isAuthenticated" to="/profile" class="nav-link hover:text-gray-600">
              PROFILE
            </router-link>
            <a href="#" class="nav-link hover:text-gray-600">CART (0)</a>
          </div>

          <!-- Mobile Menu Button -->
          <button @click="mobileMenu = !mobileMenu" class="md:hidden">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-show="mobileMenu" class="md:hidden bg-white border-t border-gray-200">
        <div class="px-6 py-4 space-y-4">
          <a href="#" class="block text-sm tracking-wide hover:text-gray-600">COLLECTION</a>
          <a href="#" class="block text-sm tracking-wide hover:text-gray-600">MEN</a>
          <a href="#" class="block text-sm tracking-wide hover:text-gray-600">WOMEN</a>
          <a href="#" class="block text-sm tracking-wide hover:text-gray-600">ATELIER</a>
          <a href="#" class="block text-sm tracking-wide hover:text-gray-600">SEARCH</a>
          <div class="pt-4 border-t border-gray-200">
            <router-link v-if="!isAuthenticated" to="/login" class="block text-sm tracking-wide hover:text-gray-600">
              SIGN IN
            </router-link>
            <router-link v-if="isAuthenticated" to="/profile" class="block text-sm tracking-wide hover:text-gray-600">
              PROFILE
            </router-link>
            <a href="#" class="block text-sm tracking-wide hover:text-gray-600">CART (0)</a>
          </div>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="min-h-screen flex items-center justify-center geometric-bg relative overflow-hidden pt-20">
      <div class="text-center z-10">
        <h1 class="hero-text text-8xl md:text-9xl font-light mb-8 tracking-wider text-black" style="font-family: 'Times New Roman', Georgia, serif;">
          VMC
        </h1>
        <p class="text-lg md:text-xl mb-4 tracking-widest font-light opacity-70 text-gray-700">
          FALL-WINTER COLLECTION
        </p>
        <p class="text-4xl md:text-5xl font-light mb-12 tracking-wider text-black">
          2025
        </p>
        <button class="cta-button px-8 py-3 text-sm tracking-widest font-medium hover:scale-105 transform transition-all bg-white text-black">
          ENTER VMC WORLD
        </button>
      </div>

      <!-- Geometric Elements -->
      <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div class="absolute top-1/4 left-1/4 w-32 h-32 border border-gray-300 rotate-45 animate-pulse"></div>
        <div class="absolute bottom-1/4 right-1/4 w-24 h-24 border border-gray-200 rotate-12"></div>
        <div class="absolute top-1/2 right-1/3 w-16 h-16 border border-gray-300 -rotate-45"></div>
      </div>
    </section>

    <!-- Collection Preview -->
    <section class="py-20 px-6 bg-gray-50">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-light tracking-wider mb-4 text-black">NEW COLLECTION</h2>
          <div class="section-divider w-24 mx-auto mb-8"></div>
          <p class="text-gray-600 max-w-2xl mx-auto leading-relaxed">
            Discover the unique blend of minimalism and avant-garde in our new Fall-Winter 2025 collection
          </p>
        </div>

        <!-- Gender Split Section -->
        <div class="grid md:grid-cols-2 gap-8 min-h-screen">
          <!-- Men's Section -->
          <div class="model-card group relative bg-white rounded-lg overflow-hidden shadow-lg">
            <div class="absolute inset-0 image-overlay z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            <img
              src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&h=800&fit=crop&crop=face"
              alt="Men's Collection"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
            />

            <div class="relative z-20 p-8 h-full flex flex-col justify-end bg-gradient-to-t from-black/50 to-transparent">
              <h3 class="text-2xl md:text-3xl font-light tracking-wider mb-4 text-white">MEN'S</h3>
              <p class="text-gray-200 mb-8 max-w-xs">Clean lines and impeccable tailoring</p>
              <button class="cta-button px-6 py-2 text-sm tracking-widest text-white border-white hover:bg-white hover:text-black">
                VIEW COLLECTION
              </button>
            </div>
          </div>

          <!-- Women's Section -->
          <div class="model-card group relative bg-white rounded-lg overflow-hidden shadow-lg">
            <div class="absolute inset-0 image-overlay z-10 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
            <img
              src="https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=600&h=800&fit=crop&crop=face"
              alt="Women's Collection"
              class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
            />

            <div class="relative z-20 p-8 h-full flex flex-col justify-end bg-gradient-to-t from-black/50 to-transparent">
              <h3 class="text-2xl md:text-3xl font-light tracking-wider mb-4 text-white">WOMEN'S</h3>
              <p class="text-gray-200 mb-8 max-w-xs">Elegance in every detail</p>
              <button class="cta-button px-6 py-2 text-sm tracking-widest text-white border-white hover:bg-white hover:text-black">
                VIEW COLLECTION
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-20 px-6 bg-white">
      <div class="max-w-7xl mx-auto">
        <div class="grid md:grid-cols-3 gap-12">
          <div class="text-center">
            <div class="w-16 h-16 border border-gray-300 mx-auto mb-6 flex items-center justify-center bg-gray-50">
              <svg class="w-8 h-8 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zM21 5a2 2 0 00-2-2h-4a2 2 0 00-2 2v12a4 4 0 004 4h4a4 4 0 004-4V5z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-light tracking-wide mb-4 text-black">ATELIER</h3>
            <p class="text-gray-600 text-sm leading-relaxed">Bespoke tailoring and custom fitting</p>
          </div>

          <div class="text-center">
            <div class="w-16 h-16 border border-gray-300 mx-auto mb-6 flex items-center justify-center bg-gray-50">
              <svg class="w-8 h-8 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"></path>
              </svg>
            </div>
            <h3 class="text-xl font-light tracking-wide mb-4 text-black">QUALITY</h3>
            <p class="text-gray-600 text-sm leading-relaxed">Premium materials and flawless execution</p>
          </div>

          <div class="text-center">
            <div class="w-16 h-16 border border-gray-300 mx-auto mb-6 flex items-center justify-center bg-gray-50">
              <svg class="w-8 h-8 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-light tracking-wide mb-4 text-black">INNOVATION</h3>
            <p class="text-gray-600 text-sm leading-relaxed">Modern technologies in classic design</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 px-6 border-t border-gray-200 bg-gray-50">
      <div class="max-w-7xl mx-auto">
        <div class="grid md:grid-cols-4 gap-8">
          <div>
            <h4 class="text-lg font-medium tracking-wide mb-4 text-black">VMC</h4>
            <p class="text-gray-600 text-sm leading-relaxed">
              Minimalist fashion for modern people
            </p>
          </div>

          <div>
            <h5 class="font-medium tracking-wide mb-4 text-black">COLLECTIONS</h5>
            <ul class="space-y-2 text-sm text-gray-600">
              <li><a href="#" class="hover:text-black transition-colors">Men's</a></li>
              <li><a href="#" class="hover:text-black transition-colors">Women's</a></li>
              <li><a href="#" class="hover:text-black transition-colors">Accessories</a></li>
            </ul>
          </div>

          <div>
            <h5 class="font-medium tracking-wide mb-4 text-black">SERVICES</h5>
            <ul class="space-y-2 text-sm text-gray-600">
              <li><a href="#" class="hover:text-black transition-colors">Atelier</a></li>
              <li><a href="#" class="hover:text-black transition-colors">Consultations</a></li>
              <li><a href="#" class="hover:text-black transition-colors">Delivery</a></li>
            </ul>
          </div>

          <div>
            <h5 class="font-medium tracking-wide mb-4 text-black">CONTACTS</h5>
            <ul class="space-y-2 text-sm text-gray-600">
              <li>info@vmc.fashion</li>
              <li>+1 (555) 123-4567</li>
              <li>New York, USA</li>
            </ul>
          </div>
        </div>

        <div class="section-divider mt-8 mb-6"></div>

        <div class="flex flex-col md:flex-row justify-between items-center text-sm text-gray-600">
          <p>&copy; 2025 VMC. All rights reserved.</p>
          <div class="flex space-x-6 mt-4 md:mt-0">
            <a href="#" class="hover:text-black transition-colors">Privacy Policy</a>
            <a href="#" class="hover:text-black transition-colors">Terms of Use</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const mobileMenu = ref(false)

const isAuthenticated = computed(() => authStore.isAuthenticated)
</script>

<style scoped>
.geometric-bg {
  background-image: linear-gradient(
      45deg,
      transparent 40%,
      rgba(0, 0, 0, 0.03) 40%,
      rgba(0, 0, 0, 0.03) 60%,
      transparent 60%
    ),
    linear-gradient(
      -45deg,
      transparent 40%,
      rgba(0, 0, 0, 0.02) 40%,
      rgba(0, 0, 0, 0.02) 60%,
      transparent 60%
    );
  background-size: 120px 120px, 80px 80px;
  animation: geometricMove 20s linear infinite;
  background-color: #ffffff;
}

@keyframes geometricMove {
  0% {
    background-position: 0 0, 0 0;
  }
  100% {
    background-position: 120px 120px, -80px 80px;
  }
}

.hero-text {
  font-family: 'Inter', sans-serif;
  letter-spacing: 0.1em;
}

.nav-link {
  position: relative;
  transition: all 0.3s ease;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 1px;
  background: #000;
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}

.section-divider {
  background: linear-gradient(90deg, transparent, rgba(0, 0, 0, 0.2), transparent);
  height: 1px;
}

.model-card {
  transition: all 0.5s ease;
  cursor: pointer;
}

.model-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.cta-button {
  border: 1px solid rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.cta-button:hover {
  background: rgba(0, 0, 0, 0.1);
  border-color: #000;
}

.image-overlay {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.3) 100%);
}
</style>
