<script> // post *
	import _ from "lodash"
	import { site } from '$lib/site.js'
	import {timeSince} from '$lib/utils/utils.js'

	import { query } from '$lib/query.js'
	import Search from "$lib/Search.svelte"

	import { browser } from "$app/environment"
	import { goto } from "$app/navigation"

	import { innerwidth } from '$lib/query.js'


	let sokruta = $query
	// $: WIDTH = innerwidth
	// if (browser) WIDTH = innerWidth-1000
	
	$: if (browser) {
		query.set(sokruta)
		goto('/query/' + sokruta)
	}

	const posts = _.map(_.keys($site.posts), (key) => {
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
		if (katalog == "php") {
			return [key,href,katalog,filename]
		} else {
			return [key,href,katalog,filename]
		}
	})

</script>

	<h1>🏠 Hem</h1>

	<p>
		<Search bind:sokruta />
	</p>
		
	<table style="width:{$innerwidth}px">
		<thead>
			<th>Post</th>
			<th>Ålder</th>
			<th>Katalog</th>
		</thead>
		<tbody>
			{#each posts as [key, href, katalog, filnamn]}
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


