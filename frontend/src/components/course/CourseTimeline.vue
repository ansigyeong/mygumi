<template>
	<section>
		<v-card-text class="course-timeline">
			<div class="course-total">
				<p class="course-time">여행 일정</p>
			</div>
			<div
				class="v-timeline course-line v-timeline--align-top v-timeline--dense theme--light"
			>
				<div
					v-for="course in courses"
					:key="course.id"
					class="v-timeline-item theme--light"
				>
					<div class="v-timeline-item__body">
						<div class="course-card v-card v-sheet theme--light">
							<div class="row course-content">
								<div class="course-info col">
									<strong>{{ course.place }}</strong>
									<article>{{ course.dong }}</article>
								</div>
							</div>
						</div>
						<v-row v-if="course.time" class="course-moving">
							<span class="course-time">
								<v-icon small>mdi-timetable</v-icon>
								{{ course.time }}
							</span>
						</v-row>
					</div>
					<div class="v-timeline-item__divider">
						<div class="v-timeline-item__dot v-timeline-item__dot--small">
							<v-img
								:src="'https://k3d201.p.ssafy.io:8080' + `${course.image}`"
								class="v-timeline-item__inner-dot blue"
							></v-img>
						</div>
					</div>
				</div>
			</div>
		</v-card-text>
	</section>
</template>

<script>
import { courseTour } from '@/api/tour';
export default {
	data() {
		return {
			courseId: null,
			courses: [],
		};
	},
	mounted() {
		this.courseData();
	},
	methods: {
		async courseData() {
			try {
				const coursePk = this.$route.params.courseId;
				const { data } = await courseTour(coursePk);
				this.courses = data.data;
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style lang="scss" scoped>
.course-timeline {
	padding-left: 0px;
	padding-right: 0px;
	padding-bottom: 40px;

	.course-total {
		font-weight: bold;
		margin-bottom: 8px;

		.course-time {
			margin: 0px 20px;
		}
	}
	.course-total:after {
		content: '';
		display: block;
		width: 100%;
		height: 55px;
		background: #fff;
		margin-top: -40px;
		box-shadow: 0 5px 15px lavender;
	}
	.course-line {
		.course-card {
			width: 90%;
			padding: 10px;
			margin-bottom: 10px;

			.course-content {
				padding-left: 10px;
				padding-right: 10px;

				.course-info {
					padding: 5px;
				}
				.course-img {
					max-width: 80px;
					padding: 0px;
				}
			}
		}
		.course-moving {
			margin-left: 0px;
			width: 90%;

			.course-time {
				font-size: 14px;
				margin-right: 10px;
			}
		}
	}
}
.v-timeline:before {
	bottom: 0;
	content: '';
	height: 100%;
	position: absolute;
	top: -8px;
	width: 2px;
}
.v-application--is-ltr
	.v-timeline--dense
	.v-timeline-item
	.v-timeline-item__body
	> .v-card:before {
	transform: rotate(0);
	left: -10px;
	top: 25px;
	right: auto;
}
.v-timeline-item__divider {
	position: relative;
	min-width: 180px;
	display: flex;
	align-items: center;
	justify-content: center;
}
.v-timeline-item__dot--small {
	height: 130px;
	left: calc(50% - 12px);
	width: 130px;
}
.v-timeline-item__dot--small .v-timeline-item__inner-dot {
	height: 120px;
	margin: 5px;
	width: 120px;
}
.v-application--is-ltr .v-timeline--dense:not(.v-timeline--reverse):before,
.v-application--is-rtl .v-timeline--reverse.v-timeline--dense:before {
	right: auto;
	left: 90px;
}
.v-timeline--align-top .v-timeline-item__body > .v-card:after {
	top: 23px;
}
.course-timeline .course-line .course-card {
	width: 90%;
	padding: 10px;
	margin: 30px 0px 10px;
}
</style>
