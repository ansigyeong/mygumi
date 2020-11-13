<template>
	<section class="login-container">
		<img
			class="logo-img"
			src="@/assets/images/logo.png"
			alt="logo"
			@click="goMain"
		/>
		<p class="login-msg">로그인</p>
		<div class="login-box">
			<label class="login-label" for="email">이메일</label>
			<input
				id="email"
				type="email"
				v-model="loginData.email"
				placeholder="example@example.com"
			/>
		</div>
		<div class="login-box">
			<label class="login-label" for="password">비밀번호</label>
			<input
				id="password"
				type="password"
				v-model="loginData.password"
				placeholder="*********"
			/>
			<span class="signup-box" @click="goToSignup">회원가입</span>
		</div>
		<button class="submit-btn" @click.prevent="submitForm">로그인</button>
	</section>
</template>

<script>
import { loginUser } from '@/api/auth';
import { mapMutations } from 'vuex';
import cookies from 'vue-cookies';

export default {
	data() {
		return {
			loginData: {
				email: '',
				password: '',
			},
		};
	},
	methods: {
		...mapMutations(['setUsername', 'setToken', 'setId']),
		async submitForm() {
			try {
				const { data } = await loginUser(this.loginData);
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
		goToSignup() {
			this.$router.push('/signup');
		},
		goMain() {
			this.$router.push('/');
		},
	},
};
</script>

<style lang="scss" scoped>
.login-container {
	margin: 5% 3%;

	.logo-img {
		margin-top: 2rem;
		width: 10%;
	}

	.login-msg {
		font-size: 2rem;
		color: #3e4042;
		margin-top: 1rem;
		margin-bottom: 1rem;
	}
	.login-box {
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
	.signup-box {
		margin-top: 1rem;
		font-size: 12px;
		color: #3e4042;
		text-align: end;
		margin-right: 5%;
		&:hover {
			cursor: pointer;
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
