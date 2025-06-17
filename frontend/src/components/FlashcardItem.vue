<template>
  <div class="flashcard">
    <div class="flashcard-word">{{ card.word }}</div>
    <div class="flashcard-translation">{{ card.translation }}</div>
    <div class="flashcard-example">{{ card.example }}</div>
  </div>
</template>

<script>
export default {
  name: 'FlashcardItem',
  props: {
    card: Object,
  },
}
</script>

<style scoped>
.flashcard {
  background-color: #1f1f1f;
  padding: 1rem;
  border-radius: 10px;
  margin-bottom: 1rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
  transition: transform 0.2s;
}
.flashcard:hover {
  transform: scale(1.02);
}
.flashcard-word {
  font-size: 1.3rem;
  font-weight: bold;
  color: #4fc3f7;
}
.flashcard-translation {
  font-size: 1.1rem;
  color: #81c784;
}
.flashcard-example {
  font-size: 0.95rem;
  color: #ccc;
  margin-top: 0.5rem;
}
</style>
