<template>
	<section>
		<v-row justify="space-around" width="100px">
			<v-img height="180px" :src="courseImg">
				<v-app-bar flat color="rgba(0, 0, 0, 0)" class="app-bar">
					<v-spacer />

					<!-- 일정 추가 버튼 -->
					<v-btn class="course-add" color="white" icon @click="createSchedule">
						<v-icon>mdi-calendar-plus</v-icon>
					</v-btn>
					<div />
				</v-app-bar>

				<v-card-title class="white--text py-1">
					<p class="course-title">
						{{ courseName }}
					</p>
				</v-card-title>
			</v-img>
		</v-row>
	</section>
</template>

<script>
import { courseTour } from '@/api/tour';
import { mapMutations } from 'vuex';

export default {
	data() {
		return {
			courseImg: 'https://picsum.photos/300', // 코스 사진
			courseName: null,
			coursePk: null,
		};
	},
	mounted() {
		this.courseData();
	},
	methods: {
		...mapMutations(['setCourseId']),
		async courseData() {
			try {
				this.coursePk = this.$route.params.courseId;
				this.setCourseId(this.coursePk);
				const { data } = await courseTour(this.coursePk);
				this.courseName = data.data[0].course_name;
			} catch (error) {
				console.log(error);
			}
		},
		createSchedule() {
			return this.$router.push('/plan');
		},
	},
};
</script>

<style lang="scss" scoped>
.row {
	margin-right: 0px;
}
.course-add {
	margin: 0px;
	text-shadow: 2px 2px 6px gray;
}
.course-title {
	margin-top: 70px;
	margin-bottom: 0px;
	padding: 0px 12px;
	font-size: 18px;
	font-weight: bold;
	text-shadow: 2px 2px 6px gray;
}
</style>
