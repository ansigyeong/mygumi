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
		path: '/signup',
		name: 'signup',
		component: () => import('@/views/accounts/SignupPage.vue'),
	},
	{
		path: '/location/:locationId',
		name: 'location',
		component: () => import('@/views/LocationPage.vue'),
	},
	{
		path: '/location/:locationId/create',
		name: 'reviewCreate',
		component: () => import('@/views/review/CreateReviewPage.vue'),
	},
	{
		path: '/location/:locationId/reviews/:reviewId',
		name: 'reviewDetail',
		component: () => import('@/views/review/ReviewDetailPage.vue'),
	},
	{
		path: '/profile/:userId',
		name: 'profile',
		component: () => import('@/views/accounts/ProfilePage.vue'),
	},
	{
		path: '/search',
		name: 'search',
		component: () => import('@/views/search/SearchPage.vue'),
	},
	{
		path: '/search/:searchString',
		name: 'searchResult',
		component: () => import('@/views/search/SearchResultPage.vue'),
	},

	{
		path: '/course/:courseId',
		name: 'course',
		component: () => import('@/views/course/CoursePage.vue'),
	},
	{
		path: '/login',
		name: 'login',
		component: () => import('@/views/accounts/LoginPage.vue'),
	},
	{
		path: '/mission/:territoryName',
		name: 'mission',
		component: () => import('@/views/MissionPage.vue'),
	},
	{
		path: '/schedule',
		name: 'schedule',
		component: () => import('@/views/schedule/SchedulePage.vue'),
	},
	{
		path: '/plan',
		name: 'plan',
		component: () => import('@/views/schedule/PlanPage.vue'),
	},
	{
		path: '/plan/:scheduleId',
		name: 'planDetail',
		component: () => import('@/views/schedule/PlanDetailPage.vue'),
	},
	{
		path: '/plan/:scheduleId/update',
		name: 'planUpdate',
		component: () => import('@/views/schedule/PlanUpdatePage.vue'),
	},
	{
		path: '/achieve',
		name: 'achieve',
		component: () => import('@/views/AchievePage.vue'),
	},
	{
		path: '*',
		redirect: '/404',
	},
	{
		path: '/404',
		component: () => import('@/views/NotFoundPage.vue'),
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
