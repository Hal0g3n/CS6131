<template>
    <v-hover v-slot="{ hover }"><v-card 
        @click = "$emit('click', player)"
        outlined tile
        :class="{ 'on-hover': hover && hoverAnim }"
        class="rounded-xl hover-card"
        height="100%"
        width ="100%"
        :elevation="hover && hoverAnim ? 24 : 6">
            <div class="d-flex flex-no-wrap justify-right align-center" style="height: 100%; width: 100%">
                <v-avatar class="mx-3 my-auto" size="72px" tile>
                    <v-img size=72px v-if="player.avatar" :src="player.avatar"/>
                    <v-icon size=72px v-else>mdi-account-circle</v-icon>
                </v-avatar>
        
                <div align="left">
                    <v-card-title class="font-weight-medium">{{ player.username }}</v-card-title>
                    <v-card-text>{{ player.about_me }}</v-card-text>
                </div>
            
                <v-spacer/>
                <div class="ma-4 d-flex">
                    {{ player.rating }}
                    <v-icon>mdi-chess-pawn</v-icon>
                </div>
            </div>
        </v-card>
    </v-hover>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
    name: "PlayerCard",
    props: {
        player: {
            type: Object,
            required: true
        },

        hoverAnim: {
            type: Boolean,
            default: true,
            required: false
        }
    },
})
</script>


<style>
.hover-card {
    transition: opacity .2s ease-in-out;
    cursor: pointer;
}

.hover-card:not(.on-hover) {
    opacity: 0.8;
}
</style>