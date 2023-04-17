<template>
    <v-app>
        <!-- Navigation Drawer! -->
        <v-navigation-drawer :permanent="$vuetify.breakpoint.lgAndUp" :expand-on-hover="$vuetify.breakpoint.lgAndUp"
            :mini-variant.sync="mini" width="13rem" v-model="drawerShown" app>
            <!-- Logo?? -->
            <v-list-item-title style="font-size: 2rem; text-align: center">
                <router-link to="/" @click="drawerShown = false" style="text-decoration: none; color: inherit" key="home">
                    <v-icon v-if="mini"><v-img aspect-ratio="1" height="100%" src="./assets/logo.png" /></v-icon>
                    <v-list-item-title v-else style="font-size: 2rem; text-align: center">
                        <v-img src="./assets/logoLong.png" />
                    </v-list-item-title>
                </router-link>
            </v-list-item-title>

            <v-divider></v-divider>

            <!-- List of Links -->
            <v-list dense nav>
                <router-link v-for="item in routes" :to="item.path" @click="drawerShown = false"
                    style="text-decoration: none; color: inherit" :key="item.name">
                    <v-list-item v-if="item.showOnLogin || loggedIn" class="list" link>
                        <v-list-item-icon>
                            <v-icon>{{ item.icon }}</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content>
                            <v-list-item-title class='text-button'>
                                {{ item.name }}
                            </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </router-link>
            </v-list>

            <!-- Bottom Part -->
            <template v-slot:append>
                <v-divider></v-divider>

                <!-- Dark Mode Toggle -->
                <v-list dense nav>
                    <v-list-item class="list" @click="$vuetify.theme.dark = !$vuetify.theme.dark" color="primary">
                        <v-list-item-icon>
                            <v-icon> mdi-theme-light-dark </v-icon>
                        </v-list-item-icon>

                        <v-list-item-content color="primary">
                            <v-list-item-title class='text-button'> Theme </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>

                    <!-- Profile Button -->
                    <v-list-item v-if="loggedIn" class="list" @click="$router.push('/player/' + curPlayer.username)"  color="primary">
                        <v-list-item-icon>
                            <v-icon>mdi-account-box-outline</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-title class='text-button'> My Profile </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>

                    <!-- Login Button --> 
                    <v-list-item class="list_bot" @click="$router.push('/login')" color="primary" v-if="!loggedIn">
                        <v-list-item-icon>
                            <v-icon>mdi-login-variant</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content color="primary">
                            <v-list-item-title class='text-button'> Log In </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>

                    <!-- Logout Button -->
                    <v-list-item v-else class="list_bot" @click="$store.dispatch('logoutPlayer'); $router.push('/')" color="primary">
                        <v-list-item-icon>
                            <v-icon>mdi-logout-variant</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content color="primary">
                            <v-list-item-title class='text-button'> Logout </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>

            </template>
        </v-navigation-drawer>
        <v-app-bar v-if="$vuetify.breakpoint.mdAndDown && !($route.name in ['login', 'register'])" app color="primary" dark
            elevate-on-scroll>
            <v-app-bar-nav-icon @click="drawerShown = !drawerShown"></v-app-bar-nav-icon>

            <h1>Chessible</h1>

            <!-- Above is Left -->
            <v-spacer></v-spacer>

            <v-btn @click="$vuetify.theme.dark = !$vuetify.theme.dark" label="Toggle Dark Mode" text icon>
                <v-icon v-if="$vuetify.theme.dark"> mdi-weather-night</v-icon>
                <v-icon v-else dark> mdi-white-balance-sunny </v-icon>
            </v-btn>
        </v-app-bar>

        <!-- Router View -->
        <v-main>
            <router-view></router-view>
        </v-main>

        <!-- Notification -->
        <notifications position="bottom right" classes="my-style" animation-name="v-fade-left" :max="3" width="min(30%, 500px)">

            <template slot="body" slot-scope="props">
                <div class="custom-template">
                    <div class="custom-template-icon">
                        <i class="icon ion-android-checkmark-circle"></i>
                    </div>
                    <div class="custom-template-content">
                        <div class="custom-template-title">
                            {{ props.item.title }}
                        </div>
                        <div class="custom-template-text" v-html="props.item.text"></div>
                    </div>
                    <div class="custom-template-close" @click="props.close">
                        <i class="icon ion-android-close"></i>
                    </div>
                </div>
            </template>
        </notifications>
    </v-app>
</template>

<script>
import Vue from "vue";
import { mapGetters } from 'vuex';

export default Vue.extend({
    name: "App",

    data: () => ({
        drawerShown: false,
        mini: true,
        routes: [
            { name: "Play", icon: "mdi-chess-king", path: "/play", showOnLogin: true },
            { name: "Puzzles", icon: "mdi-puzzle", path: "/puzzles", showOnLogin: true },
            { name: "Players", icon: "mdi-account-circle", path: "/player", showOnLogin: false },
            { name: "Teams", icon: "mdi-account-multiple", path: "/teams", showOnLogin: true },
            { name: "Rankings", icon: "mdi-chart-box-outline", path: "/ranking", showOnLogin: true },
            { name: "Tournaments", icon: "mdi-trophy", path: "/tournament", showOnLogin: true },
            // { name: "Feedback", icon: "mdi-comment-quote", path: "/feedback", showOnLogin: true },
            // TODO: Fix up puzzles in the future
        ],
    }),

    mounted() {
        this.onResize();
        window.addEventListener("resize", this.onResize, { passive: true });
    },

    methods: {
        onResize() {
            if (this.$vuetify.breakpoint.mdAndDown) this.mini = false;
        },
    },

    computed: {
        ...mapGetters({
            loggedIn: "loggedIn",
            curPlayer: "getCurPlayer"
        }),
    },
});
</script>

<style>
#app .white {
    background-color: transparent !important;
}

#app .black {
    background-color: transparent !important;
}

#app .blue {
    background-color: transparent !important;
}

.together {
    padding: 0px 1px;
}

.my-style {
    padding: 0px;
    margin: 0 5px 5px;
    font-size: 12px;
    color: #ffffff;
    background: #44A4FC !important;
    border-left: 5px solid #187FE7;
}
</style>

<style lang="scss">
@import "./assets/stylesheets/notify.scss"
</style>

<style scoped>
/* Navigation Drawer */
.list:hover {
    background: var(--v-primary-lighten4);
}

.list:active {
    background: var(--v-secondary-base);
}


/* Navigation Drawer Bottom */
.list_bot {
    background: var(--v-primary-base);
}

.list_bot:hover {
    background: var(--v-primary-lighten4);
}

.list_bot:active {
    background: var(--v-secondary-base);
}

.v-card__text {
    font-size: 1rem;
}
</style>  