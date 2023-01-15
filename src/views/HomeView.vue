<template>
    <div class="home">
        <section>
            <v-parallax src="../assets/bg.png" style="height: 70vh">
                <v-layout
                    column
                    align-center
                    justify-center
                    class="white--text"
                >
                    <h1
                        class="white--text mb-5 text-h3"
                        style="font-weight: 900; text-shadow: 3px 2px #000000; text-align: center"
                    >
                        Chess is doable, with <u>Chessible</u>
                    </h1>
                    <div
                        class="white--text text-h5 ma-3"
                        style="font-weight: 900; text-shadow: 2px 2px #000000; text-align: center"
                    >
                        Mastering Chess has never been easier
                    </div>
                </v-layout>
            </v-parallax>
        </section>

        <div >
            <div style="text-align: center">
                <p class='text-h4 mt-10'>
                    One of the ways to train your chess
                </p>
                <span>
                    No paywalls, all for <b>FREE</b>
                </span>
            </div>

            <v-container style="max-width: 75%" class="my-10">
                <v-row align="center">
                    <v-col :xs="12" :md="4">
                        <v-card class="elevation-1 transparent pa-5">
                            <v-card-text style="text-align:center">
                                <v-icon
                                    x-large
                                    class="blue--text text--lighten-2"
                                    >mdi-earth</v-icon
                                >
                            </v-card-text>
                            <v-card-title
                                primary-title
                                class="layout justify-center"
                            >
                                <div class="headline text-xs-center">
                                    Play the world
                                </div>
                            </v-card-title>
                            <v-card-text style="text-align:center">
                                Play, Learn and Compete with chess
                                enthusiasts all around the world!
                            </v-card-text>
                        </v-card>
                    </v-col>
                    <v-col :xs="12" :md="4">
                        <v-card class="elevation-1 transparent pa-5">
                            <v-card-text style="text-align:center">
                                <v-icon
                                    x-large
                                    class="blue--text text--lighten-2"
                                    >mdi-flash</v-icon
                                >
                            </v-card-text>
                            <v-card-title
                                primary-title
                                class="layout justify-center"
                            >
                                <div class="headline text-xs-center">
                                    Learn Fast
                                </div>
                            </v-card-title>
                            <v-card-text style="text-align:center">
                                With our massive puzzle database, 
                                you can train for as long as you want!
                            </v-card-text>
                        </v-card>
                    </v-col>
                    <v-col :xs="12" :md="4">
                        <v-card class="elevation-1 transparent pa-5">
                            <v-card-text style="text-align:center">
                                <v-icon
                                    x-large
                                    class="blue--text text--lighten-2"
                                    >mdi-checkerboard</v-icon
                                >
                            </v-card-text>
                            <v-card-title
                                primary-title
                                class="layout justify-center"
                            >
                                <div class="headline text-xs-center">
                                    Love Chess
                                </div>
                            </v-card-title>
                            <v-card-text style="text-align:center">
                                Reignite your long lost passion for chess.
                                Chess has never been more fun!
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </div>
       
        <section>
            <v-parallax src="../assets/bg.png" style="height:30vh">
                <v-layout column align-center justify-center>
                    <div class="text-h3 white--text mb-3 text-xs-center">
                        What are you waiting for, join Chessible <u>NOW</u>!
                    </div>
                    
                    <router-link to="/register" style="text-decoration: none">
                        <v-btn
                            class="mt-3 mb-10 text-h6"
                            elevation=12
                            dark
                            large
                        >
                            SIGN UP!
                        </v-btn>
                    </router-link>

                </v-layout>
            </v-parallax>
        </section>

        <v-toolbar dark color="primary darken-1" style="text-justify: center">
            <div style="text-align: center; width: 100%">
                Made with
                <v-icon class="red--text">mdi-heart</v-icon>
                using
                <a
                    class="white--text"
                    href="https://vuetifyjs.com"
                    target="_blank"
                    >Vuetify</a
                >
            </div>
        </v-toolbar>
    </div>
</template>

<script>
export default {
    name: "Home"
};
</script>
