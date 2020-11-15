import { base } from './index';

export function fetchMission(placeId) {
	return base.get(`tour/place/${placeId}/mission/`);
}
