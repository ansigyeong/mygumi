<template>
	<section class="search-container">
		<div class="search-box">
			<input class="search-input" type="text" v-model="inputData" />
			<p class="search-cancle" @click="goToMain">취소</p>
			<p class="search-submitBtn" @click="submitData">
				확인
			</p>
		</div>
		<span class="underline"></span>
		<div class="search-history" v-if="!inputData">
			<p class="search-history__text">최근 검색</p>
			<div class="noHistoryText" v-if="!isSearchHistoryArray">
				최근 검색목록이 없어요 :(
			</div>
			<div v-else>
				<div
					class="items"
					:key="item.search"
					v-for="item in searchHistoryArray"
				>
					<i class="icon ion-md-search"></i>
					<p class="item-text" @click="submitHistory(item.search)">
						{{ item.search }}
					</p>
					<i class="icon ion-md-close" @click="deleteData(item.search)"></i>
				</div>
			</div>
		</div>
		<div class="search-auto" v-else>
			<p class="search-auto__text"></p>
			<div class="items"></div>
		</div>
	</section>
</template>

<script>
import { getHistory, getSearch, deleteHistory } from '@/api/tour';

export default {
	data() {
		return {
			inputData: '',
			searchHistoryArray: [],
			searchAutoArray: [],
		};
	},
	methods: {
		goToMain() {
			this.$router.push('/');
		},
		async fetchData() {
			try {
				const userId = this.$store.state.id;
				const { data } = await getHistory(userId);
				this.searchHistoryArray = data;
			} catch (error) {
				console.log(error);
			}
		},
		async deleteData(search) {
			try {
				const userId = this.$store.state.id;
				await deleteHistory(userId, search);
				this.fetchData();
			} catch (error) {
				console.log(error);
			}
		},
		async submitData() {
			try {
				const userId = this.$store.state.id;
				const searchData = this.inputData;
				await getSearch(userId, searchData);
				this.goToResult();
			} catch (error) {
				console.log(error);
			}
		},
		async submitHistory(data) {
			try {
				this.$router.push(`/search/${data}`);
			} catch (error) {
				console.log(error);
			}
		},
		goToResult() {
			this.$router.push(`/search/${this.inputData}`);
		},
	},
	computed: {
		inputDataLength() {
			return !!this.inputData;
		},
		isSearchHistoryArray() {
			return this.searchHistoryArray.length !== 0 ? true : false;
		},
	},
	created() {
		this.fetchData();
	},
};
</script>

<style lang="scss" scoped>
.search-container {
	display: flex;
	flex-direction: column;
	margin-top: 5%;
	margin-left: 3%;
	margin-right: 3%;
	.search-box {
		display: flex;
		position: relative;
		align-items: center;
		.search-input {
			width: 70%;
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
			margin-right: 2%;
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
		margin-bottom: 1rem;
		background: rgb(233, 233, 233);
		height: 1px;
		width: 100%;
	}
}
.search-history__text {
	height: 1rem;
	color: gray;
}
.search-auto__text {
	height: 1rem;
}
.items {
	display: flex;
	justify-content: flex-start;
	color: gray;
	margin-top: 1rem;
	position: relative;
	.item-text {
		margin-left: 1.5rem;
		color: black !important;
	}
	.ion-md-close {
		position: absolute;
		right: 2rem;
	}
}
.noHistoryText {
	margin-top: 1rem;
	text-align: center;
}
.search-submitBtn {
	color: blue;
	font-size: 16px;
	width: 2rem;
}
</style>
