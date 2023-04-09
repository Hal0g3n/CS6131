import Vue from 'vue'
import Vuex, { Store } from 'vuex'
import axios from "axios"

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        curPlayer: {
            username: "",
            access_token: "",
        }
    },
    mutations: {
        updateCurPlayer(state, {username, token}) {
            state.curPlayer.username = username;
            state.curPlayer.access_token = token
        }
    },
    getters: {
        loggedIn(state) {return state.curPlayer.access_token != "";},
        
        getTeam: (state) => async (query = "") => {
            let response = await axios.get(
                `http://chessible.pythonanywhere.com/teams${query ? `?q=${query}` : ''}`,
                { headers: { "Authorisation": `Bearer ${state.curPlayer.access_token}` } }
            )
            return response.data;
        }
    },
    actions: {
        async loginPlayer({ commit }, { username, password }) {
            const formData = new FormData()
            formData.append('username', username)
            formData.append('password', password)

            let res = await axios.post('http://chessible.pythonanywhere.com/login', formData, {})
            console.log(res)

            if ('access_token' in res.data) {
                commit("updateCurPlayer", {username: username, token: res.data['access_token']});
                console.log(res.data['access_token'])
                return true;
            }
        },
        
        async logoutPlayer({ commit }) {
            commit("updateCurPlayer", {username: "", token: ''});
            return true;
        },
    },
    modules: {
    }
})
