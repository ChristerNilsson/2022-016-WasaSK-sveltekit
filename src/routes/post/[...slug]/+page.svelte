<script> // post 1
	import _ from "lodash"
	import { site } from '$lib/stores.js'
  export let data
	const words = $site.md[data.slug][1].split(' ')
	const [directory,title] = data.slug.replaceAll('_',' ').replace('.md','').split('/')

</script>

<h1>{title}</h1>
<i>Publicerad: {$site.md[data.slug][0]} i {directory}</i>

<svelte:component this={data.content} />

<h6>
{#each words as word}
	<a href={`/query/${word}`}>{word}</a> •&nbsp;
{/each}
</h6>
