<script>
	import _ from "lodash"
	export let keys
	export let push
	export let WIDTH
		
</script>

<div style="width:{WIDTH+5}px">
	{#each keys as key }
		<button class="row" value={key} on:click = {() => push(key)}>{key}</button>
	{/each}
</div>

<style>
	span {
		flex:1;
		overflow:hidden;
		white-space:nowrap;
	}
	div {
		margin:0px
	}
	.row {
		margin:0px;
		height:30px;
		width:98%;
		text-align:left;
		flex:1;
		overflow:hidden;
		white-space:nowrap;
	}

</style>
