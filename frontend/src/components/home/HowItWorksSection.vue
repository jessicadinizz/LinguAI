<template>
  <section class="how-it-works-section">
    <div class="max-width-container">
      <h2 class="how-it-works-title">How It Works</h2>
      <div class="how-it-works-grid">
        <div class="how-it-works-item">
          <div class="icon-circle">
            <span class="icon">📄</span>
          </div>
          <h3 class="item-title">1. Paste Content</h3>
          <p class="item-description">
            Simply paste any text or upload a document you want to learn from.
          </p>
        </div>
        <div class="how-it-works-item">
          <div class="icon-circle">
            <span class="icon">✨</span>
          </div>
          <h3 class="item-title">2. AI Processes</h3>
          <p class="item-description">
            Our AI analyzes the text and extracts key vocabulary and concepts.
          </p>
        </div>
        <div class="how-it-works-item">
          <div class="icon-circle">
            <span class="icon">🎓</span>
          </div>
          <h3 class="item-title">3. Study Smart</h3>
          <p class="item-description">
            Engage with AI-generated flashcards and quizzes tailored to your content.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HowItWorksSection',
}
</script>

<style scoped>
.how-it-works-section {
  padding: 80px 32px;
  background-color: white;
}

.how-it-works-title {
  font-size: 36px;
  font-weight: bold;
  color: #1e1e1e;
  text-align: center;
  margin-bottom: 64px;
}

.how-it-works-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}

.how-it-works-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.icon-circle {
  background-color: #f3e8ff;
  padding: 24px;
  border-radius: 50%;
  margin-bottom: 20px;
}

.item-title {
  font-size: 24px;
  font-weight: bold;
  color: #1e1e1e;
  margin-bottom: 8px;
}

.item-description {
  font-size: 16px;
  color: #1e1e1e;
  opacity: 0.7;
}
</style>
