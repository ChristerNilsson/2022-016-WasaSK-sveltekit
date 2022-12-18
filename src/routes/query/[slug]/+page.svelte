<!-- src/routes/query/[query]/+page.svelte -->
<script>
	export let data
</script>
	
<h1>Sökresultat</h1>

<table>
	<thead><tr><th align='left'>Datum</th><th align='left'>Post</th><th>Sökord</th></tr></thead>
	<tbody>
		{#each data.posts as [count,letters,post,hitWords]}
			<tr>
				<td>{new Date(post.meta.date).toISOString().split('T')[0]}</td>
				<td><a href= {post.path}> {post.meta.title}</a></td>
				<!-- <td>{letters}</td> -->
				<td>{hitWords}</td>
			</tr>
		{/each}
	</tbody>
</table>
