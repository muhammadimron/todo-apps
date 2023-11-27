<template>
	<div class="team-view">
		<h1 class="text-subtitle-1 text-grey">Team</h1>

		<v-container class="my-15">
			<v-row>
				<v-col cols="12" sm="6" md="3" v-for="person in team" :key="person.name">
					<v-card flat class="text-center ma-3">
						<v-responsive class="pt-4">
							<v-avatar size="100" color="grey">
								<img :src="person.avatar" alt="Avatar Images">
							</v-avatar>
						</v-responsive>
						<v-card-text>
							<v-card-title class="text-h6">{{ person.name }}</v-card-title>
							<div class="text-grey">{{ person.role }}</div>
						</v-card-text>
						<v-card-actions>
							<v-btn flat color="grey">
								<v-icon icon="mdi-message" class="text-grey" start></v-icon>
								<span>Message</span>
							</v-btn>
						</v-card-actions>
					</v-card>
				</v-col>
			</v-row>
		</v-container>
	</div>
</template>
  
  <script>
  export default {
    name: 'TeamView',
	data(){
		return {
			team: [
				{
					name: "The Master",
					role: "Project Manager",
					avatar: "/avatar-1.png"
				},
				{
					name: "Chihaou Nouma",
					role: "Data Analyst",
					avatar: "/avatar-2.png"
				},
				{
					name: "Sungi Sinh",
					role: "Front-End Developer",
					avatar: "/avatar-3.png"
				},
				{
					name: "Watasugi Onodesu",
					role: "Back-End Developer",
					avatar: "/avatar-4.png"
				},
				{
					name: "Sikufari Takuriyu",
					role: "Data Engineer",
					avatar: "/avatar-5.png"
				},
			],
		}
	}
  };
  </script>
  