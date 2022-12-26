<script>
	import _ from 'lodash'
	const range = _.range
	export let data
	export let macros

	function grid(arr) {return _.map(arr, (row) => _.map(row.split("|")))}
	const clean = (mx) => _.map(mx, (row) => _.map(row, (cell) => cell.trim()))
	const warn = (mx) => _.map(mx, (row) => _.map(row, (cell) => cell.includes('$') ? '**MACRO ERROR**' : cell))

	const M = clean(grid(macros))
	const H = clean(grid([data.header]))
  let   T = clean(grid(data.texts))
	let   L = clean(grid(data.links))

	for (const [name,value] of M)	{
		T = _.map(T, (row) => _.map(row, (cell) => cell.replaceAll(name,value)))
		L = _.map(L, (row) => _.map(row, (cell) => cell.replaceAll(name,value)))
	}

	T = warn(T)
	L = warn(L)

	const hash = {}
	hash.L = "text-align:left"
	hash.C = "text-align:center"
	hash.R = "text-align:right"

	const cols = H[0].length
	const rows = T.length

	if (!data.align) data.align = ""
	data.align = data.align.replaceAll(' ','')
	data.align += "L".repeat(Math.max(0,cols-data.align.length))
	const alignments = _.map(data.align, (ch) => hash[ch])

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
				{#if T[j] && (T[j][i] || T[j][i]=='')}
					{#if L[j] && L[j][i] && L[j][i] != 'x'}
						<td style={alignments[i]}><a href={L[j][i]}>{@html T[j][i]}</a></td>
					{:else}
						<td style={alignments[i]}>{@html T[j][i]}</td>
					{/if}
				{:else}
					<td>.</td>
				{/if}
			{/each}
			</tr>
		{/each}
	</tbody>
</table>
