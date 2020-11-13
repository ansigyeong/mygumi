<template>
	<v-app>
		<div class="plan-wrapper">
			<!--======= Header =======-->

			<header class="header">
				<div class="container">
					<span>일정 작성</span>
				</div>
			</header>

			<!--======= Today =======-->

			<section class="today-box" id="today-box">
				<span class="breadcrumb">여행 날짜</span>
				<v-expansion-panels>
					<v-expansion-panel>
						<v-expansion-panel-header>
							{{ viewDate }}
						</v-expansion-panel-header>
						<v-expansion-panel-content>
							<v-date-picker no-title v-model="selectDate" />
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
					<v-col cols="12" style="padding:32px 0px 0px;">
						<v-form ref="scheduleForm" v-model="scheduleValid" lazy-validation>
							<v-text-field
								v-model="scheduleData.title"
								label="일정 제목"
								placeholder="일정 제목을 입력해주세요."
								:counter="25"
								outlined
								dense
								clearable
								:rules="titleRules"
							/>
						</v-form>
					</v-col>
					<div class="events-wrapper">
						<div class="event" v-for="plan in plans" :key="plan.id">
							<div v-if="!deletePlace.includes(plan.id)">
								<h4 class="event__point">{{ plan.place }}</h4>
								<!-- <span class="event__duration">약 30분 소요</span> -->
								<p class="event__description">
									{{ plan.dong }}
								</p>
								<v-btn
									class="fire-icon"
									color="error"
									icon
									@click="removePlace(plan.id)"
								>
									<v-icon>mdi-close-circle</v-icon>
								</v-btn>
							</div>
						</div>
						<div class="event" v-if="!courseId || allDelete">
							<p style="text-align:center; margin:30px auto 50px;">
								선택된 코스가 없습니다.
							</p>
							<!-- 작성중(제목, 유저, 날짜)이면 저장 -->
							<!-- 코스Id 널 -->
							<!-- 코스검색 페이지로 이동 -->
							<!-- 검색후 생성 페이지로 와서 코스정보, 작성중정보 불러오기 -->
							<v-btn style="width:100%; margin-bottom:20px;"
								>코스 추가하기</v-btn
							>
						</div>
						<v-row class="event active">
							<i class="ion ion-ios-radio-button-on icon-in-active-mode"></i>
							<div style="width: 70%;">
								<span class="event__point">친구 추가</span>
								<br />
								<span
									v-for="(friend, index) in selectFriends"
									:key="index"
									class="event__description"
								>
									{{ friend }}
								</span>
							</div>
							<v-spacer />
							<v-btn icon @click="modalFriends = true">
								<v-icon>mdi-account-plus</v-icon>
							</v-btn>
						</v-row>
						<v-dialog v-model="modalFriends" max-width="500px">
							<v-card>
								<v-card-title>
									친구 추가
								</v-card-title>
								<v-card-text>
									<v-col cols="12">
										<v-autocomplete
											v-model="selectFriends"
											:items="userList"
											filled
											chips
											color="blue-grey lighten-2"
											label="친구 추가"
											item-text="nickname"
											item-value="nickname"
											multiple
										>
											<template v-slot:selection="addFriend">
												<v-chip
													v-bind="addFriend.attrs"
													:input-value="addFriend.selected"
													close
													@click="addFriend.select"
													@click:close="removeFriend(addFriend.item)"
												>
													<v-avatar left>
														<v-img
															:src="
																'https://k3d201.p.ssafy.io:8080' +
																	addFriend.item.profile_image
															"
														></v-img>
													</v-avatar>
													{{ addFriend.item.nickname }}
												</v-chip>
											</template>

											<template v-slot:item="friends">
												<!-- todo 1. 나 빼고 띄우기 -->
												<template>
													<v-row style="margin:0px">
														<v-list-item-avatar>
															<img
																:src="
																	'https://k3d201.p.ssafy.io:8080' +
																		friends.item.profile_image
																"
															/>
														</v-list-item-avatar>
														<v-list-item-content>
															<v-list-item-title v-html="friends.item.nickname">
															</v-list-item-title>
															<v-list-item-subtitle>{{
																friends.item.email
															}}</v-list-item-subtitle>
														</v-list-item-content>
													</v-row>
												</template>
											</template>
										</v-autocomplete>
									</v-col>
								</v-card-text>
								<v-card-actions>
									<v-btn color="primary" text @click="modalFriends = false">
										Close
									</v-btn>
								</v-card-actions>
							</v-card>
						</v-dialog>
					</div>

					<v-btn text class="add-event-button" @click="writeSchedule">
						<span class="add-event-button__title">작성</span>
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
import { courseTour } from '@/api/tour';
import { fetchUsers } from '@/api/profile';
import { addSchedule, addPlace, addFriend } from '@/api/schedule';
export default {
	data() {
		return {
			selectDate: new Date().toISOString().substr(0, 10), // 선택한 날짜
			viewDate: null, // 선택된 날짜 형식 변경
			modalFriends: false, // 친구 추가 모달
			selectFriends: [], // 선택한 친구 목록
			scheduleValid: true,
			allDelete: false,
			userList: [],
			userId: null,
			courseId: null,
			scheduleId: null,
			friendId: null,
			plans: [],
			deletePlace: [],
			placeData: [],
			friendData: [],
			titleRules: [
				v => !!v || '제목을 입력해주세요.',
				v => (v && v.length <= 25) || '25글자 이내로 입력해주세요.',
			],
			scheduleData: {
				title: null,
				date: new Date().toISOString().substr(0, 10),
			},
		};
	},
	mounted() {
		this.userId = this.$store.getters.getId;
		this.courseId = this.$store.getters.getCourseId;
		this.usersData();
		this.courseData();
		var today = new Date().toISOString().substr(0, 10);
		// 월만 따로 저장
		var todayMonth = today[5] + today[6];
		// 일만 따로 저장
		var todayDate = today[9];
		if (today[8]) {
			todayDate = today[8] + today[9];
		}
		// 년도만 따로 저장
		var todayYear = today[0] + today[1] + today[2] + today[3];
		this.viewDate = todayMonth + '월 ' + todayDate + '일, ' + todayYear + '년';

		// 캘린더 css 변경
		window.$('.v-expansion-panels').click(() => {
			var dateToggle = window.$('.v-expansion-panel')[0].ariaExpanded;
			if (dateToggle == 'true') {
				window.$('.v-picker__body')[0].style.width = 'auto';
				// window.$('.v-btn--active')[0].style.color = 'black';
			}
		});
	},
	watch: {
		selectDate() {
			this.scheduleData.date = this.selectDate;
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
		},
	},
	methods: {
		// 친구 선택 취소
		removeFriend(item) {
			const index = this.selectFriends.indexOf(item.nickname);
			if (index >= 0) this.selectFriends.splice(index, 1);
		},
		// 장소 선택 취소
		removePlace(placeId) {
			const deleteAgree = confirm('정말로 이 장소를 삭제하시겠습니까?');
			if (deleteAgree) {
				this.deletePlace.push(placeId);

				if (this.deletePlace.length == this.plans.length) {
					this.allDelete = true;
				}
			}
		},
		// 입력값 확인
		scheduleValidate() {
			this.$refs.scheduleForm.validate();
			if (!this.scheduleData.title) {
				this.scheduleValid = false;
			}
		},
		// 코스 정보 불러오기
		async courseData() {
			try {
				if (this.courseId) {
					const { data } = await courseTour(this.courseId);
					this.plans = data.data;
				}
			} catch (error) {
				console.log(error);
			}
		},
		// 전체 유저 정보 불러오기
		async usersData() {
			try {
				const { data } = await fetchUsers();
				this.userList = data.users;
			} catch (error) {
				console.log(error);
			}
		},
		// 스케쥴 작성
		writeSchedule() {
			this.createSchedule();
		},
		// 스케쥴 생성 요청
		async createSchedule() {
			try {
				this.scheduleValidate();
				if (this.allDelete) {
					alert('코스를 추가해주세요.');
				} else {
					if (this.scheduleValid) {
						const { data } = await addSchedule(this.userId, this.scheduleData);
						this.scheduleId = data.id;

						// 스케쥴 생성 후
						if (this.scheduleId) {
							// 장소 추가
							for (var i = 0; i < this.plans.length; i++) {
								if (!this.deletePlace.includes(this.plans[i])) {
									this.placeData.push(this.plans[i].id);
								}
							}
							this.createPlace();
							// 친구 추가
							for (var j = 0; j < this.selectFriends.length; j++) {
								this.friendId = this.userList.findIndex(item => {
									return item.nickname == this.selectFriends[j];
								});
								this.friendId++;
								if (this.friendId != this.userId) {
									this.friendData.push(this.friendId);
								}
							}
							this.createFriend();
						}
					}
				}
			} catch (error) {
				console.log(error);
			}
		},
		// 장소 추가 요청
		async createPlace() {
			try {
				await addPlace(this.scheduleId, this.placeData);
			} catch (error) {
				console.log(error);
			}
		},
		// 친구 추가 요청
		async createFriend() {
			try {
				await addFriend(this.scheduleId, this.friendData);
				this.$router.push('/schedule');
			} catch (error) {
				console.log(error);
			}
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
	width: 120px;
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
