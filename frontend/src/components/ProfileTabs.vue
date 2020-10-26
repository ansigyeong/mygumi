<template>
	<section class="profile-tabs">
		<template>
			<v-tabs v-model="profileTabs" color="black" grow>
				<v-tab>
					<v-icon>mdi-tooltip-image</v-icon>
				</v-tab>
				<v-tab>
					<v-icon>mdi-tooltip-edit</v-icon>
				</v-tab>
			</v-tabs>
		</template>

		<v-tabs-items v-model="profileTabs">
			<v-tab-item>
				<profile-photo />
			</v-tab-item>

			<v-tab-item>
				<!-- <review-card /> -->
			</v-tab-item>
		</v-tabs-items>
	</section>
</template>

<script>
import ProfilePhoto from '@/components/ProfilePhoto.vue';
// import ReviewCard from '@/components/ReviewCard.vue';

export default {
	data() {
		return {
			profileTabs: null, // 선택된 탭 번호
		};
	},
	components: {
		ProfilePhoto,
		// ReviewCard,
	},
};
</script>

<style lang="scss" scoped>
.profile-tabs {
	border-top: 1px solid #eeeeee;
	margin-top: 10px;
}
</style>
