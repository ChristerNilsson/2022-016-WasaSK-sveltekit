<script> // post 1
	import _ from "lodash"
	import { site } from '$lib/site.js'
	import {timeSince} from '$lib/utils/utils.js'
  export let data
	const words = $site.posts[data.slug][1].split(' ')
	$: [directory,filename] = data.slug.replaceAll('_',' ').replace('.md','').split('/')
</script>

<h1>{filename}</h1>
<i>Publicerad för {timeSince($site.posts[data.slug][0])} sedan i {directory}</i>

<svelte:component this={data.content} />

<h6>
{#each words as word}
	<a href={`/query/${word}`}>{word}</a> •&nbsp;
{/each}
</h6>
