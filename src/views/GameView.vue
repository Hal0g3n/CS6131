<template>
    <v-container class="Game" fluid fill-height fill-width>
        <v-row justify="center">
            <v-col md="5" v-if="ori != '' && $vuetify.breakpoint.mdAndUp">
                <v-card
                    elevation="12"
                    class="pb-4"
                    color="primary lighten-2"
                    height="25vh"
                    width="100%"
                    style="margin-top: 3vh"
                    shaped
                >
                    <div
                        class="
                            d-flex
                            flex-no-wrap
                            justify-space-between
                            align-center
                        "
                        style="height: 100%; width: 100%"
                    >
                        <div>
                            <v-card-title
                                style="text-align: left"
                                class="text-h3 font-weight-medium mb-auto"
                                v-text="opponent.username"
                            ></v-card-title>
                            <v-card-title
                                style="text-align: left"
                                class="text-h5 font-weight-bold mt-auto"
                                v-text="opponent.rating"
                            ></v-card-title>
                        </div>

                        <v-avatar class="ma-3" size="15vh" tile>
                            <v-img
                                :src="opponent.avatar"
                                style="
                                    border: 2px solid
                                        var(--v-secondary-lighten1);
                                "
                            ></v-img>
                        </v-avatar>
                    </div>
                </v-card>

                <!-- Spacer div -->
                <div style="height: 25vmin" />

                <v-card
                    elevation="12"
                    class="pb-4"
                    shaped
                    color="primary lighten-2"
                    height="25vh"
                    width="100%"
                >
                    <div
                        class="
                            d-flex
                            flex-no-wrap
                            justify-space-between
                            align-center
                        "
                        style="height: 100%; width: 100%"
                    >
                        <div>
                            <v-card-title
                                style="text-align: left"
                                class="text-h3 font-weight-medium mb-auto"
                                v-text="player.username"
                            ></v-card-title>
                            <v-card-title
                                style="text-align: left"
                                class="text-h5 font-weight-bold mt-auto"
                                v-text="player.rating"
                            ></v-card-title>
                        </div>

                        <v-avatar class="ma-3" size="15vh" tile>
                            <v-img
                                :src="player.avatar"
                                style="
                                    border: 2px solid
                                        var(--v-secondary-lighten1);
                                "
                            ></v-img>
                        </v-avatar>
                    </div>
                </v-card>
            </v-col>

            <v-col md="5" v-if="ori == ''" class="d-flex flex-column">
                <v-card
                    elevation="12"
                    color="primary lighten-2"
                    height="25vh"
                    width="100%"
                    style="margin-top: auto; margin-bottom: auto"
                    shaped
                >
                    <div class='d-flex flex-column'>
                        <div
                            style="text-align: center; font-size: 1.5rem; margin-top: 3%"
                            >Play As?</div
                        >

                        <div class='d-flex flex-strech justify-center align-center' style="flex-grow:2">
                            <v-btn
                                color="transparent"
                                elevation=0
                                class="whiteBtn ma-5"
                                @click="startGame('white')"/>

                            <v-btn
                                color="transparent"
                                elevation=0
                                class="blackBtn ma-5"
                                @click="startGame('black')"/>
                        </div>
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
                <v-toolbar
                    class="text-h3 lighten-2"
                    :color="`${won == 1 ? 'green' : won == 0 ? 'grey' : 'red'}`"
                >
                
                    <v-spacer/>
                    {{ won == 1 ? "Win" : won == 0 ? "Draw" : "Lose" }}
                    <v-spacer/>
                </v-toolbar>

                <v-card-text style="text-align: center;" class="my-5 text-h6">
                    {{ won == 1 ? "+100 rating points" : won == 0 ? "+50 rating points" : "-10 rating points" }}
                </v-card-text>

                <v-divider></v-divider>
            </v-card>
        </v-dialog>
    </v-container>
</template>


<script>
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
    databaseURL: "https://chessible-34200-default-rtdb.asia-southeast1.firebasedatabase.app/",
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
        won: -1,
        ori: "",
        opponent: {
            username: "AI",
            rating: 200,
            avatar: "https://thumbs.dreamstime.com/z/gear-smart-ai-icon-outline-style-vector-web-design-isolated-white-background-153382060.jpg",
        },
        player: {
            username: "Halogen",
            rating: 100,
            avatar: "https://cdn.discordapp.com/avatars/340785972545454080/6cf1fe5e726470b1903236d2638d5a58.png?size=1024",
        },
    }),

    methods: {
        onEnd(win) {
            console.log(win)
            console.log(this.ori)
            console.log(this.won)
            console.log(this.dialog)
            if (win == this.ori) this.won = 1;
            else if (win == "draw") this.won = 0;
            else this.won = -1;
            
            this.dialog = true;
            this.ori = "";
        },

        startGame(ori) {
            this.ori = ori;
            this.$refs.board.restartBoard(ori);
        },
    },
});
</script>

<style scoped>
.blackBtn {
    aspect-ratio: 1/1;
    height: 75%;
    background-size: cover;
    background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNzcuMTciIGhlaWdodD0iMTc3LjE3IiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiIgaW1hZ2UtcmVuZGVyaW5nPSJvcHRpbWl6ZVF1YWxpdHkiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiB2aWV3Qm94PSIwIDAgNTAgNTAiPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0iMCIgeDE9IjIxLjEzIiB5MT0iMzcuMjIiIHgyPSI3Ny43NiIgeTI9IjM3LjQ2OSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiNmZmYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmYiIHN0b3Atb3BhY2l0eT0iMCIvPjwvbGluZWFyR3JhZGllbnQ+PC9kZWZzPjxnIGZpbGw9IiMxZjFhMTciPjxwYXRoIGQ9Im0yNS44MjEgMTIuMDJoLTEuNzYxdi0zLjI1MWgtMi4wNjZjLS41NTkgMC0uODM4LS4yNzEtLjgzOC0uODIxdi0uMDI1YzAtLjU0Mi4yNzktLjgxMy44MzgtLjgxM2gyLjA2NnYtMi4xMDhjMC0uNTg0LjI5Ni0uODcyLjg4OS0uODcyLjU3NiAwIC44NzIuMjg4Ljg3Mi44NzJ2Mi4xMDhoMi4xMzRjLjU0MiAwIC44MTMuMjcxLjgxMy44MTN2LjAyNWMwIC41NS0uMjcxLjgyMS0uODEzLjgyMWwtMi4xMTcuMDI1LS4wMTcgMy4yMjYiLz48cGF0aCBkPSJtMTEuMDMgMzcuNzQ0bC0uODEzLTQuNjRjLS4wMTcgMC0uMDQyLS4wMzQtLjA3Ni0uMTAyLS4wODUtLjExOC0uMzIyLS4yNzEtLjcxMS0uNDU3LS4zODEtLjE5NS0uODM4LS41MTYtMS4zNDYtLjk4Mi0uNzI4LS42MS0xLjI5NS0xLjEwOS0xLjcwMi0xLjQ5LS40MDYtLjM3My0uNzcxLS43ODctMS4xMDEtMS4yMzYtMS4wMS0xLjM4OS0xLjU3NS0zLjA2NS0xLjY4NS01LjA0LS4xNjktMS44OTcuNjAxLTMuNzkzIDIuMzAzLTUuNjgxIDEuNzE5LTEuODggNC4wNDctMi43NjkgNi45NjgtMi42NSAxLjA5Mi4wNjggMi4zNzkuMzMgMy44NDQuNzk2LjQ4My4xOTUuOTc0LjM5IDEuNDgyLjU3Ni41LjE5NS45OTkuMzg5IDEuNDk5LjU4NC4yNjIuMTM1LjUuMjcxLjY5NC4zOTgtLjA4NS0uMzQ3LS4xMjctLjY5NC0uMTI3LTEuMDQxIDAtMS4yODcuNDU3LTIuMzg4IDEuMzgtMy4zMDIuOTE0LS45MDYgMi4wMjQtMS4zNzIgMy4zMTEtMS4zODkgMS4yODcgMCAyLjM4OC40NjYgMy4zMDIgMS4zOC45MDYuOTE0IDEuMzYzIDIuMDIgMS4zNjMgMy4yODUgMCAuMjYyLS4wMzQuNjEtLjEwMiAxLjA0MS4yMjktLjE0NC40NTctLjI3MS42NjktLjM3Mi43NjItLjMzIDEuNzYxLS43MiAzLjAxLTEuMTYgMS40MjItLjQ4MyAyLjcwMS0uNzU0IDMuODQ0LS44MjEgMi45MjEtLjEzNiA1LjI0MS43NTQgNi45NDMgMi42NSAxLjY2OCAxLjg4OCAyLjQ0NyAzLjc4NSAyLjMyOCA1LjY4MS0uMTI3IDEuOTczLS43MDMgMy42NDktMS43MSA1LjA0LS4zMy40NDktLjcwMy44NjQtMS4xMTggMS4yNTMtLjQwNi4zOS0uOTY1Ljg4MS0xLjY2IDEuNDczLS41NDIuNDY2LTEuMDEuNzk2LTEuMzg5Ljk4Mi0uMzgxLjE4Ni0uNjAxLjM0Ny0uNjY5LjQ1Ny0uMDE3LjAzNC0uMDM0LjA1OS0uMDUxLjA3Ni0uMDE3LjAxNy0uMDI1LjAzNC0uMDI1LjA1MWwtLjc5NiA0LjY2NSAxLjY0MyA2LjEyMWMtLjgzLjc0NS0yLjY4NCAxLjM1NS01LjU1NCAxLjgzNy0yLjg3OS40ODMtNi4yMDYuNzItOS45NzQuNzItMy44MzUgMC03LjIxNC0uMjU0LTEwLjExOC0uNzU0LTIuOTEyLS41MDgtNC43NDEtMS4xNDMtNS40ODYtMS44OTdsMS42MzQtNi4wNSIvPjwvZz48cGF0aCBmaWxsPSJ1cmwoIzApIiBkPSJtMjQuOTQ5IDIwLjY3NWMtLjAzNC0uMTYxLS4wNzYtLjMwNS0uMTI3LS40MjMtLjA5My0uMzMtLjE3OC0uNTY3LS4yNDUtLjcyLS4wNTEtLjExLS4xMTktLjI1NC0uMTk1LS40MzItLjA4NS0uMTY5LS4xNjktLjM1Ni0uMjU0LS41NTktLjA1MS0uMTE5LS4xMS0uMjcxLS4xODYtLjQ1Ny0uMDY4LS4xOTUtLjEzNi0uMzczLS4xODYtLjUzMy0uMDQyLS4xNTItLjA2OC0uMzA1LS4wNjgtLjQ3NCAwLS44NzIuNDE1LTEuMzEyIDEuMjYyLTEuMzEyLjg4MSAwIDEuMzEyLjQzMiAxLjMxMiAxLjI4NyAwIC4yMi0uMDM0LjM3My0uMDkzLjQ3NC0uMjM3LjYyNy0uMzU2Ljk2NS0uMzcyIDEuMDE2LS4yNTQuNS0uNDA2LjgyMS0uNDc0Ljk2NS0uMTE5LjI3MS0uMTk1LjUwOC0uMjIuNzItLjA1MS4xMDItLjA4NS4xODYtLjEwMi4yNjItLjAxNy4wNzYtLjAzNC4xMzYtLjA1MS4xODZtLTIuNzc3IDguNTZjLTIuMDY2LjAzNC0zLjk1NC4xMzUtNS42NzMuMzIyLTEuNzEuMTc4LTMuMDMuNDQtMy45NzkuNzctLjQ5MS0uNjE4LTEuMDY3LTEuMjI4LTEuNzE5LTEuODU0LS42Ni0uNjE4LTEuMjI4LTEuMjAyLTEuNzI3LTEuNzQ0LS44My0uODQ3LTEuMjM2LTEuNzctMS4yMzYtMi43NzcgMC0xLjI0NS4yMDMtMi4xNTEuNjE4LTIuNzI2LjQ0LS42NjkgMS4xMzUtMS4xNiAyLjA1Ny0xLjQ4Mi45MjMtLjMyMiAxLjg2My0uNDgzIDIuODAzLS40ODMgMS4xOTQgMCAyLjMyOC4yNjIgMy40Mi43OTYgMS4wNzUuNTU5IDEuNzg3IDEuMDEgMi4xMzQgMS4zMzggMS4xMjYgMS4xNDMgMi4wMSAyLjM3OSAyLjYzMyAzLjcxNy4yMTIuNS4zNzIgMS4xOTQuNDgzIDIuMDc0LjExLjg4OS4xNjkgMS41NjYuMTg2IDIuMDQ5bTIuNzc3LTQuMzE4Yy4xMTktLjQ2Ni4yMTItLjc4Ny4yOTYtLjk2NS4xNjktLjY0My4zNTYtMS4xOTQuNTc2LTEuNjQzLjA5My0uMjc5LjIzNy0uNjAxLjQzMi0uOTc0LjE4Ni0uMzczLjM4OS0uODA0LjYxLTEuMjc5LjEyNy0uMjc5LjI3MS0uNjI3LjQxNS0xLjAzMy4xNTItLjQwNi4zMDUtLjgwNC40NDktMS4yMDIuMTM1LS4zMy4yMDMtLjY4Ni4yMDMtMS4wNjcgMC0uODEzLS4yOTYtMS40OTktLjg3Mi0yLjA2Ni0uNTc2LS41NzYtMS4yNzktLjg2NC0yLjEwOC0uODY0LTEuOTY0IDAtMi45NTUuOTkxLTIuOTU1IDIuOTU1IDAgLjM4MS4wNjguNzM3LjIwMyAxLjA2Ny4zNjQgMS4wNzUuNjQzIDEuODIuODM4IDIuMjM1LjIyLjQ3NC40MTUuOTA2LjYwMSAxLjI3OS4xNzguMzcyLjMzOS42OTQuNDY2Ljk3NC4yMi41NS4zOTggMS4wOTIuNTUgMS42NDMuMDM0LjA5My4xMjcuNDE1LjI5Ni45NG0tLjg4OSA2LjIyM2MwLS42Ni0uMDE3LTEuNTc1LS4wNTEtMi43MzUtLjAzNC0xLjE2OC0uMTYxLTIuMTQyLS4zNzItMi45MjEtLjY3Ny0yLjIxLTEuNzAyLTMuOTk2LTMuMDgyLTUuMzUxLS43MTEtLjY5NC0xLjc5NS0xLjM0Ni0zLjI2OC0xLjkzOS0xLjY4NS0uNjYtMy4yODUtLjk5MS00Ljc5Mi0uOTkxLTIuNjA4IDAtNC41NDcuOTMxLTUuOCAyLjgwMy0uNzExLjk5MS0xLjA2NyAyLjIzNS0xLjA2NyAzLjcxNyAwIDEuNjI2LjM5OCAyLjk1NSAxLjE4NSAzLjk5Ni40MTUuNTkzIDEuMjExIDEuMzI5IDIuMzg4IDIuMjEgMS4xNjguODcyIDIuMTY4IDEuNjg1IDIuOTcyIDIuNDMgMS40MzktLjMxMyAzLjA2NS0uNTg0IDQuODc3LS44MjEgMS44MTItLjIyOSA0LjE0OS0uMzY0IDcuMDEtLjM5OG0xMy43ODQgMTEuNzM1bC0uNzM3LTIuOTI5Yy0zLjIyNi0uNzM3LTcuMjgxLTEuMTA5LTEyLjE1OC0xLjEwOS00LjgyNiAwLTguODY1LjM3My0xMi4xMSAxLjEwOWwtLjc4NyAyLjk1NWMzLjE0MS0uOTU3IDcuNDQyLTEuNDM5IDEyLjkyLTEuNDM5IDIuNjI1IDAgNS4wNzIuMTM2IDcuMzE1LjM5OCAyLjI1Mi4yNjIgNC4xMDYuNjAxIDUuNTU0IDEuMDE2bS0uNjQzLTcuNDE3Yy0zLjA0LS44MzgtNy4wOTUtMS4yNjItMTIuMTUtMS4yNjItNS4wOTcgMC05LjE5NS40MzItMTIuMzAyIDEuMjg3bC4zNzMgMi41MDZjMy4xMjQtLjgxMyA3LjA5NS0xLjIxOSAxMS45My0xLjIxOSA0LjgwOSAwIDguNzI5LjM5OCAxMS43NTIgMS4xOTRsLjM5OC0yLjUwNm0tMTEuMzYyLTQuMjkzYzIuODQ1LjA1MSA1LjE4Mi4xOTUgNyAuNDIzIDEuODEyLjIyOSAzLjQ1NC41MDggNC45MTEuODIxLjkwNi0uODk4IDEuOTEzLTEuNzQ0IDMuMDItMi41NTcgMS4xMDktLjgxMyAxLjg4OC0xLjUwNyAyLjMzNy0yLjA4My43ODctMS4wNzUgMS4xODUtMi40MTMgMS4xODUtNC4wMiAwLTEuNDY1LS4zNTYtMi43MDEtMS4wNjctMy42OTItMS4yNy0xLjg3MS0zLjIxNy0yLjgwMy01LjgyNS0yLjgwMy0xLjUyNCAwLTMuMTA3LjMzLTQuNzY3Ljk5MS0xLjUwNy41OTMtMi41OTEgMS4yMzYtMy4yNzcgMS45My0xLjQwNSAxLjM2My0yLjQzIDMuMTUtMy4wNzMgNS4zNTktLjI0NS43NjItLjM4MSAxLjcyNy0uNDA2IDIuOTA0LS4wMjUgMS4xNzctLjA0MiAyLjA4My0uMDQyIDIuNzI2bTEuODEyLTEuOTNjMC0uNDgzLjA1OS0xLjE2LjE2MS0yLjA0OS4xMS0uODgxLjI3OS0xLjU3NS41MDgtMi4wNzQuNjE4LTEuMzM4IDEuNDktMi41NzQgMi42MzMtMy43MTcuMzMtLjMzIDEuMDQxLS43NzkgMi4xMzQtMS4zMzggMS4wNzUtLjUzMyAyLjIyNy0uNzk2IDMuNDQ2LS43OTYuOTMxIDAgMS44NDYuMTYxIDIuNzY5LjQ4My45MTQuMzIyIDEuNjA5LjgxMyAyLjA2NiAxLjQ4Mi40MTUuNTU5LjYyNyAxLjQ2NS42MjcgMi43MjYgMCAuOTkxLS40MDYgMS45MTMtMS4yMTkgMi43NzctLjUyNS41NDItMS4xMDEgMS4wOTItMS43MSAxLjY1MS0uNjEuNTUtMS4yMDIgMS4yMDItMS43NjEgMS45NDctLjk1Ny0uMzMtMi4yOTQtLjU5My00LS43Ny0xLjcxLS4xODYtMy41OS0uMjg4LTUuNjQ3LS4zMjIiLz48L3N2Zz4=");
}
.whiteBtn {
    aspect-ratio: 1/1;
    height: 75%;
    background-size: cover;
    background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNzcuMTciIGhlaWdodD0iMTc3LjE3IiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiIgaW1hZ2UtcmVuZGVyaW5nPSJvcHRpbWl6ZVF1YWxpdHkiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiB2aWV3Qm94PSIwIDAgNTAgNTAiPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0iMCIgeDE9IjIxLjM3NiIgeDI9Ijc3LjY0IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iI2ZmZiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iI2ZmZiIgc3RvcC1vcGFjaXR5PSIwIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PGcgZmlsbD0iIzFmMWExNyI+PHBhdGggZD0ibTI1LjgyMSAxMi4wMmgtMS43NjF2LTMuMjUxaC0yLjA2NmMtLjU1OSAwLS44MzgtLjI3MS0uODM4LS44MjF2LS4wMjVjMC0uNTQyLjI3OS0uODEzLjgzOC0uODEzaDIuMDY2di0yLjEwOGMwLS41ODQuMjk2LS44NzIuODg5LS44NzIuNTc2IDAgLjg3Mi4yODguODcyLjg3MnYyLjEwOGgyLjEzNGMuNTQyIDAgLjgxMy4yNzEuODEzLjgxM3YuMDI1YzAgLjU1LS4yNzEuODIxLS44MTMuODIxbC0yLjExNy4wMjUtLjAxNyAzLjIyNiIvPjxwYXRoIGQ9Im0xMS4wMyAzNy43NDRsLS44MTMtNC42NGMtLjAxNyAwLS4wNDItLjAzNC0uMDc2LS4xMDItLjA4NS0uMTE4LS4zMjItLjI3MS0uNzExLS40NTctLjM4MS0uMTk1LS44MzgtLjUxNi0xLjM0Ni0uOTgyLS43MjgtLjYxLTEuMjk1LTEuMTA5LTEuNzAyLTEuNDktLjQwNi0uMzczLS43NzEtLjc4Ny0xLjEwMS0xLjIzNi0xLjAxLTEuMzg5LTEuNTc1LTMuMDY1LTEuNjg1LTUuMDQtLjE2OS0xLjg5Ny42MDEtMy43OTMgMi4zMDMtNS42ODEgMS43MTktMS44OCA0LjA0Ny0yLjc2OSA2Ljk2OC0yLjY1IDEuMDkyLjA2OCAyLjM3OS4zMyAzLjg0NC43OTYuNDgzLjE5NS45NzQuMzkgMS40ODIuNTc2LjUuMTk1Ljk5OS4zODkgMS40OTkuNTg0LjI2Mi4xMzUuNS4yNzEuNjk0LjM5OC0uMDg1LS4zNDctLjEyNy0uNjk0LS4xMjctMS4wNDEgMC0xLjI4Ny40NTctMi4zODggMS4zOC0zLjMwMi45MTQtLjkwNiAyLjAyNC0xLjM3MiAzLjMxMS0xLjM4OSAxLjI4NyAwIDIuMzg4LjQ2NiAzLjMwMiAxLjM4LjkwNi45MTQgMS4zNjMgMi4wMiAxLjM2MyAzLjI4NSAwIC4yNjItLjAzNC42MS0uMTAyIDEuMDQxLjIyOS0uMTQ0LjQ1Ny0uMjcxLjY2OS0uMzcyLjc2Mi0uMzMgMS43NjEtLjcyIDMuMDEtMS4xNiAxLjQyMi0uNDgzIDIuNzAxLS43NTQgMy44NDQtLjgyMSAyLjkyMS0uMTM2IDUuMjQxLjc1NCA2Ljk0MyAyLjY1IDEuNjY4IDEuODg4IDIuNDQ3IDMuNzg1IDIuMzI4IDUuNjgxLS4xMjcgMS45NzMtLjcwMyAzLjY0OS0xLjcxIDUuMDQtLjMzLjQ0OS0uNzAzLjg2NC0xLjExOCAxLjI1My0uNDA2LjM5LS45NjUuODgxLTEuNjYgMS40NzMtLjU0Mi40NjYtMS4wMS43OTYtMS4zODkuOTgyLS4zODEuMTg2LS42MDEuMzQ3LS42NjkuNDU3LS4wMTcuMDM0LS4wMzQuMDU5LS4wNTEuMDc2LS4wMTcuMDE3LS4wMjUuMDM0LS4wMjUuMDUxbC0uNzk2IDQuNjY1IDEuNjQzIDYuMTIxYy0uODMuNzQ1LTIuNjg0IDEuMzU1LTUuNTU0IDEuODM3LTIuODc5LjQ4My02LjIwNi43Mi05Ljk3NC43Mi0zLjgzNSAwLTcuMjE0LS4yNTQtMTAuMTE4LS43NTQtMi45MTItLjUwOC00Ljc0MS0xLjE0My01LjQ4Ni0xLjg5N2wxLjYzNC02LjA1Ii8+PC9nPjxwYXRoIGZpbGw9InVybCgjMCkiIGQ9Im0yNS43OTYgMjkuNTMyYzIuODQ1LjAzNCA1LjQ0NC4yMDMgNy44MDYuNTA4IDIuMzcxLjMwNSA0LjIyNS42OTQgNS41NjMgMS4xNTEuNjI3LS40OTEgMS4zMTItMS4wNDEgMi4wNTctMS42NTEuNzQ1LS42MDEgMS4zNjMtMS4yMTkgMS44NjMtMS44NDYuNzg3LTEuMDEgMS4xODUtMi4zMzcgMS4xODUtMy45OTYgMC0xLjQ4Mi0uMzU2LTIuNzI2LTEuMDY3LTMuNzE3LTEuMjctMS44NTQtMy4yMDktMi43NzctNS44LTIuNzc3LTEuNTU4IDAtMy4xNS4zMjItNC43OTIuOTY1LTEuNDM5LjU4NC0yLjUzMiAxLjIyOC0zLjI2OCAxLjkzOS0xLjM4OSAxLjM4OS0yLjQyMSAzLjE3NS0zLjA4MiA1LjM1MS0uMjI5Ljc3OS0uMzY0IDEuNDktLjQwNiAyLjEyNS0uMDQyLjYzNS0uMDU5IDEuMjg3LS4wNTkgMS45NDdtLTEzLjI1IDYuNjk3YzMuMTQxLS43OTYgNy4zMDctMS4xOTQgMTIuNTA1LTEuMTk0IDUuMDg5IDAgOS4yMDMuMzgxIDEyLjMyNyAxLjE0M2wuNjE4LTMuNjQ5Yy0zLjMyNy0uODcyLTcuNjcxLTEuMzEyLTEzLjA1LTEuMzEyLTUuNDEgMC05Ljc0NS40NDktMTMuMDIgMS4zMzhsLjYxOCAzLjY3NW0yNS4yOTggNC40MTFsLS43MzctMi44NDVjLTMuMjc3LS43MjgtNy4zMzItMS4wOTItMTIuMTU4LTEuMDkyLTQuODA5IDAtOC44NTYuMzY0LTEyLjEzMyAxLjA5MmwtLjc4NyAyLjg3YzMuMTU4LS45MjMgNy40NjgtMS4zODkgMTIuOTQ1LTEuMzg5IDUuNDQ0IDAgOS43MjguNDU3IDEyLjg2OSAxLjM2M20uNjUyIDIuMzM3Yy0zLjE5Mi0xLjI4Ny03LjY3OS0xLjkzOS0xMy40NDUtMS45MzktNS45ODYgMC0xMC41MTYuNjYtMTMuNTk4IDEuOTkgMi45MTMgMS4xNTEgNy40MTcgMS43MzYgMTMuNTIxIDEuNzM2IDIuOTEzIDAgNS41NjMtLjE2MSA3Ljk1OS0uNDgzIDIuNDA0LS4zMjIgNC4yNS0uNzYyIDUuNTYzLTEuMzA0bS0xNC40MTktMTMuNDQ1Yy0uMDA4LS42NDMtLjAzNC0xLjI4Ny0uMDY4LTEuOTIyLS4wMzQtLjYzNS0uMTYxLTEuMzQ2LS4zNzItMi4xMjUtLjY3Ny0yLjIxLTEuNzAyLTMuOTk2LTMuMDgyLTUuMzUxLS43MTEtLjY5NC0xLjc5NS0xLjM0Ni0zLjI2OC0xLjkzOS0xLjY4NS0uNjYtMy4yODUtLjk5MS00Ljc5Mi0uOTkxLTIuNjA4IDAtNC41NDcuOTMxLTUuOCAyLjgwMi0uNzExLjk5MS0xLjA2NyAyLjIzNS0xLjA2NyAzLjcxNyAwIDEuNjI2LjM5OCAyLjk1NSAxLjE4NSAzLjk5Ni40ODMuNjEgMS4wOTIgMS4yMjggMS44MzcgMS44MzcuNzQ1LjYxIDEuNDM5IDEuMTY4IDIuMDgzIDEuNjYgMi44OTYtMS4wNDEgNy4zNDEtMS42IDEzLjM0My0xLjY4NW0uODcyLTQuNjE0Yy4xMTktLjQ2Ni4yMTItLjc4Ny4yOTYtLjk2NS4xNjktLjY0My4zNTYtMS4xOTQuNTc2LTEuNjQzLjA5My0uMjc5LjIzNy0uNjAxLjQzMi0uOTc0LjE4Ni0uMzczLjM4OS0uODA0LjYxLTEuMjc5LjEyNy0uMjc5LjI3MS0uNjI3LjQxNS0xLjAzMy4xNTItLjQwNi4zMDUtLjgwNC40NDktMS4yMDIuMTM1LS4zMy4yMDMtLjY4Ni4yMDMtMS4wNjcgMC0uODEzLS4yOTYtMS40OTktLjg3Mi0yLjA2Ni0uNTc2LS41NzYtMS4yNzktLjg2NC0yLjEwOC0uODY0LTEuOTY0IDAtMi45NTUuOTkxLTIuOTU1IDIuOTU1IDAgLjM4MS4wNjguNzM3LjIwMyAxLjA2Ny4zNjQgMS4wNzUuNjQzIDEuODIuODM4IDIuMjM1LjIyLjQ3NC40MTUuOTA2LjYwMSAxLjI3OS4xNzguMzcyLjMzOS42OTQuNDY2Ljk3NC4yMi41NS4zOTggMS4wOTIuNTUgMS42NDMuMDM0LjA5My4xMjcuNDE1LjI5Ni45NCIvPjwvc3ZnPg==");
}

.v-btn:not(.v-btn--round).v-size--default {
    height: auto;
}
</style>