<template>
    <div class="mx-auto mt-4" style="max-width: max(69%, 900px);">
        <h1 class="mx-auto mt-4" width="100%">Find a Team!</h1>

        <div class="d-flex">        
            <!-- left side search -->
            <div style="width: 75%" class="ma-2">
                <v-text-field dense solo label="Search Teams" append-icon="mdi-magnify" single-line outlined hide-details
                clearable height="min(100px, 5vh)" class="mx-auto grey lighten-3 rounded-pill"
                style=" margin-top: min(50px, max(1.5%, 1.5vh));" v-model="search"
                @click:clear="search = ''" />
                
                <v-container class="my-4 mx-auto rounded-xl">
                    <v-row>
                        <v-col v-for="team in filteredTeams" :key="team.id" cols="12" xl="6">
                            <TeamCard :team="team" @click="selectTeam(team)" />
                        </v-col>
                    </v-row>
                </v-container>
            </div>
            
            <!-- right side user team management -->
            <div style="width: 25%" class="ma-2">
                <v-expansion-panels popout v-model="panels">

                    <!-- Show Moderators -->
                    <v-expansion-panel class="primary lighten-3">
                        <v-expansion-panel-header>
                            My Applications
                        </v-expansion-panel-header>
                        <v-expansion-panel-content>
                            <v-data-table :headers="mod_table_headers" :items="moderators" class="elevation-10" hide-default-header :items-per-page="-1"
                                no-data-text="No Applications Yet" hide-default-footer @click:row="toPlayer" sort-by="rating" :sort-desc="true">

                                <template v-slot:item.avatar="{ item }">
                                    <v-img v-if="item.avatar" :src="item.avatar"/>
                                    <v-icon v-else>mdi-account-circle</v-icon>
                                </template>
                        
                                <template v-slot:item.username="{ item }">
                                    {{ item.username }}
                                </template>
                            </v-data-table>
                        </v-expansion-panel-content>
                    </v-expansion-panel>

                    <!-- Only for moderators -->
                    <v-expansion-panel class="primary lighten-3" v-if="curPlayer.mod_start_date && $route.params.teamId === curPlayer.team_id.toString()">
                        <v-expansion-panel-header>
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
                                        color="green"
                                        @click="approveApp(item, true)">
                                        <v-icon>mdi-check</v-icon>
                                    </v-btn>

                                    <v-btn
                                        medium icon
                                        color="red"
                                        @click="approveApp(item, false)">
                                        <v-icon>mdi-close</v-icon>
                                    </v-btn>
                                </template>

                            </v-data-table>
                        </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>

                
                    <v-btn 
                        v-if="$store.state.curPlayer.mod_start_date"
                        block style="font-size: 2rem;" 
                        @click="quitModding()"
                        class="red darken-1 pa-6 py-8 my-4" dark>
                        <v-icon size="2rem" left>mdi-cancel</v-icon>
                        <v-spacer/>
                            Stop Mod
                    </v-btn>

                    <v-btn 
                        v-if="!$store.state.curPlayer.team_id"
                        block style="font-size: 2rem;" 
                        @click="applyToTeam()"
                        class="green pa-6 py-8 my-4">
                        <v-icon size="2rem" left>mdi-account-plus</v-icon>
                        <v-spacer/>
                        Apply NOW!
                    </v-btn>
                
                    <v-btn 
                        v-else
                        @click="quitTeam()"
                        block style="font-size: 2rem;" 
                        class="red darken-1 pa-6 py-8 my-4" dark>
                            <v-icon size="2rem" left>mdi-logout</v-icon>
                            <v-spacer/>
                            Quit Team
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
            teams: []
        }
    },

    methods: {
        selectTeam(team) {
            this.$router.push("/teams/" + team.team_id)
        }
    },

    computed: {
        filteredTeams() {
            return this.teams.filter(team => {
                return team.team_name.toLowerCase().includes(this.search.toLowerCase())
            })
        },

        ...mapGetters({curPlayer: 'getCurPlayer'})
    },

    async created() {
        console.log(this.$route.params)
        this.teams = await this.$store.getters.getTeams(this.$route.params.id)
    }
}
</script>


<style scoped>
.v-text-field>>>input,
.v-text-field>>>label {
    font-size: 1.3rem;
}
</style>
