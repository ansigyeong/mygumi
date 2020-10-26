<template>
	<v-app>
		<section>
			<course-info />
			<course-timeline />
		</section>
	</v-app>
</template>

<script>
import CourseInfo from '@/components/CourseInfo.vue';
import CourseTimeline from '@/components/CourseTimeline.vue';

export default {
	components: {
		CourseInfo,
		CourseTimeline,
	},
};
</script>

<style lang="scss" scoped>
.course-title {
	margin-left: 5px;
}
</style>
