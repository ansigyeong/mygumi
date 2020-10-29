import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'main',
		component: () => import('@/views/MainPage.vue'),
	},
	{
		path: '/location',
		name: 'location',
		component: () => import('@/views/LocationPage.vue'),
	},
	{
		path: '/profile',
		name: 'profile',
		component: () => import('@/views/accounts/ProfilePage.vue'),
	},
	{
		path: '/search',
		name: 'search',
		component: () => import('@/views/search/SearchPage.vue'),
		children: [
			{
				path: 'result',
				name: 'searchResult',
				component: () => import('@/components/search/SearchResult.vue'),
			},
		],
	},
	{
		path: '/course',
		name: 'course',
		component: () => import('@/views/course/CoursePage.vue'),
	},
	{
		path: '/schedule',
		name: 'schedule',
		component: () => import('@/views/schedule/SchedulePage.vue'),
	},
	{
		path: '/plan',
		name: 'plan',
		component: () => import('@/views/schedule/SchedulePlanPage.vue'),
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
