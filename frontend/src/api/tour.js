import { base } from '@/api/index';

function location(placeId) {
	return base.get(`tour/place/${placeId}`);
}

export { location };
