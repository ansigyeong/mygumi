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
			<i class="icon ion-md-arrow-back" @click="goToMain"></i>
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
				주소 : {{ locationData.dong }} <br />
				시간 : {{ locationData.time }}
			</v-card-subtitle>
			<v-card-subtitle style="margin: 10px;" v-if="!content == '.'">
				{{ content }}
			</v-card-subtitle>
		</v-card>

		<!-- 지도 -->
		<div
			id="map"
			style="width:95%;height:400px; margin: auto; z-index: 0;"
		></div>
		<hr />
		<div class="no-review" v-if="noReview">💬 후기가 없습니다!</div>
		<div class="review-title" v-else>💬{{ locationData.place }}의 리뷰</div>
		<v-card
			class="mx-auto"
			v-for="review in reviews"
			:key="`review_${review.id}`"
			style="margin: 10px;"
			@click="goToDetail(review.id)"
		>
			<v-img :src="checkImg(review.images)" height="200px"></v-img>

			<v-card-title>
				{{ review.title }}
			</v-card-title>

			<v-card-subtitle>
				{{ review.created_at.slice(0, 10) }}
			</v-card-subtitle>
			<div style="padding: 10px;">
				<v-avatar>
					<img
						:src="`${baseURL}${review.create_user.profile_image.slice(1)}`"
						alt="John"
					/>
				</v-avatar>
				{{ review.create_user.nickname }}
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
			content: null,
			longitude: null,
			latitude: null,
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
		kakaoKEY() {
			return process.env.VUE_APP_KAKAO_KEY;
		},
		noReview() {
			return this.reviews.length === 0 ? true : false;
		},
	},
	updated() {
		if (window.kakao && window.kakao.maps) {
			this.initMap();
		} else {
			const script = document.createElement('script');
			/* global kakao */
			script.onload = () => kakao.maps.load(this.initMap);
			script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${this.kakaoKey}`;
			document.head.appendChild(script);
		}
	},
	methods: {
		checkImg(array) {
			if (array.length === 0) {
				var ramdomNumber = Math.floor(Math.random() * 100) + 1;
				return `https://picsum.photos/500/300?image=${ramdomNumber}`;
			} else {
				var firstImg = array[0];
				var image = firstImg.picture.slice(1);
				return `${this.baseURL}${image}`;
			}
		},
		initMap() {
			var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
			function displayMarker(place) {
				// 마커를 생성하고 지도에 표시합니다
				var marker = new kakao.maps.Marker({
					map: map,
					position: new kakao.maps.LatLng(place.y, place.x),
				});

				// 마커에 클릭이벤트를 등록합니다
				kakao.maps.event.addListener(marker, 'click', function() {
					// 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
					infowindow.setContent(
						'<div style="padding:5px;font-size:12px;">' +
							place.place_name +
							'</div>',
					);
					infowindow.open(map, marker);
				});
			}
			function placesSearchCB(data, status) {
				if (status === kakao.maps.services.Status.OK) {
					// 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
					// LatLngBounds 객체에 좌표를 추가합니다
					var bounds = new kakao.maps.LatLngBounds();

					for (var i = 0; i < data.length; i++) {
						displayMarker(data[i]);
						bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
					}
					// 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
					map.setBounds(bounds);
				}
			}
			var container = document.getElementById('map');
			var options = {
				center: new kakao.maps.LatLng(this.latitude, this.longitude),
				level: 4,
			};
			var map = new kakao.maps.Map(container, options);
			// 장소 검색 객체를 생성합니다
			var ps = new kakao.maps.services.Places();
			// 키워드로 장소를 검색합니다
			ps.keywordSearch('금오산', placesSearchCB);
			map.setMapTypeId(kakao.maps.MapTypeId.HYBRID);
		},

		async fetchData() {
			const locationId = this.$route.params.locationId;
			const { data } = await location(locationId);
			this.locationData = data.data;
			this.reviews = data.data.reviews;
			this.longitude = data.data.longitude;
			this.latitude = data.data.latitude;
			this.content = data.data.content;
		},
<<<<<<< frontend/src/views/LocationPage.vue
=======
		addTravelList() {},
>>>>>>> frontend/src/views/LocationPage.vue
		goWriteReview() {
			const locationId = this.$route.params.locationId;
			this.$router.push(`/location/${locationId}/create`);
		},
		goToDetail(reviewId) {
			const locationId = this.$route.params.locationId;
			this.$router.push(`/location/${locationId}/reviews/${reviewId}`);
		},
		goToMain() {
			// this.$router.push('/');
			this.$router.go(-1);
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
.review-title {
	margin-top: 1rem;
	margin-bottom: 1rem;
	margin-left: 1rem;
	font-size: 1.5rem;
}
.ion-md-arrow-back {
	position: absolute;
	color: black;
	font-size: 1.5rem;
	top: 1rem;
	left: 1rem;
	z-index: 999;
}
.no-review {
	margin-top: 1rem;
	margin-left: 1rem;
	margin-bottom: 2rem;
	font-size: 1.5rem;
}
</style>
