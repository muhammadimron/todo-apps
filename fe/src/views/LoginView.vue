<template>
    <div class="login">
        <v-container class="d-flex align-center justify-center py-15 my-15">
            <v-card width="750" class="pa-5">
                <v-card-title class="text-center">
                    <h3>Login TODO Apps</h3>
                </v-card-title>
                <v-form @submit.prevent="handleSubmit" ref="loginForm">
                    <v-card-text>
                        <v-text-field v-model="formData.email" type="email" label="Email" color="indigo" class="text-indigo" :rules="[rules.required, rules.minLength, rules.emailFormat]"></v-text-field>
                        <v-text-field v-model="formData.password" type="password" label="Password" color="indigo" class="text-indigo" :rules="[rules.required, rules.minLength, rules.complexPassword]"></v-text-field>
                    </v-card-text>
                    <v-card-actions class="d-flex align-center justify-center">
                        <v-btn type="submit" class="bg-indigo" width="500">Submit</v-btn>
                    </v-card-actions>
                </v-form>
                <v-card-text class="text-center">
                    <v-btn flat color="indigo" variant="text" size="x-small" @click="toRegister">Not yet registered?</v-btn>
                </v-card-text>
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
                rules: {
                    required: (value) => !!value || 'This field is required.',
                    minLength: (value) => (value && value.length >= 4) || 'Min 4 characters.',
                    emailFormat: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) || 'Invalid email address',
                    complexPassword: (value) => /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])/.test(value) || 'Password must include a number, lowercase, uppercase, and a symbol'
                }
            }
        },
        methods: {
            async handleSubmit(){
                const { valid } = await this.$refs.loginForm.validate()
                if (valid) {
                    await axios.post(`http://127.0.0.1:8000/login/`, this.formData)
                    .then(response => {
                        localStorage.setItem("refresh", response.data.refresh)
                        localStorage.setItem("token", response.data.access)
                        this.$router.push('/dashboard/')
                    })
                    .catch(error => {
                        console.error(error)
                    })
                }
            },
            toRegister(){
                this.$router.push('/register')
            }
        }
    }
</script>