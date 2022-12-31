<script> // query 1

	import {browser} from "$app/environment"
	import {goto}    from "$app/navigation"

	import {query}   from '$lib/query.js'
	import Search    from "$lib/Search.svelte"
	import QUERY     from '$lib/QUERY.svelte'

	$: sokruta = $query
	$: query.set(sokruta)
	// $: if (browser) goto('/query/' + $query)

</script>

<h1>🏠 Hem</h1>
<p><Search bind:sokruta /></p>
<QUERY/>
