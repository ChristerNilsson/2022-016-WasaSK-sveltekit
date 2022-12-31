<script>
	export let sokruta

	import { query,innerwidth } from '$lib/query.js'

	$: query.set(sokruta)

</script>

<input autofocus autocomplete="off" id="search" bind:value={sokruta} placeholder='Sök' style="width:{$innerwidth-8}px">

<style>
	input { margin:0px; height:30px;}
	::placeholder { color: lightgray; opacity: 1; } 
</style>
