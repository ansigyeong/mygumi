import { auth } from '@/api/index';

export function scheduleList(userId) {
	return auth.get(`schedule/${userId}/`);
}
export function addSchedule(userId, scheduleData) {
	return auth.post(`schedule/${userId}/`, scheduleData);
}
export function addPlace(placeId, schedulePk) {
	console.log('장소 정보');
	console.log(placeId);
	console.log('스케쥴 정보');
	console.log(schedulePk);
	return auth.post(`schedule/${placeId}/${schedulePk}/`);
}
