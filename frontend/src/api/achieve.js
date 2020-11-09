import { base } from '@/api/index';

function achieve(userId) {
	return base.get(`achievements/${userId}`);
}

export { achieve };
