<script>
	import _ from 'lodash'
	export let label
  export let chars  // number of characters returned
	export let values // list of strings
	export let result

	let value = '____'.slice(0,chars)
	let i = 3
	let state = 'off'

	const STATES = {on:'off',off:'on'}

	$: empty = '____'.slice(0,chars)
	$: values1 = values.split(' ')
	$: values2 = [" "," "].concat(values1).concat([" "," "])
	$: result = state=='off' ? "nix" : values2[i].slice(0,chars)

	const toggle = () => state = STATES[state]
	const move = (delta) => {if (1 < i+delta && i+delta < values2.length-2) i += delta}
</script>

<table>
	<tr>
		{#if state=="off"}
			<td></td>
			<td></td>
			<td class="prevent-select" style="color:black" on:click={toggle} on:keyup={toggle} >{label}</td>
			<td></td>
			<td></td>
		{:else}
			<td on:keyup={toggle} class="prevent-select"         on:click={()=> move(-2)}   >{values2[i-2]}</td>
			<td on:keyup={toggle} class="prevent-select"         on:click={()=> move(-1)}   >{values2[i-1]}</td>
			<td on:keyup={toggle} class="prevent-select {state}" on:click={toggle}          >{values2[i]}</td>
			<td on:keyup={toggle} class="prevent-select"         on:click={()=> move(1)}    >{values2[i+1]}</td>
			<td on:keyup={toggle} class="prevent-select"         on:click={()=> move(2)}    >{values2[i+2]}</td>
		{/if}
	</tr>	
</table>

<style>
	table {width:397px; font-size:16px; margin:0 }
	td { width:60px; text-align:center; background:gray; color:white; }
	.lbl { text-align:right; background:white; color:black; }
	.on { background:black; color:yellow }
	.off { color:white }
</style>
