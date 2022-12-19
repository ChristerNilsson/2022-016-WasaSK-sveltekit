<!-- src/routes/post/+page.svelte -->

<script>
	import _ from "lodash"
	import { site } from 'C:/github/2022-016-WasaSK-sveltekit/src/lib/stores.js'
	export let data
	// $: console.log(data)
</script>
	
	<h1>Senaste posterna</h1>
		
	<table>
		<thead><tr><th align='left'>Datum</th><th align='left'>Post</th></tr></thead>
		<tbody>
		{#each data.posts as post}
		<tr>
			<td>
				{$site.md[post.path.slice(6)][0]}
			</td>
			<td>
				<a href={post.path}>
					{post.path.slice(6).replaceAll('_',' ').replace('.md','')}
				</a>
			</td>
		</tr>
		{/each}
		</tbody>
</table>
