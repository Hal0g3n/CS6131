<template>
    <chessboard @onMove="onMove" fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" ref="__board"/>
</template>

<script>
// import { chessboard } from "vue-chessboard";
import chessboard from "./TempAIBoard.vue";
import "../assets/stylesheets/board.css";

import Vue from "vue";
export default Vue.extend({
    name: "Chessboard",
    components: { chessboard },
    methods: {
        onMove(data) {
            if ("turn" in data) return;
            forceEnd();
        },

        forceEnd() {
            this.$emit(
                "onEnd",
                this.$refs.__board.game.isDraw() ? 'draw' : // If draw
                    this.$refs.__board.turn() == 'w' ? 'black' : 'white' // Current turn is loser
            );
        },

        restartBoard(n_ori) {
            this.$refs.__board.game.reset();
            
            if (n_ori == 'black') this.$refs.__board.aiNextMove();
            else 
                this.$refs.__board.board.set({
                    fen: this.$refs.__board.game.fen(),
                    turnColor: "white",
                    movable: { 
                        color: "white", 
                        dests: this.$refs.__board.possibleMoves(),
                        events: { after: this.$refs.__board.userPlay() } },
                });

            if (this.$refs.__board.board.state.orientation != n_ori)
                this.$refs.__board.board.toggleOrientation();
        }
    },

    mounted() {
        this.$refs.__board.board.set({
            fen: this.$refs.__board.game.fen(),
            turnColor: "white",
            movable: { 
                color: "white", 
                dests: [], 
            },
        });

        // Reponsive to resizing
        window.addEventListener('resize', this.onResize);
    }, 

    unmounted() {
        window.removeEventListener('resize', this.onResize);
    }
});
</script>