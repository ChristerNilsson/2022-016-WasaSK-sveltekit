# Långt driven hantering av tabell

https://mdsvex.com/playground

## App.svx

* Rader separeras med ny rad. 
	* > och dubbla mellanslag nödvändiga pga YAML
* Kolumner separeras med |
* x anger cell utan länk
* macron skapas bland metadatat
	* Ersätt mellanslag med %20
	* Ersätt _ med %5F
	* Dessa två tecken är ej tillåtna i macron
		* De får bara användas för att ange gridens struktur

```
---
header: Lag|Serie|1|2|3|4|Lagledare|Telefon
texts: >
  Wasa_I|Div_1|19/09|13/03|14/03|15/03|Birger_Wentzel|070-123_45_67
  Wasa_II|Div_2|12/04|13/04|14/04|15/04|Birger_Wentzel|070-123_45_67
  Wasa_III|Div_3|12/05|13/05|14/05|15/05|Birger_Wentzel|070-123_45_67
  Wasa_IV|Div_4|10/10|13/06|14/06|15/06|Birger_Wentzel|070-123_45_67
  Wasa_V|Div_5|12/06|13/06|14/06|15/06|Birger_Wentzel|070-123_45_67
links: >
  x|$T=10508|$X1_2022-09-19|$X1_2022-05-12|$X1_2022-05-12|$X1_2022-05-12|x|x
  x|$T=10509|$X2_2022-05-12|$X2_2022-05-12|$X2_2022-05-12|$X2_2022-05-12|x|x
  x|$T=10510|$X3_2022-05-12|$X3_2022-05-12|$X3_2022-05-12|$X3_2022-05-12|x|x
  x|$T=10511|$X4_2022-10-10|$X4_2022-05-12|$X4_2022-05-12|$X4_2022-05-12|x|x
  x|$T=10512|$X5_2022-05-12|$X5_2022-05-12|$X5_2022-05-12|$X5_2022-05-12|x|x
macron: >
  $T|https://member.schack.se/ShowTournamentServlet?id
  $X|https://bildbanken.schack.se/?query=Vy-Lag-DM%20%5FDivision%20
---

<script>
	import TABLE from "./TABLE.svelte"
</script>

<TABLE {header} {texts} {links} {macron} />
```

## TABLE.svelte
```
<script>
	import _ from 'lodash'
	const range = _.range
	export let header
	export let texts
	export let links
	export let macron
	function grid(s) {return _.map(s.split(" "), (row) => _.map(row.replaceAll('_',' ').split("|")))}
	const M = grid(macron)
	const H = grid(header)
	const T = grid(texts)
	for (const item of M)	{
		links = links.replaceAll(item[0],item[1])
	}
	const L = grid(links)
	const cols = header.split('|').length
	const rows = L.length
</script>

<table>
	<thead>
	{#each H[0] as h}
		<th>{h}</th>
	{/each}
	</thead>
	<tbody>
		{#each range(rows) as j}
			<tr>
			{#each range(cols) as i}
				{#if L[j][i] && L[j][i] != 'x'}
					<td><a href={L[j][i]}>{T[j][i]}</a></td>
				{:else}
					<td>{T[j][i]}</td>
				{/if}
			{/each}
			</tr>
		{/each}
	</tbody>
</table>
```

## Kommentar
```
[//]: # (This may be the most platform independent comment)
```

## Iakttagelser på Wasas hemsida

### Tabeller

Följande nyckelord definieras av HTML plus avslutning med `</>` :
```
table
	thead
		th
	tbody
		tr
			td

Dessa tolv taggar ersätts av tre tecken i Markdown: lodstreck, kolon och bindestreck (|:-)
```

Av dessa tolv ord, använder Wasa bara table, tr och td, ofta obalanserat.
Till exempel används aldrig `<thead>`,`<tbody>` eller `</tr>`

### Övrigt

* Vid flytt av filer, hänger inte relativa länkar med.
* Följande felaktiga konstruktion är vanlig: `target="_blank" target="_blank"`
* Även denna bryter mot syntaxen: `<b><font></b></font>`
* Denna godkänns inte heller: `<==>`

### Frekvenser i wasask.se/2021_inbjudningar.php (ca 600 rader, 140 i markdown)

```
         <> </>
<thead>   0   0
<th>      0   0
<tbody>   0   0
<tr>    373   0
<td>    893 957
&nbsp; 2399
```

### Sortering av filnamn

* Ersätt alla mellanslag med underscore i filnamn

1. Inbjudan / Program
2. Junior / Senior
3. 2021 / 2022
4. VT / HT (tyvärr sorteras HT före VT)

Exempel: `Program_och_Tävlingar_Junior_2011_HT.md`