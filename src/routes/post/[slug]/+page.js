// src/routes/post/[slug]/+page.js

import _ from "lodash"

export async function load({ params }){
	const pos = params.slug.indexOf('.')
	console.log(params.slug.slice(0,pos))
	const post = await import(`../../../md/${params.slug.slice(0,pos)}.md`)

	const content = post.default
	const slug = params.slug
  return {
    content,
		slug
  }
}