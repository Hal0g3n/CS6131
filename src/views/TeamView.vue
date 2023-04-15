<template>
    <div>
        <v-card class="mx-auto" color="grey-lighten-3" max-width="400">
            <v-card-text>
                <v-text-field density="compact" variant="solo" label="Search templates"
                    append-inner-icon="mdi-magnify" single-line hide-details v-model="search"/>
            </v-card-text>
        </v-card>

        <v-container>
            <v-row>
                <v-col v-for="Team in filteredTeams" :key="Team.id" cols="12" sm="6" md="4">
                    <TeamCard :team="Team" />
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import TeamCard from '../components/TeamCard.vue'

export default {
    components: {
        TeamCard
    },
    data() {
        return {
            search: '',
            teams: []
        }
    },
    computed: {
        filteredTeams() {
            return this.teams.filter(team => {
                return team.team_name.toLowerCase().includes(this.search.toLowerCase())
            })
        }
    },

    async created() {
        this.teams = (await axios.get("http://127.0.0.1:5000/teams")).data
        console.log(this.teams)
    }
}
</script>

