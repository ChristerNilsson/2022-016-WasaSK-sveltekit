<script>
	import _ from 'lodash'
	export let label
	export let value // ' ' = no selection
	export let values // list of strings
	const STATES = {on:'off',off:'on'}
	const n = value.length
	const empty = '____'.slice(0,n)
	values = ' ' + values + ' '
	values = values.split(' ')
	
	let i = _.findIndex(values, (v) => v.slice(0,n) == value)
	if (i==-1) i=1
	
	let state = value==empty ? 'off' : 'on'
	$: result = state=='on' ? values[i].slice(0,n) : empty
	const toggle = () => state = STATES[state]
	const prev = () => {if (i > 1) i -= 1}
	const next = () => {if (i < values.length-2) i += 1}
</script>

<table>
	<tr>
		<td class='lbl'                                      >{label}</td>
		<td on:click={prev}   on:keyup={prev}                >{values[i-1]}</td>
		<td on:click={toggle} on:keyup={toggle} class={state}>{values[i]}</td>
		<td on:click={next}   on:keyup={next}                >{values[i+1]}</td>
		<td class='lbl'>{result}</td>
	</tr>
</table>

<style>
	td {
		width:100px;
		text-align:center;
		background:gray;
		color:white;
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

###############################

<script>
	import Selector from './Selector.svelte'
</script>

<Selector label='year'      value='2022'     values={'2020 2021 2022 2023 2024'} />
<Selector label='month'     value='__'       values={'01 02 03 04 05 06 07 08 09 10 11 12'} />
<Selector label='age'       value='S'        values={'Junior Senior Veteran'} />
<Selector label='team size' value='_'        values={'1 2 3 4 5 6 7 8'} />
<Selector label='sex'       value='F'        values={'Female Male Other'} />
<Selector label='level'     value='K'        values={'KM DM SM NM EM WM'} />
<Selector label='typ'       value='I'        values={'Inbjudan Resultat Program'} />
