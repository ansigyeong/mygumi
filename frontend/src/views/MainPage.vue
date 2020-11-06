<template>
	<section class="main-container">
		<AppHeader />
		<div class="main-box">
			<p class="main-box__text">오늘은 어디로 가볼까?</p>
			<div class="main-box__fakeInput" @click="goToSearchPage">
				<i class="icon ion-md-search"></i>
				<p class="placeholder">검색</p>
			</div>
		</div>
		<section class="recommend-box">
			<p class="recommend-title">
				여기는 어때?
			</p>
			<section class="recommend-card">
				<img
					class="recommend-img"
					src="@/assets/images/temp_gumi.png"
					alt="recommendImg"
					@click="goToCoursePage"
				/>
			</section>
			<section class="recommend-card">
				<img
					class="recommend-img"
					src="@/assets/images/temp_gumi2.png"
					alt="recommendImg"
				/>
			</section>
		</section>
	</section>
</template>

<script>
import AppHeader from '@/components/common/AppHeader.vue';

export default {
	data() {
		return {
			// 임시
			courseId: 1,
		};
	},
	components: {
		AppHeader,
	},
	methods: {
		goToSearchPage() {
			this.$router.push('/search');
		},
		goToCoursePage() {
			this.$router.push(`/course/${this.courseId}`);
		},
	},
};
</script>

<style lang="scss" scoped>
.main-container {
	margin-left: 5%;
	margin-right: 5%;
	.main-box {
		display: flex;
		flex-direction: column;
		width: 100%;
		.main-box__text {
			font-size: 20px;
			font-weight: bolder;
			margin-left: 5px;
			margin-bottom: 25px;
		}
		.main-box__fakeInput {
			width: 100%;
			height: 45px;
			border: 1px solid $Gray;
			border-radius: 10px;
			display: flex;
			align-items: center;
			padding: 0 10px;
			color: $lightGray;
			.ion-md-search {
				font-size: 25px;
				margin-right: 10px;
			}
			.placeholder {
				font-size: 15px;
			}
		}
	}
	.recommend-box {
		display: flex;
		flex-direction: column;
		width: 100%;
		margin-top: 32px;
		.recommend-title {
			font-size: 18px;
			margin-bottom: 16px;
		}
		.recommend-card {
			margin-bottom: 16px;
			.recommend-img {
				width: 100%;
				height: 180px;
				border-radius: 10px;
			}
		}
	}
}
</style>
