<script>
	import chartjs from 'chart.js'
	import { onMount } from 'svelte'
	export let title
	export let labels
	export let data
	let chartCanvas
	
	onMount(async (promise) => {
		const ctx = chartCanvas.getContext('2d')
		const chart = new chartjs(ctx, {
			options : {
				animation: false,
				scales: {
            yAxes: [{ticks: {fontSize: 15}}],
            xAxes: [{ticks: {fontSize: 15}}],
        },
				legend: {display: false	}}, 
			type: 'bar',
			data: {
				labels,
				datasets: [{data,backgroundColor: '#888'}]
			}
		})
	})
</script>

<div style='background:white; margin-bottom:20px; width:500px'>
	<h2 style="text-align:center">{title}</h2>
	<canvas bind:this={chartCanvas}></canvas>
</div>

