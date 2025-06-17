<template>
  <section class="input-preview-section">
    <div class="max-width-container">
      <div class="input-preview">
        <textarea
          class="textarea"
          placeholder="Paste your text here..."
          @focus="checkLogin"
        ></textarea>
        <div class="divider">or</div>
        <button class="upload-button" @click="checkLogin">
          <span class="icon">📁</span>
          Upload a file
        </button>
      </div>
    </div>

    <!-- Condicionalmente renderiza o componente Popup -->
    <LoginPopup v-if="showPopup" @close-popup="closePopup" />
  </section>
</template>

<script>
import { ref } from 'vue'
import LoginPopup from '@/components/geral/LoginPopup.vue'

export default {
  name: 'InputPreviewSection',
  components: {
    LoginPopup,
  },
  setup() {
    const showPopup = ref(false)

    // Verificar se o usuário está logado
    const checkLogin = () => {
      const token = localStorage.getItem('token')
      if (!token) {
        showPopup.value = true // Exibir popup se não estiver logado
      }
    }

    const closePopup = () => {
      showPopup.value = false // Fechar a popup
    }

    return {
      showPopup,
      checkLogin,
      closePopup,
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
</style>
