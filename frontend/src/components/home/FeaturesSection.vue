<template>
  <section class="features-section">
    <div class="max-width-container">
      <h2 class="features-title">See the Magic in Action</h2>
      <div class="grid-container">
        <div class="card">
          <h3 class="card-title">Generated Flashcards</h3>
          <div class="card-content">
            <div class="flashcard">
              <div class="flashcard-text">
                <p class="flashcard-word">Hola</p>
                <p class="flashcard-translation">Hello</p>
              </div>
              <span class="icon">🔊</span>
            </div>
            <div class="flashcard">
              <div class="flashcard-text">
                <p class="flashcard-word">Mundo</p>
                <p class="flashcard-translation">World</p>
              </div>
              <span class="icon">🔊</span>
            </div>
          </div>
        </div>
        <div class="card">
          <h3 class="card-title">Interactive Quiz</h3>
          <div class="card-content">
            <p class="quiz-question">What is "adiós" in English?</p>
            <div class="quiz-options">
              <button class="quiz-option">A. Hello</button>
              <button class="quiz-option">B. Goodbye</button>
              <button class="quiz-option">C. Please</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'FeaturesSection',
}
</script>

<style scoped>
.features-section {
  padding: 80px 32px;
}

.features-title {
  font-size: 36px;
  font-weight: bold;
  color: #1e1e1e;
  text-align: center;
  margin-bottom: 48px;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
}

.card {
  background-color: white;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 24px;
  font-weight: bold;
  color: #1e1e1e;
  margin-bottom: 16px;
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.flashcard {
  background-color: #f3f4f6;
  padding: 16px;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.flashcard-text {
  display: flex;
  flex-direction: column;
}

.flashcard-word {
  font-weight: medium;
  color: #1e1e1e;
}

.flashcard-translation {
  font-size: 14px;
  color: #6b7280;
}

.quiz-question {
  font-size: 18px;
  font-weight: medium;
  color: #1e1e1e;
}

.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.quiz-option {
  padding: 16px;
  background-color: #f3f4f6;
  border-radius: 8px;
  text-align: left;
  transition: background-color 0.3s ease;
}

.quiz-option:hover {
  background-color: #e5e7eb;
}
</style>
