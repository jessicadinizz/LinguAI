<template>
  <div v-if="questions.length && current < questions.length" class="quiz-question">
    <p>
      <strong>{{ questions[current].pergunta }}</strong>
    </p>
    <ul>
      <li
        v-for="(opt, i) in questions[current].opcoes"
        :key="i"
        :class="{
          selected: selected === i,
          correct: showAnswer && opt === questions[current].resposta,
          wrong: showAnswer && selected === i && opt !== questions[current].resposta,
        }"
        @click="!showAnswer && (selected = i)"
      >
        {{ opt }}
      </li>
    </ul>
    <button v-if="!showAnswer" @click="verificarResposta" :disabled="selected === null">
      Responder
    </button>
    <button v-else @click="proximaPergunta">Próxima</button>

    <p v-if="showAnswer" class="feedback">
      <span v-if="questions[current].opcoes[selected] === questions[current].resposta"
        >✅ Correto!</span
      >
      <span v-else
        >❌ Errado. A resposta correta é: <strong>{{ questions[current].resposta }}</strong></span
      >
    </p>
  </div>

  <div v-else>
    <h3>Quiz finalizado! 🏁</h3>
    <p>Acertos: {{ acertos }} de {{ questions.length }}</p>
  </div>
</template>

<script>
export default {
  name: 'QuizItem',
  props: {
    questions: Array,
  },
  data() {
    return {
      current: 0,
      selected: null,
      showAnswer: false,
      acertos: 0,
    }
  },
  methods: {
    verificarResposta() {
      this.showAnswer = true
      const certa = this.questions[this.current].resposta // Fixed: 'resposta' from 'answer'
      const marcada = this.questions[this.current].opcoes[this.selected] // Fixed: 'opcoes' from 'options'
      if (marcada === certa) {
        this.acertos++
      }
    },
    proximaPergunta() {
      this.current++
      this.selected = null
      this.showAnswer = false
    },
  },
}
</script>

<style scoped>
.quiz-question {
  padding: 1rem;
  border-radius: 10px;
  margin-bottom: 2rem;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  background: #f9fafe;
  padding: 0.5rem;
  margin: 0.5rem 0;
  cursor: pointer;
  border-radius: 6px;
}
li:hover {
  background: #959595;
}
.selected {
  border: 2px solid #4fc3f7;
}
.correct {
  background-color: #2e7d32 !important;
}
.wrong {
  background-color: #c62828 !important;
}
.feedback {
  margin-top: 1rem;
}
</style>
