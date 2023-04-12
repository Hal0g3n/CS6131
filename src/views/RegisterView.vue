<template>
    <v-container fill-width fill-height class='register-page'>
        <v-row align="center" justify="center">
            <v-col xs="12" sm="10" md="8">
                
                <v-card elevation=12 shaped class='pb-4'>
                    <v-toolbar dark color="primary" class='my-4'>
                        <!-- LOGO -->
                        <v-spacer/>
                        <h1>Join Now!</h1>
                        <v-spacer/>
                    </v-toolbar>

                    <v-card-text class='pa-5'>
                        <v-form>
                            <v-text-field
                                v-model="username"
                                outlined
                                clearable
                                prepend-inner-icon="mdi-account-circle"
                                
                                :rules="[username != '' || 'This field is required']"

                                name="username"
                                label="Username"
                                type="text"
                            ></v-text-field>
                            <v-text-field
                                id="password"
                                v-model="password"
                                name="password"
                                label="Password"
                                outlined
                                prepend-inner-icon="mdi-lock"
                                :append-icon="
                                    showPw1 ? 'mdi-eye' : 'mdi-eye-off'
                                "
                                :type="showPw1 ? 'text' : 'password'"
                                @click:append="showPw1 = !showPw1"
                                class="input-group--focused"
                            ></v-text-field>

                            <v-text-field
                                v-model="confirmPassword"
                                name="password"
                                label="Confirm Password"
                                outlined
                                prepend-inner-icon="mdi-lock"
                                
                                :rules="[confirmPassword == password || 'Password do not match']"
                                hide-details="auto"

                                :append-icon="showPw2 ? 'mdi-eye' : 'mdi-eye-off'"
                                :type="showPw2 ? 'text' : 'password'"
                                @click:append="showPw2 = !showPw2"
                                class="input-group--focused"
                            ></v-text-field>
                        </v-form>
                    </v-card-text>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" @click="register" class='px-5'
                            >Register</v-btn
                        >
                    </v-card-actions>

                    <br>
                    <h3 align=center>
                        Got an account? <router-link to="/login">Log in now!</router-link>
                    </h3>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from "axios";

export default {
    name: "App",
    data() {
        return {
            username: "",
            password: "",
            confirmPassword: "",
            showPw1: false,
            showPw2: false,
        };
    },
    methods: {
        async register() {
            if (this.username == "" || this.password == "" || this.confirmPassword == "") {
                alert("Missing Values: Please fill in all fields");
                return;
            }

            if (this.password != this.confirmPassword) {
                alert("Mismatch Password: Check your passwords");
                return;
            }
            
            // If register Player was successful
            if (await this.$store.dispatch("registerPlayer", {
                username: this.username,
                password: this.password,
            })) this.$router.push("/login"); // Go to logi
            else {
                // State the error
                this.$notify({
                    type: "error",
                    title: 'Registration Failed',
                    text: 'Error connecting to !'
                });
            }
        },
    },
};
</script>