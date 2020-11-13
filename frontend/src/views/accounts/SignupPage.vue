<template>
	<section class="signup-container">
		<img
			class="logo-img"
			src="@/assets/images/logo.png"
			alt="logo"
			@click="goMain"
		/>
		<p class="signup-msg">회원가입</p>
		<div class="signup-box">
			<label class="signup-label" for="email">이메일</label>
			<input
				id="email"
				type="email"
				v-model="signupData.email"
				placeholder="example@example.com"
			/>
		</div>
		<div class="signup-box">
			<label class="signup-label" for="name">이름</label>
			<input
				id="name"
				type="text"
				v-model="signupData.nickname"
				placeholder="김구미"
			/>
		</div>
		<div class="signup-box">
			<label class="signup-label" for="password">비밀번호</label>
			<input
				id="password"
				type="password"
				v-model="signupData.password1"
				placeholder="*********"
			/>
		</div>
		<div class="signup-box">
			<label class="signup-label" for="password">비밀번호 확인</label>
			<input
				id="password"
				type="password"
				v-model="signupData.password2"
				placeholder="*********"
			/>
		</div>
		<button class="submit-btn" @click.prevent="submitForm">회원가입</button>
	</section>
</template>

<script>
import { registerUser, loginUser } from '@/api/auth';
import { mapMutations } from 'vuex';
import cookies from 'vue-cookies';

export default {
	data() {
		return {
			signupData: {
				nickname: '',
				email: '',
				password1: '',
				password2: '',
			},
		};
	},
	methods: {
		...mapMutations(['setUsername', 'setToken', 'setId']),
		async submitForm() {
			try {
				const { data } = await registerUser(this.signupData);
				const tempLoginData = {
					email: this.signupData.email,
					password: this.signupData.password1,
				};
				await loginUser(tempLoginData);
				console.log(data);
				cookies.set('id', data.user.pk);
				cookies.set('username', data.user.username);
				cookies.set('auth-token', data.token);
				this.setUsername(data.user.username);
				this.setToken(data.token);
				this.setId(data.user.pk);
				this.$router.push('/');
			} catch (error) {
				console.log(error);
			}
		},
		goMain() {
			this.$router.push('/');
		},
	},
};
</script>

<style lang="scss" scoped>
.signup-container {
	margin: 5% 3%;
	.logo-img {
		margin-top: 2rem;
		width: 10%;
	}
	.signup-msg {
		font-size: 2rem;
		color: #3e4042;
		margin-top: 1rem;
		margin-bottom: 1rem;
	}
	.signup-box {
		display: flex;
		flex-direction: column;
		label {
			margin-top: 10px;
			margin-bottom: 3px;
		}
		input {
			border: 1px solid #e5e8e9;
			margin-top: 2px;
			border-radius: 3px;
			width: 95%;
			height: 3rem;
			padding: 10px;
		}
	}
	.submit-btn {
		margin-top: 1rem;
		width: 95%;
		height: 3rem;
		background: $gumiBlue;
		color: white;
		font-weight: bolder;
	}
}
</style>
