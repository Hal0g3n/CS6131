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
            this.$emit(
                "onEnd",
                data.history[data.history.length-1].includes("#") ? data.history.length % 2 ? 'white' : 'black' : 'draw'
            );
        },

        restartBoard(n_ori) {
            this.$refs.__board.game.reset();
            this.$refs.__board.game.loadPgn('1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 exd4 7.O-O d3 8.Qb3 Qf6 9.e5 Qg6 10.Re1 Nge7 11.Ba3 b5 12.Qxb5 Rb8 13.Qa4 Bb6 14.Nbd2 Bb7 15.Ne4 Qf5 16.Bxd3 Qh5 17.Nf6+ gxf6 18.exf6 Rg8 19.Rad1 Qxf3 20.Rxe7+ Nxe7 21.Qxd7+ Kxd7 22.Bf5+ Ke8 23.Bd7+ Kf8 24.Bxe7# 1-0')
            
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
        // TODO: Make Chessboard more responsive
    }
});
</script>