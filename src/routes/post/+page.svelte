<!-- src/routes/post/+page.svelte -->
<script>
	export let data
	$: console.log(data)
</script>
	
	<h1>Senaste posterna</h1>
		
	<table>
		<thead><tr><th align='left'>Datum</th><th align='left'>Post</th></tr></thead>
		<tbody>
		{#each data.posts as post}
		<tr>
			<td>
				{new Date(post.meta.date).toISOString().split('T')[0]}
			</td>
			<td>
				<a href={post.path}>
					{post.meta.title}
				</a>
			</td>
		</tr>
		{/each}
		</tbody>
</table>
