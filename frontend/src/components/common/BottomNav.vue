<template>
	<div class="nav">
		<div class="nav-slot bg-white round-top-left" @click="goHome">
			<div class="nav-link">
				<v-icon>mdi-home</v-icon>
				<small class="explain"> 홈</small>
			</div>
		</div>

		<div class="nav-slot" @click="goSchedule">
			<div class="floating-button">
				<v-icon color="rgb(255, 255, 255)">mdi-map-marker</v-icon>
				<small class="nav-link" style="display: block; padding: 0px;"
					>여행</small
				>
			</div>
		</div>

		<div class="nav-slot bg-white round-top-right" @click="goProfile">
			<div class="nav-link">
				<v-icon>mdi-account</v-icon>
				<small class="explain"> 프로필</small>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			value: 1,
		};
	},
	methods: {
		goHome() {
			this.$router.push('/');
		},
		goSchedule() {
			this.$router.push('/schedule');
		},
		goProfile() {
			this.$router.push('/profile');
		},
	},
};
</script>

<style scoped>
.nav {
	display: flex;
	justify-content: center;
	flex-direction: row;
	width: 100%;
	height: 50px;
	filter: drop-shadow(0 0 5px rgba(31, 31, 31, 0.1));
	position: fixed;
	bottom: 0;
	z-index: 999;
}

.nav-slot {
	flex-basis: 100%;
	text-align: center;
	height: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color: white;
}

.nav-link {
	align-items: center;
	color: #aab2bd;
	border-radius: 50rem;
	padding: 0.5rem 0.5rem;
	transition: 0.3s all;
}

.explain {
	display: block;
}

.nav-link:hover {
	transition: 0.3s all;
	background: rgba(31, 31, 31, 0.1);
}

.bg-white {
	background: white;
}

.floating-button {
	position: fixed;
	width: 55px;
	height: 55px;
	line-height: 3;
	text-align: center;
	color: #ffce54;
	border-radius: 50%;
	bottom: 20px;
	background-image: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
	box-shadow: 10px 10px 10px -10px #777;
	z-index: 1;
	transition: 0.3s all;
}

.round-top-left {
	border-top-left-radius: 15px;
}

.round-top-right {
	border-top-right-radius: 15px;
}

svg {
	height: 100%;
}
</style>
