<template>
	<v-app>
		<v-container>
			<schedule-mission />
			<section class="schedule-bicycle">
				<bicycle />
			</section>
			<schedule-challenge />
		</v-container>
	</v-app>
</template>

<script>
import Bicycle from '@/components/animation/Bicycle.vue';
import ScheduleMission from '@/components/schedule/ScheduleMission.vue';
import ScheduleChallenge from '@/components/schedule/ScheduleChallenge.vue';

export default {
	components: {
		Bicycle,
		ScheduleMission,
		ScheduleChallenge,
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
</style>
