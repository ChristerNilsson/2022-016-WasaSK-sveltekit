<!-- src/routes/post/[slug]/+page.svelte -->
<script>
  export let data
	const datum = new Date(data.date).toISOString().split('T')[0]
</script>

<article>
  <h1>{data.title}</h1>
  <h2>Publicerad: {datum} av {data.author}</h2>
  <h2>{data.words}</h2>

  <svelte:component this={data.content} />
</article>