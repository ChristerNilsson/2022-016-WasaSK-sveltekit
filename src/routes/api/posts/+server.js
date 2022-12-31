import { fetchMarkdownPosts } from '$lib/utils'
import { json } from '@sveltejs/kit'
export const prerender = true
export const GET = async () => {
  const allMD = await fetchMarkdownPosts()
	const allPosts = allMD 
  const sortedPosts = allPosts.sort()
  return json(sortedPosts)
}