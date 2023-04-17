<template>
    <div class="mx-auto mt-4" style="max-width: max(69%, 900px);">
        <h1 class="mx-auto mt-4" width="100%">Find a Team!</h1>

        <div class="d-flex">        
            <!-- left side search -->
            <div :width="loggedIn ? '63%' : '100%'" class="ma-2">
                <v-text-field dense solo label="Search Teams" append-icon="mdi-magnify" single-line outlined hide-details
                clearable height="min(100px, 5vh)" class="mx-auto grey lighten-3 rounded-pill"
                style=" margin-top: min(50px, max(1.5%, 1.5vh));" v-model="search"
                @click:clear="search = ''" />
                
                <v-container class="my-4 mx-auto">
                    <v-row v-for="team in filteredTeams" :key="team.id"> <v-col class="pa-0 py-1">
                        <TeamCard :team="team" @click="selectTeam(team)"/>
                    </v-col> </v-row>
                </v-container>
            </div>
            
            <!-- right side user team management -->
            <div v-if="loggedIn" style="width: 37%" class="ma-2">
                <v-expansion-panels accordion v-if="!curPlayer.team_id">
                    
                    <v-expansion-panel class="primary lighten-3">
                        <v-expansion-panel-header class="font-weight-bold" style="font-size: 1.3rem;">
                            Applications
                        </v-expansion-panel-header>
                        <v-expansion-panel-content>
                            <v-data-table :headers="app_table_headers" :items="applications" class="elevation-10" hide-default-header :items-per-page="-1"
                                no-data-text="No Applications Yet..." hide-default-footer>
                    
                                <template v-slot:item.username="{ item }">
                                    {{ item.creator_name }}
                                </template>
                            
                                <!-- Accept/Reject Button -->
                                <template v-slot:item.actions="{ item }">
                                    <v-btn
                                        medium icon
                                        color="grey"
                                        @click="approveApp(item, true)">
                                        <v-icon>mdi-trash</v-icon>
                                    </v-btn>
                                </template>

                            </v-data-table>
                        </v-expansion-panel-content>
                    </v-expansion-panel>

                    <!-- To create a team -->
                    <v-expansion-panel class="green lighten-3" v-if="!curPlayer.team_id">
                        <v-expansion-panel-header class="font-weight-bold" expand-icon="mdi-plus" style="font-size: 1.3rem;">
                            Create Team
                        </v-expansion-panel-header>
                        <v-expansion-panel-content>
                            <v-text-field 
                                label="Team Name"
                                placeholder="My Team"
                                v-model="team_name"
                                solo @keydown.enter="createTeam()"
                                clearable/>
                        </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>

                <v-btn 
                    v-if="curPlayer.team_id"
                    block style="font-size: 1.3rem;" 
                    @click="$router.push('teams/' + curPlayer.team_id)"
                    class="primary lighten-1 py-6 px-5 mt-2 font-weight-bold">
                    <v-icon size="2rem" left>mdi-account-group</v-icon>
                    <v-spacer/>
                        My Team
                </v-btn>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex';
import TeamCard from '../components/TeamCard.vue'

export default {
    components: {
        TeamCard
    },
    data() {
        return {
            search: '',
            teams: [],
            team_name: '',
            applications: [],

            
            app_table_headers: [
                {
                    text: 'team_name',
                    sortable: false,
                    value: 'team_name',
                },
                {
                    text: "actions",
                    sortable: false,
                    align: 'end',
                    value: "actions",
                }
            ],
        }
    },

    methods: {
        selectTeam(team) {
            this.$router.push("/teams/" + team.team_id)
        },

        async createTeam() {
            let n_team = await this.$store.dispatch('createTeam', this.team_name)
            console.log(n_team)
            this.$router.push("/teams/" + n_team.team_id)
        }
    },

    computed: {
        filteredTeams() {
            return this.teams.filter(team => {
                return team.team_name.toLowerCase().includes(this.search.toLowerCase())
            })
        },

        ...mapGetters({curPlayer: 'getCurPlayer', loggedIn: 'loggedIn'})
    },

    async created() {
        console.log(this.$route.params)
        this.teams = await this.$store.getters.getTeams(this.$route.params.id)

        // Get applications
        this.applications = await this.$store.getters.getUserApplications()
        console.log(this.applications)
    }
}
</script>


<style scoped>
.v-text-field>>>input,
.v-text-field>>>label {
    font-size: 1.3rem;
}

/deep/ .v-btn {
  text-transform: none;
  letter-spacing: normal;
}
</style>
