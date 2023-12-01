import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Index',
    component: () => import('@/views/AuthView.vue'),
    children: [
      {
        path: 'dashboard/',
        name: 'Dashboard',
        component: () => import('@/views/DashboardView.vue'),
      },
      {
        path: 'projects/',
        name: 'Projects',
        component: () => import('@/views/ProjectsView.vue'),
      },
      {
        path: 'team/',
        name: 'Team',
        component: () => import('@/views/TeamView.vue'),
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/LoginView.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/RegisterView.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
