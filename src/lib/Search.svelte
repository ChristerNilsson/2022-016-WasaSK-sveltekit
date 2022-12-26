<script>
	export let sokruta
	export let stack
	export let WIDTH
	// export let GAP
	// export let spreadWidth
	export let _
	export let pop

	// import { saveAs } from 'file-saver'
	import { goto } from '$app/navigation'
	import { query } from '$lib/query.js'

	function clear() {
		sokruta = ""
		query.set('')
	}

	$: query.set(sokruta)
	
	function share () {
		const q1 = stack.length <= 1 ? "" : "folder=" + stack.join("\\") 
		const q2 = sokruta == "" ? "" : "query=" + sokruta		
		const q = q1=="" && q2=="" ? "" : "?"
		const a = q1!="" && q2!="" ? "&" : ""
		navigator.clipboard.writeText(location.origin + location.pathname + q + q1 + a + q2)
	}

	function help() {goto("/post/Common/Hjälp.md")}
	function search() {goto("/query/" + sokruta)}

</script>

<input autocomplete="off" id="search" bind:value={sokruta} placeholder='Sök' style="width:{WIDTH-8}px">
<div style="width:{WIDTH}px; height:34px">

	{#if _.last(stack) == "Hem"}
		<button style="left:0%; width:50px" on:click = {pop} disabled >Upp</button>
	{:else}
		<button style="left:0%; width:50px" on:click = {pop} >Upp</button>
	{/if}

	<button on:click={clear}  style="left:50px; width:60px">Rensa</button>
	<button on:click={share}  style="left:110px; width:50px">Dela</button>
	<button on:click={help}   style="left:160px; width:50px">Hjälp</button>
	<button on:click={search} style="left:210px; width:40px">Sök</button>

	<!-- <button on:click={clear}  style="left:{1*WIDTH/5}px; width:{spreadWidth(1/5,WIDTH)}px">Rensa</button>
	<button on:click={share}  style="left:{2*WIDTH/5}px; width:{spreadWidth(1/5,WIDTH)}px">Dela</button>
	<button on:click={help}   style="left:{3*WIDTH/5}px; width:{spreadWidth(1/5,WIDTH)}px">Hjälp</button>
	<button on:click={search} style="left:{4*WIDTH/5}px; width:{spreadWidth(1/5,WIDTH)}px">Sök</button> -->

</div>

<style>
	div {
		margin:0px;
	}
	button {
		position:absolute;
		margin:2px;
		height:30px;
	}
	input {
		margin:0px;
		height:30px;
	}
	::placeholder {
		color: lightgray;
		opacity: 1;
	} 
</style>
