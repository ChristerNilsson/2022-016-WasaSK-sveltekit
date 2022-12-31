<script>

	import { browser } from "$app/environment"
	import { goto } from "$app/navigation"

	import { query} from '$lib/stores.js'

	import Search from "$lib/components/Search.svelte"
	import QUERY from '$lib/components/QUERY.svelte'

	let sokruta = $query
	$: if (browser) {
		query.set(sokruta)
		goto('/query/' + sokruta)
	}

</script>

<h1>🏠 Hem</h1>
<p><Search bind:sokruta /></p>
<QUERY />