<script>
	import _ from 'lodash'
	const range = _.range
	export let header
	export let align // optional
	export let texts
	export let links
	export let macros

	function grid(s) {return _.map(s.split(" "), (row) => _.map(row.replaceAll('_',' ').split("|")))}
	function pretty(s) { return s.replaceAll('%20',' ').replaceAll('%5F','_') }

	const M = grid(macros)
	for (const item of M)	{
		texts = texts.replaceAll(item[0],item[1])
		links = links.replaceAll(item[0],item[1])
	}
	const H = grid(header.trim())
	const T = grid(texts.trim())
	const L = grid(links.trim())

	const hash = {}
	hash.L = "text-align:left"
	hash.C = "text-align:center"
	hash.R = "text-align:right"

	if (!align) align = "LLLLLLLLLLLLL"
	align = align.replaceAll(' ','')
	const alignments = []
	for (const ch of align) {
		alignments.push(hash[ch])
	}

	const cols = header.split('|').length
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
