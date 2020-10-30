<template>
	<section>
		<header class="review-header">
			<i class="icon ion-md-close"></i>
			<p class="header-title">후기 작성</p>
			<p class="header-back">작성</p>
		</header>
		<TiptapEditor :status="status" />
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
		};
	},
	created() {
		this.title = '글 작성';
		this.status = 'create';
	},
};
</script>
<style lang="scss" scoped>
.review-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	border-bottom: 1px solid $lightGray;
	position: sticky;
	top: 0;
	height: 3rem;
	.ion-md-close {
		font-size: 1.5rem;
		transform: translate(50%, -50%);
		margin-left: 10px;
	}
	.header-title {
		font-weight: bold;
	}
	.header-back {
		margin-right: 10px;
	}
}
</style>
