<script> // post *
	import _ from "lodash"
	import { site } from '$lib/site.js'
	import {timeSince} from '$lib/utils/utils.js'

	// import { query } from '$lib/query.js'
	import Search from "$lib/Search.svelte"

	import { browser } from "$app/environment"
	import { goto } from "$app/navigation"

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
		return [key,href,katalog,filename]
	})

	$: posts2 = _.filter(posts,([key,href,katalog,filename]) => selected(key,$multiselect,$site))

	function selected(key,multiselect,site) {
		const attributes = site.posts[key][0].slice(11,18)
		let result = true

		// year
		const year = site.posts[key][0].slice(0,4)
		if (year != '____' && multiselect[6] != '____' && year != multiselect[6]) result = false

		for (const i in _.range(6)) {
			if (attributes[i] != '_' && multiselect[i] != '_' && attributes[i] != multiselect[i]) result = false
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
			<th>Ålder</th>
			<th>Katalog</th>
		</thead>
		<tbody>
			{#each posts2 as [key, href, katalog, filnamn]}
				<tr>
					<td>
						<a {href}>
							{filnamn.replaceAll("_"," ").replace(".md","").replace(".php","")} 
						</a>
					</td>
					<td>
						{timeSince($site.posts[key][0].slice(0,10))} 
					</td>
					<td>
						{katalog}
					</td>
				</tr>
			{/each}
		</tbody>
</table>


