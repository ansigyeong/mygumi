<template>
	<section class="detail-container">
		<DetailHeader />
		<header class="detail-header">
			<section class="user-box">
				<img
					class="user-profile"
					:src="checkImg(writer.profile_image)"
					alt=""
				/>
				<p class="user-id">{{ writer.nickname }}</p>
			</section>
			<p class="header-title">{{ reviewData.title }}</p>
			<section class="header-etc">
				<p class="createtime">{{ reviewData.created_at.slice(0, 10) }}</p>
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
		checkImg(img) {
			if (img === null) {
				var ramdomNumber = Math.floor(Math.random() * 100) + 1;
				return `https://picsum.photos/500/300?image=${ramdomNumber}`;
			} else {
				const image = img.slice(1);
				return `${this.baseURL}${image}`;
			}
		},
	},
	computed: {
		baseURL() {
			return process.env.VUE_APP_API_URL;
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
