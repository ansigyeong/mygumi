<template>
	<div>
		<div class="plan-wrapper">
			<!--======= Header =======-->

			<header class="header">
				<div class="container">
					<span>일정 작성</span>
					<v-row>
						<v-col cols="12">
							<v-text-field label="일정 제목" clearable />
						</v-col>
					</v-row>
				</div>
			</header>

			<!--======= Today =======-->

			<section class="today-box" id="today-box">
				<span class="breadcrumb">여행 날짜</span>
				<!-- <v-col class="my-2 px-1" cols="12" sm="6">
					<v-date-picker
						v-model="date"
						@contextmenu:year="contextMenu"
						@dblclick:date="dblClick"
						@mouseenter:month="mouseEnter"
						@mouseleave:month="mouseLeave"
					></v-date-picker>
				</v-col> -->
				<v-expansion-panels>
					<v-expansion-panel>
						<v-expansion-panel-header>
							May 15, 2018
						</v-expansion-panel-header>
						<v-expansion-panel-content>
							<v-date-picker no-title />
						</v-expansion-panel-content>
					</v-expansion-panel>
				</v-expansion-panels>

				<!-- <div class="plus-icon">
					<i class="ion ion-ios-add"></i>
				</div> -->
			</section>

			<!--======= Upcoming Events =======-->

			<section class="upcoming-events">
				<div class="container">
					<h3>
						여행 일정
					</h3>
					<div class="events-wrapper">
						<div class="event">
							<v-icon class="fire-icon done">mdi-help-circle</v-icon>
							<h4 class="event__point">첫번째 여행지 (퀴즈)</h4>
							<span class="event__duration">약 30분 소요</span>
							<p class="event__description">
								황상동 52-3번지
							</p>
						</div>
						<div class="event">
							<v-icon class="fire-icon done">mdi-flag-checkered</v-icon>
							<h4 class="event__point">두번째 여행지 (장소)</h4>
							<span class="event__duration">약 1시간 소요</span>
							<p class="event__description">
								진평동 373번지
							</p>
						</div>
						<div class="event">
							<v-icon class="fire-icon done">mdi-airballoon</v-icon>
							<h4 class="event__point">세번째 여행지 (활동)</h4>
							<span class="event__duration">약 45분 소요</span>
							<p class="event__description">
								옥계동 3-23번지
							</p>
						</div>
						<div class="event">
							<v-icon class="fire-icon done">mdi-food</v-icon>
							<h4 class="event__point">네번째 여행지 (음식)</h4>
							<span class="event__duration">약 20분 소요</span>
							<p class="event__description">
								산동면 32번지
							</p>
						</div>
						<v-row class="event active">
							<i class="ion ion-ios-radio-button-on icon-in-active-mode"></i>
							<div>
								<span class="event__point">친구 추가</span>
								<p class="event__description">
									김영주, 안시경
								</p>
							</div>
							<v-spacer />
							<v-btn icon>
								<v-icon>mdi-account-plus</v-icon>
							</v-btn>
						</v-row>
					</div>
					<button class="add-event-button">
						<span class="add-event-button__title">Add Event</span>

						<span class="add-event-button__icon">
							<i class="ion ion-ios-star-outline"></i>
						</span>
					</button>
				</div>
			</section>
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			date: new Date().toISOString().substr(0, 10),
		};
	},
	methods: {},
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
	padding: 10px 0 20px;
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
		// &::after {
		// 	content: '\f3d1';
		// 	font-family: 'Ionicons';
		// 	vertical-align: middle;
		// 	font-size: 12px;
		// 	font-weight: 100;
		// 	display: inline-block;
		// 	color: #fff;
		// 	text-align: center;
		// 	position: absolute;
		// 	left: 70px;
		// 	top: 3px;
		// }
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
	// .plus-icon {
	// 	border: 2px solid rgba(#fff, 0.6);
	// 	border-radius: 50%;
	// 	box-shadow: 0px 10px 30px -14px #000;
	// 	position: absolute;
	// 	top: 50%;
	// 	transform: translateY(-50%);
	// 	right: 40px;
	// 	cursor: pointer;
	// 	transition: all 350ms ease;
	// 	transition-timing-function: cubic-bezier(0.05, 1.8, 1, 1.57);
	// 	&:hover {
	// 		transform: translateY(-40%);
	// 	}
	// 	i {
	// 		font-size: 22px;
	// 		font-weight: 700;
	// 		background: #fff;
	// 		color: #777;
	// 		width: 45px;
	// 		height: 45px;
	// 		border: 6px solid #485fed;
	// 		border-radius: 50%;
	// 		display: flex;
	// 		align-items: center;
	// 		justify-content: center;
	// 	}
	// 	&:active {
	// 		top: 52%;
	// 		transform: translatey(-52%);
	// 		right: 38px;
	// 		box-shadow: 0px 8px 30px -14px #000;
	// 	}
	// }
}

.upcoming-events {
	margin-top: 10px;
	.container {
		h3 {
			color: #333;
			font-size: 17px;
			margin-bottom: 30px;
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
			// &::after {
			// 	content: '\f3ff';
			// 	font-family: 'Ionicons';
			// 	color: rgba(0, 0, 0, 0.1);
			// 	vertical-align: middle;
			// 	font-size: 36px;
			// 	font-weight: 100;
			// 	display: inline-block;
			// 	background: #fff;
			// 	color: #919294;
			// 	width: 38px;
			// 	text-align: center;
			// 	position: absolute;
			// 	right: 60px;
			// 	top: -10px;
			// }
		}
		.events-wrapper {
			margin-bottom: 30px;
			.event {
				position: relative;
				margin-bottom: 25px;
				padding-left: 30px;
				cursor: pointer;
				.fire-icon {
					font-size: 24px;
					font-weight: 100;
					position: absolute;
					left: 0;
					top: -4px;
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
					top: 5px;
					right: 0;
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
					// i {
					// 	position: absolute;
					// 	left: 25px;
					// 	top: 17px;
					// }
					// .event__description {
					// 	&::before,
					// 	&::after {
					// 		content: '\F0014';
					// 		font-family: 'Ionicons';
					// 		font-size: 32px;
					// 		display: inline-block;
					// 		color: #919294;
					// 		text-align: center;
					// 		position: absolute;
					// 		right: 30px;
					// 		top: 50%;
					// 		transform: translateY(-50%);
					// 		cursor: pointer;
					// 	}
					// 	&::before {
					// 		right: 45px;
					// 		font-size: 22px;
					// 		transition: all 550ms ease;
					// 		transition-timing-function: cubic-bezier(0.05, 1.8, 1, 1.57);
					// 	}
					// }
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
</style>
