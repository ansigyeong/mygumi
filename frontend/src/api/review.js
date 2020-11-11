import { auth } from '@/api/index';

function submitArticle(articleData) {
	return auth.post('review/', articleData);
}

function fetchArticle(articleId) {
	return auth.get(`review/${articleId}`);
}
export { submitArticle, fetchArticle };
