<template>
    <v-hover v-slot="{hover}">
        <v-card 
        @click = "$emit('click', team)"
        outlined tile
        :class="{ 'on-hover': hover && hoverAnim }"
        class="rounded-xl hover-card"
        height="100%"
        width ="100%"
        :elevation="hover && hoverAnim ? 24 : 6">
            <div class="d-flex flex-no-wrap justify-right align-center" style="height: 100%; width: 100%">
                <v-avatar class="mx-3 my-auto" size="72px" tile>
                    <v-img size=72px v-if="team.icon" :src="team.icon"/>
                    <v-icon size=72px v-else>mdi-forum</v-icon>
                </v-avatar>
            
                <div align="left">
                    <v-card-title class="font-weight-medium">{{ team.team_name }}</v-card-title>
                    <v-card-text>{{ team.about_team }}</v-card-text>
                </div>
                
                <v-spacer/>
                <div class="ma-4 d-flex">
                    <v-icon>mdi-account-multiple</v-icon>
                    {{ team.member_count }}
                </div>
            </div>
        </v-card>
    </v-hover>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
    name: "TeamCard",
    props: {
        team: {
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


<style scoped>
.hover-card {
  transition: opacity .2s ease-in-out;
  cursor: pointer;
}

.hover-card:not(.on-hover) {
  opacity: 0.8;
}
</style>