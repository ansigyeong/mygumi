<template>
	<section>
		<div class="temp-header">헤더가 올자리임 ㅎ</div>
		<header class="detail-header">
			<section class="user-box">
				<img class="user-profile" src="@/assets/images/temp_gumi.png" alt="" />
				<p class="user-id">dudghkd1</p>
			</section>
			<p class="header-title">TEMP TITLE</p>
			<section class="header-etc">
				<p class="createtime"></p>
				<p class="views"></p>
			</section>
		</header>
		<article class="detail-body"></article>
		<section class="user-profile"></section>
		<footer></footer>
	</section>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.temp-header {
	height: 40px;
}
.detail-header {
	.user-box {
		display: flex;
		align-items: center;
		.user-profile {
			background: black;
			width: 1.5rem;
			height: 1.5rem;
			border-radius: 50%;
		}
	}
}
</style>
