<template>
    <v-hover v-slot="{ hover }">
        <v-card @click="$emit('click', player)" outlined shaped :class="{ 'on-hover': hover }" height="100%"
            :elevation="hover ? 24 : 6">
            <div class="d-flex flex-no-wrap justify-right align-center" style="height: 100%; width: 100%">
                <v-avatar class="mx-3 my-auto" size="72px">
                    <v-img :src="player.avatar"></v-img>
                </v-avatar>

                <div align="left">
                    <v-card-title class="font-weight-medium">{{ player.username }}</v-card-title>
                    <v-card-text>{{ player.about_me }}</v-card-text>
                </div>

                <v-spacer/>
                <div class="ma-4 d-flex">
                    {{ player.rating }}
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
        }
    },
})
</script>


<style>
.v-card {
    transition: opacity .2s ease-in-out;
    cursor: pointer;
}

.v-card:not(.on-hover) {
    opacity: 0.8;
}
</style>