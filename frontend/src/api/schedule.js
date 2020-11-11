import { auth } from '@/api/index';

export function scheduleList(userId) {
	return auth.get(`schedule/${userId}/`);
}

export function addSchedule(userId, scheduleData) {
	return auth.post(`schedule/${userId}/`, scheduleData);
}
