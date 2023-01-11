<template>
    <div class="Game">
        <Chessboard align="center" @onEnd="onEnd" ori="white" :fen="curfen"/>
        
        <v-dialog v-model="dialog" width="500">
            <!-- <template v-slot:activator="{ on, attrs }">
                <v-btn
                color="red lighten-2"
                dark
                v-bind="attrs"
                v-on="on"
                >
                Click Me
                </v-btn>
            </template> -->

            <v-card>
                <v-card-title class="text-h5 grey lighten-2">
                {{won ? "Win" : "Loss"}} by Checkmate
                </v-card-title>

                <v-card-text>
                {{won ? "Defeated" : "Lost to "}} AI
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="primary"
                    text
                    @click="playAgain"
                >
                    Play again
                </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
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
    data: {
        dialog: false, 
        won: false, 
        curfen:"rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2"
    },

    methods: {
        onEnd: function(win) {
            this.dialog = true;
            this.won = win;
        },

        playAgain() {
            this.dialog = false;
            this.curfen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";
        }
    },
});
</script>