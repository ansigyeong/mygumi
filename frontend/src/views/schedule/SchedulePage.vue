<template>
	<v-app>
		<v-container>
			<header>
				<v-app-bar flat color="rgba(0, 0, 0, 0)" class="schedule-bar">
					<h2 class="schedule-title">여행 일정</h2>
					<v-spacer />

					<!-- 일정 추가 버튼 -->
					<v-btn class="schedule-icon" icon>
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
			<section class="schedule-bicycle">
				<bicycle />
			</section>
			<section class="schedule-content">
				<header>
					<v-row class="schedule-header">
						<div class="schedule-today">
							<p class="schedule-date">{{ todayDate }}</p>
							<p class="schedule-month">{{ todayMonth }}</p>
						</div>
						<span class="schedule-text">즐거운 여행되세요~~!!</span>
					</v-row>
				</header>
				<section>
					<v-card class="schedule-card">
						<v-row class="schedule-list">
							<section class="schedule-user">
								<v-avatar size="30" class="schedule-img">
									<img :src="scheduleImg" alt="profile-image" />
								</v-avatar>
								<p class="schedule-name">
									{{ writerName }}
								</p>
							</section>
							<v-col class="schedule-challenge">
								<p class="schedule-name">{{ scheduleName }}</p>
								<p class="schedule-date">{{ scheduleDate }}</p>
							</v-col>
							<section class="schedule-play">
								<!-- 챌린지 시작 버튼 -->
								<v-btn class="schedule-btn" icon>
									<v-icon>mdi-play-circle-outline</v-icon>
								</v-btn>
							</section>
						</v-row>
					</v-card>
				</section>
			</section>
		</v-container>
	</v-app>
</template>

<script>
import Bicycle from '@/components/animation/Bicycle.vue';
export default {
	data() {
		return {
			todayMonth: null, // 오늘 날짜(월)
			todayDate: null, // 오늘 날짜(일)

			scheduleImg: 'https://picsum.photos/200', // 일정 작성자 이미지
			writerName: '김영주', // 일정 작성자 이름
			scheduleName: '구미 첫 여행~~!', // 일정 이름
			scheduleDate: '10월 30일', // 여행 날짜
		};
	},
	components: {
		Bicycle,
	},
	created() {
		// 오늘 날짜
		var today = new Date();
		this.todayDate = today.getDate();
		var month = today.getMonth() + 1;
		if (month == 1) {
			this.todayMonth = 'Jan';
		} else if (month == 2) {
			this.todayMonth = 'Feb';
		} else if (month == 3) {
			this.todayMonth = 'Mar';
		} else if (month == 4) {
			this.todayMonth = 'Apr';
		} else if (month == 5) {
			this.todayMonth = 'May';
		} else if (month == 6) {
			this.todayMonth = 'Jun';
		} else if (month == 7) {
			this.todayMonth = 'Jul';
		} else if (month == 8) {
			this.todayMonth = 'Aug';
		} else if (month == 9) {
			this.todayMonth = 'Sep';
		} else if (month == 10) {
			this.todayMonth = 'Oct';
		} else if (month == 11) {
			this.todayMonth = 'Nov';
		} else if (month == 12) {
			this.todayMonth = 'Dec';
		}
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
.schedule-content {
	width: 100%;
	height: 100vh;
	background-color: white;
	border-top-left-radius: 50px;
	box-shadow: -3px -3px 10px 1px navy;
	padding: 35px 30px;

	.schedule-header {
		margin: 0px 0px 20px;

		.schedule-today {
			width: 60px;
			height: 60px;
			border-radius: 18px;
			background-color: $gumiBlue;

			.schedule-date {
				margin: 0px;
				padding-top: 7px;
				text-align: center;
				font-size: 20px;
				color: white;
			}
			.schedule-month {
				margin: 0px;
				text-align: center;
				font-size: 10px;
				color: lightblue;
			}
		}
		.schedule-text {
			margin: auto;
			color: grey;
		}
	}
	.schedule-card {
		border-radius: 0px;
		border-left: 5px solid lightsteelblue;
		// box-shadow: inset 5px 5px 10px lightgrey;
		box-shadow: none;
		margin-bottom: 20px;
		// border: 10px solid lavender;
		// background-color: ghostwhite;
		// background: linear-gradient(0.75turn, white, lavender);

		.schedule-list {
			margin: 0px;

			.schedule-user {
				width: 60px;

				.schedule-img {
					border-radius: 50px;
					margin-left: 25%;
				}
				.schedule-name {
					margin: 0px;
					text-align: center;
					font-size: 12px;
				}
			}
			.schedule-challenge {
				padding: 0px 12px;

				.schedule-name {
					margin: 0px;
				}
				.schedule-date {
					margin: 0px;
					font-size: 10px;
					color: rgba(0, 0, 0, 0.6);
				}
			}
			.schedule-play {
				.schedule-btn {
					color: $gumiBlue;
				}
			}
		}
	}
}
</style>
