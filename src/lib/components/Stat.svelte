<script>
	import _ from 'lodash'
	import Chart from '$lib/components/Chart.svelte'

	export let title
	export let data

	const values = _.values(data) 
	const labels = _.keys(data)
</script>

<Chart {title} {labels} data={values}  />
