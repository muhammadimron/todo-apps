<template>
    <div class="login">
        <v-container class="d-flex align-center justify-center py-15 my-15">
            <v-card width="750" class="pa-5">
                <v-card-title class="text-center">
                    <h3>Register TODO Apps</h3>
                </v-card-title>
                <v-form @submit.prevent="handleRegister" ref="registerForm">
                    <v-card-text>
                        <div class="d-flex justify-center align-center">
                            <v-text-field v-model="formData.first_name" label="First Name" color="indigo" class="text-indigo mr-2" :rules="[rules.required, rules.minLength]"></v-text-field>
                            <v-text-field v-model="formData.last_name" label="Last Name" color="indigo" class="text-indigo ml-2" :rules="[rules.required, rules.minLength]"></v-text-field>
                        </div>
                        <v-text-field v-model="formData.role" label="Role" color="indigo" class="text-indigo" :rules="[rules.required, rules.minLength]"></v-text-field>
                        <v-text-field v-model="formData.email" label="Email" color="indigo" class="text-indigo" :rules="[rules.required, rules.minLength, rules.emailFormat]"></v-text-field>
                        <v-text-field v-model="formData.password" label="Password" color="indigo" class="text-indigo" :rules="[rules.required, rules.minLength, rules.complexPassword]"></v-text-field>
                        <v-text-field v-model="formData.confirmPassword" label="Confirm Password" color="indigo" class="text-indigo" :rules="[rules.required, rules.minLength, rules.matchPassword]"></v-text-field>
                        <v-file-input v-model="formData.avatar" label="Avatar" color="indigo" class="text-indigo" :rules="[rules.required]"></v-file-input>
                    </v-card-text>
                    <v-card-actions class="d-flex align-center justify-center">
                        <v-btn type="submit" class="bg-indigo" width="500">Register</v-btn>
                    </v-card-actions>
                </v-form>
                <v-card-text class="text-center">
                    <v-btn flat color="indigo" variant="text" size="x-small" @click="toLogin">Already registered?</v-btn>
                </v-card-text>
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
                    role: '',
                    email: '',
                    password: '',
                    confirmPassword: '',
                    avatar: null 
                },
                rules: {
                    required: (value) => !!value || 'This field is required.',
                    minLength: (value) => (value && value.length >= 4) || 'Min 4 characters.',
                    matchPassword: (value) => value === this.formData.password || 'Passwords do not match.',
                    emailFormat: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value) || 'Invalid email address',
                    complexPassword: (value) => /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])/.test(value) || 'Password must include a number, lowercase, uppercase, and a symbol'
                },
                successDialog: false,
            }
        },
        methods: {
            async handleRegister(){
                const { valid } = await this.$refs.registerForm.validate()
                if (valid) {
                    await axios.post('http://127.0.0.1:8000/api/register/', this.formData, {
                        headers: {
                            "Content-Type": 'multipart/form-data',
                        }
                    })
                    .then(response => {
                        console.log(response.status)
                        this.successDialog = true
                    })
                    .catch(error => console.error(error))
                }
            },
            closeDialog(){
                this.successDialog = false
                this.$router.push('/login')
            },
            toLogin(){
                this.$router.push('/login')
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