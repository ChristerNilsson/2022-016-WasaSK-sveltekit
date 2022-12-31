<script>

	import { browser } from "$app/environment"
	import { goto } from "$app/navigation"

	import Search from "$lib/Search.svelte"
	import { query} from '$lib/stores.js'
	import QUERY from '$lib/QUERY.svelte'

	let sokruta = $query
	$: if (browser) {
		query.set(sokruta)
		goto('/query/' + sokruta)
	}

</script>

<h1>🏠 Hem</h1>
<p><Search bind:sokruta /></p>
<QUERY />