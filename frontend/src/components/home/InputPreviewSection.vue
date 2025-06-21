<template>
  <section class="input-preview-section">
    <div class="max-width-container">
      <div class="input-preview">
        <textarea
          class="textarea"
          placeholder="Paste your text here..."
          v-model="inputText"
          @focus="checkLogin"
        ></textarea>
        <div class="divider">or</div>
        <button class="upload-button" @click="handleSubmit">
          <span class="icon">📁</span>
          Upload a file
        </button>
      </div>
    </div>

    <!-- Flashcards Generating Card -->
    <div v-if="generatingFlashcards" class="progress-card">
      <p>Gerando flashcards...</p>
    </div>

    <!-- Quiz Generating Card -->
    <div v-if="generatingQuiz" class="progress-card">
      <p>Gerando quiz...</p>
    </div>

    <!-- Flashcards Success Card -->
    <div v-if="flashcardsGenerated" class="success-message-card">
      <p>Flashcards gerados com sucesso!</p>
    </div>

    <!-- Quiz Success Card -->
    <div v-if="quizGenerated" class="success-message-card">
      <p>Quiz gerado com sucesso!</p>
    </div>

    <!-- Button to view activity after both are generated -->
    <div v-if="flashcardsGenerated && quizGenerated" class="success-message-card">
      <button @click="redirectToActivities" class="success-button">Ver atividade</button>
    </div>

    <!-- Condicionalmente renderiza o componente Popup -->
    <LoginPopup v-if="showPopup" @close-popup="closePopup" />

    <!-- Debugging Output (console view) -->
    <div v-if="debugOutput.length > 0" class="debug-output">
      <h3>Debug Output:</h3>
      <pre>{{ debugOutput }}</pre>
    </div>
  </section>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import LoginPopup from '@/components/geral/LoginPopup.vue'
import { useRouter } from 'vue-router'

export default {
  name: 'InputPreviewSection',
  components: {
    LoginPopup,
  },
  setup() {
    const showPopup = ref(false)
    const inputText = ref('')
    const showSuccess = ref(false)
    const debugOutput = ref('') // For debugging output
    const generatingFlashcards = ref(false)
    const generatingQuiz = ref(false)
    const flashcardsGenerated = ref(false)
    const quizGenerated = ref(false)

    const router = useRouter() // Using useRouter to get the router instance

    // Verificar se o usuário está logado
    const checkLogin = () => {
      const token = localStorage.getItem('token')
      if (!token) {
        showPopup.value = true // Exibir popup se não estiver logado
      }
    }

    // Fechar popup
    const closePopup = () => {
      showPopup.value = false
    }

    // Enviar dados de atividades para o backend
    const handleSubmit = async () => {
      const token = localStorage.getItem('token')
      if (!token) {
        showPopup.value = true
        return
      }

      try {
        // Iniciar a geração dos flashcards
        generatingFlashcards.value = true
        const flashcardsResponse = await axios.post('http://127.0.0.1:8001/gerar-flashcards', {
          texto: inputText.value,
        })
        const flashcards = flashcardsResponse.data.conteudo // Dados retornados pela API
        flashcardsGenerated.value = true // Flashcards gerados com sucesso
        generatingFlashcards.value = false // Finalizou a geração de flashcards

        // Iniciar a geração do quiz
        generatingQuiz.value = true
        const quizResponse = await axios.post('http://127.0.0.1:8001/gerar-quiz', {
          texto: inputText.value,
        })
        const quiz = quizResponse.data.conteudo // Dados retornados pela API
        quizGenerated.value = true // Quiz gerado com sucesso
        generatingQuiz.value = false // Finalizou a geração do quiz

        // Enviar atividade para o backend
        const response = await axios.post(
          'http://127.0.0.1:8001/atividades', // Substitua pela URL do seu backend
          {
            nome: 'Nova Atividade', // Nome da atividade
            prompt: inputText.value,
            flashcards: JSON.stringify(flashcards), // Passando os flashcards gerados como string JSON
            quiz: JSON.stringify(quiz), // Passando o quiz gerado como string JSON
          },
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          },
        )

        // Exibir mensagem de sucesso
        console.log('Atividade criada:', response.data)
        showSuccess.value = true
        inputText.value = '' // Limpar o campo de entrada após o envio

        // Exibir a resposta para depuração
        debugOutput.value = JSON.stringify(response.data, null, 2)
      } catch (error) {
        console.error('Erro ao criar atividade:', error)
        debugOutput.value = `Erro: ${error.message}`
      }
    }

    // Redirecionar para a página de atividades
    const redirectToActivities = () => {
      router.push('/atividades') // Uso correto do router.push com useRouter()
    }

    return {
      showPopup,
      checkLogin,
      closePopup,
      inputText,
      handleSubmit,
      showSuccess,
      redirectToActivities,
      debugOutput, // Retornar debugOutput para o template
      generatingFlashcards,
      generatingQuiz,
      flashcardsGenerated,
      quizGenerated,
    }
  },
}
</script>

<style scoped>
.input-preview-section {
  padding: 40px 32px;
}

.input-preview {
  background-color: white;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  min-height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.textarea {
  width: 100%;
  height: 128px;
  padding: 16px;
  border: none;
  resize: none;
  color: #6b7280;
}

.divider {
  margin-top: 16px;
  color: #d1d5db;
}

.upload-button {
  margin-top: 16px;
  display: flex;
  align-items: center;
  color: #ad46ff;
  font-weight: medium;
}

.icon {
  margin-right: 8px;
}

/* Progress Cards */
.progress-card {
  background-color: #f3e8ff;
  padding: 16px;
  border-radius: 8px;
  margin-top: 20px;
  text-align: center;
}

.success-message-card {
  background-color: #f3e8ff;
  padding: 16px;
  border-radius: 8px;
  margin-top: 20px;
  text-align: center;
}

.success-button {
  background-color: #ad46ff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
}

.success-button:hover {
  background-color: #9b39d2;
}

/* Debug Output Styles */
.debug-output {
  margin-top: 20px;
  background-color: #f9fafb;
  padding: 16px;
  border-radius: 8px;
  width: 100%;
  max-width: 600px;
  text-align: left;
  font-family: 'Courier New', Courier, monospace;
}

.debug-output pre {
  background-color: #e5e7eb;
  padding: 16px;
  border-radius: 8px;
  overflow-x: auto;
}
</style>
