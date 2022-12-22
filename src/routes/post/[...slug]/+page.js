// post 1

import _ from "lodash"

export const prerender = true

export async function load({ params }){
	console.log('params',params)
	const pos = params.slug.indexOf('.')
	let post = null
	if (_.endsWith(params.slug,'.md')) {

		const name = params.slug.replace('.md','')
		const splitName = name.split('/')

		// https://github.com/vitejs/vite/issues/4945#issuecomment-951770052 Troligen orsakad av kodanalys
		if (splitName.length === 1) post = await import(`../../../../src/md/${splitName[0]}.md`)
		if (splitName.length === 2) post = await import(`../../../../src/md/${splitName[0]}/${splitName[1]}.md`)
		if (splitName.length === 3) post = await import(`../../../../src/md/${splitName[0]}/${splitName[1]}/${splitName[2]}.md`)
		if (splitName.length === 4) post = await import(`../../../../src/md/${splitName[0]}/${splitName[1]}/${splitName[2]}/${splitName[3]}.md`)

	} else {
		console.log('unexpected',params.slug)
	}
	// if (_.endsWith(params.slug,'.html')) {
	// 	post = await import(`../../../../src/html/${params.slug.slice(0,pos)}.html`)
	// }
	// if (_.endsWith(params.slug,'.pdf')) {
	// 	console.log(params.slug)
	// 	post = await import(`../../../../src/${params.slug.slice(0,pos)}.pdf`)
	// }

	// console.log('post',post)

	const content = post.default
	const slug = params.slug
	return {
		content,
		slug
	}
}