<template>
	<v-app>
		<v-container>
			<header>
				<h2 class="profile-title">프로필</h2>
			</header>
			<section v-if="isLogin">
				<profile-user />
			</section>
			<section v-if="isLogin">
				<profile-tabs />
			</section>
			<section v-else>
				<v-btn class="profile-btn" color="grey" outlined @click="goToLoginPage">
					로그인
				</v-btn>
			</section>
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
			isLogin: true,
		};
	},
	components: {
		ProfileUser,
		ProfileTabs,
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
