<script>
	import _ from 'lodash'
	import {site} from '$lib/stores.js'
	import {timeSince} from '$lib/utils.js'
	import Stat from '$lib/components/Stat.svelte'

	const kb = (bytes) => Math.round(bytes/1024)

	const stats = $site.stats
</script>

<h1>🧮 Statistik</h1> 

<table>
	<thead><tr>
		<th>Statistik</th>
		<th>Antal</th>
		<th>Bytes</th>
		<th>Bytes/post</th>
	</tr></thead>
	<tbody>
		<tr><td>Uppdaterad  </td><td align='right'> {timeSince(stats.updated)} sedan</td><td></td><td></td></tr>
		<tr><td>Poster md   </td><td align='right'> {stats.mdPosts}   </td><td align='right'>{kb(stats.mdBytes)}k</td><td align='right'>{Math.round(stats.mdBytes/stats.mdPosts)}</td></tr>
		<tr><td>Poster php  </td><td align='right'> {stats.phpPosts}  </td><td align='right'>{kb(stats.phpBytes)}k</td><td align='right'>{Math.round(stats.phpBytes/stats.phpPosts)}</td></tr>
		<tr><td>Poster blog </td><td align='right'> {stats.blogPosts} </td><td align='right'>{kb(stats.blogBytes)}k</td><td align='right'>{Math.round(stats.blogBytes/stats.blogPosts)}</td></tr>
		<tr><td>Unika ord   </td><td align='right'> {stats.uniqWords} </td><td align='right'>{kb(stats.wordBytes)}k</td><td></td></tr>
		<tr><td>Menyrader   </td><td align='right'> {stats.menuItems} </td><td></td><td></td></tr>
		<tr><td>Filer       </td><td align='right'> {stats.files}     </td><td></td><td></td></tr>
	</tbody>
</table>

<a href="/words">{stats.uniqWords} unika datum och ord</a>

<p>I alla diagrammen innehåller y-axeln antal publicerade artiklar.</p>

<Stat title="År"      data={stats.år} />
<Stat title="Månad"   data={stats.månad} />
<Stat title="Ålder"   data={stats.ålder} />
<Stat title="Typ"     data={stats.typ} />
<Stat title="Lag"     data={stats.lag} />
<Stat title="Nivå"    data={stats.nivå} />
<Stat title="Tid"     data={stats.tid} />
<Stat title="Kön"     data={stats.kön} />
