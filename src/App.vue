<template>
    <v-app>
        <!-- Navigation Drawer! -->
        <v-navigation-drawer
            :permanent="$vuetify.breakpoint.lgAndUp"
            :mini-variant.sync="mini"
            width="10%"
            expand-on-hover
            v-model="drawerShown"
            app
        >
            <!-- Logo?? -->
            <v-list-item-title
                v-if="mini"
                style="font-size: 2em; text-align: center"
                ><v-icon>mdi-chess-queen</v-icon></v-list-item-title
            >
            <v-list-item-title v-else style="font-size: 2em; text-align: center"
                >Chessible</v-list-item-title
            >

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
                            <v-list-item-title>
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
                        @click="$vuetify.theme.dark = !$vuetify.theme.dark"
                        color="primary"
                    >
                        <v-list-item-icon>
                            <v-icon> mdi-theme-light-dark </v-icon>
                        </v-list-item-icon>

                        <v-list-item-content color="primary">
                            <v-list-item-title> Theme </v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>

                <!-- Login / Logout Button -->
                <div class="px-2">
                    <v-btn
                        color="primary"
                        @click="login()"
                        v-if="!loggedIn"
                        block
                        class="my-1 together"
                        >
                        <v-icon>mdi-logout-variant</v-icon>
                        <v-spacer/>
                        <div v-if="!mini">Sign Up</div></v-btn
                    >
                    <v-btn
                        color="primary"
                        @click="login()"
                        v-if="!loggedIn"
                        block
                        class="together"
                        >
                        
                        <v-icon>mdi-logout-variant</v-icon>
                        <v-spacer/>
                        <div v-if="!mini">Log in</div>
                        </v-btn
                    >

                    <v-btn
                        color="primary"
                        @click="logout()"
                        v-else
                        block
                        class="together"
                    >
                        <v-icon>mdi-logout-variant</v-icon>
                        <v-spacer/>
                        <div v-if="!mini">Logout</div>
                    </v-btn>
                </div>
            </template>
        </v-navigation-drawer>

        <v-app-bar
            v-if="$vuetify.breakpoint.mdAndDown"
            app
            color="primary"
            dark
            elevate-on-scroll
        >
            <v-app-bar-nav-icon
                v-if="loggedIn"
                @click="drawerShown = !drawerShown"
            ></v-app-bar-nav-icon>

            <!-- Above is right -->
            <v-spacer></v-spacer>

            <!-- Dark Mode Toggle -->
            <!-- TODO: Make it look better -->
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
            <v-container fluid>
                <router-view></router-view>
            </v-container>
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
        hideSubtitle: false,
        routes: [
            { name: "Play", icon: "mdi-chess-king", path: "/play" },
            { name: "Puzzles", icon: "mdi-checkerboard", path: "/puzzles" },
            { name: "Profile", icon: "mdi-account-circle", path: "/profile" },
            { name: "Friends", icon: "mdi-account-multiple", path: "/friends" },
            {
                name: "Rankings",
                icon: "mdi-chart-box-outline",
                path: "/ranking",
            },
            { name: "Feedback", icon: "mdi-comment-quote", path: "/feedback" },
        ],
    }),

    methods: {
        login() {
            this.loggedIn = true;
        },

        logout() {
            this.loggedIn = false;
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

.together{
    padding: 0px 1px
}
</style>

<style scoped>
/* Navigation Drawer */
.list:hover {
    background: var(--v-primary-base);
}
.list:active {
    background: var(--v-secondary-base);
}
</style>  