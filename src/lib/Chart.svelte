<script>
	import chartjs from 'chart.js'
	import { onMount } from 'svelte'
	export let title
	export let labels
	export let data
	let chartCanvas
	let ctx
	
	onMount(async (promise) => {
		ctx = chartCanvas.getContext('2d')
		var chart = new chartjs(ctx, {
			type: 'bar',
			data: {
					labels: labels,
					datasets: [{
						label:title, 
						data:data,
						borderColor: '#880',
	      		backgroundColor: '#660',
						color : '#440',
					}]
			}
		})
		// chart.defaults.backgroundColor = '#9BD0F5';
		// chart.defaults.borderColor = '#36A2EB';
		// chart.defaults.color = '#888';
	})
</script>




<canvas bind:this={chartCanvas}></canvas>
