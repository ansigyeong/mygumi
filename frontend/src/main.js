import App from './App.vue';
import Vue from 'vue';
import './registerServiceWorker';
import router from './router';
import store from './store';
import VueCookies from 'vue-cookies';
import axios from 'axios';
import vueMoment from 'vue-moment'; //날짜
import Vuetify from 'vuetify'; //Vuetify 1
import 'vuetify/dist/vuetify.min.css'; //Vuetify 2
import '@mdi/font/css/materialdesignicons.css';

Vue.use(vueMoment); //날짜
Vue.prototype.$http = axios;
Vue.use(Vuetify); //Vuetify 3

Vue.config.productionTip = false;
Vue.use(VueCookies);

new Vue({
	router,
	store,
	vuetify: new Vuetify({
		icons: {
			iconfont: 'mdi',
		},
	}),
	render: h => h(App),
}).$mount('#app');
