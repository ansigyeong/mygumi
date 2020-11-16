<template>
	<section class="main-container">
		<AppHeader />
		<div class="main-history" v-if="isLogin">
			<p class="main-history__text">{{ username }}! 어디까지 가봤니?</p>
			<div class="main-history__imgbox">
				<img
					class="main-history__img"
					src="@/assets/images/gumi_map.png"
					alt="map"
				/>
				<img
					v-if="mapData.진평동"
					class="flag flag-jinpeong"
					src="@/assets/images/flag.png"
					alt="flag"
				/>
				<img
					v-if="mapData.선산읍"
					class="flag flag-seonsan"
					src="@/assets/images/flag.png"
					alt="flag"
				/>
				<img
					v-if="mapData.인동"
					class="flag flag-in"
					src="@/assets/images/flag.png"
					alt="flag"
				/>
			</div>
		</div>
		<div class="main-box">
			<p class="main-box__text">오늘은 어디로 가볼까?</p>
			<div class="main-box__fakeInput" @click="goToSearchPage">
				<i class="icon ion-md-search"></i>
				<p class="placeholder">검색</p>
			</div>
		</div>
		<section class="recommend-box">
			<p class="recommend-title">
				여기는 어때?
			</p>
			<section class="recommend-card">
				<img
					class="recommend-img"
					src="@/assets/images/course2.png"
					alt="recommendImg"
					@click="goToCoursePage(1)"
				/>
			</section>
			<section class="recommend-card">
				<img
					class="recommend-img"
					src="@/assets/images/course1.png"
					alt="recommendImg"
					@click="goToCoursePage(2)"
				/>
			</section>
		</section>
	</section>
</template>

<script>
import AppHeader from '@/components/common/AppHeader.vue';
import { mapGetters } from 'vuex';
import { fetchProfile, getMap } from '@/api/profile';

export default {
	data() {
		return {
			username: null,
			mapData: {
				진평동: false,
				인동: false,
				선산읍: false,
			},
		};
	},
	components: {
		AppHeader,
	},
	computed: {
		...mapGetters(['isLogined']),
		isLogin() {
			return this.isLogined;
		},
	},
	created() {
		if (this.isLogined) {
			this.fetchData();
			this.fetchMap();
		}
	},
	methods: {
		async fetchData() {
			const userId = this.$store.getters.getId;
			const { data } = await fetchProfile(userId);
			this.username = data.user.nickname;
		},
		async fetchMap() {
			const userId = this.$store.getters.getId;
			const { data } = await getMap(userId);
			data.visited.forEach(el => {
				const place = el.place;
				this.mapData[`${place}`] = true;
			});
		},
		goToSearchPage() {
			this.$router.push('/search');
		},
		goToCoursePage(courseId) {
			this.$router.push(`/course/${courseId}`);
		},
	},
};
</script>

<style lang="scss" scoped>
.main-container {
	margin-left: 5%;
	margin-right: 5%;
	.main-history {
		margin-bottom: 1.1rem;
		.main-history__text {
			font-size: 1.2rem;
			margin-bottom: 1rem;
		}
		.main-history__imgbox {
			position: relative;
			display: flex;
			flex-direction: center;
			justify-content: center;
			.main-history__img {
				width: 90%;
			}
			.flag {
				position: absolute;
				width: 8%;
			}
			.flag-seonsan {
				top: 30%;
				left: 37%;
			}
			.flag-jinpeong {
				top: 72%;
				right: 33%;
			}
			.flag-in {
				top: 74%;
				right: 24%;
			}
		}
	}
	.main-box {
		display: flex;
		flex-direction: column;
		width: 100%;
		.main-box__text {
			font-size: 20px;
			font-weight: bolder;
			margin-left: 5px;
			margin-bottom: 25px;
		}
		.main-box__fakeInput {
			width: 100%;
			height: 45px;
			border: 1px solid $Gray;
			border-radius: 10px;
			display: flex;
			align-items: center;
			padding: 0 10px;
			color: $lightGray;
			.ion-md-search {
				font-size: 25px;
				margin-right: 10px;
			}
			.placeholder {
				font-size: 15px;
			}
		}
	}
	.recommend-box {
		display: flex;
		flex-direction: column;
		width: 100%;
		margin-top: 32px;
		.recommend-title {
			font-size: 18px;
			margin-bottom: 16px;
		}
		.recommend-card {
			margin-bottom: 16px;
			.recommend-img {
				width: 100%;
				height: 180px;
				border-radius: 10px;
			}
		}
	}
}
</style>
