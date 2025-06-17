<template>
  <div class="container">
    <!-- Geometric Background -->
    <div class="geometric-bg">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
    </div>

    <div class="content">
      <!-- Content Sections (Navbar, Main Section, etc.) -->
      <MainHeader />
      <MainSection />
      <InputPreviewSection />
      <FeaturesSection />
      <HowItWorksSection />
      <CallToActionSection />
      <Footer />
    </div>
  </div>
</template>

<script>
import MainHeader from '@/components/cabecalho/MainHeader.vue'
import MainSection from '@/components/home/MainSection.vue'
import InputPreviewSection from '@/components/home/InputPreviewSection.vue'
import FeaturesSection from '@/components/home/FeaturesSection.vue'
import HowItWorksSection from '@/components/home/HowItWorksSection.vue'
import CallToActionSection from '@/components/home/CallToActionSection.vue'
import Footer from '@/components/geral/Footer.vue'

export default {
  name: 'HomePage',
  components: {
    MainHeader,
    MainSection,
    InputPreviewSection,
    FeaturesSection,
    HowItWorksSection,
    CallToActionSection,
    Footer,
  },
}
</script>

<style scoped>
/* Geometric Background Styles */
.geometric-bg {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 50%;
  overflow: hidden;
  z-index: -1;
}

.shape {
  position: absolute;
  background-color: #ad46ff;
  opacity: 0.8;
  border-radius: 30px;
}

.shape-1 {
  width: 300px;
  height: 300px;
  top: -50px;
  right: -100px;
  transform: rotate(30deg);
}

.shape-2 {
  width: 400px;
  height: 400px;
  bottom: -150px;
  right: 50px;
  transform: rotate(-20deg);
  opacity: 0.6;
}

.shape-3 {
  width: 250px;
  height: 250px;
  bottom: 100px;
  right: -120px;
  transform: rotate(15deg);
  opacity: 0.4;
}

/* General Body and Background */
body {
  font-family: 'Urbanist', sans-serif;
  background-color: #f9fafe;
  color: #1e1e1e;
  overflow-x: hidden;
}
</style>
