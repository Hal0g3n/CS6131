<template>
    <!-- TODO: Adapt this to Users -->
    <div>
        <h1 class="mx-auto my-4" style="max-width: max(66%, 880px);">Find a Team!</h1>
        <!-- <v-card class="my-4 mx-auto grey lighten-3 rounded-xl" style="max-width: max(60%, 800px)">
            <v-card-text> -->
        <v-text-field dense solo label="Search Teams" append-icon="mdi-magnify" single-line outlined hide-details clearable
            height="min(100px, 5vh)" class="mx-auto grey lighten-3 rounded-pill"
            style="max-width: max(60%, 800px); margin-top: min(150px, max(2.5%, 2.5vh));" v-model="search"
            @click:clear="search = ''" />
        <!-- </v-card-text>
        </v-card> -->

        <v-container class="my-4 mx-auto rounded-xl" style="max-width: max(65%, 867px)">
            <v-row>
                <v-col v-for="Team in filteredTeams" :key="Team.id" cols="12" sm="6" md="4">
                    <TeamCard :team="Team" />
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
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


<style scoped>
.v-text-field>>>input,
.v-text-field>>>label {
    font-size: 1.3rem;
}
</style>
