<template>
	<header class="header-box">
		<img class="header-img" src="@/assets/images/logo.png" alt="logo" />
	</header>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.header-box {
	display: flex;
	position: relative;
	margin-top: 16px;
	margin-bottom: 32px;
	justify-content: center;
	.header-img {
		width: 15%;
	}
	.ion-md-notifications {
		position: absolute;
		right: 10px;
		font-size: 26px;
	}
}
</style>
