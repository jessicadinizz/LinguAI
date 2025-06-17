// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/pages/HomePage.vue'
import LoginPage from '@/pages/LoginPage.vue'
// Se tiver uma página de cadastro:
import CadastroPage from '@/pages/CadastroPage.vue'

const routes = [
  {
    path: '/atividades',
    name: 'Atividades',
    component: () => import('@/pages/AtividadesPage.vue'),
  },
  { path: '/home', name: 'Home', component: HomePage },
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/cadastro', name: 'Cadastro', component: CadastroPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
