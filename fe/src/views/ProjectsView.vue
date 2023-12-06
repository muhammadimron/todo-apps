<template>
  <div class="projects-view">
    <h1 class="text-subtitle-1 text-grey">Projects</h1>

    <v-container class="my-15">
      <v-expansion-panels>
        <v-expansion-panel v-for="project in myProjects" :key="project.id">
          <v-expansion-panel-title>
            {{ project.title }}
          </v-expansion-panel-title>
          <v-expansion-panel-text>
            <v-card flat class="px-4">
              <v-card-item class="text-grey">
                <v-card-subtitle class="font-weight-bold">
                  due to {{ getFormatedDate(project.due) }}
                </v-card-subtitle>
                <v-card-text>
                  {{ project.content }}
                </v-card-text>
                <v-card-actions>
                  <v-btn v-if="project.status == 'ongoing'" class="bg-indigo" size="small" @click="updateCompleteStatus(project)">Make complete</v-btn>
                  <v-btn v-if="project.status == 'complete'" class="bg-grey" size="small" disabled>Completed</v-btn>
                  <v-btn v-if="project.status == 'overdue'" class="bg-danger" size="small" disabled>Overdue</v-btn>
                </v-card-actions>
              </v-card-item>
            </v-card>
          </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ProjectsView',
  data(){
    return {
      projects: [],
      person: '',
    }
  },
  computed: {
    myProjects(){
      return this.projects.filter(project => {
        const fullName = `${project.person_detail.first_name} ${project.person_detail.last_name}`
        return fullName === this.person
      })
    }
  },
  methods: {
    getFormatedDate(date){
      const dateObj = new Date(date)
      const options = {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      }
      const formattedDate = dateObj.toLocaleDateString('en-US', options)
      return formattedDate
    },
    async updateCompleteStatus(project){
      const token = localStorage.getItem("token")

      project.status = "complete"
      try {
        await axios.put(`http://127.0.0.1:8000/api/project/${project.id}/`, project, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
      } catch (error) {
        console.error(error)
      }
    }
  },
  async mounted(){
    const token = localStorage.getItem("token")
    const response = await axios.get('http://127.0.0.1:8000/api/project/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    
    if (response.status == 200) {
      this.projects = response.data
    }

    const responsePerson = await axios.get('http://127.0.0.1:8000/api/person/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    if (responsePerson.status == 200) {
      this.person = `${responsePerson.data.first_name} ${responsePerson.data.last_name}`
    }
  }
};
</script>
