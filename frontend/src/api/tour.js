
import { base } from '@/api/index';

export function location(placeId) {
	return base.get(`tour/place/${placeId}`);
}

export function courseTour(courseId) {
	return base.get(`tour/${courseId}`);
}
