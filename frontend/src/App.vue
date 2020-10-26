<template>
	<div id="app">
		<router-view />
		<BottomNav></BottomNav>
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

#app {
	min-height: 100vh;
}
</style>
