<template>
	<section @click="goToDetail">
		<!-- 클릭시 여행지 상세 페이지로 이동 -->
		<v-card v-ripple class="search-card">
			<v-img class="search-card-img" :src="totalURL" />

			<v-card-title class="search-card-title">
				{{ searchTitle }}
			</v-card-title>

			<v-card-text class="search-card-rating">
				<v-rating
					v-model="searchRating"
					background-color="grey"
					color="yellow accent-4"
					size="18"
					readonly
					dense
				/>
			</v-card-text>
		</v-card>
	</section>
</template>

<script>
export default {
	data() {
		return {
			searchTitle: this.searchData.place, // 여행지 제목
			searchRating: 4, // 여행지 별점
			searchId: this.searchData.id,
		};
	},
	props: {
		searchData: Object,
	},
	computed: {
		baseURL() {
			return process.env.VUE_APP_API_URL;
		},
		imgURL() {
			return this.searchData.image.slice(1);
		},
		totalURL() {
			return this.baseURL + this.imgURL;
		},
	},
	methods: {
		goToDetail() {
			this.$router.push(`/location/${this.searchId}`);
		},
	},
};
</script>

<style lang="scss" scoped>
.search-card {
	margin: 0px auto;
	width: 98%;
	height: 260px;
	margin-top: 12px;

	.search-card-img {
		height: 180px;
		width: 100%;
	}
	.search-card-title {
		font-size: 17px;
		font-weight: bold;
		padding: 8px 15px 0px;
	}
	.search-card-rating {
		padding-bottom: 0px;
	}
}
</style>
