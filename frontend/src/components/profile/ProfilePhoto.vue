<template>
	<v-container fluid>
		<v-row>
			<!-- 클릭시 크게보기 -->
			<v-col v-for="i in 25" :key="i" cols="4" style="padding: 1px;">
				<v-img
					:src="`https://picsum.photos/500/300?image=${i * 5 + 10}`"
					aspect-ratio="1"
				/>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
export default {};
</script>

<style></style>
