<template>
	<section>
		<TiptapEditor :locationId="locationId" :status="status" />
	</section>
</template>

<script>
import TiptapEditor from '@/components/review/TiptapEditor.vue';
export default {
	components: {
		TiptapEditor,
	},
	data() {
		return {
			status: null,
			locationId: this.$route.params.locationId,
		};
	},
	created() {
		this.status = 'create';
	},
};
</script>
<style lang="scss" scoped></style>
