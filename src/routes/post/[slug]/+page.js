// post 1

import _ from "lodash"

export async function load({ params }){
	const pos = params.slug.indexOf('.')
	let post = null
	if (_.endsWith(params.slug,'.md')) {
		post = await import(`../../../../src/md/${params.slug.slice(0,pos)}.md`)
	}

	const content = post.default
	const slug = params.slug
	return {
		content,
		slug
	}
}