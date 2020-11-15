<template>
	<v-container fluid>
		<v-row v-if="userName == 'skawngur'">
			<!-- 클릭시 크게보기 -->
			<v-col v-for="i in 7" :key="i" cols="4" style="padding: 1px;">
				<v-img
					:src="
						`https://raw.githubusercontent.com/kei9641/pjt-img-file/master/gumi%20(${i}).jpg`
					"
					aspect-ratio="1"
					v-ripple
				/>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
import { fetchProfile } from '@/api/profile';
export default {
	data() {
		return {
			userName: null,
		};
	},
	mounted() {
		this.fetchData();
	},
	methods: {
		async fetchData() {
			try {
				const userPK = this.$store.getters.getId;
				const { data } = await fetchProfile(userPK);
				this.userName = data.user.nickname;
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style></style>
