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
<script
	type="text/javascript"
	src="//dapi.kakao.com/v2/maps/sdk.js?appkey=ee44fe7d97581683a916ae26e90c5ba1"
></script>
<template>
	<div>
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
	data() {
		return {
			container: document.getElementById('map'),
			options: {
				center: new kakao.maps.LatLng(33.450701, 126.570667),
				level: 3,
			},
			map: new kakao.maps.Map(container, options),
		};
	},
};
</script>

<style></style>
