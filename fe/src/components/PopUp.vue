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
                    <v-textarea v-model="content" label="Information" prepend-inner-icon="mdi-pencil" color="indigo" class="text-indigo" :rules="rules"></v-textarea>
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
    export default {
        name: "PopUp",
        data(){
            return {
                dialog: false,
                menu: false,
                title: '',
                content: '',
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
                    console.log(`Title : ${this.title}\nInformation : ${this.content}\nDue : ${this.due}`)
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