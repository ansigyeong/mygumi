<template>
	<v-app>
		<v-container>
			<header>
				<h2 class="search-title">검색</h2>
				<!-- 검색창 -->
			</header>
			<section>
				<!-- 자동완성 or 검색결과 -->
				<router-view />
			</section>
		</v-container>
	</v-app>
</template>

<script>
export default {
	data() {
		return {};
	},
	components: {},
};
</script>

<style lang="scss" scoped>
.search-title {
	margin-left: 5px;
	font-weight: bold;
	font-size: 20px;
}
</style>
