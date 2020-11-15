<template>
	<v-app>
		<v-container>
			<!-- 헤더 -->
			<div class="card-header">
				<p class="title">미션</p>
				<p class="result">
					🏆 {{ completes.length }}/{{ missions.length + completes.length }}
				</p>
				<hr />
			</div>

			<!-- 미션 카드 -->
			<section class="mission">
				<v-timeline :dense="$vuetify.breakpoint.smAndDown">
					<!-- 완료한 미션 -->
					<v-timeline-item
						v-for="complete in completes"
						:key="complete.id"
						color="cyan lighten-1"
						fill-dot
						right
					>
						<v-card>
							<v-card-title class="cyan lighten-1">
								<v-icon dark size="30" class="mr-4">
									mdi-map-marker-outline
								</v-icon>
								<h5 class="white--text">
									{{ complete.answer }}
								</h5>
							</v-card-title>
							<div style="text-align: center;">
								{{ complete.content }}
							</div>
							<v-divider></v-divider>
							<br />
							<v-img
								:src="`https://k3d201.p.ssafy.io:8080/${complete.image}`"
								max-height="150"
								max-width="250"
								style="margin: auto;"
							></v-img>
							<br />
							<v-divider></v-divider>
							<p style="text-align: center;">
								Mission Complete!
							</p>
						</v-card>
					</v-timeline-item>

					<v-timeline-item
						v-for="mission in missions"
						:key="mission.id"
						color="cyan lighten-1"
						fill-dot
						right
					>
						<!-- 잠긴 미션 -->
						<v-card v-if="!mission.open">
							<v-card-title class="green lighten-1">
								<v-icon class="mr-2" dark size="30">
									mdi-lock
								</v-icon>
								<h5 class="white--text">{{ mission.order }}번째 미션</h5>
							</v-card-title>
							<div style="text-align: center;">
								<v-icon size="100">mdi-lock</v-icon>
								<p>이전 미션을 완료해주세요.</p>
							</div>
						</v-card>
						<!-- 진행중인 미션 -->
						<v-card v-else>
							<v-card-title class="cyan lighten-1">
								<input
									type="text"
									placeholder=" 정답을 입력해주세요."
									v-model="inputData"
									style="font-size: 15px; max-width: 150px; border: solid 1px gray; border-radius: 0.5rem; margin-right: 5px;"
								/>
								<v-btn @click="submitData" small>제출</v-btn>
							</v-card-title>

							<div style="text-align: center;">
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
							<div style="text-align: center;">
								<v-btn v-if="!hint[mission.id]" @click="showHint(mission.id)"
									>힌트 보기</v-btn
								>
								<small v-else>{{ mission.hint }}</small>
							</div>
							<br />
							<v-divider></v-divider>
						</v-card>
					</v-timeline-item>
				</v-timeline>
			</section>
		</v-container>
	</v-app>
</template>

<script>
import { visitCheck } from '@/api/visit';
import { fetchMission } from '@/api/tour';
import Vue from 'vue';

export default {
	data() {
		return {
			inputData: '',
			missions: [],
			completes: [],
			idx: 0,
			hint: [],
		};
	},
	computed: {},
	mounted() {
		this.fetchData();
	},
	watch: {},
	methods: {
		async fetchData() {
			try {
				const territory = this.$route.params.territoryName;
				const { data } = await fetchMission(territory);
				this.missions = data.territory.missions;
				this.missions.forEach(el => {
					el.open = false;
					const temp = el.id;
					this.hint[`${temp}`] = false;
				});
				this.missions[0].open = true;
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
				var tempImg = this.missions[this.idx].image;
				var tempOrder = this.missions[this.idx].order;
				var tempTerritory = this.missions[this.idx].territory;
				this.completes.push({
					answer: tempAnswer,
					content: tempContent,
					hint: tempHint,
					id: tempId,
					image: tempImg,
					order: tempOrder,
					territory: tempTerritory,
				});
				this.missions.shift();
				this.inputData = '';
				if (!this.missions.length) {
					this.runVisitCheck();
				} else {
					this.missions[this.idx].open = true;
				}
				if (
					this.completes.length ==
					this.missions.length + this.completes.length
				) {
					alert('최종장소는 마지막 정답입니다. 해당 장소로 이동해주세요:)');
					this.$router.push('/');
				} else {
					alert('정답입니다 :)');
				}
			} else {
				alert('틀렸습니다 :(');
			}
		},
		showHint(id) {
			Vue.set(this.hint, id, true);
		},
		async runVisitCheck() {
			try {
				const dong = this.$route.params.territoryName;
				const userId = this.$store.getters.getId;
				const form = {
					place: dong,
					check: 1,
					user: userId,
				};
				await visitCheck(this.userPK, form);
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style lang="scss" scoped>
.mission {
	padding-right: 1rem;
	margin-bottom: 10px;
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
