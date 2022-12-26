<script> // post *
	import _ from "lodash"
	import { site } from '$lib/site.js'
	import {timeSince} from '$lib/utils/utils.js'

	const posts = _.map(_.keys($site.md), (key) => {
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
		if (katalog=='legacy') href='https://wasask.se/' + filename
		else href = 'post/' + katalog + "/" + filename
		if (katalog == "legacy") {
			return [key,href,katalog,filename]
		} else {
			return [key,href,katalog,filename]
		}
	})

</script>

	<h1>Senaste posterna</h1>
		
	<table>
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
						{timeSince($site.md[key][0])} 
					</td>
					<td>
						{katalog}
					</td>
				</tr>
			{/each}
		</tbody>
</table>

<table>
	<thead><tr><th align='left'>Statistik</th><th align='right'></th></tr></thead>
	<tbody>
		<tr><td>Uppdaterad</td><td>{timeSince($site.stats.updated)}</td></tr>
		<tr><td>Poster</td><td>{$site.stats.posts}</td></tr>
		<tr><td>Filer</td><td> {$site.stats.files}</td></tr>
		<tr><td>Legacy</td><td> {$site.stats.legacy}</td></tr>
		<tr><td>Menyrader</td><td> {$site.stats.items}</td></tr>
		<tr><td>Ord</td><td><a href="/query">{$site.stats.words}</a></td></tr>
	</tbody>
</table>
