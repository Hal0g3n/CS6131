import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'
import axios from "axios"

Vue.use(Vuex)

let server = "http://chessible.pythonanywhere.com"

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
        updateCurPlayer(state, curPlayer) {
            state.curPlayer = curPlayer;
        },
        
        updateToken(state, access_token) {
            state.access_token = access_token
        }
    },
    getters: {
        loggedIn(state) {
            return state.access_token != "";
        },

        getTeams: (state) => async (query = "") => {
            
            let response;
            if (state.access_token == "")
                response = await axios.get(
                    server + `/teams${query ? `?q=${query}` : ''}`,
                )
            else
                response = await axios.get(
                    server + `/teams${query ? `?q=${query}` : ''}`,
                    { headers: { "Authorization": `Bearer ${state.access_token}` } }
                )

            return response.data;
        },

        getTeam: (state) => async (id: number) => {
            console.log(id)

            let response;
            if (state.access_token == "")
                response = await axios.get(
                    server + `/teams/${id}`,
                )
            else
                response = await axios.get(
                    server + `/teams/${id}`,
                    { headers: { "Authorization": `Bearer ${state.access_token}` } }
                )
            return response.data;
        },

        getGame: (state) => async (id = "") => {
            let response = await axios.get(
                server + `/games/${id}`,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            return response.data
        },

        getGames: (state) => async (username = "") => {
            let response = await axios.get(
                server + `/games/player/${username}`,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            return response.data
        },

        getPlayer: (state) => async (username: string) => {
            let response;
            if (state.access_token == "")
                response = await axios.get(
                    server + `/player/${username}`,
                )
            else
                response = await axios.get(
                    server + `/player/${username}`,
                    { headers: { "Authorization": `Bearer ${state.access_token}` } }
                )

            return response.data;
        },

        getPlayers: (state) => async () => {
            let response = await axios.get(server + `/player/search`)
            return response.data;
        },

        getApplications: (state) => async (id: string) => {
            let response = await axios.get(
                server + `/apply/team/${id}`,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            
            return response.data
        },

        getUserApplications: (state) => async () => {
            let response = await axios.get(
                server + `/apply/user/${state.curPlayer.username}`,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            
            return response.data
        },

        getCurPlayer: (state) => state.curPlayer,
        
    },
    actions: {
        async kick({ state }, { username, team_id }) {
            console.log(username, team_id)
            const formData = new FormData()
            formData.append('username', username)
            formData.append('team_id', team_id)

            let res = await axios.post(
                server + '/teams/kick', 
                formData,                 
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )

            return res.status == 200
        },

        async makeMod({ state }, { username, team_id }) {
            const formData = new FormData()
            formData.append('username', username)
            formData.append('team_id', team_id)

            let res = await axios.post(
                server + '/teams/promoMod', 
                formData,                 
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )

            return res.status == 200
        },

        async loginPlayer({ commit, getters }, { username, password }) {
            const formData = new FormData()
            formData.append('username', username)
            formData.append('password', password)

            let res = await axios.post(server + '/player/login', formData, {})

            if ('access_token' in res.data) {
                commit("updateToken", res.data['access_token']);
                commit("updateCurPlayer", await getters.getPlayer(username));
                return true;
            }

        },

        async logoutPlayer({ commit }) {
            commit("updateCurPlayer", {});
            commit("updateToken", "");
            return true;
        },

        async makeApplication({ state }, { team_id, message }) {
            console.log(team_id, message)
            const formData = new FormData();
            formData.append('message', message);

            let response = await axios.post(
                server + `/apply/team/${team_id}`,
                formData,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )

            if (response.status === 200) return true;
            else return false;
        },

        async approveApplication({ state }, { team_id, applicant }) {
            try {
                const formData = new FormData();
                formData.append('team_id', team_id);
                formData.append('applicant', applicant);

                let response = await axios.post(
                    server + `/apply/approve`,
                    formData,
                    { headers: { "Authorization": `Bearer ${state.access_token}` } }
                )

                if (response.status == 200) return true;
                return false;
            }
            catch (error) {return false;}
        },

        async rejectApplication({ state }, { id, team_id, applicant }) {
            try {
                const formData = new FormData();
                formData.append('id', id);
                formData.append('team_id', team_id);
                if (applicant) formData.append('applicant', applicant);

                let response = await axios.post(
                    server + `/apply/delete`,
                    formData,
                    { headers: { "Authorization": `Bearer ${state.access_token}` } }
                )

                if (response.status == 200) return true;
                return false;
            }
            catch (error) {return false;}
        },

        async createTeam({state, getters, commit}, team_name) {
            const formData = new FormData();
            formData.append('team_name', team_name);
            
            let response = await axios.post(
                server + `/teams/create`,
                formData,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            
            // Update Player Information
            commit("updateCurPlayer", await getters.getPlayer(state.curPlayer.username))
            return response.data;
        },
        
        async updateProfile({state, commit, getters}, {username, about}) {
            const formData = new FormData();
            formData.append('about', about);
            
            let response = await axios.post(
                server + `/player/update`,
                formData,
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            
            // Update Player Information (Already updated due to v-model)
            commit("updateCurPlayer", await getters.getPlayer(state.curPlayer.username))

            return true;
        },

        async quitTeamMod({state, commit, getters}, ) {
            let response = await axios.post(
                server + `/teams/quitMod`,
                {},
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            
            // Update Player Information
            commit("updateCurPlayer", await getters.getPlayer(state.curPlayer.username))

            return true;
        },
        
        async quitTeam({state, commit, getters}, ) {
            console.log(state.access_token)
            let response = await axios.post(
                server + `/teams/quitTeam`,
                {},
                { headers: { "Authorization": `Bearer ${state.access_token}` } }
            )
            
            // Update Player Information
            commit("updateCurPlayer", await getters.getPlayer(state.curPlayer.username))
            return true;
        }
    },
        modules: {},
        
        plugins: [new VuexPersistence({ storage: window.localStorage, reducer: (state: any) => ({
        curPlayer: state.curPlayer,
        access_token: state.access_token
    }) }).plugin],
})
