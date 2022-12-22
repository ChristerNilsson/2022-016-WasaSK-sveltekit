import _ from "lodash"

export const fetchMarkdownPosts = async () => {
	console.log('fetchMarkdownPosts')
	const allPostFiles = import.meta.glob("./../../../src/md/**/*.md")
	const iterablePostFiles = Object.entries(allPostFiles)
	const allPosts = await Promise.all(
		iterablePostFiles.map(async ([path, resolver]) => {
			const { metadata } = await resolver()
			const postPath = '/post' + path.slice(8)

			return {
				meta: metadata,
				path: postPath,
			}
		})
	)

	return allPosts
}

export const fetchHTMLPosts = async () => {
	const allPostFiles = import.meta.glob("./../../../src/html/*.html")
	// console.log('allPostFiles HTML',allPostFiles)
	const iterablePostFiles = Object.entries(allPostFiles)
	const allPosts = await Promise.all(
		iterablePostFiles.map(async ([path, resolver]) => {
			// const { metadata } = await resolver()
			return ({meta: {}, path: '/post' + path.replace('../../html','')})
		}
	))
	
	// console.log(allPosts)
	return allPosts
}