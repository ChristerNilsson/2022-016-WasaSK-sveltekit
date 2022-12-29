<script> // post *
	import _ from "lodash"
	import {timeSince} from '$lib/utils/utils.js'

	import Search from "$lib/Search.svelte"

	import { browser } from "$app/environment"
	import { goto } from "$app/navigation"

	import { site } from '$lib/site.js'
	import { query,innerwidth,multiselect } from '$lib/query.js'

	let sokruta = $query
	// $: WIDTH = innerwidth
	// if (browser) WIDTH = innerWidth-1000
	
	$: if (browser) {
		query.set(sokruta)
		goto('/query/' + sokruta)
	}

	$: posts = _.map(_.keys($site.posts), (key) => {
		const arr = key.split('/')
		let katalog
		let subdir=''
		let filename
		let href
		if (arr.length == 1) {
			console.log(key,arr)
		} else if (arr.length == 2) {
			[katalog,filename] = arr
		} else if(arr.length == 3) {
			[katalog,subdir,filename] = arr
			filename = subdir + '/' + filename
		} else {
			console.log('problem',arr.length)
		}
		if (katalog=='php') href='https://wasask.se/' + filename
		else href = 'post/' + katalog + "/" + filename
		const datum = $site.posts[key][0].slice(0,10)
		const attributes = $site.posts[key][0].slice(11).split('').join(' ')

		filename = filename.replaceAll("_"," ")
		if (filename.endsWith(".md")) {
			filename = filename.slice(18).replace(".md","")
		} else {
			filename = filename.replace(".php","").replace('.ulenkar','')
		}

		return [key,href,katalog,filename,datum,attributes]
	})

	$: posts2 = _.filter(posts,(post) => selected(post[0],$multiselect,$site))

	function selected(key,multiselect,site) {
		const attributes = site.posts[key][0].slice(11,18)
		let result = true

		// year
		const year = site.posts[key][0].slice(0,4)

		// if (year != '____' && multiselect[6] != '____' && year != multiselect[6]) result = false
		// for (const i in _.range(6)) {
		// 	if (attributes[i] != '_' && multiselect[i] != '_' && attributes[i] != multiselect[i]) result = false
		// }

		if (multiselect[6] != 'nix' && year != multiselect[6]) result = false
		for (const i in _.range(6)) {
			// console.log(attributes[i], multiselect[i])
			if (multiselect[i] != "nix"  && attributes[i] != multiselect[i]) result = false
		}

		return result
	}
	
</script>

	<h1>🏠 Hem</h1>

	<p>
		<Search bind:sokruta />
	</p>

	{posts2.length}
		
	<table style="width:{$innerwidth}px">
		<thead>
			<th>Post</th>
			<th>Datum</th>
			<th>Ålder</th>
			<th>Katalog</th>
			<th>Attribut</th>
		</thead>
		<tbody>
			{#each posts2 as [key, href, katalog, filnamn, datum, attributes]}
				<tr>
					<td><a {href}>{filnamn}</a></td>
					<td>{datum}</td>
					<td>{timeSince($site.posts[key][0].slice(0,10))}</td>
					<td>{katalog}</td>
					<td style="font-family:monospace">{attributes}</td>
				</tr>
			{/each}
		</tbody>
</table>


