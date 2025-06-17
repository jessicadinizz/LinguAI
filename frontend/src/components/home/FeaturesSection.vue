<template>
  <section class="features-section">
    <div class="max-width-container">
      <h2 class="features-title">See the Magic in Action</h2>
      <div class="grid-container">
        <!-- Flashcards Card -->
        <div v-if="activities.length > 0 && flashcards.length > 0" class="card">
          <h3 class="card-title">Recent Generated Flashcards</h3>
          <div class="card-content">
            <!-- Exibe no máximo 3 flashcards mais recentes -->
            <div
              v-for="(flashcard, index) in flashcards.slice(0, 3)"
              :key="index"
              class="flashcard"
            >
              <div class="flashcard-text">
                <p class="flashcard-word">{{ flashcard.front }}</p>
                <p class="flashcard-translation">{{ flashcard.back }}</p>
              </div>
              <span class="icon">🔊</span>
            </div>
          </div>
        </div>

        <!-- Quiz Card -->
        <div v-if="activities.length > 0 && quiz.length > 0" class="card">
          <h3 class="card-title">Recent Interactive Quiz</h3>
          <div class="card-content">
            <!-- Exibe o quiz mais recente -->
            <p class="quiz-question">{{ quiz[0].pergunta }}</p>
            <div class="quiz-options">
              <button v-for="(option, index) in quiz[0].opcoes" :key="index" class="quiz-option">
                {{ option }}
              </button>
            </div>
          </div>
        </div>

        <!-- No Activities -->
        <div v-else class="card">
          <h3 class="card-title">No Recent Activities</h3>
          <div class="card-content">
            <p>No activities found. Start learning by pasting content or uploading a file!</p>
            <router-link to="/activities" class="btn-redirect">Go to Activities</router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  name: 'FeaturesSection',
  setup() {
    const activities = ref([])
    const flashcards = ref([])
    const quiz = ref([])
    const isLoggedIn = ref(false)
    const router = useRouter()

    // Verificar se o usuário está logado
    const checkLogin = () => {
      const token = localStorage.getItem('token')
      if (token) {
        isLoggedIn.value = true
        fetchActivities(token)
      } else {
        isLoggedIn.value = false
      }
    }

    // Obter as atividades do usuário logado
    const fetchActivities = async (token) => {
      try {
        const response = await axios.get('http://localhost:8001/atividades', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        activities.value = response.data

        // Parsear flashcards e quiz
        if (activities.value.length > 0) {
          flashcards.value = JSON.parse(activities.value[0].flashcards)
          quiz.value = JSON.parse(activities.value[0].quiz)
        }
      } catch (error) {
        console.error('Erro ao obter atividades:', error)
      }
    }

    // Verificar login assim que o componente for montado
    onMounted(() => {
      checkLogin()
    })

    return {
      activities,
      flashcards,
      quiz,
      isLoggedIn,
      router,
    }
  },
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

.btn-redirect {
  color: #ad46ff;
  font-weight: bold;
  text-decoration: none;
}
</style>
