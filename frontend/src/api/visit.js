import { auth } from '@/api/index';

export function visitCheck(userId, userData) {
	return auth.patch(`user/${userId}/visieted/`, userData);
}
