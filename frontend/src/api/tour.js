import { base, auth } from '@/api/index';

export function location(placeId) {
	return base.get(`tour/place/${placeId}`);
}

export function courseTour(courseId) {
	return base.get(`tour/${courseId}`);
}

export function getHistory(userId) {
	return auth.get(`tour/search/${userId}`);
}

export function getSearch(userId, dong) {
	return auth.get(`tour/search/${userId}/${dong}`);
}

export function deleteHistory(userId, dong) {
	return auth.delete(`tour/search/${userId}/${dong}`);
}
