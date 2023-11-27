<template>
  <div class="projects-view">
    <h1 class="text-subtitle-1 text-grey">Projects</h1>

    <v-container class="my-15">
      <v-expansion-panels>
        <v-expansion-panel v-for="project in myProjects" :key="project.title">
          <v-expansion-panel-title>
            {{ project.title }}
          </v-expansion-panel-title>
          <v-expansion-panel-text>
            <v-card flat class="px-4">
              <v-card-item class="text-grey">
                <v-card-subtitle class="font-weight-bold">
                  due to {{ project.due }}
                </v-card-subtitle>
                <v-card-text>
                  {{ project.content }}
                </v-card-text>
              </v-card-item>
            </v-card>
          </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'ProjectsView',
  data(){
    return {
      projects: [
        {
          title: "Design a New Website",
          person: "The Master",
          due: "1st January 2024",
          status: "complete",
          content: "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Rerum libero dicta, tenetur quos quas qui fugiat obcaecati corporis quo? Quibusdam optio fuga veritatis quisquam et? Delectus molestiae assumenda suscipit totam."
        },
        {
          title: "Building Secure Microserver",
          person: "Chihaou Nouma",
          due: "31th December 2023",
          status: "ongoing",
          content: "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Rerum libero dicta, tenetur quos quas qui fugiat obcaecati corporis quo? Quibusdam optio fuga veritatis quisquam et? Delectus molestiae assumenda suscipit totam."
        },
        {
          title: "Design a New Website - Version 2",
          person: "The Master",
          due: "1st February 2024",
          status: "ongoing",
          content: "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Rerum libero dicta, tenetur quos quas qui fugiat obcaecati corporis quo? Quibusdam optio fuga veritatis quisquam et? Delectus molestiae assumenda suscipit totam."
        },
        {
          title: "How to Make a Great API with Django",
          person: "Sungi Sinh",
          due: "12 November 2023",
          status: "complete",
          content: "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Rerum libero dicta, tenetur quos quas qui fugiat obcaecati corporis quo? Quibusdam optio fuga veritatis quisquam et? Delectus molestiae assumenda suscipit totam."
        },
        {
          title: "Tips How to Become a Great Programmer",
          person: "Watasugi Onodesu",
          due: "11st December 2023",
          status: "overdue",
          content: "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Rerum libero dicta, tenetur quos quas qui fugiat obcaecati corporis quo? Quibusdam optio fuga veritatis quisquam et? Delectus molestiae assumenda suscipit totam."
        },
      ]
    }
  },
  computed: {
    myProjects(){
      return this.projects.filter(project => {
        return project.person === "The Master"
      })
    }
  }
};
</script>
