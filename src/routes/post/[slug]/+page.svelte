<!-- src/routes/post/[slug]/+page.svelte -->

<script>
	import _ from "lodash"
	import { site } from 'C:/github/2022-016-WasaSK-sveltekit/src/lib/stores.js'
  export let data
</script>

<article>
  <h1>{data.slug.replaceAll('_',' ').replace('.md','')}</h1>
  <h2>Publicerad: {$site.md[data.slug][0]}</h2>
  <h6>{$site.md[data.slug][1]}</h6>

  <svelte:component this={data.content} />
</article>