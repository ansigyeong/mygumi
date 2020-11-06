<template>
	<section>
		<header>
			<v-app-bar flat color="rgba(0, 0, 0, 0)" class="schedule-bar">
				<h2 class="schedule-title">여행 일정</h2>
				<v-spacer />

				<!-- 일정 추가 버튼 -->
				<v-btn class="schedule-icon" icon @click="goToPlanPage">
					<v-icon>mdi-calendar-plus</v-icon>
				</v-btn>
			</v-app-bar>
		</header>
		<section>
			<v-row class="schedule-mission">
				<v-col>
					<p class="schedule-random">랜덤 미션</p>
					<p class="schedule-text">주변 여행을 즐기고 싶다면?</p>
				</v-col>
				<div class="schedule-start">
					<!-- 미션 시작 버튼 -->
					<v-btn class="schedule-btn">Start</v-btn>
				</div>
			</v-row>
		</section>
	</section>
</template>

<script>
export default {
	methods: {
		goToPlanPage() {
			this.$router.push('/plan');
		},
	},
};
</script>

<style lang="scss" scoped>
.schedule-bar {
	.schedule-title {
		margin-left: 25px;
		// font-weight: bold;
		width: 100%;
		text-align: center;
		font-size: 20px;
		color: lightsteelblue;
		text-shadow: 2px 2px 6px navy;
	}
	.schedule-icon {
		color: lightsteelblue;
		text-shadow: 2px 2px 6px navy;
	}
}
.schedule-mission {
	margin: 0px;
	height: 115px;

	.schedule-random {
		margin: 10px 5px 5px;
		font-size: 20px;
		color: white;
		text-shadow: 2px 2px 6px navy;
	}
	.schedule-text {
		margin: 0px 5px;
		font-size: 12px;
		color: lightblue;
		text-shadow: 2px 2px 6px navy;
	}
	.schedule-start {
		margin: 30px 30px 0px 0px;
		.schedule-btn {
			width: 100px;
		}
	}
}
</style>
