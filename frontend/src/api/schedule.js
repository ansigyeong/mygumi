import { auth } from '@/api/index';

export function scheduleList(userId) {
	return auth.get(`schedule/${userId}/`);
}
export function addSchedule(userId, scheduleData) {
	return auth.post(`schedule/${userId}/`, scheduleData);
}
export function addPlace(schedulePk, placeData) {
	return auth.post(`schedule/${schedulePk}/place/`, placeData);
}
export function addFriend(schedulePk, userData) {
	return auth.post(`schedule/${schedulePk}/invite/`, userData);
}
export function getSchedule(userId, schedulePk) {
	return auth.get(`schedule/${userId}/${schedulePk}/`);
}
export function updateSchedule(userId, schedulePk, scheduleData) {
	return auth.patch(`schedule/${userId}/${schedulePk}/`, scheduleData);
}
export function deletePlace(placeId, schedulePk) {
	return auth.delete(`schedule/${placeId}/${schedulePk}/place/`);
}
export function deleteSchedule(userId, schedulePk) {
	return auth.delete(`schedule/${userId}/${schedulePk}/`);
}
export function deleteFriend(userId, schedulePk) {
	return auth.delete(`schedule/${userId}/${schedulePk}/invite/`);
}
