<template>
	<section class="result-container">
		<div class="fakeinput-box">
			<div class="fakeinput" @click="goToSearch">
				<p class="fakeText">{{ dong }}</p>
			</div>
			<i class="icon ion-md-close" @click="goToMain"></i>
		</div>
		<p class="noResult" v-if="!isSearchArray">찾으시는 장소가 없습니다 :(</p>
		<div></div>
		<hr />
		<p>장소</p>
		<div :key="searchData.id" v-for="searchData in searchArray">
			<SearchCard :searchData="searchData" />
		</div>
	</section>
</template>

<script>
import SearchCard from '@/components/search/SearchCard.vue';
import { getSearch } from '@/api/tour';
export default {
	components: {
		SearchCard,
	},
	data() {
		return {
			searchArray: [],
			courseArrat: [],
			dong: this.$route.params.searchString,
		};
	},
	methods: {
		async fetchData() {
			try {
				const userId = this.$store.getters.getId;
				const dong = this.$route.params.searchString;
				const { data } = await getSearch(userId, dong);
				console.log(data);
				this.searchArray = data;
			} catch (error) {
				console.log(error);
			}
		},
		goToMain() {
			this.$router.push('/');
		},
		goToSearch() {
			this.$router.push('/search');
		},
	},
	created() {
		this.fetchData();
	},
	computed: {
		isSearchArray() {
			return this.searchArray.length !== 0 ? true : false;
		},
	},
};
</script>

<style lang="scss" scoped>
.result-container {
	margin: 5% 3%;
	.fakeinput-box {
		display: flex;
		align-content: center;
		justify-content: space-between;
		margin-bottom: 1.5rem;
		.fakeinput {
			width: 70%;
			height: 40px;
			background: gray;
			border: 1px solid $Gray;
			border-radius: 10px;
			background: rgb(233, 233, 233);
			margin-left: 5%;
			padding: 10px;
		}
		.ion-md-close {
			font-size: 2.5rem;
			margin-right: 2rem;
		}
	}
	.noResult {
		font-size: 1.5rem;
		text-align: center;
	}
}
</style>
