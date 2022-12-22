<script> // post *
	import _ from "lodash"
	import { site } from '$lib/stores.js'
	// export let data
</script>

	<h1>Senaste posterna</h1>
		
	<table>
		<thead><tr><th align='left'>Datum</th><th align='left'>Post</th></tr></thead>
		<tbody>
			{#each _.keys($site.md) as key}
				<tr>
					<td>
						{$site.md[key][0]}
					</td>
					<td>
						<a href={'/post/' + key}>
							{key} 
							<!-- post.path.slice(6).replaceAll('_',' ').replace('.md','')} -->
						</a>
					</td>
				</tr>
			{/each}
		</tbody>
</table>

<table>
	<thead><tr><th align='left'>Statistik</th><th align='right'></th></tr></thead>
	<tbody>
		<tr><td>Uppdaterad</td><td>{$site.stats.updated}</td></tr>
		<tr><td>Poster</td><td>{$site.stats.posts}</td></tr>
		<tr><td>Filer</td><td> {$site.stats.files}</td></tr>
		<tr><td>Menyrader</td><td> {$site.stats.items}</td></tr>
		<tr><td>Ord</td><td><a href="/query">{$site.stats.words}</a></td></tr>
	</tbody>
</table>
