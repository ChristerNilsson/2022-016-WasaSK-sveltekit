<script>
	export let sokruta
	export let WIDTH

	// import { goto } from '$app/navigation'
	import { query } from '$lib/query.js'

	$: query.set(sokruta)	

</script>

<input autofocus autocomplete="off" id="search" bind:value={sokruta} placeholder='Sök' style="width:{WIDTH-8}px">

<style>
	input {
		margin:0px;
		height:30px;
	}
	::placeholder {
		color: lightgray;
		opacity: 1;
	} 
</style>
