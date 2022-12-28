<script>
	import _ from 'lodash'
	export let label
	export let value // ' ' = no selection
	export let values // list of strings
	const STATES = {on:'off',off:'on'}
	$: n = value.length
	$: empty = '____'.slice(0,n)
	$: values = values.split(' ')
	$: newvalues = [`${label}:`].concat(values).concat(`:${label}`)
	$: i = _.findIndex(newvalues, (v) => v.slice(0,n) == value)
	$: if (i==-1) i=1
	
	let state = value==empty ? 'off' : 'on'
	// $: result = state=='on' ? values[i].slice(0,n) : empty
	const toggle = () => state = STATES[state]
	const prev = () => {if (i > 1) i -= 1}
	const next = () => {if (i < newvalues.length-2) i += 1}
</script>

<table>
	<tr>
		<td class="prevent-select" on:click={prev}   on:keyup={prev}           >{newvalues[i-1]}</td>
		<td class="prevent-select {state}" on:click={toggle} on:keyup={toggle} >{newvalues[i]}</td>
		<td class="prevent-select" on:click={next}   on:keyup={next}           >{newvalues[i+1]}</td>
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

