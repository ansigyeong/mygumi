<template>
	<v-bottom-navigation :value="value" color="primary" grow class="bottom-nav">
		<v-btn @click="goHome">
			<span>홈</span>

			<v-icon>mdi-home</v-icon>
		</v-btn>

		<v-btn @click="goSchedule">
			<span>여행 시작하기</span>

			<v-icon>mdi-map-marker</v-icon>
		</v-btn>

		<v-btn @click="goProfile">
			<span>프로필</span>

			<v-icon>mdi-account</v-icon>
		</v-btn>
	</v-bottom-navigation>
</template>

<script>
export default {
	data() {
		return {
			value: 1,
		};
	},
	methods: {
		goHome() {
			this.$router.push('/');
		},
		goSchedule() {
			this.$router.push('/schedule');
		},
		goProfile() {
			this.$router.push('/profile');
		},
	},
};
</script>

<style scoped>
.bottom-nav {
	position: sticky;
	bottom: 0;
	z-index: 10;
}
</style>
