<template>
  <div v-for="(flashcard, index) in flashcards" :key="index" class="flashcard">
    <p class="flashcard-word">{{ flashcard.front }}</p>
    <p class="flashcard-translation">{{ flashcard.back }}</p>
    <p v-if="flashcard.example" class="flashcard-example">{{ flashcard.example }}</p>
  </div>
</template>

<script setup>
defineProps({
  flashcards: {
    type: Array,
    required: true,
  },
})
</script>

<style scoped>
.flashcard {
  background-color: #f3f4f6;
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
}
.flashcard-word {
  font-weight: 500;
  color: #160d1c;
}
.flashcard-translation {
  font-size: 14px;
  color: #7a479e;
}
.flashcard-example {
  font-size: 12px;
  color: #555a;
  margin-top: 0.5rem;
  font-style: italic;
}
</style>
