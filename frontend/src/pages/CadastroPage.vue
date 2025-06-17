<template>
  <div class="cadastro-container">
    <h2>Cadastro</h2>
    <form @submit.prevent="cadastrar">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="senha" type="password" placeholder="Senha" required />
      <button type="submit">Cadastrar</button>
    </form>

    <!-- Mensagem de feedback -->
    <p v-if="mensagem" :class="sucesso ? 'sucesso' : 'erro'">
      {{ mensagem }}
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const senha = ref('')
const mensagem = ref('')
const sucesso = ref(false)
const router = useRouter()

const cadastrar = async () => {
  mensagem.value = ''
  sucesso.value = false

  try {
    const response = await fetch('http://127.0.0.1:8001/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email.value,
        senha: senha.value,
      }),
    })

    if (!response.ok) {
      const erro = await response.json()
      throw new Error(erro.detail || 'Erro no cadastro')
    }

    const resultado = await response.json()
    mensagem.value = resultado.msg || 'Cadastro realizado com sucesso!'
    sucesso.value = true

    // Redirecionar após 5 segundos
    setTimeout(() => {
      router.push('/login')
    }, 5000)
  } catch (err) {
    mensagem.value = err.message
    sucesso.value = false
    console.error('Erro ao cadastrar:', err)
  }
}
</script>

<style scoped>
.cadastro-container {
  max-width: 400px;
  margin: auto;
  padding: 2rem;
}

input {
  display: block;
  width: 100%;
  padding: 0.5rem;
  margin: 0.5rem 0;
}

button {
  padding: 0.5rem 1rem;
}

/* Estilo das mensagens */
p.sucesso {
  color: green;
  margin-top: 1rem;
}

p.erro {
  color: red;
  margin-top: 1rem;
}
</style>
