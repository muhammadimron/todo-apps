<template>
    <v-dialog v-model="dialog" width="600">
        <template v-slot:activator="{ props }">
            <v-btn color="success" v-bind="props">Add New Project</v-btn>
        </template>
        <v-card>
            <v-card-title>Add a New Project</v-card-title>
            <v-form @submit.prevent="addSubmit" ref="form">
                <v-card-text>
                    <v-text-field v-model="title" label="Title" prepend-inner-icon="mdi-folder" color="indigo" class="text-indigo" :rules="rules"></v-text-field>
                    <v-textarea v-model="content" label="Content" prepend-inner-icon="mdi-pencil" color="indigo" class="text-indigo" :rules="rules"></v-textarea>
                    <v-select v-model="status" label="Status" :items="['ongoing', 'complete', 'overdue']" prepend-inner-icon="mdi-clock-check" color="indigo" class="text-indigo"></v-select>
                    <v-menu v-model="menu" :close-on-content-click="false" width="200">
                        <template v-slot:activator="{ props }">
                            <v-text-field v-model="formattedDate" label="Due Date" v-bind="props" prepend-inner-icon="mdi-folder" color="indigo" class="text-indigo" :rules="rules"></v-text-field>
                        </template>
                        <v-card width="fit-content">
                            <v-date-picker v-model="due" show-adjacent-months color="indigo" :min="minDate"></v-date-picker>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="warning" variant="text" @click="menu = false">Close</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-menu>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="warning" variant="text" @click="dialog = false">Cancel</v-btn>
                    <v-btn color="success" variant="text" type="submit">Add Project</v-btn>
                </v-card-actions>
            </v-form>
        </v-card>
    </v-dialog>
</template>

<script>
    import format from 'date-fns/format'
    import axios from 'axios'
    export default {
        name: "PopUp",
        data(){
            return {
                dialog: false,
                menu: false,
                title: '',
                content: '',
                status: '',
                due: null,
                minDate: new Date(),
                rules: [
                    val => val.length >= 3 || "Minimum characters is 3.",
                ]
            }
        },
        methods: {
            async addSubmit(){
                const { valid } = await this.$refs.form.validate()
                if(valid){
                    const token = localStorage.getItem("token")
                    const response = await axios.get('http://127.0.0.1:8000/api/person/', {
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    })

                    if (response.status == 200) {
                        const person = response.data.id
                        
                        try {
                            await axios.post('http://127.0.0.1:8000/api/project/', {
                                title: this.title,
                                content: this.content,
                                status: this.status,
                                due: this.due,
                                person: person
                            },
                            {
                                headers: {
                                    Authorization: `Bearer ${token}`
                                }
                            })
                        } catch (error) {
                            console.error(error)
                        }
                    }

                    this.dialog = false
                }
            },
        },
        computed: {
            formattedDate(){
                return this.due ? format(this.due, 'do MMMM yyyy') : ''
            }
        },
    }
</script>