<template>
	<div id="app">
		<router-view />
		<BottomNav></BottomNav>
		<div class="temp-space"></div>
	</div>
</template>

<script>
import BottomNav from './components/common/BottomNav';

export default {
	components: {
		BottomNav,
	},
};
</script>

<style lang="scss">
@import './assets/css/reset.css';
@import './assets/css/common.css';

@import url(//fonts.googleapis.com/earlyaccess/jejugothic.css);

.jejugothic * {
	font-family: 'Jeju Gothic', sans-serif;
}

.v-application {
	font-family: 'Jeju Gothic', sans-serif !important;
	line-height: 1.5;
}

.temp-space {
	height: 3rem;
}
</style>
