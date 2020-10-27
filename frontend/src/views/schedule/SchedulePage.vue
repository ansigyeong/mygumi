<template>
	<v-app>
		<v-container>
			<header>
				<h2 class="schedule-title">여행 일정</h2>
			</header>
			<section>
				<v-row class="schedule-mission">
					<v-col>
						<p class="schedule-random">랜덤 미션</p>
						<p class="schedule-text">주변 여행을 즐기고 싶다면?</p>
					</v-col>
					<div class="schedule-start">
						<v-btn class="schedule-btn">Start</v-btn>
					</div>
				</v-row>
			</section>
			<section class="schedule-bicycle">
				<bicycle />
			</section>
			<section class="schedule-challenge"></section>
		</v-container>
	</v-app>
</template>

<script>
import Bicycle from '@/components/animation/Bicycle.vue';
export default {
	components: {
		Bicycle,
	},
};
</script>

<style lang="scss" scoped>
.v-application--wrap {
	min-height: auto;
}
.container {
	background-color: $gumiBlue;
	padding: 0px;
}
.schedule-title {
	margin: 15px;
	// font-weight: bold;
	text-align: center;
	font-size: 20px;
	color: lightsteelblue;
	text-shadow: 2px 2px 6px navy;
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
.schedule-challenge {
	width: 100%;
	height: 100vh;
	background-color: white;
	border-top-left-radius: 50px;
	box-shadow: -3px -3px 10px 1px navy;
}
.schedule-bicycle {
	// margin-top: 100px;
}
</style>
