// src/routes/api/posts/+server.js
import { fetchMarkdownPosts } from '$lib/utils'
// import { fetchHTMLPosts } from '$lib/utils'
import { json } from '@sveltejs/kit'

export const prerender = true

export const GET = async () => {
  const allMD = await fetchMarkdownPosts()
  // const allHTML = await fetchHTMLPosts()
	const allPosts = allMD //.concat(allHTML)
	//console.log('allMD',allMD)
	//console.log('allHTML',allHTML)
  const sortedPosts = allPosts.sort()
	// console.log('sortedPosts',sortedPosts) //(a, b) => {
    //return new Date(b.meta.date) - new Date(a.meta.date)
  //})

  return json(sortedPosts)
}