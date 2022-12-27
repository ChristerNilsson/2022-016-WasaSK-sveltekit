<script>
	// query 1
	// export let data
	import _ from "lodash"
	import { site } from '$lib/site.js'
	import { query } from '$lib/query.js'
	import {timeSince} from '$lib/utils/utils.js'
	
	const SPACE = ' '

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

	$: querystring  = $query
	
	$: posts = search(querystring)

	function search(querystring) {
		// console.log('searchA', querystring)
		let words = querystring.toLowerCase().split(' ')
		const posts = []
		const md = $site.posts
		for (const key of _.keys(md)) {
			// console.log('searchB', key)
			const letters = []
			const hitWords = []
			for (const i of _.range(words.length)) {
				const word = words[i]
				if ($site.posts[key][1].includes(SPACE + word)) {
					letters.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i])
					hitWords.push(word)
				}
			}
			let subdir
			let katalog
			let filnamn
			const arr = key.split('/')
			if (arr.length==3) {
				[katalog,subdir,filnamn] = arr
				subdir += '/'
			} else if (arr.length==2){
				[katalog,filnamn] = arr
				subdir = ""
			} else {
				// console.log('problem')
			}
			// console.log(arr.length, {key,arr,katalog,subdir,filnamn})
			let href
			if (katalog == 'php') {
				href = "https://wasask.se/" + subdir + filnamn
			} else {
				href = "/post/" + key
			}
			const datum = $site.posts[key][0].slice(0,10)
			if (letters.length > 0) posts.push([letters.length,letters.join(""), href, katalog, filnamn, hitWords,datum])
		}
		posts.sort((a,b) =>  multiSort(a,b,[-1,2]))
		return posts
	}

</script>

<h1>Sökresultat</h1>

<table>
	<thead>
		<th>Post</th>
		<th>Ålder</th>
		<th>Katalog</th>
		<th>Sökord</th>
	</thead>
	<tbody>
		{#each posts as [count,letters,href,katalog,filnamn,hitWords,datum]}
			<tr>
				<td><a {href} > {filnamn.replaceAll('_',' ').replace('.md','').replace('.php','')} </a></td>
				<td>{timeSince(new Date(datum))}</td>
				<td>{katalog}</td>
				<td>{hitWords.join(' ')}</td>
			</tr>
		{/each}
	</tbody>
</table>
