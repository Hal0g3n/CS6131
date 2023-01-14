import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: colors.blue.base, // #E53935
                secondary: colors.orange.base, // #FFCDD2
                accent: colors.indigo.base, // #3F51B5
                // anchor: colors.blueGrey.base
            },
            dark: {
                primary: colors.blue.base, // #E53935
                secondary: colors.orange.base, // #FFCDD2
                accent: colors.indigo.base, // #3F51B5
                // anchor: colors.blueGrey.base
            },
        },
    },
});
