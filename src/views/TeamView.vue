<template>
    <div class="teamView mx-auto my-8" style="width: min(70%, 1785px)">

        <!-- Team card -->
        <v-card outlined height="100%" class="my-2" elevation="6">

            <v-container no-gutters height="100%" width="100%">
                <v-row :justify="$vuetify.breakpoint.lgAndDown ? 'center' : 'start'">
                    <v-col class="d-flex flex-nowrap align-center" justify="$vuetify.breakpoint.lgAndDown ? 'center' : 'start'" sm="12" xl="6">
                        <v-avatar class="mx-3 my-auto" size="100px" tile>
                            <v-img :src="team.icon"></v-img>
                        </v-avatar>

                        <div align="left">
                            <v-card-title class="font-weight-medium text-">{{ team.team_name }}</v-card-title>
                            <v-card-text>{{ team.about_team }}</v-card-text>
                        </div>
                    </v-col>

                    <v-spacer />
                    <v-col class="d-flex flex-column ma-4 align-center" sm="3" xl="2">
                        <v-icon size="64px">mdi-account-multiple</v-icon>
                        <v-card-title>{{ team.member_count }}</v-card-title>
                    </v-col>
                    <v-col class="d-flex flex-column ma-4 align-center" sm="3" xl="2">
                        <v-icon size="64px">mdi-chess-pawn</v-icon>
                        <v-card-title>{{ average_rating }}</v-card-title>
                    </v-col>
                </v-row>
            </v-container>

        </v-card>


        <p class="text-h4 mt-8">Team Members</p>

        <div class="d-flex">
            <!-- Left Side -->
            <div style="width: 65%" class="ma-2">
                <v-data-table :headers="table_headers" :items="team.players" class="elevation-5" hide-default-header :items-per-page="-1"
                    no-data-text="Loading Members" hide-default-footer @click:row="toPlayer" sort-by="rating" :sort-desc="true">

                    <template v-slot:item.ranking="{ index }">
                        {{ index+1 }}
                    </template>

                    <template v-slot:item.avatar="{ item }">
                        <v-img v-if="item.avatar" :src="item.avatar"/>
                        <v-icon v-else>mdi-account-circle</v-icon>
                    </template>
                    
                    <template v-slot:item.username="{ item }">
                        {{ item.username }}
                    </template>
                </v-data-table>
            </div>
            
            <!-- Right Side -->
            <div style="width: 35%" class="mx-2">
                
                <v-expansion-panels class="mt-2" accordion v-model="panels">

                    <!-- Show Moderators -->
                    <v-expansion-panel class="elevation-10">
                        <v-expansion-panel-header>
                            Moderators
                        </v-expansion-panel-header>
                        <v-expansion-panel-content>
                            <v-data-table :headers="mod_table_headers" :items="moderators" class="elevation-10" hide-default-header :items-per-page="-1"
                                no-data-text="Loading Moderators" hide-default-footer @click:row="toPlayer" sort-by="rating" :sort-desc="true">

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
                    <v-expansion-panel class="elevation-10" v-if="$store.state.curPlayer.mod_start_date && $route.params.teamId === $store.state.curPlayer.team_id.toString()">
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
                    v-if="curPlayer.mod_start_date && curPlayer.team_id == $route.params.teamId"
                    block style="font-size: 1.4rem;" 
                    @click="quitModding()"
                    class="orange darken-1 py-6 px-5 mt-2 font-weight-bold" dark>
                    <v-icon size="1.4rem" left>mdi-cancel</v-icon>
                    <v-spacer/>
                    Stop Mod
                </v-btn>

                <v-btn 
                    v-if="!curPlayer.team_id && loggedIn"
                    block style="font-size: 1.4rem;" 
                    @click="dialog = true"
                    class="green lighten-3 py-6 px-5 mt-2 font-weight-bold">
                    <v-icon size="1.4rem" left>mdi-account-plus</v-icon>
                    <v-spacer/>
                    Apply NOW!
                </v-btn>
                
                <v-btn 
                    v-if="!loggedIn"
                    block style="font-size: 1.4rem;" 
                    @click="$router.push('/login')"
                    class="green lighten-3 py-6 px-5 mt-2 font-weight-bold">
                    <v-icon size="1.4rem" left>mdi-account-plus</v-icon>
                    <v-spacer/>
                    Login to JOIN!
                </v-btn>
                
                <v-btn 
                v-if="curPlayer.team_id == $route.params.teamId"
                @click="quitTeam()"
                    block style="font-size: 1.4rem;" 
                    class="orange darken-1 py-6 px-5 mt-2 font-weight-bold" dark>
                    <v-icon size="1.4rem" left>mdi-logout</v-icon>
                    <v-spacer/>
                    Quit Team
                </v-btn>
                <!-- <v-btn block style="font-size: 2rem;" class="mx-auto">Login to Join NOW!</v-btn> -->
            </div>
        </div>
        
        <v-dialog v-model="dialog" width="max(500px, 50%)">
            <v-card>
                 <v-toolbar
                        class="text-h4 lighten-2"
                        color="green"
                    >
                
                    <v-spacer/>
                    <p class="ma-4">Leave A Message?</p>
                    <v-spacer/>
                </v-toolbar>

                <v-textarea 
                    solo no-resize class="mx-4 mt-4"
                    outlined v-model="message" 
                    @keydown.ctrl.enter="applyToTeam"/>

                <div width=100% class="d-flex justify-end">
                    <v-btn outlined class="ma-5 green lighten-3" @click="applyToTeam">Apply</v-btn>
                </div>

                <v-divider></v-divider>
            </v-card>
        </v-dialog>

    </div>
</template>

<script lang="js">
import Vue from "vue";
import { mapGetters } from 'vuex';
import TeamCard from "../components/TeamCard.vue";

export default Vue.extend({
    data: () => ({
        team: {},
        dialog: false,
        panels: 0,
        average_puzzle: 0,
        average_rating: 0,
        message: "",

        table_headers: [
            {
                text: 'ranking',
                align: 'start',
                sortable: false,
                value: 'ranking',
            },
            {
                text: 'Avatar',
                align: 'start',
                sortable: false,
                value: 'avatar',
            },
            {
                text: 'Username',
                sortable: false,
                value: 'username',
            },
            {
                text: 'rating',
                sortable: false,
                align: 'end',
                value: 'rating',
            },
        ],

        mod_table_headers: [
            {
                text: 'Avatar',
                align: 'start',
                sortable: false,
                value: 'avatar',
            },
            {
                text: 'Username',
                sortable: false,
                value: 'username',
            },
        ],

        app_table_headers: [
            {
                text: 'Username',
                sortable: false,
                value: 'username',
            },
            {
                text: "actions",
                sortable: false,
                align: 'end',
                value: "actions",
            }
        ],

        applications: [],
    }),

    methods: {
        toPlayer(player) {
            this.$router.push("/player/" + player.username)
        },

        async quitModding() {
            // Reload the information if it works
            if (await this.$store.dispatch("quitTeamMod")) this.$router.go()
            else { this.$notify("Failed") }
        },

        promoteToMod(item) {
        },

        async quitTeam() {
            // Reload the information if it works
            if (await this.$store.dispatch("quitTeam")) this.$router.go()
            else { this.$notify("Failed") }
        },
        
        async applyToTeam() {
            if (await this.$store.dispatch("makeApplication", {
                team_id: this.$route.params.teamId,
                message: this.message
            })) {
                // State the error
                this.$notify({
                    type: "Success",
                    title: 'Application Successful',
                    text: 'Please wait for a moderator to accept you'
                });
                this.dialog = false
            }
            else this.$notify("Application Failed")
        },

        async approveApp(item, result) {
            // If approve, dispatch approval acceptance event to server
            if (result) {
                // Reload the information if it works
                if (await this.$store.dispatch("approveApplication", {
                    team_id: this.$route.params.teamId, 
                    applicant: item.creator_name
                })) this.$router.go()
                else {this.$notify("Failed")}
            }
            
            // Else reject, and delete application from server
            else {
                // Reload the information if it works
                if (await this.$store.dispatch("rejectApplication", {
                    id: item.id,
                    team_id: item.team_id,
                    applicant: item.creator_name
                })) this.$router.go()
                else { this.$notify("Failed") }
            }
        }
    },

    computed: {
        moderators() {
            return this.team.players.filter(player => player.is_moderator)
        },

        ...mapGetters({
            curPlayer: 'getCurPlayer',
            loggedIn: 'loggedIn',
        })
    },

    components: { TeamCard },

    beforeMount: async function () {
        this.team = (await this.$store.getters.getTeam(this.$route.params.teamId));

        for (let player of this.team.players) {
            this.average_puzzle += player.puzzle
            this.average_rating += player.rating
        }

        this.average_puzzle = Math.round(this.average_puzzle / this.team.players.length);
        this.average_rating = Math.round(this.average_rating / this.team.players.length);
        
        // Check if player is moderator
        if (!this.$store.state.curPlayer.mod_start_date || this.$route.params.teamId !== this.$store.state.curPlayer.team_id.toString()) return;
        
        // Get applications
        this.applications = await this.$store.getters.getApplications(this.$route.params.teamId)
    }
});
</script>

<style scoped>
.v-tabs--vertical {
    background-color: var(--v-primary-lighten4);
}

svg {
    overflow: visible;
}
</style>