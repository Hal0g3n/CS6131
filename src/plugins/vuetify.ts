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
                primary: {
                    base: colors.blue.base, // #E53935
                    lighten1: colors.blue.darken1,
                    lighten2: colors.blue.darken2,
                    lighten3: colors.blue.darken3,
                    lighten4: colors.blue.darken4
                },
                secondary: colors.orange.base, // #FFCDD2
                accent: colors.indigo.base, // #3F51B5
                // anchor: colors.blueGrey.base
                green: {
                    base: colors.green.base, // #E53935
                    lighten1: colors.green.darken1,
                    lighten2: colors.green.darken2,
                    lighten3: colors.green.darken3,
                    lighten4: colors.green.darken4
                },
            },
        },
        options: { customProperties: true }
    },
});
