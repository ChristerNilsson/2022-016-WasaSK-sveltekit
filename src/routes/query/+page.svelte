<script> // post *

	import Search from "$lib/Search.svelte"

	import { browser } from "$app/environment"
	import { goto } from "$app/navigation"

	import { query, a,b,c,d,e,f,g} from '$lib/query.js'
	import QUERY from '$lib/QUERY.svelte'

	let sokruta = $query
	
	$: if (browser) {
		query.set(sokruta)
		goto('/query/' + sokruta)
	}

	$: console.log({$a,$b,$c,$d,$e,$f,$g})

</script>

<h1>🏠 Hem</h1>
<p><Search bind:sokruta /></p>
<QUERY />