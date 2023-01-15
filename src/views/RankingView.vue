<template>
    <div class="ranking">
        <v-card elevation="5" class="ma-10">
            <v-tabs
                grow
                color="secondary darken-1"
                background-color="transparent"
                icons-and-text
            >
                <v-tab>
                    Top Players
                    <v-icon> mdi-chess-king </v-icon>
                </v-tab>

                <v-tab-item>
                    <div>
                        <v-switch
                            inset
                            label="Friends Only"
                            style="
                                max-width: fit-content;
                                margin-left: auto;
                                margin-right: 5%;
                            "
                            v-model="chess_friend_toggle"
                        />
                    </div>

                    <v-card-title>
                        <v-spacer></v-spacer>
                        <v-text-field
                            v-model="search"
                            append-icon="mdi-magnify"
                            label="Search"
                            single-line
                            hide-details
                            style="margin-right: 5%; max-width: 45%"
                        ></v-text-field>
                    </v-card-title>

                    <v-data-table
                        no-data-text="Go make some friends!"
                        height="90vh"
                        :headers="headers"
                        :items="chess_friend_toggle? friend_chess : top_chess"
                        class="elevation-5 mx-10 mb-5"
                        :items-per-page="20"
                        :search="chess_search"
                        :loading="top_chess.length < 20"
                    >
                    </v-data-table>
                </v-tab-item>

                <v-tab>
                    Top Puzzlers
                    <v-icon> mdi-puzzle </v-icon>
                </v-tab>

                <v-tab-item>
                    <div>
                        <v-switch
                            inset
                            label="Friends Only"
                            style="
                                max-width: fit-content;
                                margin-left: auto;
                                margin-right: 5%;
                            "
                            v-model="puzzle_friend_toggle"
                        />
                    </div>

                    <v-data-table
                        style="margin-right: 5%; max-width: 45%"
                        no-data-text="Go make some friends!"
                        height="90vh"
                        :headers="headers"
                        :items="puzzle_friend_toggle? friend_puzzle : top_puzzle"
                        class="elevation-5 mx-10 mb-5"
                        :items-per-page="20"
                        :loading="top_puzzle.length < 20"
                    >
                    </v-data-table>
                </v-tab-item>
            </v-tabs>
        </v-card>
    </div>
</template>

<script>
export default {
    name: "App",
    data: () => ({
        headers: [
            {
                text: "Player",
                align: "start",
                sortable: false,
                value: "username",
            },
            {
                text: "Rating",
                sortable: false,
                value: "rating",
            },
            {
                text: "Delta",
                sortable: false,
                value: "delta",
            },
        ],
        chess_friend_toggle: false,
        puzzle_friend_toggle: false,

        top_chess: [],
        top_puzzle: [],
        friend_chess: [],
        friend_puzzle: [],

        chess_search: "",
        puzzle_search: "",
    }),
    methods: {
        feedback() {},
    },

    created() {
        fetch("https://lichess.org/api/player/top/100/classical")
            .then((response) => response.json())
            .then((data) =>
                data["users"].forEach((element) => {
                    this.top_chess.push({
                        username: element["username"],
                        rating: element["perfs"]["classical"]["rating"],
                        delta: element["perfs"]["classical"]["progress"],
                    });
                })
            );

        // When API no have puzzle leaderboard :/
        fetch("https://lichess.org/api/player/top/100/threeCheck")
            .then((response) => response.json())
            .then((data) =>
                data["users"].forEach((element) => {
                    this.top_puzzle.push({
                        username: element["username"],
                        rating: element["perfs"]["threeCheck"]["rating"],
                        delta: element["perfs"]["threeCheck"]["progress"],
                    });
                })
            );
    },
};
</script>