<script>
	import _ from 'lodash'
	const range = _.range
	export let data
	export let macros

	function grid(arr) {return _.map(arr, (row) => _.map(row.split("|")))}
	const clean = (mx) => _.map(mx, (row) => _.map(row, (cell) => cell.trim()))

	const M = clean(grid(macros))
	const H = clean(grid([data.header]))
  let   T = clean(grid(data.texts))
	let   L = clean(grid(data.links))

	for (const item of M)	{
		T = _.map(T, (row) => _.map(row, (cell) => cell.replaceAll(item[0],item[1])))
		L = _.map(L, (row) => _.map(row, (cell) => cell.replaceAll(item[0],item[1])))
	}

	const hash = {}
	hash.L = "text-align:left"
	hash.C = "text-align:center"
	hash.R = "text-align:right"

	if (!data.align) data.align = "LLLLLLLLLLLLL"
	data.align = data.align.replaceAll(' ','')
	const alignments = _.map(data.align, (ch) => hash[ch])

	const cols = H[0].length
	const rows = T.length
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
				{#if L[j] && L[j][i] && L[j][i] != 'x'}
					<td style={alignments[i]}><a href={L[j][i]}>{T[j][i]}</a></td>
				{:else}
					<td style={alignments[i]}>{@html T[j][i]}</td>
				{/if}
			{/each}
			</tr>
		{/each}
	</tbody>
</table>
