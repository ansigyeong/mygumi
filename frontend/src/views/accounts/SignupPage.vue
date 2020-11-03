<template>
	<section class="signup-container">
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
				v-model="signupData.username"
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
import { registerUser } from '@/api/auth';

export default {
	data() {
		return {
			signupData: {
				username: '',
				email: '',
				password1: '',
				password2: '',
			},
		};
	},
	methods: {
		async submitForm() {
			try {
				const { data } = await registerUser(this.signupData);
				this.$store.dispatch('SETUP_USER', data);
				this.$store.dispatch('LOGIN', data);
				this.$router.push('/');
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style lang="scss" scoped>
.signup-container {
	margin: 5% 3%;
	.signup-msg {
		font-size: 2rem;
		color: #3e4042;
		margin-top: 2rem;
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
