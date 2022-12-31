<script>
	import _ from 'lodash'
	import {log, range, timeSince, multiSort, spaceShip} from '$lib/utils.js'
	import {site,dimensions,query,innerwidth,a,b,c,d,e,f,g,h} from '$lib/stores.js' 

	const SPACE = ' '
	let details = false

	function searchWords(query,md) {
		const words = query.toLowerCase().split(' ')
		const posts = []
		for (const key of _.keys(md)) {
			const post = md[key]
			const letters = []
			const hitWords = []

			for (const i of range(words.length)) {
				const word = words[i]
				if (post[1].includes(SPACE + word)) {
					letters.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i])
					hitWords.push(word)
				}
			}

			if (letters.length > 0) {
				const arr = key.split('/')
				const katalog = arr[0]
				const subdir = arr.length==3 ? arr[1] + '/' : ""
				const filnamn = _.last(arr)
				const href = katalog == 'php' ? "https://wasask.se/" + subdir + filnamn : "/post/" + key
				const {date,attr,size} = post[0]
				const hash = {key, href, katalog, filnamn, hitWords, date, attr, size}
				posts.push([letters.length, letters.join(""), hash])
			}
		}
		posts.sort((a,b) =>  multiSort(a,b,[-1,2]))
		return posts
	}

	function selected(a,b,c,d,e,f,g,h,post) {
		const {attr,date,katalog} = post[2]
		// log(katalog,h,katalog != h)
		const year = date.slice(0,4)
		if (a != "nix" && attr[0] != a) return false
		if (b != "nix" && attr[1] != b) return false
		if (c != "nix" && attr[2] != c) return false
		if (d != "nix" && attr[3] != d) return false
		if (e != "nix" && attr[4] != e) return false
		if (f != "nix" && attr[5] != f) return false
		if (g != 'nix' && year    != g) return false
		if (h != 'nix' && katalog[0] != h) return false
		return true
	}

	function expand(hash,i) {
		const key = 'ålder typ lag nivå tid kön år'.split(' ')[i]
		return _.filter($dimensions[key].split(' '), (s) => s[0] == hash.attr[i])[0]
	}

	$: posts = searchWords($query,$site.posts)
	$: posts2 = _.filter(posts, (post) => selected($a,$b,$c,$d,$e,$f,$g,$h, post))

</script>

<div class="prevent-select" on:click={()=> details = !details} on:keyup={()=>1}>
	{posts2.length} poster
</div>

<table style="width:{$innerwidth}px">
	<thead>
		<th>Post</th><th>Datum</th><th>Publ.tid</th><th>Sökord</th>
		{#if details}
			<th>ålder</th><th>typ</th><th>lag</th><th>nivå</th><th>tid</th><th>kön</th><th>Bytes</th>
		{/if}		
	</thead>
	<tbody>
		{#each posts2 as [_1, _2, hash]}
			<tr>
				<td><a href={hash.href}>{hash.filnamn}</a></td>
				<td>{hash.date}</td>
				<td>{timeSince(hash.date)}</td>
				<td>{hash.hitWords.join(' ')}</td>
				{#if details}
					<td>{expand(hash,0)}</td>
					<td>{expand(hash,1)}</td>
					<td>{expand(hash,2)}</td>
					<td>{expand(hash,3)}</td>
					<td>{expand(hash,4)}</td>
					<td>{expand(hash,5)}</td>
					<td class="size">{hash.size}</td>
				{/if}
			</tr>
		{/each}
	</tbody>
</table>

<style>
	.attr { text-align:center; font-family:monospace; font-size:18px;}
	.size { text-align:right; }
</style>
