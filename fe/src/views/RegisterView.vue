<template>
    <div class="login">
        <v-container class="d-flex align-center justify-center py-15 my-15">
            <v-card width="500" class="pa-5">
                <v-card-title class="text-center">
                    <h3>Register TODO Apps</h3>
                </v-card-title>
                <v-form @submit.prevent="handleRegister">
                    <v-card-text>
                        <div class="d-flex justify-center align-center">
                            <v-text-field v-model="formData.first_name" label="First Name" color="indigo" class="text-indigo mr-2"></v-text-field>
                            <v-text-field v-model="formData.last_name" label="Last Name" color="indigo" class="text-indigo ml-2"></v-text-field>
                        </div>
                        <v-text-field v-model="formData.email" label="Email" color="indigo" class="text-indigo"></v-text-field>
                        <v-text-field v-model="formData.password" label="Password" color="indigo" class="text-indigo"></v-text-field>
                    </v-card-text>
                    <v-card-actions class="d-flex align-center justify-center">
                        <v-btn type="submit" class="bg-indigo" width="500">Register</v-btn>
                    </v-card-actions>
                </v-form>
            </v-card>
        </v-container>
        <v-dialog v-model="successDialog" content-class="centered-content">
            <v-card color="grey-lighten-3" width="300">
                <v-card-title class="text-success">Success</v-card-title>
                <v-card-text class="text-center">Person registered successfully</v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="text-warning" @click="closeDialog">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "LoginView",
        data(){
            return {
                formData: {
                    first_name: '',
                    last_name: '',
                    email: '',
                    password: '' 
                },
                successDialog: true,
            }
        },
        methods: {
            async handleRegister(){
                await axios.post('http://127.0.0.1:8000/api/register/', this.formData)
                        .then(response => {
                            console.log(response.status)
                            this.successDialog = true
                        })
                        .catch(error => console.error(error))
                },
                closeDialog(){
                    this.successDialog = false
                    this.$router.push('login')
                }
        }
    }
</script>

<style>
    .v-overlay__content {
        align-items: center;
        justify-content: center;
    }
</style>