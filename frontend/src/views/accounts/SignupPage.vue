<template>
	<section class="signup-container">
		<p class="signup-msg">회원가입</p>
		<div class="signup-box">
			<label class="signup-label" for="email">이메일</label>
			<input id="email" type="email" v-model="email" />
		</div>
		<div class="signup-box">
			<label class="signup-label" for="name">이름</label>
			<input id="name" type="text" v-model="username" />
		</div>
		<div class="signup-box">
			<label class="signup-label" for="password">비밀번호</label>
			<input id="password" type="password" v-model="password1" />
		</div>
		<div class="signup-box">
			<label class="signup-label" for="password">비밀번호 확인</label>
			<input id="password" type="password" v-model="password2" />
		</div>
	</section>
</template>

<script>
import { registerUser } from '@/api/auth';
export default {
	data() {
		return {
			signupData: {
				email: '',
				username: '',
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
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style lang="scss" scoped></style>
