import { base } from './index';

export function registerUser(userData) {
	return base.post('rest-auth/signup/', userData);
}
export function loginUser(userData) {
	return base.post('rest-auth/login/', userData);
}
