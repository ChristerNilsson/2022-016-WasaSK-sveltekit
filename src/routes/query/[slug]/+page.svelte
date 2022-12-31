<script> 

	import {browser} from "$app/environment"
	import {goto}    from "$app/navigation"

	import {query}   from '$lib/stores.js'
	import Search    from "$lib/Search.svelte"
	import QUERY     from '$lib/QUERY.svelte'

	export let data
	let sokruta = data.slug 
	$: query.set(sokruta)

</script>

<h1>🏠 Hem</h1>
<p><Search bind:sokruta /></p>
<QUERY/>
