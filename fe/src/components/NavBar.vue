<template>
    <nav>
        <v-toolbar flat>
            <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer" color="text-grey"></v-app-bar-nav-icon>
            <v-toolbar-title class="text-uppercase text-grey">
                <span class="font-weight-light">Todo</span>
                <span>Apps</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-menu>
                <template v-slot:activator="{ props }">
                    <v-btn flat color="bg-grey" v-bind="props" class="text-grey">
                        Menu
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                        <v-list-item-title>{{ link.text }}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
            <v-btn flat color="bg-grey" @click="logout">
                <span class="text-grey">Sign Out</span>
                <v-icon end class="text-grey" icon="mdi-exit-to-app"></v-icon>
            </v-btn>
        </v-toolbar>
        <v-navigation-drawer v-model="drawer" temporary color="indigo" disable-route-watcher location="left">
            <v-card flat color="indigo" class="my-5">
                <v-responsive class="pt-4">
                    <v-img :src="avatar" width="100" class="mx-auto rounded-circle"></v-img>
                </v-responsive>
                <v-card-title class="text-center">{{ name }}</v-card-title>
                <v-card-subtitle class="text-center">{{ role }}</v-card-subtitle>
            </v-card>
            <v-container class="my-2 text-center">
                <PopUp />
            </v-container>
            <v-list>
                <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                    <template v-slot:prepend>
                        <v-icon :icon="link.icon"></v-icon>
                    </template>
                    <v-list-item-title>{{ link.text }}</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script>
    import axios from 'axios';
    import PopUp from './PopUp.vue';
    export default {
        components: {
            PopUp
        },
        name: "NavBar",
        data(){
            return {
                name: '',
                role: '',
                avatar: '',
                drawer: false,
                links: [
                    {
                        icon: 'mdi-view-dashboard',
                        text: 'Dashboard',
                        route: '/dashboard/'
                    },
                    {
                        icon: 'mdi-folder',
                        text: 'My Projects',
                        route: '/projects/'
                    },
                    {
                        icon: 'mdi-account-group',
                        text: 'Team',
                        route: '/team/'
                    },
                ]
            }
        },
        methods: {
            logout(){
                localStorage.removeItem("refresh")
                localStorage.removeItem("token")
                this.$router.push("/login")
            }
        },
        async mounted(){
            const token = localStorage.getItem("token")
            const response = await axios.get('http://127.0.0.1:8000/api/person/', {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })

            if (response.status == 200){
                this.name = `${response.data.first_name} ${response.data.last_name}`
                this.role = response.data.role
                this.avatar = response.data.avatar
            }
        }
    }
</script>