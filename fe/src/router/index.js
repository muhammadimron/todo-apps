import axios from 'axios'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Index',
    component: () => import('@/views/AuthView.vue'),
    meta: {
      requiresAuth: true,
      authPage: false
    },
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
    component: () => import('@/views/LoginView.vue'),
    meta: {
      requiresAuth: false,
      authPage: true,
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/RegisterView.vue'),
    meta: {
      requiresAuth: false,
      authPage: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)){
    const token = localStorage.getItem("token")

    try {
      if (token) {
        await axios.post('http://127.0.0.1:8000/verify/', { token: token })

        next()
      } else {
        throw new Error("Token not found")
      }
    } catch (error) {
      const refresh = localStorage.getItem("refresh")

      try {
        const response = await axios.post('http://127.0.0.1:8000/refresh/', { refresh: refresh })
        localStorage.setItem("token", response.data.access)

        await axios.post('http://127.0.0.1:8000/verify/', { token: response.data.access })

        next()
      } catch (refreshError) {
        console.error(refreshError)
        next({ name: "Login" })
      }
    }
  }

  if (to.matched.some(record => record.meta.authPage)) {
    next(!to.matched.some(record => record.meta.requiresAuth) ? null : from)
  }
})

export default router
