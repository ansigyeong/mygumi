<!--
여행지 상세 정보

- 참고) 배민, 요기요
- 정보 카드 => 사진( 장소명, 소개 )
- 여행지 추가 버튼 (-> __Travel Page__)
- 주소
- <span style="color:red">지도 API</span>
- 후기 내용 카드 <span style="color:red">(-> __Review Detail Page__)</span>
  - 참고) 유디니</span>
  - 사진
  - 제목
  - 별점
  - 프로필
  - 이름
  - 작성일
- 후기 작성 버튼 (-> __Review Create Page__)
-->
<template>
	<div class="temp">
		<!-- 여행지 정보 -->
		<v-card class="mx-auto">
			<v-img
				class="white--text align-end"
				height="200px"
				src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
			>
				<v-card-title>금오산</v-card-title>
			</v-img>

			<v-card-actions>
				<div>
					<v-btn class="mx-2" fab dark large color="indigo">
						<v-icon dark>
							mdi-plus
						</v-icon>
					</v-btn>
					<small>여행지 추가</small>
				</div>

				<div>
					<v-btn class="mx-2" fab dark large color="indigo">
						<v-icon dark>
							mdi-pencil
						</v-icon>
					</v-btn>
					<small>여행지 후기</small>
				</div>
			</v-card-actions>

			<v-card-subtitle class="pb-0" style="margin: 10px;">
				경북 구미시 남통동 288-2
			</v-card-subtitle>

			<v-card-text class="text--primary" style="margin: 10px;">
				<div>면적: 39.91㎢</div>
				<div>높이: 976.5m (약사봉)</div>
				<div>좌표: 북위 36° 05′ 17″; 동경 128° 18′ 21″″</div>
			</v-card-text>
		</v-card>

		<!-- 지도 -->
		<div id="map" style="width:300px;height:500px;"></div>

		<!-- 후기 => if문으로 변경하기 -->
		<v-card class="mx-auto" style="margin: 10px;">
			<v-img
				src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
				height="200px"
			></v-img>

			<v-card-title>
				단풍 구경은 금오산에서!
			</v-card-title>

			<v-card-subtitle>
				1,000 miles of wonder
			</v-card-subtitle>
		</v-card>

		<v-card class="mx-auto" style="margin: 10px;">
			<v-img
				src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
				height="200px"
			></v-img>

			<v-card-title>
				단풍 구경은 금오산에서!
			</v-card-title>

			<v-card-subtitle>
				1,000 miles of wonder
			</v-card-subtitle>
		</v-card>

		<v-card class="mx-auto" style="margin: 10px;">
			<v-img
				src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
				height="200px"
			></v-img>

			<v-card-title>
				단풍 구경은 금오산에서!
			</v-card-title>
			<v-card-subtitle>
				1,000 miles of wonder
			</v-card-subtitle>
		</v-card>
	</div>
</template>

<script>
export default {
	// data() {
	// 	return {
	// 		container: document.getElementById('map'),
	// 		options: {
	// 			center: new kakao.maps.LatLng(33.450701, 126.570667),
	// 			level: 3,
	// 		},
	// 		map: new kakao.maps.Map(container, options),
	// 	};
	// },
	computed: {
		kakaoKey() {
			return process.env.VUE_APP_KAKAO_KEY;
		},
		kakaoRESTAPI() {
			return process.env.VUE_APP_KAKAO_REST_API_KEY;
		},
	},
	mounted() {
		// console.log(this.kakaoKey);
		if (window.kakao && window.kakao.maps) {
			this.initMap();
			console.log('여기');
		} else {
			const script = document.createElement('script');
			console.log('저기');
			/* global kakao */
			script.onload = () => kakao.maps.load(this.initMap);
			script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${this.kakaoKey}`;
			document.head.appendChild(script);
		}
	},
	methods: {
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
				center: new kakao.maps.LatLng(33.450701, 126.570667),
				level: 3,
			};

			var map = new kakao.maps.Map(container, options);
			// 장소 검색 객체를 생성합니다
			var ps = new kakao.maps.services.Places();
			console.log(ps);
			// 키워드로 장소를 검색합니다
			ps.keywordSearch('금오산', placesSearchCB);
			map.setMapTypeId(kakao.maps.MapTypeId.HYBRID);
		},
	},
	// async keywordToLoaction() {

	// }
};
</script>

<style lang="scss" scoped></style>
