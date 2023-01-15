<template>
    <div class="profile flex-column" style="width: 100%">
        <!-- Profile Card -->
        <v-card
            elevation="12"
            class="pb-4"
            style="margin: 3vh 25vw"
            color="primary lighten-2"
            height="25vh"
        >
            <div
                class="d-flex flex-no-wrap justify-space-between align-center"
                style="height: 100%; width: 100%"
            >
                <div>
                    <v-card-title
                        style="text-align: left"
                        class="text-h3 font-weight-medium mb-auto"
                        v-text="player.username"
                    ></v-card-title>
                    <v-card-title
                        style="text-align: left"
                        class="text-h5 font-weight-bold mt-auto"
                        v-text="player.rating"
                    ></v-card-title>
                </div>

                <v-avatar class="ma-3" size="15vh" tile>
                    <v-img :src="player.avatar" style="border: 2px solid var(--v-secondary-lighten1);"></v-img>
                </v-avatar>
            </div>
        </v-card>

        <!-- Graphing -->
        <v-card class="ma-10" elevation="5">
            <v-toolbar flat color="primary" dark>
                <v-toolbar-title class="text-h3 ma-5">Statistics</v-toolbar-title>
            </v-toolbar>
            <v-tabs
                vertical
                grow
                color="secondary darken-1"
                background-color="transparent"
                icon
            >
                <v-tab>
                    <v-icon left> mdi-information </v-icon>
                    About
                    <v-spacer />
                </v-tab>

                <v-tab-item>
                    <v-card height="60vh" class="d-flex align-center">
                        <v-card
                            elevation="10"
                            class="ma-10"
                            width="calc(40% - 40px)"
                            height="35vh"
                        >
                            <v-card-title>About Me!</v-card-title>
                            <v-card-text>{{ player.about }}</v-card-text>
                        </v-card>
                        <div style="flex-grow: 1; margin-right: 2%;">
                            <p class="text-h4">Recent Games</p>
                            <v-data-table
                                height="30vh"
                                :headers="headers"
                                :items="games"
                                class="elevation-1"
                                items-per-page="6"
                                no-data-text="No games played so far..."
                            >
                                <template v-slot:item.result="{ item }">
                                    <v-icon v-if="item.result === 1" color="green">mdi-plus</v-icon>
                                    <v-icon v-else-if="item.result === 0" color="grey">mdi-equal</v-icon>
                                    <v-icon v-else color="red">mdi-minus</v-icon>
                                </template>
                                <template v-slot:item.date="{ item }">
                                    {{item.date.toLocaleDateString("en-UK", {day: "numeric", month:"short", year: "numeric"})}}
                                </template>
                                <template v-slot:item.side="{ item }">
                                    <div v-if="item.side == 'black'" style="width: 2vmin; height: 2vmin; border: 2px solid var(--v-primary-base); background-color: #616161"/>
                                    <div v-else style="width: 2vmin; height: 2vmin; border: 2px solid var(--v-primary-base); background-color: #eeeeee"/>
                                </template>
                            </v-data-table>
                        </div>
                    </v-card>
                </v-tab-item>

                <v-tab>
                    <v-icon left> mdi-checkerboard </v-icon>
                    Classical
                    <v-spacer />
                </v-tab>

                <v-tab-item>
                    <v-card height="60vh" class="pa-5" flat>
                        <div
                            style="width: 50%; justify: "
                            class="d-flex justify-center align-center"
                        >
                            <v-btn
                                v-for="range in ranges"
                                :key="range.name"
                                :id="range.name"
                                @click="rezoomClassicalData(range.name)"
                                :outlined="classicalSelection !== range.name"
                                depressed
                                color="primary"
                                class="ma-1"
                            >
                                {{ range.display }}
                            </v-btn>
                            <v-spacer />
                            <div class="text-h5">Rating History</div>
                        </div>

                        <LineChart
                            ref="classicalChart"
                            width="50%"
                            height="80%"
                            type="area"
                            style="
                                .svg {
                                    overflow: visible;
                                }
                            "
                            :options="chartOptions"
                            :series="classical_data"
                        />
                    </v-card>
                </v-tab-item>

                <v-tab>
                    <v-icon left> mdi-puzzle </v-icon>
                    Puzzles
                    <v-spacer />
                </v-tab>

                <v-tab-item>
                    <v-card height="60vh" class="pa-5" flat>
                        <div
                            style="width: 50%; justify: "
                            class="d-flex justify-center align-center"
                        >
                            <v-btn
                                v-for="range in ranges"
                                :key="range.name"
                                :id="range.name"
                                @click="rezoomPuzzleData(range.name)"
                                :outlined="puzzleSelection !== range.name"
                                depressed
                                color="primary"
                                class="ma-1"
                            >
                                {{ range.display }}
                            </v-btn>
                            <v-spacer />
                            <div class="text-h5">Puzzle History</div>
                        </div>

                        <LineChart
                            ref="puzzleChart"
                            width="50%"
                            height="80%"
                            type="area"
                            :options="chartOptions"
                            :series="puzzle_data"
                        />
                    </v-card>
                </v-tab-item>
            </v-tabs>
        </v-card>
    </div>
</template>

<script lang="js">
import Vue from "vue";
import VueApexCharts from "vue-apexcharts";

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
        classical_data: [],
        puzzle_data: [],

        classicalSelection: "all",
        puzzleSelection: "all",

        ranges: [
            {display: "1M", name:"one_month"},
            {display: "6M", name:"six_months"},
            {display: "1Y", name:"one_year"},
            {display: "All", name:"all"},
        ],

        player: {
            username: "Halogen",
            rating: 100,
            avatar: "https://cdn.discordapp.com/avatars/340785972545454080/6cf1fe5e726470b1903236d2638d5a58.png?size=1024",
            about: "Hello I am Halogen! Let's all have fun together!"
        },

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
            { text: "Result", value: "result"},
            { text: 'Moves', value: 'moves' },
            { text: 'Date', value: 'date' }
        ],
        games: [
            {
                opponent: "AI",
                result: 1,
                moves: 70,
                side: "white",
                date: new Date(2023, 0, 12)
            },
            {
                opponent: "AI",
                result: -1,
                moves: 69,
                side: "white",
                date: new Date(2023, 1, 11)
            },
            {
                opponent: "AI",
                result: 0,
                moves: 50,
                side: "white",
                date: new Date(2023, 2, 11)
            },
            {
                opponent: "AI",
                result: 1,
                moves: 70,
                side: "black",
                date: new Date(2023, 1, 10)
            },
            {
                opponent: "AI",
                result: 0,
                moves: 69,
                side: "black",
                date: new Date(2023, 1, 10)
            },
            {
                opponent: "AI",
                result: -1,
                moves: 50,
                side: "black",
                date: new Date(2023, 1, 10)
            },
            {
                opponent: "AI",
                result: 1,
                moves: 9,
                side: "white",
                date: new Date(2023, 1, 9)
            },
            {
                opponent: "AI",
                result: -1,
                moves: 6,
                side: "white",
                date: new Date(2023, 1, 8)
            },
            {
                opponent: "AI",
                result: 1,
                moves: 9,
                side: "black",
                date: new Date(2023, 1, 7)
            },
            {
                opponent: "AI",
                result: -1,
                moves: 6,
                side: "black",
                date: new Date(2023, 1, 7)
            }
        ]
    }),
    methods: {
        rezoomClassicalData(timeline) {
            this.selection = timeline;
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
                new Date().getTime() // Today
            );
        },
        
        rezoomPuzzleData(timeline) {
            this.selection = timeline;
            var right = this.puzzle_data[0]['data'][this.puzzle_data[0]['data'].length - 1][0];
            var left = new Date(right);

            switch (timeline) {
                case "one_month": left.setMonth(left.getMonth() - 1); break;
                case "six_months": left.setMonth(left.getMonth() - 6); break;
                case "one_year": left.setFullYear(left.getFullYear() - 1); break;
                case "all": left = this.puzzle_data[0]['data'][0][0]; break;
                default:
            }
            
            this.$refs.puzzleChart.zoomX(
                left.getTime(),
                new Date().getTime() // Today
            );
        },
    },
    components: { LineChart: VueApexCharts },

    created: async function() {
        var data = await fetch("https://lichess.org/api/user/penguingim1/rating-history").then((response) => response.json())

        for (var i in data[0]['points']) {
            this.classical_data.push([new Date(data[0]['points'][i][0], data[0]['points'][i][1], data[0]['points'][i][2]), data[0]['points'][i][3]]);
        }

        for (var i in data[13]['points']) {
            this.puzzle_data.push([new Date(data[13]['points'][i][0], data[13]['points'][i][1], data[13]['points'][i][2]), data[13]['points'][i][3]]);
        }

        this.classical_data = [{
            data: this.classical_data,
            name: "Classical"
        }];

        this.puzzle_data = [{
            data: this.puzzle_data,
            name: "Puzzles"
        }];
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