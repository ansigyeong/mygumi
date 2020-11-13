<template>
	<v-app>
		<v-container>
			<header>
				<h2 class="profile-title">프로필</h2>
			</header>
			<profile-user />
			<profile-tabs />
		</v-container>
	</v-app>
</template>

<script>
import ProfileUser from '@/components/profile/ProfileUser';
import ProfileTabs from '@/components/profile/ProfileTabs';

export default {
	name: 'profile',
	data() {
		return {
			isLogin: false,
		};
	},
	components: {
		ProfileUser,
		ProfileTabs,
	},
	mounted() {
		if (!this.$store.getters.isLogined) {
			this.goToLoginPage();
			// console.log('go login');
		}
	},
	methods: {
		goToLoginPage() {
			this.$router.push('/login');
		},
	},
};
</script>

<style lang="scss" scoped>
.profile-title {
	margin-left: 5px;
	font-weight: bold;
	font-size: 20px;
}
.profile-btn {
	width: 100%;
	margin: 0px;
	box-shadow: none;
	background-color: white !important;
}
</style>
