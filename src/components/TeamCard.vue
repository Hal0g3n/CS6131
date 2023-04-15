<template>
    <!-- TODO: Style this -->
    <v-card>
        <v-img :src=" team.icon " height="200px" />
        <v-card-title>{{ team.team_name }}</v-card-title>
        <v-card-text>{{ team.about_team }}</v-card-text>
    </v-card>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
    name: "TeamCard",
    props: {
        team: {
            type: Object,
            required: true
        }
    },
})
</script>