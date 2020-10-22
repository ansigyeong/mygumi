<template>
	<v-bottom-navigation :value="value" color="primary" grow>
		<v-btn>
			<span>HOME</span>

			<v-icon>mdi-home</v-icon>
		</v-btn>

		<v-btn>
			<span>GO</span>

			<v-icon>mdi-map-marker</v-icon>
		</v-btn>

		<v-btn>
			<span>PROFILE</span>

			<v-icon>mdi-account</v-icon>
		</v-btn>
	</v-bottom-navigation>
</template>

<script>
export default {
	data() {
		return {
			value: 1,
		};
	},
};
</script>

<style></style>
