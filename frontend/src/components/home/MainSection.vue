<template>
  <section class="main-section">
    <div class="max-width-container">
      <h1 class="main-title">Turn any text into smart language lessons</h1>
      <p class="main-description">
        Paste a text and generate flashcards and quizzes instantly with AI.
      </p>
      <button class="cta-button">Get Started</button>
    </div>
  </section>
</template>

<script>
export default {
  name: 'MainSection',
}
</script>

<style scoped>
.main-section {
  padding: 80px 32px;
  text-align: center;
}

.main-title {
  font-size: 48px;
  font-weight: bold;
  color: #1e1e1e;
  margin-bottom: 24px;
}

.main-description {
  font-size: 18px;
  color: #1e1e1e;
  opacity: 0.7;
  margin-bottom: 40px;
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
