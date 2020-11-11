<template>
	<section class="detail-container">
		<DetailHeader />
		<header class="detail-header">
			<section class="user-box">
				<img class="user-profile" src="@/assets/images/temp_gumi.png" alt="" />
				<p class="user-id">{{ writer.nickname }}</p>
			</section>
			<p class="header-title">{{ reviewData.title }}</p>
			<section class="header-etc">
				<p class="createtime">{{ reviewData.created_at }}</p>
				<!-- <p>|</p>
				<p class="views">조회 100</p> -->
			</section>
		</header>
		<article class="detail-body">{{ reviewData.content }}</article>
		<section class="user-profile"></section>
		<footer class="detail-footer"></footer>
	</section>
</template>

<script>
import { fetchArticle } from '@/api/review';
import { fetchProfile } from '@/api/profile';
import DetailHeader from '@/components/common/DetailHeader.vue';
export default {
	data() {
		return {
			reviewData: null,
			writer: null,
		};
	},
	components: {
		DetailHeader,
	},
	methods: {
		async fetchData() {
			const reviewId = this.$route.params.reviewId;
			const { data } = await fetchArticle(reviewId);
			this.reviewData = data.review;
			const res = await fetchProfile(data.review.user);
			this.writer = res.data.user;
		},
	},
	mounted() {
		this.fetchData();
	},
};
</script>

<style lang="scss" scoped>
.detail-container {
	margin-left: 3%;
	margin-right: 3%;
}
.temp-header {
	height: 40px;
}
.detail-header {
	margin-bottom: 2rem;
	.user-box {
		display: flex;
		align-items: center;
		margin-bottom: 0.5rem;
		.user-profile {
			background: black;
			width: 1.2rem;
			height: 1.2rem;
			border-radius: 50%;
			margin-right: 0.3rem;
		}
		.user-id {
			font-size: 0.7rem;
		}
	}
	.header-title {
		font-size: 1.5rem;
		margin-bottom: 0.3rem;
	}
	.header-etc {
		display: flex;
		color: rgb(161, 160, 160);
		font-size: 0.7rem;
		p {
			margin-right: 0.3rem;
		}
	}
	.detail-body {
	}
}
</style>
