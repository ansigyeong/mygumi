<template>
	<section>
		<v-row>
			<v-col class="profile-info">
				<section class="profile-user">
					<v-avatar size="90">
						<img :src="profileImg" alt="profile-image" />
					</v-avatar>
					<p class="profile-name">
						{{ userName }}
					</p>
				</section>
			</v-col>

			<!-- 업적(클릭시 업적 목록으로 이동) -->
			<v-col class="profile-active">
				<p class="profile-cnt">{{ achieveCnt }}</p>
				<p class="profile-content">업적</p>
			</v-col>
			<!-- 여행 일정(클릭시 일정리스트로 이동) -->
			<v-col class="profile-active" @click="goToSchedule">
				<p class="profile-cnt">{{ travelCnt }}</p>
				<p class="profile-content">일정</p>
			</v-col>
			<!-- 후기(클릭시 후기 탭으로 이동) -->
			<v-col class="profile-active">
				<p class="profile-cnt">{{ reviewCnt }}</p>
				<p class="profile-content">후기</p>
			</v-col>
		</v-row>

		<v-row class="profile-btn">
			<v-dialog
				v-model="profileEdit"
				fullscreen
				hide-overlay
				transition="dialog-bottom-transition"
			>
				<template v-slot:activator="{ on, attrs }">
					<v-btn
						style="width: 70%;"
						color="grey"
						outlined
						v-bind="attrs"
						v-on="on"
					>
						프로필 편집
					</v-btn>
				</template>
				<v-card>
					<v-toolbar>
						<v-btn icon @click="profileEdit = false">
							<v-icon>mdi-close</v-icon>
						</v-btn>
						<v-toolbar-title>프로필 편집</v-toolbar-title>
						<v-spacer></v-spacer>
						<v-toolbar-items>
							<v-btn
								text
								color="primary"
								style="font-size:18px;"
								:disabled="!editValid"
							>
								완료
							</v-btn>
						</v-toolbar-items>
					</v-toolbar>
					<v-list subheader class="profile-edit">
						<v-avatar size="90" class="profile-edit-image">
							<img :src="profileImg" alt="profile-image" />
						</v-avatar>
						<v-btn text class="profile-edit-icon">
							편집<v-icon>mdi-tooltip-image</v-icon>
						</v-btn>
						<!-- <v-subheader>아이디</v-subheader> -->
						<v-form ref="editForm" v-model="editValid" lazy-validation>
							<v-list-item>
								<v-text-field
									v-model="email"
									label="아이디"
									readonly
								></v-text-field>
							</v-list-item>
							<v-list-item>
								<v-text-field
									v-model="userName"
									:counter="10"
									:rules="nameRules"
									label="이름"
									clearable
									required
								></v-text-field>
							</v-list-item>
							<v-list-item>
								<v-text-field
									v-model="password1"
									:append-icon="pwdShow1 ? 'mdi-eye' : 'mdi-eye-off'"
									:rules="[pwdRules.required, pwdRules.min]"
									:type="pwdShow1 ? 'text' : 'password'"
									label="비밀번호"
									@click:append="pwdShow1 = !pwdShow1"
								></v-text-field>
							</v-list-item>
							<v-list-item>
								<v-text-field
									v-model="password2"
									:append-icon="pwdShow2 ? 'mdi-eye' : 'mdi-eye-off'"
									:rules="[pwdRules.required, pwdRules.min, pwdRules.check]"
									:type="pwdShow2 ? 'text' : 'password'"
									label="비밀번호 확인"
									@click:append="pwdShow2 = !pwdShow2"
								></v-text-field>
							</v-list-item>
						</v-form>
					</v-list>
				</v-card>
			</v-dialog>

			<v-spacer />
			<v-btn style="width: 28%" color="red" outlined>
				로그아웃
			</v-btn>
		</v-row>
	</section>
</template>

<script>
import { fetchProfile } from '@/api/profile';
// import axios from 'axios';
export default {
	data() {
		return {
			achieveCnt: 0, // 완료한 업적 수
			travelCnt: 0, // 작성된 여행일정 수
			reviewCnt: 0, // 작성된 후기 수

			profileEdit: false,
			editValid: true,
			pwdShow1: false,
			pwdShow2: false,

			userInfo: [],
			userId: null,
			email: '',
			userName: '', // 유저 이름
			profileImg: null, // 유저 프로필 이미지
			password1: '',
			password2: '',

			nameRules: [
				v => !!v || '이름을 입력해주세요.',
				v => (v && v.length <= 10) || '10글자 이내로 입력해주세요.',
			],
			pwdRules: {
				required: value => !!value || '비밀번호를 입력해주세요.',
				min: v => v.length >= 8 || '비밀번호가 너무 짧습니다.',
				check: v => this.password1 == v || '비밀번호가 일치하지 않습니다.',
			},
		};
	},
	mounted() {
		this.fetchData();
	},
	methods: {
		// validate() {
		// 	this.$refs.form.validate();
		// },
		async fetchData() {
			try {
				const userPK = this.$store.getters.getId;
				const { data } = await fetchProfile(userPK);
				this.profileImg = data.user.profile_image;
				this.userName = data.user.nickname;
				this.email = data.user.email;
			} catch (error) {
				console.log(error);
			}
		},
		goToSchedule() {
			this.$router.push('/schedule');
		},
	},
};
</script>

<style lang="scss" scoped>
.profile-info {
	max-width: 120px;

	.profile-user {
		width: 90px;
		margin: 0 auto;

		.profile-name {
			text-align: center;
			width: 90px;
			font-weight: bold;
			margin-bottom: 5px;
		}
	}
}
.profile-undefined {
	height: 20px;
}
.profile-active {
	margin-top: 10px;

	.profile-cnt {
		font-size: 25px;
		text-align: center;
		margin: 0px;
	}
	.profile-content {
		text-align: center;
		font-size: 15px;
		margin: 0px;
	}
}
.profile-btn {
	width: 100%;
	margin: 0px;
	box-shadow: none;
	background-color: white !important;
}
.profile-edit {
	.profile-edit-image {
		margin: 30px 38% 0px;
	}
	.profile-edit-icon {
		margin: 0px 39%;
	}
}
</style>
