<template>
    <NavBar/>
    <v-main class="mx-5">
      <router-view/>
    </v-main>
  </template>
  
  <script>
  import NavBar from '@/components/NavBar.vue';
  
  export default {
    name: 'AuthView',
    components: {
      NavBar,
    }
  }
  </script>