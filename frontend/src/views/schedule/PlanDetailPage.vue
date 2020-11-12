<template>
	<v-app>
		<div class="plan-wrapper">
			<!--======= Header =======-->

			<header class="header">
				<div class="container">
					<span>{{ scheduleTitle }}</span>
					<v-btn @click="goToPlanUpdatePage">수정</v-btn>
				</div>
			</header>

			<!--======= Today =======-->

			<section class="today-box" id="today-box">
				<span class="breadcrumb">여행 날짜</span>
				<p style="font-size:20px; padding: 16px 40px 0px;">
					{{ viewDate }}
				</p>
			</section>

			<!--======= Upcoming Events =======-->

			<section class="upcoming-events">
				<div class="container">
					<h3 style="margin-bottom:20px;">
						여행 일정
					</h3>
					<div class="events-wrapper">
						<div class="event" v-for="plan in plans" :key="plan.id">
							<h4 class="event__point">{{ plan.place }}</h4>
							<p class="event__description">
								{{ plan.dong }}
							</p>
						</div>
						<v-row class="event active">
							<i class="ion ion-ios-radio-button-on icon-in-active-mode"></i>
							<div style="width: 70%;">
								<span class="event__point">함께 갈 친구</span>
								<br />
								<span
									v-for="(friend, index) in friends"
									:key="index"
									class="event__description"
								>
									{{ friend }}
								</span>
							</div>
							<v-spacer />
						</v-row>
					</div>

					<v-btn text class="add-event-button" @click="goToChallengePage">
						<span class="add-event-button__title">여행 시작</span>
						<span class="add-event-button__icon">
							<v-icon>mdi-playlist-plus</v-icon>
						</span>
					</v-btn>
				</div>
			</section>
		</div>
	</v-app>
</template>

<script>
import { getSchedule } from '@/api/schedule';
import { location } from '@/api/tour';
export default {
	data() {
		return {
			selectDate: new Date().toISOString().substr(0, 10), // 선택한 날짜
			viewDate: null, // 선택된 날짜 형식 변경
			friends: [], // 친구 목록
			userId: null,
			scheduleId: null,
			scheduleData: [],
			scheduleTitle: null,
			placeData: [],
			plans: [],
		};
	},
	mounted() {
		this.userId = this.$store.getters.getId;
		this.scheduleId = this.$route.params.scheduleId;
		this.fetchSchedule();
	},
	methods: {
		// 스케줄 정보 불러오기
		async fetchSchedule() {
			try {
				const { data } = await getSchedule(this.userId, this.scheduleId);
				this.scheduleData = data.data[0];
				this.placeData = this.scheduleData.place;
				this.selectDate = this.scheduleData.date;
				this.scheduleTitle = this.scheduleData.title;
				// 월만 따로 저장
				var selectMonth = this.selectDate[5] + this.selectDate[6];
				// 일만 따로 저장
				var selectD = this.selectDate[9];
				if (this.selectDate[8]) {
					selectD = this.selectDate[8] + this.selectDate[9];
				}
				// 년도만 따로 저장
				var selectYear =
					this.selectDate[0] +
					this.selectDate[1] +
					this.selectDate[2] +
					this.selectDate[3];
				this.viewDate =
					selectMonth + '월 ' + selectD + '일, ' + selectYear + '년';
				for (var i = 0; i <= this.placeData.length - 1; i++) {
					this.fetchPlace(this.placeData[i]);
				}
				for (var j = 0; j <= this.scheduleData.user.length - 1; j++) {
					this.friends.push(this.scheduleData.user[j].nickname);
				}
			} catch (error) {
				console.log(error);
			}
		},
		// 장소 정보 불러오기
		async fetchPlace(placeId) {
			try {
				const { data } = await location(placeId);
				this.plans.push(data.data);
			} catch (error) {
				console.log(error);
			}
		},
		goToPlanUpdatePage() {
			return this.$router.push(`/plan/${this.scheduleId}/update`);
		},
		goToChallengePage() {
			alert('챌린지 하자!!!!');
		},
	},
};
</script>

<style lang="scss" scoped>
.container {
	width: 90%;
	margin: auto;
}

.plan-wrapper {
	background: #fff;
	/* relative with .today-box::before*/
	z-index: 1; /*positive*/ // PARENT
	position: relative;
	/*---------*/
	// width: 380px;
	min-height: 100%;
	// margin: auto;
	padding: 10px 0 60px;
	// border-radius: 10px;
	// box-shadow: 0px 10px 30px -10px #000;
	overflow: auto;
	height: 100vh;
}

.header {
	// padding-bottom: 15px;
	// margin-bottom: 40px;
	.container {
		position: relative;
		.col-12 {
			padding: 12px 12px 0px;
		}
		span {
			color: #444;
			font: {
				size: 21px;
				weight: 700;
			}
		}
		h1 {
			margin-top: 5px;
			color: #919294;
			font: {
				size: 13px;
				weight: 300;
			}
		}

		.menu-toggle {
			width: 25px;
			height: 25px;
			background: #fff;
			padding: 24px;
			border-radius: 50%;
			direction: rtl;
			display: flex;
			align-items: center;
			justify-content: center;
			box-shadow: 0px 10px 30px -14px #000;
			position: absolute;
			top: 0;
			right: 0;
			cursor: pointer;
			span {
				display: block;
				width: 25px;
				height: 2px;
				background: #777;
				border-radius: 2px;
				transition: all 300ms ease;
				&:not(:last-child) {
					margin-bottom: 5px;
				}
				&:first-child {
					width: 20px;
				}
				&:last-child {
					width: 15px;
				}
			}
			&:hover span:first-child,
			&:hover span:last-child {
				width: 100%;
			}
		}
	}
}

.today-box {
	background: linear-gradient(to left, #485fed, rgba(255, 44, 118, 0.25)),
		#485fed;
	color: #fff;
	padding: 32px 0px 16px;
	position: relative;
	box-shadow: 0px 0px 40px -9px #485fed;
	// margin-bottom: 50px;
	&::before {
		content: '';
		background: linear-gradient(to left, #485fed, rgba(255, 44, 118, 0.25)),
			#485fed;
		opacity: 0.4;
		z-index: -1; // CHILD /*negative*/ /* relative with .mobile-wrapper it's his parent background*/
		display: block;
		width: 100%;
		height: 40px;
		margin: auto;
		position: absolute;
		bottom: -13px;
		left: 50%;
		transform: translatex(-50%);
		border-radius: 50%;
		box-shadow: 0px 0px 40px 0 #485fed;
	}
	.breadcrumb {
		padding: 0px 40px;
		font-weight: 300;
		position: relative;
	}
	.v-expansion-panels {
		.v-expansion-panel {
			background-color: rgba(0, 0, 0, 0);
			color: white;
			&::before {
				box-shadow: none;
			}
			.v-expansion-panel-header {
				padding: 16px 40px;
				font-size: 20px;
				letter-spacing: 1px;
				font-weight: 600;
				text-shadow: 0px 0px 5px rgba(#000, 0.15);
			}
			.v-expansion-panel-content {
				.v-picker {
					width: 100%;
				}
			}
		}
	}
}

.upcoming-events {
	margin: 10px 0px 20px;
	.container {
		h3 {
			color: #333;
			font-size: 17px;
			position: relative;
			&::before {
				content: '';
				display: block;
				width: 58%;
				height: 2px;
				background-color: #e8e8e8;
				position: absolute;
				top: 60%;
				transform: translatey(-60%);
				right: 0;
			}
		}
		.col-12 {
			padding: 12px 0px;
		}
		.events-wrapper {
			margin: 0px;
			.event {
				position: relative;
				margin-bottom: 25px;
				padding-left: 0px;
				cursor: pointer;
				.fire-icon {
					font-size: 24px;
					font-weight: 100;
					position: absolute;
					right: 0;
					top: 0px;
				}
				.event__point {
					margin: 0px 10px;
					color: #555;
					font: {
						size: 15px;
						weight: 800;
					}
					letter-spacing: 1px;
				}
				.event__duration {
					position: absolute;
					top: 30px;
					right: 20px;
					color: #999;
					font: {
						size: 10px;
						weight: 800;
						style: italic;
					}
				}
				.event__description {
					margin: 5px 10px;
					color: #919294;
					font-size: 13px;
					font-weight: 300;
				}
				&.active {
					margin: 0px 0px 38px 0px;
					background: #e8e8e8;
					padding: 17px 15px 15px;
					border-radius: 5px;
					&::after {
						content: '';
						display: block;
						width: 90%;
						height: 10px;
						background: #fff;
						border: 2px solid #ddd;
						border-top: 0;
						border-radius: 0 0 5px 5px;
						position: absolute;
						bottom: -10px;
						left: 50%;
						transform: translatex(-50%);
					}
				}
			}
		}
	}
}

.hot {
	color: #ee6b51;
}

.done {
	color: #999 !important;
}

.icon-in-active-mode {
	color: #43ff28;
	font-size: 20px !important;
}

.upcoming {
	font-weight: bold;
	color: #777;
}

.add-event-button {
	height: 50px !important;
	width: 160px;
	display: flex;
	align-items: center;
	margin-left: auto;
	border: 0;
	padding: 0;
	background: linear-gradient(to left, #485fed, rgba(255, 44, 118, 0.25)),
		#485fed;
	border-radius: 50px;
	cursor: pointer;
	box-shadow: 0px 0px 40px -9px #485fed;
	&:active {
		position: relative;
		top: 2px;
		left: 2px;
	}
	.add-event-button__title {
		color: #fff;
		padding: 0 18px 0 23px;
		text-shadow: 0px 0px 5px rgba(#000, 0.2);
		font: {
			family: 'Lato';
			size: 15px;
			weight: 600;
		}
	}
	.add-event-button__icon {
		display: inline-block;
		background: rgba(#fff, 0.1);
		padding: 0 17px 0 12px;
		height: 100%;
		i {
			margin: 0;
			color: #fff;
			font-size: 25px;
			padding: 13px 0;
		}
	}
	.v-menu__content {
		z-index: 9999 !important;
	}
}
</style>
