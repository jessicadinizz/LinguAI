<template>
  <header class="header">
    <nav class="nav">
      <!-- Logo à esquerda -->
      <div class="logo">
        <img
          alt="LinguaAI Logo"
          class="logo__img"
          src="https://lh3.googleusercontent.com/aida-public/AB6AXuCPB_nygOi2UTowiIaEVvZiNQnPHEHLZnQuvONhqh9gQ6Xw-N99Z7oVIiEagU8QDAknSCzgOwKaph_DYUYoREhlv3puT8S4WSUdjO0gUqvrrZAHRAS9O_S-cMUBh8Bf3MnTdVpmevyRv6uevj07A8CyO9i3TXu63fOgURem4XXF6RJE4NARFdjS0BhFYJODEBUSgiFDzoO8xZ5vzUjC2OzhihWu4_B4IXa3gWSxoSrXNR2fxLSgbnDgVb4L7syR-O1LEsggGMvGBW0"
        />
        <span class="logo__text">LinguaAI</span>
      </div>

      <!-- Navegação à direita -->
      <div class="nav__actions">
        <template v-if="usuario">
          <span class="nav__greeting">Olá, {{ usuario.nome || 'Usuário' }}</span>
          <router-link to="/atividades" class="nav__link">Ver atividades</router-link>
          <button @click="logout" class="nav__logout">Sair</button>
        </template>
        <template v-else>
          <router-link to="/login" class="nav__link">Log in</router-link>
          <router-link to="/cadastro" class="nav__signup">Sign up</router-link>
        </template>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const usuario = ref(null)
const router = useRouter()

async function buscarUsuarioLogado() {
  const token = localStorage.getItem('token')
  if (!token) return

  try {
    const res = await fetch('http://localhost:8001/teste-token?token=' + token)
    const data = await res.json()
    usuario.value = { nome: 'ID ' + data.user_id }
  } catch (e) {
    console.warn('Token inválido')
    localStorage.removeItem('token')
  }
}

function logout() {
  localStorage.removeItem('token')
  usuario.value = null
  router.push('/login')
}

onMounted(buscarUsuarioLogado)
</script>

<style scoped>
.header {
  background-color: #f9fafe;
  padding: 24px 32px;
  width: 100%;
  font-family: 'Urbanist', sans-serif;
}

.nav {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
}

.logo__img {
  height: 40px;
  width: 40px;
  border-radius: 50%;
  margin-right: 12px;
}

.logo__text {
  font-size: 24px;
  font-weight: bold;
  color: #1e1e1e;
}

.nav__actions {
  display: flex;
  align-items: center;
  gap: 24px;
}

.nav__link {
  color: #1e1e1e;
  text-decoration: none;
  font-weight: 500;
  font-size: 16px;
}

.nav__link:hover {
  color: #ad46ff;
}

.nav__signup {
  background-color: #ad46ff;
  color: #ffffff;
  text-decoration: none;
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: 500;
  font-size: 16px;
  border: none;
  display: inline-block;
}

.nav__signup:hover {
  opacity: 0.9;
}

.nav__logout {
  background: none;
  border: none;
  color: #ad46ff;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
}

.nav__logout:hover {
  text-decoration: underline;
}

.nav__greeting {
  font-size: 16px;
  color: #1e1e1e;
}
</style>
