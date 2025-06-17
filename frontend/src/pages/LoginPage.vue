<!-- eslint-disable no-unused-vars -->
<template>
  <div class="login-container">
    <h2>Login</h2>
    <input v-model="email" placeholder="Email" type="email" />
    <input v-model="senha" placeholder="Senha" type="password" />
    <button @click="login">Entrar</button>

    <!-- Mensagem de erro ou sucesso -->
    <p v-if="mensagem" :class="sucesso ? 'sucesso' : 'erro'">{{ mensagem }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      email: '',
      senha: '',
      mensagem: '',
      sucesso: false,
    }
  },
  methods: {
    async login() {
      this.mensagem = ''
      this.sucesso = false

      try {
        const res = await axios.post('http://localhost:8001/login', {
          email: this.email,
          senha: this.senha,
        })

        localStorage.setItem('token', res.data.access_token)
        this.sucesso = true
        this.mensagem = 'Login realizado com sucesso! Redirecionando...'

        // Redireciona para /home após 5 segundos
        setTimeout(() => {
          this.$router.push('/home')
        }, 5000)
      } catch (e) {
        this.mensagem = 'Email ou senha inválidos.'
        this.sucesso = false
      }
    },
  },
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input {
  padding: 0.5rem;
  font-size: 1rem;
}

button {
  padding: 0.5rem;
  font-size: 1rem;
}

.erro {
  color: red;
}

.sucesso {
  color: green;
}
</style>
