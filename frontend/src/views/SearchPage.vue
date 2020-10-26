<template>
	<section class="search-container">
		<div class="search-box">
			<input class="search-input" type="text" v-model="inputData" />
			<p class="search-cancle" @click="goToMain">취소</p>
		</div>
		<span class="underline"></span>
	</section>
</template>

<script>
export default {
	data() {
		return {
			inputData: '',
		};
	},
	methods: {
		goToMain() {
			this.$router.push('/');
		},
	},
};
</script>

<style lang="scss" scoped>
.search-container {
	display: flex;
	flex-direction: column;
	margin-top: 5%;
	.search-box {
		display: flex;
		position: relative;
		align-items: center;
		.search-input {
			width: 80%;
			height: 40px;
			border: 1px solid $Gray;
			border-radius: 10px;
			background: rgb(233, 233, 233);
			margin-left: 5%;
			padding: 10px;
		}
		.search-cancle {
			color: blue;
			font-size: 16px;
			margin-left: 3%;
			:hover {
				cursor: pointer;
			}
		}
		.ion-md-search {
			position: absolute;
			font-size: 25px;
			margin-right: 10px;
			top: 8px;
			left: 5px;
		}
	}
	.underline {
		margin-top: 16px;
		background: rgb(233, 233, 233);
		height: 1px;
		width: 100%;
	}
}
</style>
