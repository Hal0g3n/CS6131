<template>
    <div class="chessboard">
        <chessboard @onMove="onMove" :orientation="ori" :fen="fen"/>
    </div>
</template>

<script lang="ts">
// import { chessboard } from "vue-chessboard";
import chessboard from "./TempAIBoard.vue";
import "../assets/stylesheets/board.css";

import Vue from "vue";
export default Vue.extend({
    name: "Chessboard",
    components: { chessboard },
    props: {
        ori: {
            type: String,
            required: true,
        },
        fen: {
            type: String,
            default: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        }
    },
    methods: {
        onMove(data: any) {
            console.log(this.fen)
            if ("turn" in data) return;
            this.$emit(
                "onEnd",
                data.history.length % 2 == +(this.$props.ori == "white")
            );
        },
    },
});
</script>