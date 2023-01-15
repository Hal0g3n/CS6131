<template>
    <v-app>
        <!-- Navigation Drawer! -->
        <v-navigation-drawer
            v-if="loggedIn"
            :permanent="$vuetify.breakpoint.lgAndUp"
            :expand-on-hover="$vuetify.breakpoint.lgAndUp"
            :mini-variant.sync="mini"
            width="13rem"
            v-model="drawerShown"
            app
        >
            <!-- Logo?? -->
            <v-list-item-title style="font-size: 2rem; text-align: center">
                <router-link
                    to="/"
                    @click="drawerShown = false"
                    style="text-decoration: none; color: inherit"
                    key="home"
                >
                    <v-icon v-if="mini">mdi-chess-queen</v-icon>
                    <v-list-item-title
                        v-else
                        style="font-size: 2rem; text-align: center"
                    >
                        Chessible
                    </v-list-item-title>
                </router-link>
            </v-list-item-title>

            <v-divider></v-divider>

            <!-- List of Links -->
            <v-list dense nav>
                <router-link
                    v-for="item in routes"
                    :to="item.path"
                    @click="drawerShown = false"
                    style="text-decoration: none; color: inherit"
                    :key="item.name"
                >
                    <v-list-item class="list" link>
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
                    <v-list-item
                        class="list"
                        @click="$vuetify.theme.dark = !$vuetify.theme.dark"
                        color="primary"
                    >
                        <v-list-item-icon>
                            <v-icon> mdi-theme-light-dark </v-icon>
                        </v-list-item-icon>

                        <v-list-item-content color="primary">
                            <v-list-item-title class='text-button'> Theme </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    
                    <v-list-item
                        class="list_bot"
                        @click="loggedIn = false; $router.push('/')"
                        color="primary"
                    >
                        <v-list-item-icon>
                            <v-icon>mdi-logout-variant</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content color="primary">
                            <v-list-item-title dark class='text-button'> logout </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>

                <!-- Login / Logout Button -->
                <div class="px-2">
                    <v-btn
                        color="primary"
                        @click="$router.push('/CS6131/register')"
                        v-if="!loggedIn"
                        block
                        class="my-1 together"
                    >
                        <v-icon>mdi-logout-variant</v-icon>
                        <v-spacer />
                        <div v-if="!mini">Sign Up</div></v-btn
                    >
                    <v-btn
                        color="primary"
                        @click="$router.push('/CS6131/login')"
                        v-if="!loggedIn"
                        block
                        class="my-1 together"
                    >
                        <v-icon>mdi-logout-variant</v-icon>
                        <v-spacer />
                        <div v-if="!mini">Log in</div>
                    </v-btn>
                </div>

            </template>
        </v-navigation-drawer>

        <v-app-bar
            v-if="loggedIn && $vuetify.breakpoint.mdAndDown && !($route.name in ['login', 'register'])"
            app
            color="primary"
            dark
            elevate-on-scroll
        >
            <v-app-bar-nav-icon
                @click="drawerShown = !drawerShown"
            ></v-app-bar-nav-icon>

            <h1>Chessible</h1>

            <!-- Above is Left -->
            <v-spacer></v-spacer>

            <v-btn
                @click="$vuetify.theme.dark = !$vuetify.theme.dark"
                label="Toggle Dark Mode"
                text
                icon
            >
                <v-icon v-if="$vuetify.theme.dark"> mdi-weather-night</v-icon>
                <v-icon v-else dark> mdi-white-balance-sunny </v-icon>
            </v-btn>
        </v-app-bar>

        <!-- Router View -->
        <v-main>
            <router-view @login="loggedIn = true"></router-view>
        </v-main>
    </v-app>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
    name: "App",

    data: () => ({
        loggedIn: false,
        drawerShown: false,
        mini: false,
        hideSubtitle: false,
        routes: [
            { name: "Play", icon: "mdi-chess-king", path: "/play" },
            // TODO: Fix up puzzles in the future
            // { name: "Puzzles", icon: "mdi-puzzle", path: "/puzzles" },
            { name: "Profile", icon: "mdi-account-circle", path: "/profile" },
            // { name: "Friends", icon: "mdi-account-multiple", path: "/friends" },
            {
                name: "Rankings",
                icon: "mdi-chart-box-outline",
                path: "/ranking",
            },
            { name: "Feedback", icon: "mdi-comment-quote", path: "/feedback" },
        ],
    }),

    mounted() {
        console.log(this.$route.name);
        this.onResize();
        window.addEventListener("resize", this.onResize, { passive: true });
    },

    methods: {
        onResize() {
            if (this.$vuetify.breakpoint.mdAndDown) this.mini = false;
        },
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
.list_bot{
    background: var(--v-primary-lighten1);
}
.list_bot:hover {
    background: var(--v-primary-lighten4);
}
.list_bot:active {
    background: var(--v-secondary-base);
}
</style>  