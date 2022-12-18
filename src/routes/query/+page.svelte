<!-- src/routes/query/+page.svelte -->
<script>
	import _ from 'lodash'
	export let data
	let words = []
	for (const post of data.posts) {
		words = words.concat(post.meta.words.split(' '))
	}
	words.sort()
	words = _.uniq(words)

</script>
	
	<h1>Alla ord</h1>
	•
	{#each words as word}
		<a href={`/query/${word}`}>{word}</a> •&nbsp;
	{/each}
