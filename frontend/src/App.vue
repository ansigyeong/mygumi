<template>
	<v-app id="app">
		<router-view />
		<BottomNav></BottomNav>
	</v-app>
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

#app {
	min-height: 100vh;
}
</style>
