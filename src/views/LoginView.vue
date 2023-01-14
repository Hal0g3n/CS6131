<template>
    <div class="login-page">
        <v-content>
            <v-container fill-height>
                <v-row align="center" justify="center">
                    <v-col xs="12" sm="10" md="8">
                        
                        <v-card elevation=12 class='pa-5'>
                            <v-toolbar dark color="primary">
                                <!-- LOGO -->
                                <v-spacer/>
                                <h1>Welcome</h1>
                                <v-spacer/>
                            </v-toolbar>

                            <v-card-text>
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
                            </v-form>
                            </v-card-text>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="primary" @click="register" class='px-5'
                                    >Login</v-btn
                                >
                            </v-card-actions>
                            <br>
                            <h3 align=center>
                                New here? <a href="/register">Sign up now!</a>
                            </h3>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-content>
    </div>
</template>

<script>
export default {
    name: "Login",
    data: () => ({
        source: String,
        username: "",
        password: "",
        showPw: false
    }),
    methods: {
        login() {
            this.$router.push("/");
        }
    }
};
</script>

<style></style>
