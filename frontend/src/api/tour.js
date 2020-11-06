import { base } from './index';

export function courseTour(courseId) {
	return base.get(`tour/${courseId}`);
}
