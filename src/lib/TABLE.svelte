<script>
	import _ from 'lodash'
	const range = _.range
	export let data

	function grid(arr) {return _.map(arr, (row) => _.map(row.split("|")))}
	function pretty(s) { return s.replaceAll('%20',' ').replaceAll('%5F','_') }
	const clean = (mx) => _.map(mx, (row) => _.map(row, (cell) => cell.trim()))

	const M = clean(grid(data.macros))
	// console.log({M})
	const H = clean(grid([data.header]))
	// console.log({H})
  let T = clean(grid(data.texts))
	// console.log({T})
	let L = clean(grid(data.links))
	// console.log({L})

	for (const item of M)	{
		T = _.map(T, (row) => _.map(row, (cell) => cell.replaceAll(item[0],item[1])))
		L = _.map(L, (row) => _.map(row, (cell) => cell.replaceAll(item[0],item[1])))
	}

	console.log({T})
	console.log({L})

	const hash = {}
	hash.L = "text-align:left"
	hash.C = "text-align:center"
	hash.R = "text-align:right"

	if (!data.align) data.align = "LLLLLLLLLLLLL"
	data.align = data.align.replaceAll(' ','')
	const alignments = []
	for (const ch of data.align) {
		alignments.push(hash[ch])
	}

	const cols = H[0].length
	const rows = L.length
</script>

<table>
	<thead>
	{#each range(cols) as i}
		<th>{H[0][i]}</th>
	{/each}
	</thead>
	<tbody>
		{#each range(rows) as j}
			<tr>
			{#each range(cols) as i}
				{#if L[j][i] && L[j][i] != 'x'}
					<td style={alignments[i]}><a href={L[j][i]}>{pretty(T[j][i])}</a></td>
				{:else}
					<td style={alignments[i]}>{pretty(T[j][i])}</td>
				{/if}
			{/each}
			</tr>
		{/each}
	</tbody>
</table>
