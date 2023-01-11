<template>
    <div class="board">
        <chessboard @onMove="onMove" />

        <div v-if="lost"></div>
    </div>
</template>

<script lang="ts">
// import { chessboard } from "vue-chessboard";
import chessboard from "./TempAIBoard.vue"
import "../assets/stylesheets/board.css";

import Vue from "vue";
export default Vue.extend({
    name: "Chessboard",
    extends: chessboard,
    components: { chessboard },
    data: {
        lost: false,
    },
    methods: {
        onMove() {},
    },
});
</script>