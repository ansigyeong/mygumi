<template>
	<v-app>
		<v-card tile>
			<div class="card-header">
				<p class="title">업적</p>
				<p class="result">🏆 {{ completeList.length }}/{{ toDoList.length }}</p>
				<hr />
			</div>
			<v-list rounded>
				<v-list-item-group v-model="selectedItem" color="primary">
					<v-subheader>완료한 업적</v-subheader>
					<v-list-item v-for="(item, i) in completeList" :key="i">
						<v-list-item-icon>
							<v-icon v-text="item.icon"></v-icon>
						</v-list-item-icon>
						<v-list-item-content>
							<v-list-item-title v-text="item.text"></v-list-item-title>
							<v-list-item-title v-text="item.detail"></v-list-item-title>
						</v-list-item-content>
					</v-list-item>
					<hr />
					<v-subheader>잠겨있는 업적</v-subheader>
					<v-list-item v-for="(item, i) in toDoList" :key="i">
						<v-list-item-icon>
							<v-icon v-text="item.icon"></v-icon>
						</v-list-item-icon>
						<v-list-item-content>
							<v-list-item-title v-text="item.text"></v-list-item-title>
							<v-list-item-title v-text="item.detail"></v-list-item-title>
						</v-list-item-content>
					</v-list-item>
				</v-list-item-group>
			</v-list>
		</v-card>
	</v-app>
</template>

<script>
import { fetchAchieve } from '@/api/achieve';

export default {
	data: () => ({
		selectedItem: 0,
		toDoList: [
			{
				text: '진평동 마스터',
				detail: '진평동에서 미션 10개 완료하기',
				icon: 'mdi-lock',
				jinpyeong: false,
			},
			{
				text: '금오산 정복자',
				detail: '금오산 정상에 오르기',
				icon: 'mdi-lock',
				geumosan: false,
			},
			// {
			// 	text: '디저트 매니아',
			// 	detail: '디저트 관련 미션 10개 완료하기',
			// 	icon: 'mdi-lock',
			// 	dessert: false,
			// },
			{
				text: '달려라 자전거',
				detail: '구미 자전거 종주길 완주',
				icon: 'mdi-lock',
				bicycle: false,
			},
			{
				text: '서원 러버',
				detail: '서원 코스 챌린지 완료하기',
				icon: 'mdi-lock',
				seowon: false,
			},
			{
				text: '구미 탐험가',
				detail: '랜덤 미션 5개 완료하기',
				icon: 'mdi-lock',
				explorer: false,
			},
			{
				text: '참된 한국인',
				detail: '역사 미션 10개 완료하기',
				icon: 'mdi-lock',
				korean: false,
			},
		],
		completeList: [],
	}),
	mounted() {
		this.fetchData();
	},
	methods: {
		async fetchData() {
			try {
				const userPK = this.$store.getters.getId;
				const { data } = await fetchAchieve(userPK);
				console.log(data);
				this.jinpyeong = data.jinpyeong;
				this.geumosan = data.geumosan;
				this.bicycle = data.bicycle;
				this.seowon = data.seowon;
				this.explorer = data.explorer;
				this.korean = data.korean;
				if (this.jinpyeong === true) {
					this.toDoList.shift();
					this.completeList.unshift({
						text: '진평동 마스터',
						detail: '진평동에서 미션 10개 완료하기',
						icon: 'mdi-medal',
						jinpyeong: true,
					});
				}
				if (this.geumosan === true) {
					this.toDoList.shift();
					this.completeList.unshift({
						text: '금오산 정복자',
						detail: '금오산 정상에 오르기',
						icon: 'mdi-medal',
						geumosan: true,
					});
				}
				if (this.bicycle === true) {
					this.toDoList.shift();
					this.completeList.unshift({
						text: '달려라 자전거',
						detail: '구미 자전거 종주길 완주',
						icon: 'mdi-medal',
						bicycle: true,
					});
				}
				if (this.seowon === true) {
					this.toDoList.shift();
					this.completeList.unshift({
						text: '서원 러버',
						detail: '서원 코스 챌린지 완료하기',
						icon: 'mdi-medal',
						seowon: true,
					});
				}
				if (this.explorer === true) {
					this.toDoList.shift();
					this.completeList.unshift({
						text: '구미 탐험가',
						detail: '랜덤 미션 5개 완료하기',
						icon: 'mdi-medal',
						explorer: true,
					});
				}
				if (this.korean === true) {
					this.toDoList.shift();
					this.completeList.unshift({
						text: '참된 한국인',
						detail: '역사 미션 10개 완료하기',
						icon: 'mdi-medal',
						korean: true,
					});
				}
			} catch (error) {
				console.log(error);
			}
		},
	},
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
</style>
