<script> // post *

	import Search from "$lib/Search.svelte"

	import { browser } from "$app/environment"
	import { goto } from "$app/navigation"

	import { query, a,b,c,d,e,f,g} from '$lib/query.js'
	import QUERY from '$lib/QUERY.svelte'

	$: sokruta = $query	
	$: if (browser) {goto('/query/' + sokruta)}	// query.set(sokruta)

</script>

<h1>🏠 Hem</h1>
<p><Search bind:sokruta /></p>
<QUERY />