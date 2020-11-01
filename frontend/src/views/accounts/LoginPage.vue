<template>
	<section class="login-container">
		<div class="temp"></div>
		<p class="login-msg">로그인</p>
		<div class="login-box">
			<label class="login-label" for="email">이메일</label>
			<input id="email" type="email" v-model="email" />
		</div>
		<div class="login-box">
			<label class="login-label" for="password">비밀번호</label>
			<input id="password" type="password" v-model="password" />
			<span class="login-msg"></span>
		</div>
	</section>
</template>

<script>
export default {
	data() {
		return {
			email: '',
			password: '',
		};
	},
	methods: {},
};
</script>

<style lang="scss" scoped>
.login-container {
	margin: 5% 3%;
}
.temp {
	width: 100px;
	height: 50px;
	background: $gumiBlue;
}
.login-box {
	display: flex;
	flex-direction: column;
}
</style>
