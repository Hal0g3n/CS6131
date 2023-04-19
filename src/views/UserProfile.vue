<template>
    <div class="profile flex-column" style="width: 100%">
        <!-- Profile Card -->
        <v-card elevation="12" class="pb-4" style="margin: 3vh 25vw;" height="15vh">
            <div class="d-flex flex-no-wrap justify-right align-center" style="height: 100%; width: 100%">
                <v-avatar class="mx-3 my-auto" size="72px" tile>
                    <v-img size=72px v-if="player.avatar" :src="player.avatar"/>
                    <v-icon size=72px v-else>mdi-account-circle</v-icon>
                </v-avatar>
    
                <div align="left">
                    <v-card-title class="text-h3 font-weight-medium">{{ player.username }}</v-card-title>
                </div>
            </div>
        </v-card>

        <!-- Graphing -->
        <v-card class="ma-10" elevation="5">
            <v-toolbar flat color="primary" dark>
                <v-toolbar-title class="text-h3 ma-5">Statistics</v-toolbar-title>
            </v-toolbar>
            <v-tabs vertical grow color="secondary darken-1" background-color="transparent" icon>
                <v-tab>
                    <v-icon left> mdi-information </v-icon>
                    About
                    <v-spacer />
                </v-tab>

                <v-tab-item>
                    <v-card height="60vh" class="d-flex align-center justify-start">
                        <v-card elevation="10" class="ma-10" width="calc(40% - 40px)" height="35vh">
                            <v-card-title>About Me!</v-card-title>
                            <v-card-text v-if="display">{{ player.about_me }}</v-card-text>
                            <v-textarea v-else
                                solo no-resize class="mx-4 mt-4"
                                outlined v-model="player.about_me" 
                                @keydown.ctrl.enter="swapDisplay"/>
                    
                            <div class="d-flex justify-end mx-5">
                                <v-btn v-if="player.username == curPlayer.username"
                                    large icon
                                    color="grey"
                                    @click="swapDisplay">
                                    <v-icon v-if="display">mdi-pen</v-icon>
                                    <v-icon v-else color="green">mdi-check</v-icon>
                                </v-btn>
                            </div>
                        </v-card>

                        
                        <div elevation="10" class="ma-10" width="calc(40% - 40px)" height="35vh">
                            <v-card-title>Team</v-card-title>
                            <v-card-text v-if="!player.team_id">None at the moment...</v-card-text>
                            <TeamCard v-else :hoverAnim="false" :team="team" @click="$router.push('/teams/' + player.team_id)"/>
                        </div>
                        
                    </v-card>
                </v-tab-item>



                <v-tab>
                    <v-icon left> mdi-checkerboard </v-icon>
                    Classical
                    <v-spacer />
                </v-tab>

                <v-tab-item>
                    <v-card height="60vh" class="pa-5 d-flex align-center" flat>

                        <!-- The graph -->
                        <div style="width: 50%; height:100%" class="pr-5">
                            <div class="d-flex justify-center align-center">
                                <v-btn v-for="range in ranges" :key="range.name" :id="range.name"
                                    @click="rezoomClassicalData(range.name)" :outlined="classicalSelection !== range.name"
                                    depressed color="primary" class="ma-1">
                                    {{ range.display }}
                                </v-btn>
                                <v-spacer />
                                <div class="text-h5">Rating History</div>
                            </div>

                            <LineChart ref="classicalChart" width="100%" height="80%" type="area" style=".svg {overflow: visible;}" :options="chartOptions" :series="classical_data" />
                        </div>

                        <!-- The history table -->
                        <div style="flex-grow: 1; margin-right: 2%;">
                            <p class="text-h4">Recent Games</p>
                            <v-data-table height="30vh" :headers="headers" :items="games" class="elevation-1"
                                items-per-page="6" no-data-text="No games played so far..." :footer-props="{
                                    showFirstLastPage: true,
                                    disableItemsPerPage: true
                                }">
                                <template v-slot:item.result="{ item }">
                                    <v-icon v-if="item.result === 1" color="green">mdi-plus</v-icon>
                                    <v-icon v-else-if="item.result === 0" color="grey">mdi-equal</v-icon>
                                    <v-icon v-else color="red">mdi-minus</v-icon>
                                </template>
                                <template v-slot:item.date="{ item }">
                                    {{ item.date.toLocaleDateString("en-UK", {
                                        day: "numeric", month: "short", year:
                                            "numeric"
                                    }) }}
                                </template>
                                <template v-slot:item.side="{ item }">
                                    <div v-if="item.side == 'black'"
                                        style="width: 2vmin; height: 2vmin; border: 2px solid var(--v-primary-base); background-color: #616161" />
                                    <div v-else
                                        style="width: 2vmin; height: 2vmin; border: 2px solid var(--v-primary-base); background-color: #eeeeee" />
                                </template>
                            </v-data-table>
                        </div>
                    </v-card>
                </v-tab-item>



                <v-tab v-if="false">
                    <v-icon left> mdi-puzzle </v-icon>
                    Puzzles
                    <v-spacer />
                </v-tab>

                <v-tab-item>
                    <v-card height="60vh" class="pa-5 d-flex align-center" flat>
                        <!-- The graph -->
                        <div style="width: 50%; height:100%" class="pr-5">
                            <div class="d-flex justify-center align-center">
                                <v-btn v-for="range in ranges" :key="range.name" :id="range.name"
                                    @click="rezoomPuzzleData(range.name)" :outlined="puzzleSelection !== range.name"
                                    depressed color="primary" class="ma-1">
                                    {{ range.display }}
                                </v-btn>
                                <v-spacer />
                                <div class="text-h5">Rating History</div>
                            </div>

                            <LineChart ref="puzzleChart" width="100%" height="80%" type="area" style=".svg {overflow: visible;}" :options="chartOptions" :series="puzzle_data" />
                        </div>

                        <!-- The history table -->
                        <div style="flex-grow: 1; margin-right: 2%;">
                            <p class="text-h4">Recent Puzzles</p>
                            <v-data-table height="30vh" :headers="headers" :items="games" class="elevation-1" items-per-page="6"
                                no-data-text="No games played so far..." :footer-props="{
                                    showFirstLastPage: true,
                                    disableItemsPerPage: true
                                }">
                                <template v-slot:item.result="{ item }">
                                    <v-icon v-if="item.result === 1" color="green">mdi-plus</v-icon>
                                    <v-icon v-else-if="item.result === 0" color="grey">mdi-equal</v-icon>
                                    <v-icon v-else color="red">mdi-minus</v-icon>
                                </template>
                                <template v-slot:item.date="{ item }">
                                    {{ item.date.toLocaleDateString("en-UK", {
                                        day: "numeric", month: "short", year: "numeric"
                                    }) }}
                                </template>
                                <template v-slot:item.side="{ item }">
                                    <div v-if="item.side == 'black'"
                                        style="width: 2vmin; height: 2vmin; border: 2px solid var(--v-primary-base); background-color: #616161" />
                                    <div v-else
                                        style="width: 2vmin; height: 2vmin; border: 2px solid var(--v-primary-base); background-color: #eeeeee" />
                                </template>
                            </v-data-table>
                        </div>
                    </v-card>
                </v-tab-item>

            </v-tabs>
        </v-card>
    </div>
</template>

<script lang="js">
import Vue from "vue";
import { mapGetters } from "vuex";
import VueApexCharts from "vue-apexcharts";
import TeamCard from '../components/TeamCard.vue'
import PlayerCard from '../components/PlayerCard.vue'

export default Vue.extend({
    data: () => ({
        chartOptions: {
            chart: {
                type: "area",
                curve: "straight",
                stacked: false,
                zoom: {
                    type: "x",
                    enabled: false,
                    autoScaleYaxis: true,
                },
                toolbar: {
                    show: false
                },
            },

            xaxis: {
                type: "datetime",
            },

            fill: {
                type: "gradient",
                gradient: {
                    shadeIntensity: 1,
                    inverseColors: false,
                    opacityFrom: 0.5,
                    opacityTo: 0,
                    stops: [0, 90, 100],
                },
            },

            noData: {
                text: 'Loading...'
            },

            dataLabels: {
                enabled: false,
            },
        },

        player: {},
        team: {},
        classical_data: [],
        puzzle_data: [],
        display: true,

        classicalSelection: "all",
        puzzleSelection: "all",

        ranges: [
            { display: "1M", name: "one_month" },
            { display: "6M", name: "six_months" },
            { display: "1Y", name: "one_year" },
            { display: "All", name: "all" },
        ],

        headers: [
            {
                text: 'Opponent',
                align: 'start',
                sortable: false,
                value: 'opponent',
            },
            {
                text: 'Side',
                sortable: false,
                value: 'side',
            },
            { text: "Result", value: "result" },
            { text: 'Date', value: 'date' }
        ],
        games: [
            {
                "date": "Sat, 11 Feb 2023 16:09:23 GMT",
                "is_public": true,
                "opponent": "ethantan2509",
                "result": -1,
                "side": "white"
            },
            {
                "date": "Sat, 11 Feb 2023 16:02:11 GMT",
                "is_public": true,
                "opponent": "ethantan2509",
                "result": 1,
                "side": "black"
            }
        ]
    }),

    methods: {
        rezoomClassicalData(timeline) {
            this.classicalSelection = timeline;
            var right = this.classical_data[0]['data'][this.classical_data[0]['data'].length - 1][0];
            var left = new Date(right);

            switch (timeline) {
                case "one_month": left.setMonth(left.getMonth() - 1); break;
                case "six_months": left.setMonth(left.getMonth() - 6); break;
                case "one_year": left.setFullYear(left.getFullYear() - 1); break;
                case "all": left = this.classical_data[0]['data'][0][0]; break;
                default:
            }

            this.$refs.classicalChart.zoomX(
                left.getTime(),
                right // Today
            );
        },

        rezoomPuzzleData(timeline) {
            this.puzzleSelection = timeline;
            var right = this.puzzle_data[0]['data'][this.puzzle_data[0]['data'].length - 1][0];
            var left = new Date(right);

            switch (timeline) {
                case "one_month": left.setMonth(left.getMonth() - 1); break;
                case "six_months": left.setMonth(left.getMonth() - 6); break;
                case "one_year": left.setFullYear(left.getFullYear() - 1); break;
                case "all": left = this.puzzle_data[0]['data'][0][0]; break;
                default:
            }

            console.log(left, right)

            this.$refs.puzzleChart.zoomX(
                left.getTime(),
                right // Today
            );
        },

        async swapDisplay() {
            if (this.display) {this.display = false; return;}

            if (await this.$store.dispatch("updateProfile", {
                username: this.$route.params.username,
                about: this.player.about_me
            })) this.display = true;
            else { this.$notify("Failed") }

        }
    },
    components: { LineChart: VueApexCharts, TeamCard, PlayerCard},

    computed: {
        ...mapGetters({
            curPlayer: 'getCurPlayer',
        })
    },

    beforeCreate() {

    },

    async beforeMount() {
        var data = await fetch("https://lichess.org/api/user/penguingim1/rating-history").then((response) => response.json())
        this.player = await this.$store.getters.getPlayer(this.$route.params.username)
        this.player.rating_history.map(point => [new Date(point.datetime), point.rating])
        this.player.puzzle_history.map(point => [new Date(point.datetime), point.rating])

        this.classical_data = [{
            data: this.player.rating_history.map(point => [new Date(point.datetime), point.rating]),
            name: "Classical"
        }];

        this.puzzle_data = [{
            data: this.player.puzzle_history.map(point => [new Date(point.datetime), point.rating]),
            name: "Puzzles"
        }];

        // Get the games
        this.games = await this.$store.getters.getGames(this.$route.params.username);
        this.games.map(game => game['date'] = new Date(game['date']))
        
        if (!this.player.team_id) return;

        this.team = await this.$store.getters.getTeam(this.player.team_id)
        console.log(this.team)
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