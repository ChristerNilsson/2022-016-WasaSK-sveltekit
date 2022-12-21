<script>
	// query 1
	export let data
	import _ from "lodash"
	import { site } from '$lib/stores.js'
	
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

	let words = data.slug.toLowerCase().split(' ')
	const posts = []
	const md = $site.md
	for (const key of _.keys(md)) {
		console.log(key)
		const letters = []
		const hitWords = []
		for (const i of _.range(words.length)) {
			const word = words[i]
			if ($site.md[key][1].includes(SPACE + word)) {
				letters.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i])
				hitWords.push(word)
			}
		}
		if (letters.length > 0) posts.push([letters.length,letters.join(""), key, hitWords])
	}

	posts.sort((a,b) =>  multiSort(a,b,[-1,2]))

</script>

<h1>Sökresultat</h1>

<table>
	<thead><tr><th align='left'>Post</th><th>Sökord</th></tr></thead>
	<tbody>
		{#each posts as [count,letters,key,hitWords]}
			<tr>
				<td><a href= /post/{key}>{key.replaceAll('_',' ').replace('.md','')}</a></td>
				<td>{hitWords.join(' ')}</td>
			</tr>
		{/each}
	</tbody>
</table>
