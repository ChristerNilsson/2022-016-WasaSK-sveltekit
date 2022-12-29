<script>
	import _ from 'lodash'
	export let label
  export let chars  // number of characters returned
	export let values // list of strings
	export let result

	let value = '____'.slice(0,chars)

	const STATES = {on:'off',off:'on'}

	$: empty = '____'.slice(0,chars)
	$: values = values.split(' ')
	$: newvalues = [""].concat(values).concat("")
	$: i = _.findIndex(newvalues, (v) => v.slice(0,chars) == value)
	$: if (i==-1) i=1
	
	let state = 'off'
	$: result = state=='off' ? "nix" : values[i-1].slice(0,chars)
	const toggle = () => state = STATES[state]
	const prev = () => {if (i > 1) i -= 1}
	const next = () => {if (i < newvalues.length-2) i += 1}
</script>

<table>
	<tr>
		{#if state=="off"}
			<td></td>
			<td class="prevent-select" style="color:black" on:click={toggle} on:keyup={toggle} >{label}</td>
			<td></td>
		{:else}
			<td class="prevent-select" on:click={prev}   on:keyup={prev}           >{newvalues[i-1]}</td>
			<td class="prevent-select {state}" on:click={toggle} on:keyup={toggle} >{newvalues[i]}</td>
			<td class="prevent-select" on:click={next}   on:keyup={next}           >{newvalues[i+1]}</td>
		{/if}
	</tr>	
</table>

<style>
	table {
		width:397px;
		font-size:18px;
		margin:0
	}
	td {
		width:100px;
		text-align:center;
		background:gray;
		color:white;
	}
	.prevent-select {
 		-webkit-user-select: none; /* Safari */
	  -ms-user-select: none; /* IE 10 and IE 11 */
	  user-select: none; /* Standard syntax */
	}
	.lbl {
		text-align:right;
		background:white;
		color:black;
	}
	.on {
		background:black;
		color:yellow
	}
	.off {
		color:white
	}

</style>

