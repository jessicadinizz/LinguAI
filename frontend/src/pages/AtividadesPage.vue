<template>
  <div class="container">
    <MainHeader />

    <div class="topo">
      <h1>📂 Minhas Atividades</h1>
      <button class="voltar" @click="$router.push('/home')">🏠 Voltar para Home</button>
    </div>

    <div v-if="carregando">🔄 Carregando atividades...</div>
    <div v-else-if="atividades.length === 0">⚠️ Nenhuma atividade encontrada.</div>

    <div class="cards">
      <div class="card" v-for="(a, i) in atividades" :key="i">
        <h3>{{ a.nome }}</h3>
        <p><strong>Prompt:</strong> {{ a.prompt }}</p>

        <details>
          <summary>📚 Flashcards</summary>
          <pre>{{ a.flashcards }}</pre>
        </details>

        <details>
          <summary>📝 Quiz</summary>
          <pre>{{ a.quiz }}</pre>
        </details>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import MainHeader from '@/components/cabecalho/MainHeader.vue'

const atividades = ref([])
const carregando = ref(true)

onMounted(async () => {
  const token = localStorage.getItem('token')
  try {
    const res = await fetch('http://localhost:8001/atividades', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    atividades.value = await res.json()
  } catch (e) {
    console.error('Erro ao carregar atividades:', e)
  } finally {
    carregando.value = false
  }
})
</script>

<style scoped>
.container {
  width: 100%;
}
.topo {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}
.voltar {
  padding: 0.4rem 0.8rem;
  background-color: #222;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
.cards {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.card {
  background-color: #f0f0f0;
  padding: 1rem;
  border-radius: 8px;
  color: #000;
}
pre {
  background-color: #eee;
  padding: 0.5rem;
  overflow-x: auto;
  border-radius: 4px;
}
details {
  margin-top: 0.5rem;
}
</style>
