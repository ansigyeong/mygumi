import { auth } from '@/api/index';

function fetchProfile(userId) {
	return auth.get(`user/${userId}/`);
}
function updateProfile(userId, userData) {
	return auth.patch(`user/${userId}/`, userData);
}
function getMap(userId) {
	return auth.get(`user/${userId}/visited/`);
}
// function updateImage(userId, userImage) {
// 	return auth.patch(`user/${userId}`, userImage);
// }
function fetchUsers() {
	return auth.get('user/users/');
}

export { fetchProfile, updateProfile, fetchUsers, getMap };
