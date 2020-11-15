import Vue from 'vue';
import Vuex from 'vuex';
import cookies from 'vue-cookies';
import { loginUser } from '@/api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		token: cookies.isKey('auth-token') ? cookies.get('auth-token') : null,
		username: cookies.isKey('username') ? cookies.get('username') : null,
		id: cookies.isKey('id') ? cookies.get('id') : null,
		courseId: cookies.isKey('courseId') ? cookies.get('courseId') : null,
	},
	getters: {
		isLogined: state => !!state.token,
		getToken: state => state.token,
		getUsername: state => state.username,
		getId: state => state.id,
		getCourseId: state => state.courseId,
	},
	mutations: {
		setUsername(state, username) {
			cookies.set('username', username);
			state.username = username;
		},
		setToken(state, token) {
			state.token = token;
		},
		setId(state, id) {
			state.id = id;
		},
		clearUsername(state) {
			state.username = null;
		},
		clearToken(state) {
			state.token = null;
		},
		clearId(state) {
			state.id = null;
		},
		setCourseId(state, courseId) {
			cookies.set('courseId', courseId);
			state.courseId = courseId;
		},
	},
	actions: {
		SETUP_USER({ commit }, { user: { username, pk }, token }) {
			cookies.set('id', pk);
			cookies.set('username', username);
			cookies.set('auth-token', token);
			commit('setUsername', username);
			commit('setToken', token);
			commit('setId', pk);
		},
		async LOGIN({ dispatch }, userData) {
			try {
				const { data } = await loginUser(userData);
				dispatch('SETUP_USER', data);
			} catch (error) {
				console.log(error);
			}
		},
		// async SIGNUP({ dispatch }, userData) {
		// 	try {
		// 		const { data } = await registerUser(userData);
		// 		dispatch('SETUP_USER', data);
		// 	} catch (error) {
		// 		console.log(error);
		// 	}
		// },
	},
	modules: {},
});
