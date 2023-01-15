<template>
    <v-container class="Game" fluid fill-height fill-width>
        <v-row justify="center">
            <v-col md="5" v-if="$vuetify.breakpoint.mdAndUp">
                <v-card elevation="12" shaped class="mt-6 pb-4" color="primary lighten-2" height="15vh">
                    <div class="d-flex flex-no-wrap justify-space-between">
                        <div>
                            <v-card-title style="text-align: left"
                                class="text-h2 font-weight-medium"
                                v-text="opponent.username"
                            ></v-card-title>

                            <v-card-text style="text-align: left"
                                class="text-h4 font-weight-bold"
                                v-text="opponent.rating"
                            ></v-card-text>
                        </div>

                        <v-avatar class="ma-3" size="125" tile>
                            <v-img :src="opponent.avatar"></v-img>
                        </v-avatar>
                    </div>
                </v-card>

                <!-- Spacer div -->
                <div style="height: calc(90vmin - 400px)"/>

                <v-card elevation="12" shaped class="pb-4" color="primary lighten-2" height="15vh">
                    <div class="d-flex flex-no-wrap justify-space-between">
                        <div>
                            <v-card-title style="text-align: left"
                                class="text-h2 font-weight-medium"
                                v-text="player.username"
                            ></v-card-title>

                            <v-card-text style="text-align: left"
                                class="text-h4 font-weight-bold"
                                v-text="player.rating"
                            ></v-card-text>
                        </div>

                        <v-avatar class="ma-3" size="125" tile>
                            <v-img :src="player.avatar"></v-img>
                        </v-avatar>
                    </div>
                </v-card>

            </v-col>

            <v-col lg="6" md="7" cols="12" align="center">
                <Chessboard @onEnd="onEnd" ref="board" />
            </v-col>
        </v-row>

        <!-- TODO: Make dialog look better -->
        <v-dialog v-model="dialog" width="500">
            <v-card>
                <v-card-title class="text-h5 grey lighten-2">
                    {{ won ? "Win" : "Loss" }} by Checkmate
                </v-card-title>

                <v-card-text>
                    {{ won ? "Defeated" : "Lost to " }} AI
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="playAgain('white')">
                        Play again as White
                    </v-btn>
                    <v-btn color="primary" text @click="playAgain('black')">
                        Play again as Black
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>


<script>
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
    databaseURL:
        "https://chessible-34200-default-rtdb.asia-southeast1.firebasedatabase.app/",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Realtime Database and get a reference to the service
const database = getDatabase(app);

import Vue from "vue";
import Chessboard from "../components/Chessboard.vue";

export default Vue.extend({
    name: "GameView",
    components: { Chessboard },
    data: () => ({
        dialog: false,
        won: true,
        ori: "white",
        opponent: {
            username: "AI",
            rating: 200,
            avatar: "https://thumbs.dreamstime.com/z/gear-smart-ai-icon-outline-style-vector-web-design-isolated-white-background-153382060.jpg"
        },
        player: {
            username: "Halogen",
            rating: 100,
            avatar: "https://cdn.discordapp.com/avatars/340785972545454080/6cf1fe5e726470b1903236d2638d5a58.png?size=1024"
        }
    }),

    methods: {
        onEnd(win) {
            console.log(this.dialog);
            this.dialog = true;
            this.won = this.ori == win;
        },

        playAgain(ori) {
            this.ori = ori;
            this.$refs.board.reloadBoard(ori);
            this.dialog = false;
        },
    },

    mounted() {
        this.$refs.board.reloadBoard("white");
    },
});
</script>