<template>
	<div class="team-view">
		<h1 class="text-subtitle-1 text-grey">Team</h1>

		<v-container class="my-15">
			<v-row>
				<v-col cols="12" sm="6" md="3" v-for="person in team" :key="person.id">
					<v-card flat class="text-center ma-3">
						<v-responsive class="pt-4">
							<v-avatar size="100" color="grey">
								<img :src="person.avatar" alt="Avatar Images">
							</v-avatar>
						</v-responsive>
						<v-card-text>
							<v-card-title class="text-h6">{{ `${person.first_name} ${person.last_name}` }}</v-card-title>
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
  import axios from 'axios';
  export default {
    name: 'TeamView',
	data(){
		return {
			team: []
		}
	},
	async mounted(){
		const token = localStorage.getItem("token")
		const response = await axios.get('http://127.0.0.1:8000/api/personAll', {
			headers: {
				Authorization: `Bearer ${token}`
			}
		})

		if (response.status == 200) {
			this.team = response.data
		}
	}
  };
  </script>
  