<template>
    <v-app>
        <!-- Navigation Drawer! -->
        <v-navigation-drawer
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
                    <v-icon v-if="mini"><v-img aspect-ratio="1" height="100%" src="./assets/logo.png"/></v-icon>
                    <v-list-item-title
                        v-else
                        style="font-size: 2rem; text-align: center"
                    >
                        <v-img src="./assets/logoLong.png"/>
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
                    
                    <!-- Login Button -->
                    <v-list-item
                        class="list_bot"
                        @click="$router.push('/login')"
                        color="primary"
                        v-if="!loggedIn"
                    >
                        <v-list-item-icon>
                            <v-icon>mdi-login-variant</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content color="primary">
                            <v-list-item-title class='text-button'> Log In </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    
                    <!-- Logout Button -->
                    <v-list-item
                        v-else
                        class="list_bot"
                        @click="loggedIn = false; $router.push('/')"
                        color="primary"
                    >
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
        <v-app-bar
            v-if="$vuetify.breakpoint.mdAndDown && !($route.name in ['login', 'register'])"
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
        mini: true,
        routes: [
            { name: "Play",       icon: "mdi-chess-king",        path: "/play",       showOnLogin: true},
            { name: "Puzzles",    icon: "mdi-puzzle",            path: "/puzzles",    showOnLogin: true},
            { name: "Profile",    icon: "mdi-account-circle",    path: "/profile",    showOnLogin: false},
            { name: "Teams",      icon: "mdi-account-multiple",  path: "/teams",      showOnLogin: true},
            { name: "Rankings",   icon: "mdi-chart-box-outline", path: "/ranking",    showOnLogin: true},
            { name: "Feedback",   icon: "mdi-comment-quote",     path: "/feedback",   showOnLogin: true},
            { name: "Tournament", icon: "mdi-comment-quote",     path: "/tournament", showOnLogin: true},
            // TODO: Fix up puzzles in the future
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
    background: var(--v-primary-base);
}
.list_bot:hover {
    background: var(--v-primary-lighten4);
}
.list_bot:active {
    background: var(--v-secondary-base);
}
</style>  