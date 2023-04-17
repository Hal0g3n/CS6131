<template>
    <v-container fill-width fill-height class="register-page">
        <v-row align="center" justify="center">
            <v-col xs="12" sm="10" md="8">
                <v-card elevation="12" class="pb-4 rounded-xl">
                    <v-toolbar dark color="primary" class="my-4">
                        <!-- LOGO -->
                        <v-spacer />
                        <h1>Contact Us!</h1>
                        <v-spacer />
                    </v-toolbar>

                    <v-card-text class="pa-5">
                        <v-form>
                            <v-text-field
                                v-model="name"
                                outlined
                                clearable
                                prepend-inner-icon="mdi-account-circle"
                                :rules="[
                                    name != '' || 'This field is required',
                                ]"
                                name="name"
                                label="Name"
                                type="text"
                                class="input-group--focused"
                            ></v-text-field>

                            <v-text-field
                                v-model="email"
                                outlined
                                clearable
                                prepend-inner-icon="mdi-email"
                                :rules="[(v) =>!v || /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid']"

                                name="email"
                                label="Email"
                                type="text"
                                class="input-group--focused"
                            ></v-text-field>

                            <v-textarea
                                v-model="content"
                                name="content"
                                label="What do you want to tell us?"

                                clearable
                                counter
                                auto-grow
                                outlined
                                class="input-group--focused"
                            ></v-textarea>
                        </v-form>
                    </v-card-text>

                    <v-card-actions class="mx-5">
                        <v-spacer></v-spacer>
                        <v-btn color="primary" @click="feedback" class="px-5"
                            >Submit</v-btn
                        >
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: "App",
    data() {
        return {
            name: "",
            email: "",
            content: "",
        };
    },
    methods: {
        feedback() {},
    },
};
</script>