<template>
  <section class="cta-section">
    <div class="max-width-container">
      <h2 class="cta-title">Start learning smarter today</h2>
      <!-- Usando o router-link para redirecionar -->
      <router-link to="/cadastro">
        <button class="cta-button">Sign up free</button>
      </router-link>
    </div>
  </section>
</template>

<script>
export default {
  name: 'CallToActionSection',
}
</script>

<style scoped>
.cta-section {
  padding: 80px 32px;
  text-align: center;
}

.cta-title {
  font-size: 36px;
  font-weight: bold;
  color: #1e1e1e;
  margin-bottom: 24px;
}

.cta-button {
  background-color: #ad46ff;
  color: white;
  padding: 16px 32px;
  border-radius: 8px;
  font-size: 18px;
  font-weight: medium;
}
</style>
