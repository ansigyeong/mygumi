<template>
	<section>
		<v-row>
			<v-col class="profile-info">
				<section class="profile-user">
					<v-avatar size="90">
						<img :src="`${baseURL}${profileImg}`" alt="profile-image" />
					</v-avatar>
					<p class="profile-name">
						{{ userName }}
					</p>
				</section>
			</v-col>

			<!-- 업적(클릭시 업적 목록으로 이동) -->
			<v-col class="profile-active" @click="goAchievePage">
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
						@click="openEdit"
					>
						프로필 편집
					</v-btn>
				</template>
				<v-card>
					<v-form>
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
									@click="updateInfo"
								>
									완료
								</v-btn>
							</v-toolbar-items>
						</v-toolbar>
						<v-list subheader class="profile-edit">
							<v-avatar size="90" class="profile-edit-image">
								<!-- <img
									id="edit-profile-image"
									:src="editImage"
									alt="profile-image"
								/> -->
							</v-avatar>
							<!-- <button type="file" class="btn-update__info">
								사진수정
							</button> -->
							<input
								ref="inputFile"
								type="file"
								accept="image/*"
								@change="onChangeFile"
								class="fake-btn"
							/>

							<v-form ref="editForm" v-model="editValid" lazy-validation>
								<v-list-item>
									<v-text-field
										v-model="editData.email"
										label="아이디"
										readonly
									></v-text-field>
								</v-list-item>
								<v-list-item>
									<v-text-field
										v-model="editData.nickname"
										:counter="10"
										:rules="nameRules"
										label="이름"
										clearable
										required
									></v-text-field>
								</v-list-item>
							</v-form>
						</v-list>
					</v-form>
				</v-card>
			</v-dialog>

			<v-spacer />
			<v-btn style="width: 28%" color="red" outlined @click="logoutUser">
				로그아웃
			</v-btn>
		</v-row>
	</section>
</template>

<script>
import { fetchProfile, updateProfile } from '@/api/profile';
import { mapMutations } from 'vuex';

export default {
	data() {
		return {
			achieveCnt: 0, // 완료한 업적 수
			travelCnt: 0, // 작성된 여행일정 수
			reviewCnt: 0, // 작성된 후기 수

			profileEdit: false,
			editValid: true,

			userInfo: [],
			userId: null,
			email: '',
			userName: '', // 유저 이름
			profileImg: null, // 유저 프로필 이미지

			editImage: null,
			uploadImage: null,
			editData: {
				profile_image: null,
				nickname: '',
				email: '',
			},
			nameRules: [
				v => !!v || '이름을 입력해주세요.',
				v => (v && v.length <= 10) || '10글자 이내로 입력해주세요.',
			],
			pwdRules: {
				required: value => !!value || '비밀번호를 입력해주세요.',
				min: v => v.length >= 8 || '비밀번호가 너무 짧습니다.',
				check: v => this.password1 == v || '비밀번호가 일치하지 않습니다.',
			},
			changeImage: '',
		};
	},
	mounted() {
		this.fetchData();
	},
	computed: {
		baseURL() {
			return process.env.VUE_APP_API_URL;
		},
	},
	methods: {
		...mapMutations(['clearUsername', 'clearToken', 'clearId']),
		async fetchData() {
			try {
				const userPK = this.$store.getters.getId;
				const { data } = await fetchProfile(userPK);
				this.userId = userPK;
				this.profileImg = data.user.profile_image.slice(1);
				console.log(data.user);
				this.userName = data.user.nickname;
				this.email = data.user.email;

				this.editData.profile_image = this.profileImg;
			} catch (error) {
				console.log(error);
			}
		},
		previewImage(e) {
			if (e) {
				console.log(e);
				// var fileImage = document.getElementById('profile-file-upload');
				// const formData = new FormData();
				// formData.append('profile_image', fileImage.files[0]);
				// console.log('이건 뭐?');
				// console.log(fileImage.files[0]);
				// this.editData.profile_image = formData;
				// console.log(formData.get('profile_image'));
				// this.editData.profile_image = URL.createObjectURL(e);
				window.$('#edit-profile-image').attr('src', URL.createObjectURL(e));
			}
		},
		openEdit() {
			this.editData.nickname = this.userName;
			this.editData.email = this.email;
			this.editImage = this.profileImg;
		},
		goAchievePage() {
			this.$router.push('/achieve');
		},
		goToSchedule() {
			this.$router.push('/schedule');
		},
		// async patchImage(img) {
		// 	try {
		// 		// const id = this.$store.getters.getId;
		// 		const formdata = new FormData();
		// 		formdata.append('profile_image', img);
		// 		// await updateImage(id, formdata);
		// 	} catch (error) {
		// 		bus.$emit('show:warning', '이미지를 가져오는데 실패했어요 :(');
		// 	}
		// },

		// validateFile(file) {
		// 	const imageArray = ['image/png', 'image/jpg', 'image/jpeg'];
		// 	if (imageArray.includes(file.type)) return true;
		// 	return false;
		// },
		onChangeFile() {
			try {
				console.log('@@');
			} catch (error) {
				console.log(error);
			}
		},
		async updateInfo() {
			try {
				const changeImage = this.$refs.inputFile.files[0];
				const formdata = new FormData();
				formdata.append('profile_image', changeImage);
				formdata.append('nickname', this.editData.nickname);
				formdata.append('email', this.editData.email);
				await updateProfile(this.userId, formdata);
				this.$router.go('');
			} catch (error) {
				console.log(error);
			}
		},
		logoutUser() {
			this.clearUsername();
			this.clearToken();
			this.clearId();
			this.$cookies.remove('auth-token');
			this.$cookies.remove('username');
			this.$cookies.remove('id');
			this.$router.push('/');
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
	.btn-update__info {
		margin-right: 0.5rem;
		position: relative;
		width: 150px;
		height: 40px;
		color: white;
		font-size: 1rem;
		background: green;
		border-radius: 15px;
		border: none;
		margin: 0 auto;
		&:hover {
			cursor: pointer;
			background: green;
		}
	}
	.fake-btn {
		cursor: pointer;
		margin-left: 2rem;
		width: 100%;
		height: 100%;
	}
}
</style>
