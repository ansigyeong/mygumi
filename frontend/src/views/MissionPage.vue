<template>
	<v-app>
		<v-container>
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
						<v-container style="text-align: center;">
							저수지에서 사진찍기
						</v-container>
						<v-divider></v-divider>
						<v-img
							lazy-src="https://picsum.photos/id/11/10/6"
							max-height="150"
							max-width="250"
							style="margin: 10px;"
							src="https://picsum.photos/id/11/500/300"
						></v-img>
						<v-divider></v-divider>
						<p style="text-align: center;">Mission Complete!</p>
					</v-card>
				</v-timeline-item>

				<v-timeline-item color="amber lighten-1" fill-dot left small>
					<v-card>
						<v-card-title class="amber lighten-1 justify-end">
							<v-icon class="mr-4" dark size="30">
								mdi-map-marker-outline
							</v-icon>
							<h5 class="white--text">
								금오산 둘레길
							</h5>
						</v-card-title>
						<v-container style="text-align: center;">
							둘레길에서 사진찍기
						</v-container>
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
						<v-container style="text-align: center;">
							<v-icon size="100">mdi-lock</v-icon>
							<p>
								이전 미션을 완료해주세요.
							</p>
						</v-container>
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
						<v-container style="text-align: center;">
							<v-icon size="100">mdi-lock</v-icon>
							<p>이전 미션을 완료해주세요.</p>
						</v-container>
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
						<v-container style="text-align: center;">
							<v-icon size="100">mdi-lock</v-icon>
							<p>이전 미션을 완료해주세요.</p>
						</v-container>
					</v-card>
				</v-timeline-item>
			</v-timeline>
		</v-container>
	</v-app>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped></style>
