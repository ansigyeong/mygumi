<template>
	<v-app>
		<v-container>
			<!-- 헤더 -->
			<div class="card-header">
				<p class="title">미션</p>
				<p class="result">🏆 {{ completes.length }}/{{ missions.length }}</p>
				<hr />
			</div>

			<!-- 미션 카드 -->
			<section class="mission">
				<v-timeline :dense="$vuetify.breakpoint.smAndDown">
					<v-timeline-item
						v-for="mission in missions"
						:key="mission.id"
						color="cyan lighten-1"
						fill-dot
						right
					>
						<!-- 완료한 미션 -->
						<!-- 진행중인 미션 -->
						<v-card>
							<v-card-title v-if="!complete" class="cyan lighten-1">
								<input
									type="text"
									placeholder="정답을 입력해주세요."
									v-model="inputData"
								/>
								<v-btn @click="submitData">제출</v-btn>
							</v-card-title>
							<v-card-title v-if="complete" class="cyan lighten-1">
								<v-icon dark size="30" class="mr-4">
									mdi-map-marker-outline
								</v-icon>
								<h5 class="white--text">
									{{ mission.answer }}
								</h5>
							</v-card-title>
							<div v-if="!complete" style="text-align: center;">
								{{ mission.content }}
							</div>
							<v-divider></v-divider>
							<br />
							<v-img
								:src="`https://k3d201.p.ssafy.io:8080/${mission.image}`"
								max-height="150"
								max-width="250"
								style="margin: auto;"
							></v-img>
							<br />
							<div style="text-align: center;" v-if="!complete">
								<v-btn v-if="!hint" @click="showHint()">힌트 보기</v-btn>
								<small v-if="hint">{{ mission.hint }}</small>
							</div>
							<br />
							<v-divider></v-divider>
							<p style="text-align: center;" v-if="complete">
								Mission Complete!
							</p>
						</v-card>
					</v-timeline-item>

					<!-- 잠긴 미션 -->
					<v-timeline-item
						color="green lighten-1"
						fill-dot
						right
						style="margin-bottom: 100px;"
					>
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
import { fetchMission } from '@/api/tour';
export default {
	data() {
		return {
			inputData: '',
			missions: [],
			completes: [],
			idx: 0,
			complete: false,
			hint: false,
		};
	},
	mounted() {
		this.fetchData();
	},
	methods: {
		async fetchData() {
			try {
				const territory = this.$route.params.territoryName;
				const { data } = await fetchMission(territory);
				this.missions = data.territory.missions;
			} catch (error) {
				console.log(error);
			}
		},
		submitData() {
			var ans = this.inputData;
			if (ans === '') {
				alert('정답을 입력해주세요.');
				return;
			} else if (ans === this.missions[this.idx].answer) {
				var tempAnswer = this.missions[this.idx].answer;
				var tempContent = this.missions[this.idx].content;
				var tempHint = this.missions[this.idx].hint;
				var tempId = this.missions[this.idx].id;
				var tempImg = this.missions[this.idx].imgage;
				var tempOrder = this.missions[this.idx].order;
				var tempTerritory = this.missions[this.idx].territory;
				this.completes.push({
					answer: tempAnswer,
					content: tempContent,
					hint: tempHint,
					id: tempId,
					imgage: tempImg,
					order: tempOrder,
					territory: tempTerritory,
				});
				this.missions.shift();
				this.idx++;
				this.complete = true;
				alert('정답입니다 :)');
				console.log('미션미션미션');
				console.log(this.missions);
				console.log('완료완료완료');
				console.log(this.completes);
			} else {
				alert('틀렸습니다 :(');
			}
		},
		showHint() {
			this.hint = true;
		},
	},
};
</script>

<style lang="scss" scoped>
.mission {
	padding-right: 1rem;
}
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
