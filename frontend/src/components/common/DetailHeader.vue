<template>
	<section class="dh-container">
		<i class="icon ion-md-arrow-back" @click="goToBack"></i>
	</section>
</template>

<script>
export default {
	methods: {
		goToBack() {
			this.$router.go(-1);
		},
	},
};
</script>

<style lang="scss" scoped>
.dh-container {
	display: flex;
	margin-top: 0.7rem;
	margin-bottom: 0.7rem;
	width: 95%;
	i {
		font-size: 1.5rem;
	}
}
</style>
