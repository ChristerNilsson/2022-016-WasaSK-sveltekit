// src/routes/query/[slug]/+page.js

export const load = async ({ fetch, params }) => {
	const { slug } = params	
	return {slug}
}