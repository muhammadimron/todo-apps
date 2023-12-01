<template>
    <div class="login">
        <v-container class="d-flex align-center justify-center py-15 my-15">
            <v-card width="500" class="pa-5">
                <v-card-title class="text-center">
                    <h3>Login TODO Apps</h3>
                </v-card-title>
                <v-form @submit.prevent="handleSubmit">
                    <v-card-text>
                        <v-text-field v-model="formData.email" type="email" label="Email" color="indigo" class="text-indigo"></v-text-field>
                        <v-text-field v-model="formData.password" type="password" label="Password" color="indigo" class="text-indigo"></v-text-field>
                    </v-card-text>
                    <v-card-actions class="d-flex align-center justify-center">
                        <v-btn type="submit" class="bg-indigo" width="500">Submit</v-btn>
                    </v-card-actions>
                    <v-btn class="bg-indigo" width="500" @click="refreshButton">Refresh</v-btn>
                    <v-btn class="bg-indigo" width="500" @click="personButton">Verify</v-btn>
                </v-form>
            </v-card>
        </v-container>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "LoginView",
        data(){
            return {
                formData: {
                    email: '',
                    password: ''
                },
            }
        },
        methods: {
            async handleSubmit(){
                await axios.post(`http://127.0.0.1:8000/login/`, this.formData)
                .then(response => {
                    localStorage.setItem("refresh", response.data.refresh)
                    localStorage.setItem("token", response.data.access)
                })
                .catch(error => {
                    console.error(error)
                })
                
            },
            async personButton(){
                console.log(localStorage.getItem("token"))
                await axios.get(`http://localhost:8000/api/person/`, {
                    "Authorization": `Token ${localStorage.getItem("token")}`
                })
                .then(response => console.log(response))
                .catch(error => console.error(error))
            }
        }
    }
</script>