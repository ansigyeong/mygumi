import { base } from './index';

export function registerUser(userData) {
	console.log(userData);
	return base.post('rest-auth/signup/', userData);
}
export function loginUser(userData) {
	return base.post('rest-auth/login/', userData);
}
