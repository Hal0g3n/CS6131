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
