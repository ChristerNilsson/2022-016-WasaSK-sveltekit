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
		} else if (arr.length == 2) {
			[katalog,filename] = arr
		} else if(arr.length == 3) {
			[katalog,subdir,filename] = arr
			filename = subdir + '/' + filename
		} else {
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
