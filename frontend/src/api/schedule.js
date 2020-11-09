import { auth } from '@/api/index';

export function scheduleList(userId) {
	return auth.get(`schedule/${userId}`);
}
