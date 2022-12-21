<script>
	// post 1
	import _ from "lodash"
	import { site } from '$lib/stores.js'
  export let data
	const words = $site.md[data.slug][1].split(' ')
</script>

<h1>{data.slug.replaceAll('_',' ').replace('.md','')}</h1>
<i>Publicerad: {$site.md[data.slug][0]}</i>

<svelte:component this={data.content} />

<h6>
{#each words as word}
	<a href={`/query/${word}`}>{word}</a> •&nbsp;
{/each}
</h6>
