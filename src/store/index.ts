import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'
import axios from "axios"

Vue.use(Vuex)
let server = "http://localhost:5000"

export default new Vuex.Store({
    state: {
        curPlayer: {
            about_me: "",
            avatar: null,
            birthday: "",
            create_date: "",
            email: "",
            join_date: "",
            mod_start_date: "",
            password: "",
            puzzle_history: [],
            rating_history: [],
            team_id: null,
            username: ""
        },
        access_token: ""
    },
    mutations: {
        updateCurPlayer(state, { curPlayer, token }) {
            state.curPlayer = curPlayer;
            state.access_token = token
        }
    },
    getters: {
        loggedIn(state) {
            return state.access_token != "";
        },

        getTeams: (state) => async (query = "") => {
            let response = await axios.get(
                server + `/teams${query ? `?q=${query}` : ''}`,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            return response.data;
        },

        getTeam: (state) => async (id: number) => {
            let response = await axios.get(
                server + `/teams/${id}`,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            return response.data;
        },

        getGame: (state) => async (id = "") => {
            let response = await axios.get(
                server + `/teams/${id}`,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            return response
        },

        getPlayer: (state) => async (username: string) => {
            let response = await axios.get(
                server + `/player/${username}`,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )

            return response.data
        },

        getApplications: (state) => async (id: string) => {
            let response = await axios.get(
                server + `/apply/${id}`,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            
            return response.data
        },

        getCurPlayer: (state) => state.curPlayer,
        
    },
    actions: {
        async loginPlayer({ commit, getters }, { username, password }) {
            const formData = new FormData()
            formData.append('username', username)
            formData.append('password', password)

            let res = await axios.post(server + '/player/login', formData, {})

            if ('access_token' in res.data) {
                commit("updateCurPlayer", { curPlayer: {}, token: res.data['access_token'] });
                commit("updateCurPlayer", { curPlayer: await getters.getPlayer(username), token: res.data['access_token'] });
                return true;
            }

        },

        async logoutPlayer({ commit }) {
            commit("updateCurPlayer", { curPlayer: {}, token: '' });
            return true;
        },

        async makeApplication({ state }, { team_id, message }) {
            const formData = new FormData();
            formData.append('message', message);

            let response = await axios.post(
                server + `/apply/${team_id}`,
                formData,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
        },

        quitTeam() {

        }
    },
    modules: {},

    plugins: [new VuexPersistence({ storage: window.localStorage, reducer: (state: any) => ({
        curPlayer: state.curPlayer,
        access_token: state.access_token
    }) }).plugin],
})
