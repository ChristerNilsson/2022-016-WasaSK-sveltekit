<script> // post 1
	import _ from "lodash"
	import { site } from '$lib/site.js'
	import {timeSince} from '$lib/utils/utils.js'
  export let data

	$: [directory,filename] = data.slug.split('/') //.replaceAll('_',' ').replace('.md','').split('/')
	$: words = data.slug.includes('common') ? [] : $site.posts[data.slug][1].split(' ')
	$: published = data.slug.includes('common') ? "" : `Publicerad för ${timeSince($site.posts[data.slug][0].date)} sedan i ${directory}`
</script>

<h1>{filename}</h1>
<i>{published}</i>

<svelte:component this={data.content} />

<h6>
{#each words as word}
	<a href={`/query/${word}`}>{word}</a> •&nbsp;
{/each}
</h6>
