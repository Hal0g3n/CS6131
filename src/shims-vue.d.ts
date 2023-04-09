declare module '*.vue' {
  import Vue from 'vue'
  export default Vue
}

declare module 'vue-chessboard' {
  import {chessboard} from 'vue-chessboard'
  export default chessboard
}

declare module 'vuetify/lib/framework' {
  import Vuetify from 'vuetify'
  export default Vuetify
}

declare module 'vue-apexcharts' {
  import VueApexCharts from 'vue-apexcharts'
  export default VueApexCharts
}

declare module '@vue-notification' {
    import Notifications from 'vue-notification'
    export default Notifications
}
