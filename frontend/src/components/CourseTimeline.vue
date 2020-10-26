<template>
	<section>
		<v-card-text class="course-timeline">
			<div class="course-total">
				약 5시간 소요
			</div>

			<v-timeline class="course-line" align-top dense>
				<v-timeline-item
					v-for="course in courses"
					:key="course.index"
					:color="course.color"
					small
				>
					<v-card class="course-card">
						<v-row class="course-content">
							<v-col class="course-info">
								<strong>{{ course.name }}</strong>
								<article>{{ course.address }}</article>
							</v-col>
							<v-col class="course-img">
								<v-img :src="course.image" />
							</v-col>
						</v-row>
					</v-card>
					<v-row class="course-moving">
						<span class="course-transport">
							<v-icon small>mdi-car</v-icon>
							{{ course.time.car }}
						</span>
						<span class="course-transport">
							<v-icon small>mdi-bus</v-icon>
							{{ course.time.bus }}
						</span>
						<span class="course-transport">
							<v-icon small>mdi-bike</v-icon>
							{{ course.time.bike }}
						</span>
						<span class="course-transport">
							<v-icon small>mdi-walk</v-icon>
							{{ course.time.walk }}
						</span>
					</v-row>
				</v-timeline-item>
			</v-timeline>
		</v-card-text>
	</section>
</template>

<script>
export default {
	data() {
		return {
			courses: [
				// 코스 정보
				{
					index: 1,
					image: 'https://picsum.photos/100',
					name: '동락공원',
					address: '경북 구미시 3공단1로 191',
					dayoff: '무휴',
					color: 'deep-purple lighten-1',
					time: {
						car: '약 20분',
						bus: '약 40분',
						bike: '약 1시간',
						walk: '약 1시간 40분',
					},
				},
				{
					index: 2,
					image: 'https://picsum.photos/200',
					name: '낙동강체육공원',
					address: '경북 구미시 낙동제방길 200',
					dayoff: '무휴',
					color: 'green',
					time: {
						car: '약 20분',
						bus: '약 40분',
						bike: '약 1시간',
						walk: '약 1시간 40분',
					},
				},
				{
					index: 3,
					image: 'https://picsum.photos/400',
					name: '새마을운동테마공원',
					address: '경북 구미시 박정희로 155',
					dayoff:
						'매일 10:00 - 17:00 야외공원 24시간 / 월요일 휴무 신정, 설, 추석당일 휴무',
					color: 'deep-purple lighten-1',
					time: {
						car: '약 20분',
						bus: '약 40분',
						bike: '약 1시간',
						walk: '약 1시간 40분',
					},
				},
			],
		};
	},
};
</script>

<style lang="scss" scoped>
.course-timeline {
	padding-left: 0px;
	padding-right: 0px;

	.course-total {
		font-weight: bold;
		margin-left: 20px;
		margin-bottom: 8px;
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

			.course-transport {
				font-size: 10px;
				margin-right: 10px;
			}
		}
	}
}
</style>
