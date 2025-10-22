<template>
  <div class="min-h-screen transition-colors duration-1000" :style="{ backgroundColor: backgroundColor }">
    <!-- Navigation -->
    <nav class="fixed top-0 w-full z-50 transition-all duration-700" :class="scrolled ? 'bg-black/90 border-white/10' : 'bg-white/90 border-gray-200'" :style="{ borderBottomWidth: '1px', borderBottomStyle: 'solid' }">
      <div class="max-w-7xl mx-auto px-6 py-5">
        <div class="flex items-center justify-between">
          <!-- Logo -->
          <div class="text-xl font-light tracking-[0.3em] transition-colors duration-700" :class="scrolled ? 'text-white' : 'text-black'">
            <router-link to="/" class="hover:opacity-60 transition-opacity duration-500">
              MVS
            </router-link>
          </div>

          <div class="hidden md:flex items-center space-x-12 text-xs font-light tracking-[0.25em] transition-colors duration-700" :class="scrolled ? 'text-white' : 'text-black'">
            <a href="#" class="nav-link opacity-70 hover:opacity-100 transition-all duration-500">COLLECTION</a>
            <a href="#" class="nav-link opacity-70 hover:opacity-100 transition-all duration-500">MEN</a>
            <a href="#" class="nav-link opacity-70 hover:opacity-100 transition-all duration-500">WOMEN</a>
          </div>

          <!-- Right Navigation -->
          <div class="hidden md:flex items-center space-x-8 text-xs tracking-[0.2em] transition-colors duration-700" :class="scrolled ? 'text-white' : 'text-black'">
            <router-link v-if="!isAuthenticated" to="/login" class="nav-link opacity-70 hover:opacity-100 transition-all duration-500">
              LOG IN
            </router-link>
            <router-link v-if="isAuthenticated" to="/profile" class="nav-link opacity-70 hover:opacity-100 transition-all duration-500">
              PROFILE
            </router-link>
          </div>

          <!-- Mobile Menu Button -->
          <button @click="mobileMenu = !mobileMenu" class="md:hidden transition-colors duration-700" :class="scrolled ? 'text-white' : 'text-black'">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-show="mobileMenu" class="md:hidden border-t transition-all duration-700" :class="scrolled ? 'bg-black/95 border-white/10 text-white' : 'bg-white border-gray-200 text-black'">
        <div class="px-6 py-6 space-y-6 text-xs tracking-[0.2em]">
          <a href="#" class="block opacity-70 hover:opacity-100 transition-opacity">COLLECTION</a>
          <a href="#" class="block opacity-70 hover:opacity-100 transition-opacity">MEN</a>
          <a href="#" class="block opacity-70 hover:opacity-100 transition-opacity">WOMEN</a>
          <div class="pt-6 border-t transition-colors duration-700" :class="scrolled ? 'border-white/10' : 'border-gray-200'">
            <router-link v-if="!isAuthenticated" to="/login" class="block opacity-70 hover:opacity-100 transition-opacity">
              LOG IN
            </router-link>
            <router-link v-if="isAuthenticated" to="/profile" class="block opacity-70 hover:opacity-100 transition-opacity">
              PROFILE
            </router-link>
          </div>
        </div>
      </div>
    </nav>

    <!-- Hero Section - Light -->
    <section class="min-h-screen flex items-center justify-center relative overflow-hidden pt-20">
      <!-- Subtle grid -->
      <div class="absolute inset-0 opacity-5" style="background-image: linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px); background-size: 100px 100px;"></div>

      <div class="text-center z-10 px-6">
        <div class="mb-16 overflow-hidden">
          <h1 class="hero-text text-7xl md:text-9xl font-thin tracking-[0.3em] mb-2 transition-colors duration-700" :style="{ color: heroTextColor }" style="font-family: Georgia, serif;">
            MVS
          </h1>
          <div class="h-px w-32 mx-auto my-8 transition-colors duration-700" :style="{ backgroundColor: heroDividerColor }"></div>
        </div>
        
        <p class="text-xs md:text-sm mb-3 tracking-[0.4em] font-light opacity-40 transition-colors duration-700" :style="{ color: heroSubTextColor }">
          NEW COLLECTION
        </p>
        <p class="text-5xl md:text-6xl font-thin mb-20 tracking-[0.2em] opacity-90 transition-colors duration-700" :style="{ color: heroTextColor }">
          2025
        </p>
        
        <router-link
          to="/products"
          class="group relative px-12 py-4 text-xs tracking-[0.3em] font-light border transition-all duration-700 overflow-hidden inline-block"
          :style="{ borderColor: heroBorderColor, backgroundColor: heroButtonBg, color: heroTextColor }"
        >
          <span class="relative z-10">DISCOVER</span>
          <div class="absolute inset-0 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-700 origin-left" :style="{ backgroundColor: heroButtonHoverBg }"></div>
        </router-link>
      </div>

      <!-- Floating elements -->
      <div class="absolute top-1/4 left-1/4 w-px h-32 animate-float transition-colors duration-700" :style="{ background: `linear-gradient(to bottom, transparent, ${heroFloatingLineColor}, transparent)` }"></div>
      <div class="absolute bottom-1/3 right-1/4 w-px h-24 animate-float-delay transition-colors duration-700" :style="{ background: `linear-gradient(to bottom, transparent, ${heroFloatingLineColor}, transparent)` }"></div>
    </section>

    <!-- Transition Section -->
    <section class="transition-section py-32 px-6 relative overflow-hidden">
      <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-24">
          <div class="h-px w-16 mx-auto transition-line mb-8"></div>
          <h2 class="transition-title text-2xl md:text-3xl font-thin tracking-[0.3em] mb-6 opacity-90">COLLECTION</h2>
          <p class="transition-text text-xs tracking-[0.25em] opacity-40 max-w-md mx-auto leading-loose">
            WHERE LIGHT FADES INTO SHADOW
          </p>
        </div>
      </div>
    </section>

    <!-- Collection Preview - Dark -->
    <section class="py-32 px-6 relative">
      <div class="max-w-7xl mx-auto relative z-10">
        <!-- Gender Split Section -->
        <div class="grid md:grid-cols-2 gap-16">
  <!-- Men's Section -->
  <router-link 
    to="/products?gender=men"
    class="group relative h-[500px] md:h-[600px] bg-zinc-900 overflow-hidden block"
  >
    <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent opacity-60"></div>
    <img 
      src="/src/static/men1.WEBP" 
      alt="Men's Collection"
      class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
    />
    <div class="absolute inset-0 border border-white/5 group-hover:border-white/20 transition-all duration-700"></div>
    
    <div class="absolute bottom-0 left-0 right-0 p-8 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-700">
      <div class="h-px w-12 bg-white/30 mb-6"></div>
      <h3 class="text-xl md:text-2xl font-thin tracking-[0.25em] mb-3 opacity-90 text-white">MEN</h3>
      <p class="text-xs tracking-[0.2em] opacity-50 mb-6 font-light text-gray-400">PRECISION IN SILENCE</p>
      <div class="text-xs tracking-[0.3em] opacity-0 group-hover:opacity-70 transition-all duration-700 font-light text-white">
        EXPLORE →
      </div>
    </div>
  </router-link>

  <!-- Women's Section -->
  <router-link 
    to="/products?gender=women"
    class="group relative h-[500px] md:h-[600px] bg-zinc-900 overflow-hidden block"
  >
    <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent opacity-60"></div>
    <div class="absolute inset-0 border border-white/5 group-hover:border-white/20 transition-all duration-700"></div>
    <img 
      src="/src/static/women2.JPG" 
      alt="Women's Collection"
      class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-700"
    />
    <div class="absolute bottom-0 left-0 right-0 p-8 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-700">
      <div class="h-px w-12 bg-white/30 mb-6"></div>
      <h3 class="text-xl md:text-2xl font-thin tracking-[0.25em] mb-3 opacity-90 text-white">WOMEN</h3>
      <p class="text-xs tracking-[0.2em] opacity-50 mb-6 font-light text-gray-400">ELEGANCE UNDEFINED</p>
      <div class="text-xs tracking-[0.3em] opacity-0 group-hover:opacity-70 transition-all duration-700 font-light text-white">
        EXPLORE →
      </div>
    </div>
  </router-link>
</div>
      </div>
    </section>

    <!-- Philosophy Section - Dark -->
    <section class="py-32 px-6 relative border-t transition-colors duration-700" :style="{ borderTopColor: philosophyLineColor }">
      <div class="max-w-5xl mx-auto">
        <div class="grid md:grid-cols-2 gap-16 items-center">
          <div>
            <div class="h-px w-12 mb-8 transition-colors duration-700" :style="{ backgroundColor: philosophyLineColor }"></div>
            <h3 class="text-2xl font-thin tracking-[0.25em] mb-6 opacity-90 transition-colors duration-700" :style="{ color: philosophyTitleColor }">PHILOSOPHY</h3>
            <p class="text-sm leading-loose opacity-80 tracking-wide font-light transition-colors duration-700" :style="{ color: philosophyTextColor }">
              In the space between light and dark, we find our essence. Each piece speaks in whispers, 
              demanding attention through absence rather than presence.
            </p>
          </div>
          <div class="space-y-12">
            <div class="border-l pl-6 transition-colors duration-700" :style="{ borderLeftColor: philosophyLineColor }">
              <h4 class="text-xs tracking-[0.3em] mb-3 opacity-90 font-light transition-colors duration-700" :style="{ color: philosophyLabelColor }">QUALITY</h4>
              <p class="text-xs leading-relaxed opacity-70 tracking-wide font-light transition-colors duration-700" :style="{ color: philosophyDescColor }">Materials that transcend time</p>
            </div>
            <div class="border-l pl-6 transition-colors duration-700" :style="{ borderLeftColor: philosophyLineColor }">
              <h4 class="text-xs tracking-[0.3em] mb-3 opacity-90 font-light transition-colors duration-700" :style="{ color: philosophyLabelColor }">CRAFT</h4>
              <p class="text-xs leading-relaxed opacity-70 tracking-wide font-light transition-colors duration-700" :style="{ color: philosophyDescColor }">Precision in every stitch</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer - Dark -->
    <footer class="py-16 px-6 border-t relative transition-colors duration-700" :style="{ borderTopColor: philosophyLineColor }">
      <div class="max-w-7xl mx-auto">
        <div class="grid md:grid-cols-4 gap-12 mb-16">
          <div>
            <h4 class="text-sm font-light tracking-[0.25em] mb-6 opacity-90 transition-colors duration-700" :style="{ color: footerTitleColor }">MVS</h4>
            <p class="text-xs leading-relaxed opacity-70 tracking-wide font-light transition-colors duration-700" :style="{ color: footerTextColor }">
              Form follows darkness
            </p>
          </div>

          <div>
            <h5 class="text-xs tracking-[0.2em] mb-6 opacity-90 font-light transition-colors duration-700" :style="{ color: footerTitleColor }">EXPLORE</h5>
            <ul class="space-y-3 text-xs opacity-70 tracking-wider font-light transition-colors duration-700" :style="{ color: footerTextColor }">
              <li><a href="#" class="hover:opacity-100 transition-opacity">Men's</a></li>
              <li><a href="#" class="hover:opacity-100 transition-opacity">Women's</a></li>
              <li><a href="#" class="hover:opacity-100 transition-opacity">Archive</a></li>
            </ul>
          </div>

          <div>
            <h5 class="text-xs tracking-[0.2em] mb-6 opacity-90 font-light transition-colors duration-700" :style="{ color: footerTitleColor }">SERVICES</h5>
            <ul class="space-y-3 text-xs opacity-70 tracking-wider font-light transition-colors duration-700" :style="{ color: footerTextColor }">
              <li><a href="#" class="hover:opacity-100 transition-opacity">Consultation</a></li>
              <li><a href="#" class="hover:opacity-100 transition-opacity">Delivery</a></li>
            </ul>
          </div>

          <div>
            <h5 class="text-xs tracking-[0.2em] mb-6 opacity-90 font-light transition-colors duration-700" :style="{ color: footerTitleColor }">CONTACT</h5>
            <ul class="space-y-3 text-xs opacity-70 tracking-wider font-light transition-colors duration-700" :style="{ color: footerTextColor }">
              <li>info@mvs.fashion</li>
              <li>New York</li>
            </ul>
          </div>
        </div>

        <div class="h-px mb-8 transition-colors duration-700" :style="{ backgroundColor: philosophyLineColor }"></div>

        <div class="flex flex-col md:flex-row justify-between items-center text-xs opacity-60 tracking-wider font-light transition-colors duration-700" :style="{ color: footerCopyrightColor }">
          <p>© 2025 MVS</p>
          <div class="flex space-x-8 mt-4 md:mt-0">
            <a href="#" class="hover:opacity-100 transition-opacity">Privacy</a>
            <a href="#" class="hover:opacity-100 transition-opacity">Terms</a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const mobileMenu = ref(false)
const scrolled = ref(false)
const transitionProgress = ref(0)
const backgroundColor = ref('rgb(255, 255, 255)')

const heroTextColor = ref('rgb(0, 0, 0)')
const heroSubTextColor = ref('rgb(107, 114, 128)')
const heroDividerColor = ref('rgba(0, 0, 0, 0.2)')
const heroBorderColor = ref('rgba(0, 0, 0, 0.2)')
const heroButtonBg = ref('rgb(255, 255, 255)')
const heroButtonHoverBg = ref('rgba(0, 0, 0, 0.05)')
const heroFloatingLineColor = ref('rgba(0, 0, 0, 0.1)')

// Dynamic colors for dark sections
const philosophyTitleColor = ref('rgb(120, 120, 120)')
const philosophyTextColor = ref('rgb(156, 156, 156)')
const philosophyLineColor = ref('rgba(255, 255, 255, 0.2)')
const philosophyLabelColor = ref('rgb(180, 180, 180)')
const philosophyDescColor = ref('rgb(200, 200, 200)')

const footerTitleColor = ref('rgb(120, 120, 120)')
const footerTextColor = ref('rgb(200, 200, 200)')
const footerCopyrightColor = ref('rgb(180, 180, 180)')

const isAuthenticated = computed(() => authStore.isAuthenticated)

const handleScroll = () => {
  const currentScroll = window.scrollY
  scrolled.value = currentScroll > 100

  const heroHeight = window.innerHeight
  const transitionStart = heroHeight * 0.3
  const transitionEnd = heroHeight * 1.3
  
  if (currentScroll < transitionStart) {
    transitionProgress.value = 0
  } else if (currentScroll > transitionEnd) {
    transitionProgress.value = 1
  } else {
    transitionProgress.value = (currentScroll - transitionStart) / (transitionEnd - transitionStart)
  }
  
  const bgValue = Math.round(255 * (1 - transitionProgress.value))
  backgroundColor.value = `rgb(${bgValue}, ${bgValue}, ${bgValue})`

  const progress = transitionProgress.value

  const textValue = Math.round(255 * progress)
  heroTextColor.value = `rgb(${textValue}, ${textValue}, ${textValue})`

  const subTextValue = Math.round(107 + (148 * progress))
  heroSubTextColor.value = `rgb(${subTextValue}, ${Math.round(114 + (46 * progress))}, ${Math.round(128 + (32 * progress))})`

  heroDividerColor.value = `rgba(${textValue}, ${textValue}, ${textValue}, 0.2)`

  heroBorderColor.value = `rgba(${textValue}, ${textValue}, ${textValue}, 0.2)`

  heroButtonBg.value = `rgb(${bgValue}, ${bgValue}, ${bgValue})`
  
  heroButtonHoverBg.value = `rgba(${textValue}, ${textValue}, ${textValue}, 0.05)`
  
  heroFloatingLineColor.value = `rgba(${textValue}, ${textValue}, ${textValue}, 0.1)`
  
  // Update philosophy and footer colors based on progress
  const philoTitleValue = Math.round(120 + (135 * progress))
  philosophyTitleColor.value = `rgb(${philoTitleValue}, ${philoTitleValue}, ${philoTitleValue})`
  
  const philoTextValue = Math.round(156 + (99 * progress))
  philosophyTextColor.value = `rgb(${philoTextValue}, ${philoTextValue}, ${philoTextValue})`
  
  philosophyLineColor.value = `rgba(255, 255, 255, ${0.2 + (0.3 * progress)})`
  
  const philoLabelValue = Math.round(180 + (75 * progress))
  philosophyLabelColor.value = `rgb(${philoLabelValue}, ${philoLabelValue}, ${philoLabelValue})`
  
  const philoDescValue = Math.round(200 + (55 * progress))
  philosophyDescColor.value = `rgb(${philoDescValue}, ${philoDescValue}, ${philoDescValue})`
  
  const footerTitleValue = Math.round(120 + (135 * progress))
  footerTitleColor.value = `rgb(${footerTitleValue}, ${footerTitleValue}, ${footerTitleValue})`
  
  const footerTextValue = Math.round(200 + (55 * progress))
  footerTextColor.value = `rgb(${footerTextValue}, ${footerTextValue}, ${footerTextValue})`
  
  const footerCopyrightValue = Math.round(180 + (75 * progress))
  footerCopyrightColor.value = `rgb(${footerCopyrightValue}, ${footerCopyrightValue}, ${footerCopyrightValue})`
  
  const transitionTitle = document.querySelector('.transition-title')
  const transitionText = document.querySelector('.transition-text')
  const transitionLine = document.querySelector('.transition-line')
  
  const titleColor = `rgb(${120 + progress * 135}, ${120 + progress * 135}, ${120 + progress * 135})`
  const textColor = `rgb(${112 + progress * 88}, ${112 + progress * 88}, ${112 + progress * 88})`
  const lineColor = `rgb(${156 + progress * 99}, ${156 + progress * 99}, ${156 + progress * 99})`
  
  if (transitionTitle) transitionTitle.style.color = titleColor
  if (transitionText) transitionText.style.color = textColor
  if (transitionLine) transitionLine.style.backgroundColor = lineColor
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  handleScroll() // Initial call
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-float-delay {
  animation: float 6s ease-in-out infinite 3s;
}

.hero-text {
  animation: fadeIn 1.5s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.nav-link {
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 1px;
  background: currentColor;
  transition: width 0.5s ease;
}

.nav-link:hover::after {
  width: 100%;
}

.transition-section {
  position: relative;
}

.transition-title,
.transition-text,
.transition-line {
  transition: color 0.1s linear, background-color 0.1s linear;
}

.transition-title {
  color: rgb(120, 120, 120);
}

.transition-text {
  color: rgb(112, 112, 112);
}

.transition-line {
  background-color: rgb(156, 156, 156);
}
</style>