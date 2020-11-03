<template>
	<section>
		<v-row v-if="isLogin">
			<v-col class="profile-info">
				<section class="profile-user">
					<v-avatar size="90">
						<img :src="profileImg" alt="profile-image" />
					</v-avatar>
					<p class="profile-name">
						{{ userName }}
					</p>
				</section>
			</v-col>

			<!-- 업적(클릭시 업적 목록으로 이동) -->
			<v-col class="profile-active">
				<p class="profile-cnt">{{ achieveCnt }}</p>
				<p class="profile-content">업적</p>
			</v-col>
			<!-- 여행 일정(클릭시 일정리스트로 이동) -->
			<v-col class="profile-active" @click="goSchedule">
				<p class="profile-cnt">{{ travelCnt }}</p>
				<p class="profile-content">일정</p>
			</v-col>
			<!-- 후기(클릭시 후기 탭으로 이동) -->
			<v-col class="profile-active">
				<p class="profile-cnt">{{ reviewCnt }}</p>
				<p class="profile-content">후기</p>
			</v-col>
		</v-row>
		<v-row v-else class="profile-undefined" />
		<v-row v-if="isLogin" class="profile-btn">
			<v-btn style="width: 70%;" color="grey" outlined>
				프로필 편집
			</v-btn>
			<v-spacer />
			<v-btn style="width: 28%" color="red" outlined>
				로그아웃
			</v-btn>
		</v-row>
		<v-btn v-else class="profile-btn" color="grey" outlined>
			로그인
		</v-btn>
	</section>
</template>

<script>
export default {
	data() {
		return {
			isLogin: true, // 로그인 여부

			userName: '김영주', // 유저 이름

			achieveCnt: 0, // 완료한 업적 수
			travelCnt: 0, // 작성된 여행일정 수
			reviewCnt: 0, // 작성된 후기 수

			profileImg: 'https://picsum.photos/200', // 유저 프로필 이미지
		};
	},
	methods: {
		goSchedule() {
			this.$router.push('/schedule');
		},
	},
};
</script>

<style lang="scss" scoped>
.profile-info {
	max-width: 120px;

	.profile-user {
		width: 90px;
		margin: 0 auto;

		.profile-name {
			text-align: center;
			width: 90px;
			font-weight: bold;
			margin-bottom: 5px;
		}
	}
}
.profile-undefined {
	height: 20px;
}
.profile-active {
	margin-top: 10px;

	.profile-cnt {
		font-size: 25px;
		text-align: center;
		margin: 0px;
	}
	.profile-content {
		text-align: center;
		font-size: 15px;
		margin: 0px;
	}
}
.profile-btn {
	width: 100%;
	margin: 0px;
	box-shadow: none;
	background-color: white !important;
}
</style>
