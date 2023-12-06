<template>
  <div class="dashboard-view">
    <h1 class="text-subtitle-1 text-grey">Dashboard</h1>
    <v-container class="my-15">
      <v-row class="mb-5">
        <v-col cols="12" md="2">
          <v-tooltip location="top" text="Sort by project names">
            <template v-slot:activator="{ props }">
              <v-btn v-bind="props" flat color="grey-lighten-3" size="small" @click="sortBy('title')">
                <v-icon icon="mdi-folder" class="text-grey" start></v-icon>
                <span class="text-caption text-grey text-lowercase">By project name</span>
              </v-btn>
            </template>
          </v-tooltip>
        </v-col>
        <v-col cols="12" md="2">
          <v-tooltip location="top" text="Sort by person">
            <template v-slot:activator="{ props }">
              <v-btn v-bind="props" flat color="grey-lighten-3" size="small" @click="sortBy('person')">
                <v-icon icon="mdi-account-group" class="text-grey" start></v-icon>
                <span class="text-caption text-grey text-lowercase">By person</span>
              </v-btn>
            </template>
          </v-tooltip>
        </v-col>
      </v-row>
      <v-card flat v-for="project in projects" :key="project.id" >
        <v-row no-gutters :class="`pa-5 project ${project.status}`">
          <v-col cols="12" md="6">
            <div class="text-caption text-grey">Project title</div>
            <div>{{ project.title }}</div>
          </v-col>
          <v-col cols="6" md="2" sm="4">
            <div class="text-caption text-grey">Person</div>
            <div>{{ `${project.person_detail.first_name} ${project.person_detail.last_name}` }}</div>
          </v-col>
          <v-col cols="6" md="2" sm="4">
            <div class="text-caption text-grey">Due by</div>
            <div>{{ getFormatedDate(project.due) }}</div>
          </v-col>
          <v-col cols="6" md="2" sm="4">
            <div class="text-right">
              <v-chip :class="`${project.status} text-caption text-white my-2`" size="small">{{ project.status }}</v-chip>
            </div>
          </v-col>
        </v-row>
        <v-divider></v-divider>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'DashboardView',
  data(){
    return {
      projects: [],
    }
  },
  methods: {
    sortBy(prop){
      this.projects.sort((a, b) => a[prop] < b[prop] ? -1 : 1)
    },
    getFormatedDate(date){
      const dateObj = new Date(date)
      const options = {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      }
      const formattedDate = dateObj.toLocaleDateString('en-US', options)
      return formattedDate
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
  }
};
</script>

<style>

.project.complete {
  border-left: 4px solid #3cd1c2;
}

.project.ongoing {
  border-left: 4px solid orange;
}

.project.overdue {
  border-left: 4px solid tomato;
}

.v-chip.complete {
  background: #3cd1c2;
}

.v-chip.ongoing {
  background: #ffaa2c;
}

.v-chip.overdue {
  background: #f83e70;
}

</style>