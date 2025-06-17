<template>
  <div class="container">
    <MainHeader />

    <div class="topo">
      <h1>📂 Minhas Atividades</h1>
      <button class="voltar" @click="$router.push('/home')">🏠 Voltar para Home</button>
    </div>

    <!-- Estado de carregamento e de lista vazia -->
    <div v-if="carregando" class="loading">🔄 Carregando atividades...</div>
    <div v-else-if="atividades.length === 0" class="no-activities">
      ⚠️ Nenhuma atividade encontrada.
    </div>

    <!-- Lista das atividades -->
    <div class="cards">
      <div v-for="(a, i) in atividades" :key="i" class="card">
        <div class="header">
          <h3>{{ a.nome }}</h3>
        </div>

        <p class="prompt">{{ a.prompt }}</p>

        <!-- Sessão de Flashcards -->
        <details>
          <summary>📚 Flashcards</summary>
          <div v-if="parseFlashcards(a.flashcards).length > 0" class="flashcards">
            <Flashcard :flashcards="parseFlashcards(a.flashcards).slice(0, 3)" />
          </div>
          <div v-else style="margin-top: 10px; color: #7a479e">Nenhum flashcard cadastrado.</div>
        </details>

        <!-- Sessão de Quiz -->
        <details>
          <summary>📝 Quiz</summary>
          <div v-if="parseQuiz(a.quiz).length > 0" class="quiz">
            <QuizItem :questions="parseQuiz(a.quiz)" />
          </div>
          <div v-else style="margin-top: 10px; color: #7a479e">
            Nenhuma pergunta de quiz cadastrada.
          </div>
        </details>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import MainHeader from '@/components/cabecalho/MainHeader.vue'
import Flashcard from '@/components/FlashcardItem.vue'
import QuizItem from '@/components/QuizItem.vue'

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
    // Veja no console os dados recebidos para depuração
    console.log('Atividades recebidas:', atividades.value)
  } catch (e) {
    console.error('Erro ao carregar atividades:', e)
  } finally {
    carregando.value = false
  }
})

// Função para tratar as strings de flashcards do backend
const parseFlashcards = (flashcardsStrRaw) => {
  if (!flashcardsStrRaw || typeof flashcardsStrRaw !== 'string') return []

  let str = flashcardsStrRaw

  // Se a string começa e termina com aspas, tente dar JSON.parse
  if (str.trim().startsWith('"') && str.trim().endsWith('"')) {
    try {
      str = JSON.parse(str)
    } catch (e) {
      // Se não conseguir dar JSON.parse, segue com a string original mesmo
    }
  }

  // Troca todos os "\n" (sequência barra+n) por QUEBRA DE LINHA de verdade
  str = str.replace(/\\n/g, '\n')

  // Remove prefixo FLASHCARDS: se existir
  str = str.replace(/^FLASHCARDS:\s*/i, '')

  // Divide em blocos por "\n-", funcionando mesmo se tiver espaços
  const parts = str.split(/\n\s*-\s*/g)

  return parts
    .map((line) => line.trim())
    .filter((line) => !!line)
    .map((fcard) => {
      // Divide por | em até 3 partes (palavra | tradução | exemplo)
      let fields = fcard.split('|').map((f) => f.trim())
      return {
        front: fields[0] || '',
        back: fields[1] || '',
        example: fields[2] || '',
      }
    })
    .filter((card) => card.front && card.back)
}

// Função para tratar as strings de quiz do backend
const parseQuiz = (quizStrRaw) => {
  if (!quizStrRaw || typeof quizStrRaw !== 'string') return []

  let str = quizStrRaw

  // Se vier com aspas extras (tipo de JSON serializado), dar um JSON.parse() antes
  if (str.trim().startsWith('"') && str.trim().endsWith('"')) {
    try {
      str = JSON.parse(str)
    } catch (e) {
      // Se der erro, segue com string crua mesmo
    }
  }

  // Converte todos \\n para quebras de linha reais
  str = str.replace(/\\n/g, '\n')

  // Remove o cabeçalho "QUIZ:"
  str = str.replace(/^QUIZ:\s*/i, '')

  // Divide as perguntas pelo padrão de duplo \n seguido de número/pergunta
  // (cada bloco de pergunta é separado por linha vazia)
  const blocos = str.split(/\n\s*\n/).filter(Boolean)

  return blocos
    .map((bloco) => {
      // Quebra bloco em linhas
      const linhas = bloco
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l)

      // Primeira linha é a pergunta, sem o número
      const pergunta = linhas[0]?.replace(/^\d+\.\s*/, '') || ''

      // Seleciona opções: linhas que começam com "a)", "b)", etc
      const opcoes = linhas
        .filter((l) => /^[a-dA-D]\)\s/.test(l.replace(/^\s+/, '')))
        .map((l) => l.replace(/^[a-dA-D]\)\s*/, '').trim())

      // Procura linha da resposta correta
      const respostaLine = linhas.find((l) => /Resposta correta/i.test(l))
      let resposta = ''
      if (respostaLine) {
        const letraMatch = respostaLine.match(/letra\s*([a-dA-D])\)/i)
        if (letraMatch && letraMatch[1]) {
          const idx = 'abcd'.indexOf(letraMatch[1].toLowerCase())
          resposta = opcoes[idx] ?? ''
        }
      }

      return {
        pergunta: pergunta,
        opcoes: opcoes,
        resposta: resposta,
      }
    })
    .filter((item) => item.pergunta && item.opcoes.length > 0)
}
</script>

<style scoped>
.container {
  width: 100%;
  font-family: 'Lexend', 'Noto Sans', sans-serif;
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

.loading,
.no-activities {
  text-align: center;
  padding: 1rem;
  font-size: 1.2rem;
}

.cards {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.card {
  background-color: #fff;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card h3 {
  color: #160d1c;
  font-size: 1.25rem;
}

.card p {
  color: #7a479e;
}

details {
  margin-top: 1rem;
}

details summary {
  font-weight: 600;
  color: #160d1c;
  cursor: pointer;
}

.flashcards {
  margin-top: 1rem;
}

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

.quiz {
  margin-top: 1rem;
}
</style>
