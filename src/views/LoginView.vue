<template>
    <v-container fill-width fill-height class='login-page'>
        <v-row align="center" justify="center">
            <v-col xs="12" sm="10" md="8">
                
                <v-card elevation=12 shaped class='pb-4'>
                    <v-toolbar dark color="primary" class='my-4'>
                        <!-- LOGO -->
                        <v-spacer/>
                        <h1>Welcome</h1>
                        <v-spacer/>
                    </v-toolbar>

                    <v-card-text class='pa-4'>
                        <v-form>
                            <v-text-field
                                id="username"
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
                                    showPw ? 'mdi-eye' : 'mdi-eye-off'
                                "
                                :type="showPw ? 'text' : 'password'"
                                @click:append="showPw = !showPw"
                                class="input-group--focused"
                            ></v-text-field>
                        </v-form>
                    </v-card-text>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" @click="login" class='px-5'
                            >Login</v-btn
                        >
                    </v-card-actions>
                    <br>
                    <h3 align=center>
                        New here? <router-link to="/register">Sign up now!</router-link>
                    </h3>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
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
            this.$router.push("/profile");
            this.$emit("login");
        }
    }
};
</script>

<style></style>
