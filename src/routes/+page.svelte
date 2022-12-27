<script>
	import { browser } from "$app/environment"
	import { goto } from "$app/navigation"
	import { query } from '$lib/query.js'

	$: if (browser) {
		query.set("")
		goto('/query' )
	}

</script>

<svelte:head>
	<title>Wasa SK</title>
	<meta name="description" content="Wasa SK" />
</svelte:head>

