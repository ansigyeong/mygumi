import { auth } from '@/api/index';

function fetchProfile(userId) {
	return auth.get(`user/${userId}`);
}

export { fetchProfile };
