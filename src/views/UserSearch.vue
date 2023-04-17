<template>
    <div class="mx-auto mt-4" style="max-width: max(69%, 900px);">
        <h1 class="mx-auto mt-4" width="100%">Find a Team!</h1>

        <div class="d-flex">
            <!-- left side search -->
            <div style="width: 69%" class="ma-2">
            </div>

            <!-- right side user team management -->
            <div style="width: 31%" class="ma-2">
                <v-expansion-panels accordion v-model="panels">
                    <!-- Only for moderators -->
                    <v-expansion-panel class="primary lighten-3" v-if="!curPlayer.team_id">
                        <v-expansion-panel-header class="font-weight-bold" style="font-size: 1.3rem;">
                                Applications
                            </v-expansion-panel-header>
                            <v-expansion-panel-content>
                                <v-data-table :headers="app_table_headers" :items="applications" class="elevation-10"
                            hide-default-header :items-per-page="-1" no-data-text="No Applications Yet..."
                            hide-default-footer>

                            <template v-slot:item.username="{ item }">
                                {{ item.creator_name }}
                            </template>

                            <!-- Accept/Reject Button -->
                            <template v-slot:item.actions="{ item }">
                                <v-btn medium icon color="grey" @click="approveApp(item, true)">
                                    <v-icon>mdi-trash</v-icon>
                                </v-btn>
                            </template>

                            </v-data-table>
                            </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>


                <v-btn v-if="!$store.state.curPlayer.team_id" @click="createTeam()" block style="font-size: 1.3rem;"
                    class="green lighten-3 py-6 px-5 mt-2 font-weight-bold">
                    Make Team
                    <v-spacer />
                    <v-icon size=1.3rem left>mdi-plus</v-icon>
                </v-btn>

                <v-btn v-else block style="font-size: 1.3rem;" @click="$router.push('teams/' + curPlayer.team_id)"
                    class="primary lighten-1 py-6 px-5 mt-2 font-weight-bold">
                    <v-icon size="2rem" left>mdi-account-group</v-icon>
                    <v-spacer />
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
            players: []
        }
    },

    methods: {
        selectTeam(player) {
            this.$router.push("/player/" + player.username)
        }
    },

    computed: {
        filteredPlayers() {
            return this.players.filter(team => {
                return team.team_name.toLowerCase().includes(this.search.toLowerCase())
            })
        },

        ...mapGetters({ curPlayer: 'getCurPlayer' })
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

/deep/ .v-btn {
    text-transform: none;
    letter-spacing: normal;
}
</style>
