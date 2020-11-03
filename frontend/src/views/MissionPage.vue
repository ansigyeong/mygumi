<template>
	<v-app>
		<v-container>
			<!-- 헤더 -->
			<div class="card-header">
				<p class="title">미션</p>
				<p class="result">🏆 1/5</p>
				<hr />
			</div>

			<!-- 미션 카드 -->
			<section>
				<v-timeline :dense="$vuetify.breakpoint.smAndDown">
					<v-timeline-item color="purple lighten-2" fill-dot right>
						<v-card>
							<v-card-title class="purple lighten-2">
								<v-icon dark size="30" class="mr-4">
									mdi-map-marker-outline
								</v-icon>
								<h5 class="white--text">
									금오산 저수지
								</h5>
							</v-card-title>
							<div style="text-align: center;">
								저수지에서 사진찍기
							</div>
							<v-divider></v-divider>
							<br />
							<v-img
								lazy-src="https://picsum.photos/id/11/10/6"
								max-height="150"
								max-width="250"
								style="margin: auto;"
								src="https://picsum.photos/id/11/500/300"
							></v-img>
							<br />
							<v-divider></v-divider>
							<p style="text-align: center;">Mission Complete!</p>
						</v-card>
					</v-timeline-item>

					<v-timeline-item color="amber lighten-1" fill-dot left small>
						<v-card>
							<v-card-title class="amber lighten-1">
								<v-icon class="mr-4" dark size="30">
									mdi-map-marker-outline
								</v-icon>
								<h5 class="white--text">
									금오산 둘레길
								</h5>
							</v-card-title>
							<div style="text-align: center;">
								둘레길에서 사진찍기
							</div>
							<v-file-input accept="image/*" label="File input"></v-file-input>
						</v-card>
					</v-timeline-item>

					<v-timeline-item color="cyan lighten-1" fill-dot right>
						<v-card>
							<v-card-title class="cyan lighten-1">
								<v-icon class="mr-4" dark size="30">
									mdi-lock
								</v-icon>
								<h5 class="white--text">
									세 번째 미션
								</h5>
							</v-card-title>
							<div style="text-align: center;">
								<v-icon size="100">mdi-lock</v-icon>
								<p>
									이전 미션을 완료해주세요.
								</p>
							</div>
						</v-card>
					</v-timeline-item>

					<v-timeline-item color="red lighten-1" fill-dot left small>
						<v-card>
							<v-card-title class="red lighten-1">
								<v-icon class="mr-4" dark size="30">
									mdi-lock
								</v-icon>
								<h5 class="white--text">
									네 번째 미션
								</h5>
							</v-card-title>
							<div style="text-align: center;">
								<v-icon size="100">mdi-lock</v-icon>
								<p>이전 미션을 완료해주세요.</p>
							</div>
						</v-card>
					</v-timeline-item>

					<v-timeline-item color="green lighten-1" fill-dot right>
						<v-card>
							<v-card-title class="green lighten-1">
								<v-icon class="mr-2" dark size="30">
									mdi-lock
								</v-icon>
								<h5 class="white--text">
									다섯 번째 미션
								</h5>
							</v-card-title>
							<div style="text-align: center;">
								<v-icon size="100">mdi-lock</v-icon>
								<p>이전 미션을 완료해주세요.</p>
							</div>
						</v-card>
					</v-timeline-item>
				</v-timeline>
			</section>
		</v-container>
	</v-app>
</template>

<script>
export default {
	components: {},
};
</script>

<style lang="scss" scoped>
.card-header {
	margin: 1.5rem;
	.title {
		display: inline-block;
		font-size: 2rem;
		font-weight: bold;
	}
	.result {
		display: inline-block;
		font-size: 1rem;
		float: right;
	}
}
.v-application--wrap {
	min-height: auto;
}
.container {
	padding: 0px;
}
</style>
