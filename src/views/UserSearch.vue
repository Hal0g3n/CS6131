<template>
    <div class="mx-auto mt-4" style="max-width: max(69%, 900px);">
        <h1 class="mx-auto mt-4" width="100%">Find a Player!</h1>

        <div class="d-flex justify-space-between">
            <!-- left side result display-->
            <div style="width: 60%" class="ma-2">
                <v-container class="my-4" width="100%">
                    <v-row v-for="player in filteredPlayers" :key="player.username"> <v-col class="pa-0 py-1">
                        <PlayerCard :player="player" @click="selectTeam(player)"/>
                    </v-col> </v-row>
                </v-container>
            </div>

            <!-- right side searching -->
            <div style="width: 31%" class="ma-2">
                <v-text-field dense solo label="Search Username" append-icon="mdi-magnify" single-line outlined hide-details
                    clearable height="min(100px, 5vh)" class="mx-auto my-4 grey lighten-3 rounded-pill"
                    style=" margin-top: min(50px, max(1.5%, 1.5vh));" v-model="search" @click:clear="search = ''"/>

                <v-expansion-panels accordion v-model="panels">
                    <!-- Only for moderators -->
                    <v-expansion-panel class="elevation-5">
                        <v-expansion-panel-header class="font-weight-bold" style="font-size: 1.3rem;">
                                Filters
                            </v-expansion-panel-header>
                            <v-expansion-panel-content>
                                
                            </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex';
import PlayerCard from '../components/PlayerCard.vue'

export default {
    components: {
        PlayerCard
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
            return this.players.filter(player => {
                return player.username.toLowerCase().includes(this.search.toLowerCase())
            })
        },

        ...mapGetters({ curPlayer: 'getCurPlayer' })
    },

    async created() {
        this.players = await this.$store.getters.getPlayers()
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
