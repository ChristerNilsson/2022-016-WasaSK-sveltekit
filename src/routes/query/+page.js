// src/routes/query/+page.js
export const load = async ({ fetch, params }) => {
	const { word } = params
	const response = await fetch("/api/posts")
	const allPosts = await response.json()

	const posts = allPosts

	return {
		word,
		posts
	}
}