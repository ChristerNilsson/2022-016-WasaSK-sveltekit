<script>
	export let title
	export let data
	import _ from 'lodash'
	import Chart from './Chart.svelte'
	const values = _.values(data) 
	const labels = _.keys(data)
</script>

<Chart {title} {labels} data={values}  />
