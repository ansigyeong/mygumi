<template>
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
			<v-card
				class="schedule-card"
				v-for="schedule in schedules"
				:key="schedule.id"
			>
				<v-row class="schedule-list" v-if="schedule.date >= today">
					<section class="schedule-user">
						<v-avatar size="30" class="schedule-img">
							<img
								:src="
									'https://k3d201.p.ssafy.io:8080' + schedule.host.profile_image
								"
								alt="profile-image"
							/>
						</v-avatar>
						<p class="schedule-name">
							{{ schedule.host.nickname }}
						</p>
					</section>
					<v-col
						class="schedule-challenge"
						@click="goToDetailPlan(schedule.id)"
					>
						<p class="schedule-name">{{ schedule.title }}</p>
						<p class="schedule-date">
							{{ schedule.date[5] }}{{ schedule.date[6] }}월
							{{ schedule.date[8] }}{{ schedule.date[9] }}일
						</p>
					</v-col>
					<section class="schedule-play">
						<!-- 챌린지 시작 버튼 -->
						<v-btn class="schedule-btn" icon @click="goToChallenge">
							<v-icon>mdi-play-circle-outline</v-icon>
						</v-btn>
					</section>
				</v-row>
			</v-card>
		</section>
	</section>
</template>

<script>
import { scheduleList } from '@/api/schedule';
import { fetchProfile } from '@/api/profile';

export default {
	data() {
		return {
			todayMonth: null, // 오늘 날짜(월)
			todayDate: null, // 오늘 날짜(일)
			today: null,

			scheduleImg: 'https://picsum.photos/200', // 일정 작성자 이미지
			writerName: '김영주', // 일정 작성자 이름
			scheduleName: '구미 첫 여행~~!', // 일정 이름
			scheduleDate: '10월 30일', // 여행 날짜

			schedules: [],
			hostId: null,
			hostName: null,
			hostImage: null,
		};
	},
	mounted() {
		this.getSchedule();
	},
	created() {
		// 오늘 날짜
		var today = new Date();
		this.todayDate = today.getDate();
		var month = today.getMonth() + 1;
		var year = today.getFullYear();
		this.today = year + '-' + month + '-' + this.todayDate;
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
	methods: {
		async getSchedule() {
			try {
				const userId = this.$store.getters.getId;
				const { data } = await scheduleList(userId);
				this.schedules = data.data;
				this.schedules.sort(function(a, b) {
					if (a.date > b.date) {
						return 1;
					}
					if (a.date < b.date) {
						return -1;
					}
					return 0;
				});
			} catch (error) {
				console.log(error);
			}
		},
		async fetchData() {
			try {
				const { data } = await fetchProfile(this.hostId);
				this.hostImage = data.user.profile_image;
				this.hostName = data.user.nickname;
			} catch (error) {
				console.log(error);
			}
		},
		goToChallenge() {
			alert('챌린지하자!!');
		},
		goToDetailPlan(scheduleId) {
			return this.$router.push(`/plan/${scheduleId}`);
		},
	},
};
</script>

<style lang="scss" scoped>
.schedule-content {
	width: 100%;
	height: 100%;
	min-height: 100vh;
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
