<script>
	export let title
	export let data
	import _ from 'lodash'
	import Chart from './Chart.svelte'
	let values = _.values(data) 
	let labels = _.keys(data)
</script>

<Chart {title} {labels} data={values}  />
