<template>
    <v-app class="bg-grey-lighten-3">
      <NavBar/>
      <v-main class="mx-5">
        <router-view/>
      </v-main>
    </v-app>
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