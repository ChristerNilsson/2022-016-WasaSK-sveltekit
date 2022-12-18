// src/routes/query/[query]/+page.js

import _ from "lodash"

function spaceShip (a,b) {
	if (a < b) return -1
	else if (a == b) return 0
	return 1 
}

function multiSort (a,b,indexes) {
	for (const i in _.range(indexes.length)) {
		const index = Math.abs(indexes[i])-1 // 0..
		let res = spaceShip(a[index],b[index])
		if (res != 0) return indexes[i] < 0 ? -res : res
	}
}

export const load = async ({ fetch, params }) => {
	const { slug } = params
	const response = await fetch(`/api/posts`)
	const allPosts = await response.json()

	const posts = []
	
	let words = slug.toLowerCase().split(' ')
	words = words.map((word => word[0].toUpperCase() + word.slice(1)))
	
	for (const post of allPosts) {
		const letters = []
		const hitWords = []
		for (const i of _.range(words.length)) {
			const word = words[i]
			if (post.meta.words.includes(word)) {
				letters.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i])
				hitWords.push(word)
			}
		}
		if (letters.length > 0) posts.push([letters.length,letters.join(""), post, hitWords])
	}

	posts.sort((a,b) =>  multiSort(a,b,[-1,2]))

	return {
		slug,
		posts
	}
}