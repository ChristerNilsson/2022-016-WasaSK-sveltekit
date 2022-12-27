<script> // post *
	import _ from "lodash"
	import { site } from '$lib/site.js'
	import {timeSince} from '$lib/utils/utils.js'

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
						{timeSince($site.posts[key][0])} 
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
		<tr><td>Updated</td><td align='right'>{timeSince($site.stats.updated)}</td></tr>
		<tr><td>mdPosts</td><td align='right'>{$site.stats.mdPosts}</td></tr>
		<tr><td>mdBytes</td><td align='right'>{$site.stats.mdBytes}</td></tr>
		<tr><td>phpPosts</td><td align='right'> {$site.stats.phpPosts}</td></tr>
		<tr><td>phpBytes</td><td align='right'> {$site.stats.phpBytes}</td></tr>
		<tr><td>menuItems</td><td align='right'> {$site.stats.menuItems}</td></tr>
		<tr><td>uniqWords</td><td align='right'><a href="/query">{$site.stats.uniqWords}</a></td></tr>
		<tr><td>Files</td><td align='right'> {$site.stats.files}</td></tr>
	</tbody>
</table>
