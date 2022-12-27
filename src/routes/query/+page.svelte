<script>
	// query *
	import _ from 'lodash'
	import { site } from '$lib/site.js'
	const md = $site.posts
	let words = _.map(_.keys(md), (key) => md[key][1].split(' '))
	words = _.uniq(_.flatten(words).sort())

</script>
	
	<h1>Alla ord</h1>
	{#each words as word}
		<a href={`/query/${word}`}>{word}</a> •&nbsp;
	{/each}
