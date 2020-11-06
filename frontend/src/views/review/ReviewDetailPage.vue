<template>
	<section class="detail-container">
		<DetailHeader />
		<header class="detail-header">
			<section class="user-box">
				<img class="user-profile" src="@/assets/images/temp_gumi.png" alt="" />
				<p class="user-id">dudghkd1</p>
			</section>
			<p class="header-title">TEMP TITLE</p>
			<section class="header-etc">
				<p class="createtime">2020-11-03</p>
				<p>|</p>
				<p class="views">조회 100</p>
			</section>
		</header>
		<article class="detail-body"></article>
		<section class="user-profile"></section>
		<footer class="detail-footer"></footer>
	</section>
</template>

<script>
import DetailHeader from '@/components/common/DetailHeader.vue';
export default {
	components: {
		DetailHeader,
	},
};
</script>

<style lang="scss" scoped>
.detail-container {
	margin-left: 3%;
	margin-right: 3%;
}
.temp-header {
	height: 40px;
}
.detail-header {
	.user-box {
		display: flex;
		align-items: center;
		margin-bottom: 0.5rem;
		.user-profile {
			background: black;
			width: 1.2rem;
			height: 1.2rem;
			border-radius: 50%;
			margin-right: 0.3rem;
		}
		.user-id {
			font-size: 0.7rem;
		}
	}
	.header-title {
		font-size: 1.5rem;
		margin-bottom: 0.3rem;
	}
	.header-etc {
		display: flex;
		color: rgb(161, 160, 160);
		font-size: 0.7rem;
		p {
			margin-right: 0.3rem;
		}
	}
}
</style>
