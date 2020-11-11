<template>
	<div class="temp">
		<v-card-actions class="create-btn">
			<div @click="goWriteReview">
				<v-btn class="mx-2" fab dark color="indigo">
					<v-icon dark>
						mdi-pencil
					</v-icon>
				</v-btn>
			</div>
		</v-card-actions>
		<!-- 여행지 정보 -->
		<v-card class="mx-auto">
			<v-img
				class="white--text align-end"
				height="200px"
				:src="`${baseURL}${locationImg}`"
				alt="location-img"
			>
			</v-img>
			<div class="location-title">
				{{ locationData.place }}
			</div>
			<v-card-subtitle class="pb-0" style="margin: 10px;">
				주소 : {{ locationData.dong }}
			</v-card-subtitle>
		</v-card>

		<v-card
			class="mx-auto"
			v-for="review in reviews"
			:key="`review_${review.id}`"
			style="margin: 10px;"
			@click="goToDetail(review.id)"
		>
			<v-img
				src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
				height="200px"
			></v-img>

			<v-card-title>
				{{ review.title }}
			</v-card-title>

			<v-card-subtitle>
				{{ review.created_at }}
			</v-card-subtitle>
			<div style="padding: 10px;">
				<v-avatar>
					<img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
				</v-avatar>
				{{ review.user }}
			</div>
		</v-card>
	</div>
</template>

<script>
import { location } from '@/api/tour';

export default {
	data() {
		return {
			reviews: [],
			locationData: null,
		};
	},
	created() {
		this.fetchData();
	},
	computed: {
		baseURL() {
			return process.env.VUE_APP_API_URL;
		},
		locationImg() {
			if (this.locationData !== null) {
				const imgURL = this.locationData.image.slice(1);
				return imgURL;
			}
			return '';
		},
	},
	mounted() {},
	methods: {
		async fetchData() {
			const locationId = this.$route.params.locationId;
			const { data } = await location(locationId);
			this.locationData = data.data;
			this.reviews = data.data.reviews;
		},
		goWriteReview() {
			const locationId = this.$route.params.locationId;
			this.$router.push(`/location/${locationId}/create`);
		},
		goToDetail(reviewId) {
			const locationId = this.$route.params.locationId;
			this.$router.push(`/location/${locationId}/reviews/${reviewId}`);
		},
	},
};
</script>

<style lang="scss" scoped>
.temp {
	position: relative;
	.create-btn {
		position: fixed;
		bottom: 3rem;
		right: 1rem;
		z-index: 999;
	}
	.location-title {
		margin-top: 1rem;
		text-align: center;
		font-size: 2rem;
	}
}
</style>
