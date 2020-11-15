import axios from 'axios';
import { setInterceptors } from '@/api/common/interceptors';

function create(url, options) {
	const instance = axios.create(Object.assign({ baseURL: url }, options));
	return instance;
}

function createWithAuth(url, options) {
	const instance = axios.create(Object.assign({ baseURL: url }, options));
	setInterceptors(instance);
	return instance;
}

export const base = create('https://k3d201.p.ssafy.io:8080/');
export const auth = createWithAuth('https://k3d201.p.ssafy.io:8080/');
