<template>
	<!-- 클릭시 후기 상세 페이지로 이동 -->
	<v-card v-ripple class="review-card">
		<v-img class="review-card-img" :src="reviewImg" />

		<v-card-title class="review-card-title">
			{{ reviewTitle }}
		</v-card-title>

		<v-card-text class="review-card-rating">
			<v-rating
				v-model="reviewRating"
				background-color="grey"
				color="yellow accent-4"
				size="18"
				readonly
				dense
			/>
		</v-card-text>

		<v-card-actions class="review-card-info">
			<v-list-item calss="review-card-writer">
				<v-list-item-avatar
					color="grey darken-3"
					size="20"
					class="review-card-userimg"
				>
					<v-img :src="profileImg" alt="profile-image" />
				</v-list-item-avatar>

				<v-list-item-content class="review-card-userinfo">
					<v-card-subtitle class="review-card-text">
						{{ reviewName }} · {{ reviewDate.slice(0, 10) }}
					</v-card-subtitle>
				</v-list-item-content>
			</v-list-item>
		</v-card-actions>
	</v-card>
</template>

<script>
export default {
	data() {
		return {
			reviewTitle: '친구들이랑 첫 여행 :)', // 후기 제목
			reviewImg: 'https://picsum.photos/300', // 후기 사진
			reviewName: 'writer', // 후기 작성자 이름
			reviewDate: '2020.05.23', // 후기 작성일
			reviewRating: 4, // 후기 별점

			profileImg: 'https://picsum.photos/200', // 후기 작성자 사진
		};
	},
};
</script>

<style lang="scss" scoped>
.review-card {
	margin: 0px auto;
	width: 98%;
	height: 290px;
	margin-top: 12px;

	.review-card-img {
		height: 180px;
		width: 100%;
	}
	.review-card-title {
		font-size: 17px;
		font-weight: bold;
		padding: 8px 15px 0px;
	}
	.review-card-rating {
		padding-bottom: 0px;
	}
	.review-card-info {
		padding: 0px;

		.review-card-writer {
			padding: 0px 16px;

			.review-card-userimg {
				margin: 5px 8px 5px 0px;
			}
		}
		.review-card-userinfo {
			padding: 0px;

			.review-card-text {
				padding: 0px;
				font-size: 12px;
			}
		}
	}
}
</style>
