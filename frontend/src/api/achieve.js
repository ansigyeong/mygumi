import { base } from '@/api/index';

function fetchAchieve(userId) {
	return base.get(`achievements/${userId}`);
}

export { fetchAchieve };
