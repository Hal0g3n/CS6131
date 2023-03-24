import Vue from 'vue'
import Vuex, { Store } from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        curPlayer: {
            username: ""
        }
    },
    mutations: {
        updateCurPlayer(state, username) {
            state.curPlayer.username = username;
        }
    },
    getters: {},
    actions: {
        async loginPlayer({ commit }, {username, password}) {
            //async login check
            if (username !== password) return false;

            // Login Successful
            commit("updateCurPlayer", username);
            return true;
        },
    },
    modules: {
    }
})
