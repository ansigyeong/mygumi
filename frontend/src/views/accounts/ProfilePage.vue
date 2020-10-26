<template>
	<v-app>
		<v-container>
			<header>
				<h2 class="profile-title">프로필</h2>
			</header>
			<section>
				<profile-user />
			</section>
			<section>
				<profile-tabs />
			</section>
		</v-container>
	</v-app>
</template>

<script>
import ProfileUser from '@/components/ProfileUser';
import ProfileTabs from '@/components/ProfileTabs';

export default {
	name: 'profile',
	components: {
		ProfileUser,
		ProfileTabs,
	},
};
</script>

<style lang="scss" scoped>
.profile-title {
	margin-left: 5px;
	font-weight: bold;
	font-size: 20px;
}
</style>
