<script>
	import {site} from '$lib/site.js'
	import {timeSince} from '$lib/utils/utils.js'
	const stats = $site.stats
</script>

<h1>🧮 Statistik</h1> 

<table>
	<thead><tr>
		<th>Statistik</th>
		<th>Antal</th>
		<th>Bytes</th>
	</tr></thead>
	<tbody>
		<tr><td>Uppdaterad  </td><td align='right'> {timeSince(stats.updated)} sedan</td><td></td></tr>
		<tr><td>Poster .md  </td><td align='right'> {stats.mdPosts}   </td><td align='right'>{stats.mdBytes}</td></tr>
		<tr><td>Poster .php </td><td align='right'> {stats.phpPosts}  </td><td align='right'>{stats.phpBytes}</td></tr>
		<tr><td>Unika ord   </td><td align='right'> {stats.uniqWords} </td><td align='right'>{stats.wordBytes}</td></tr>
		<tr><td>Menyrader   </td><td align='right'> {stats.menuItems} </td><td align='right'></td></tr>
		<tr><td>Filer       </td><td align='right'> {stats.files}     </td><td align='right'></td></tr>
	</tbody>
</table>

<a href="/words">{stats.uniqWords} unika ord</a>

