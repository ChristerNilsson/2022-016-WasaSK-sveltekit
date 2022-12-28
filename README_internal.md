# Långt driven hantering av tabell

https://mdsvex.com/playground

* Rader separeras med ny rad. 
	* dubbla mellanslag och bindestreck nödvändiga pga YAML
* Kolumner separeras med |
* x anger cell utan innehåll
* macros skapas bland metadatat
* Mellanslag är EJ signifikanta

```
---
macros:
  - $T | https://member.schack.se/ShowTournamentServlet?id
  - $X | https://bildbanken.schack.se/?query=Vy-Lag-DM _Division 
januari:
  header: Lag |Serie   |1             |2             |3             |4             |Lagledare     |Telefon
  align:  L    L        C              C              C              C              L              L
  texts:
    - Wasa I  |Div 1   |19/09         |13/03         |14/03         |15/03         |Birger Wentzel|070-123 45 67
    - Wasa II |Div 2   |12/04         |13/04         |14/04         |15/04         |Birger Wentzel|070-123 45 67
    - Wasa III|Div 3   |12/05         |13/05         |14/05         |15/05         |Birger Wentzel|070-123 45 67
    - Wasa IV |Div 4   |10/10         |13/06         |14/06         |15/06         |Birger Wentzel|070-123 45 67
    - Wasa V  |Div 5   |12/06         |13/06         |14/06         |15/06         |Birger Wentzel|070-123 45 67
  links:
    - x       |$T=10508|$X1_2022-09-19|$X1_2022-05-12|$X1_2022-05-12|$X1_2022-05-12||
    - x       |$T=10509|$X2_2022-05-12|$X2_2022-05-12|$X2_2022-05-12|$X2_2022-05-12||
    - x       |$T=10510|$X3_2022-05-12|$X3_2022-05-12|$X3_2022-05-12|$X3_2022-05-12||
    - x       |$T=10511|$X4_2022-10-10|$X4_2022-05-12|$X4_2022-05-12|$X4_2022-05-12||
    - x       |$T=10512|$X5_2022-05-12|$X5_2022-05-12|$X5_2022-05-12|$X5_2022-05-12||
---

<script>
	import TABLE from "./TABLE.svelte"
</script>

<TABLE data={januari} {macros} />
```

## TABLE.svelte

* Denna komponent är avsedd att underlätta skapandet av tabeller
* Wasas tabeller kan vara mycket breda mtp att länkar till bildbanken ska in i varje cell.
* Vill man ha flera tabeller på samma sida kan man hantera det i metadatat.
* Tänk på att indentera med två mellanslag. Inga tabbar. Krävs av YAML
* parametrar
	* **header** (obligatorisk)
	* **texts**  (obligatorisk)
	* **align**
	* **links** 
	* **macros**
* **header** + **texts** motsvarar markdowns normala tabellhantering
* **links** behövs om vill att cellerna ska innehålla länkar
* **macros** kan man minska tabellens bredd så att skärmen utnyttjas bättre
* **align** är en sträng med L, C eller R för varje kolumn. L är default
* Exempel: Lagmatcher_2022_HT_2023_VT.md
* Rader behöver ett inledande bindestreck
* Kolumner separeras med **|**
* Mellanslag ignoreras
* TABLE.svelte skapar kod med `<table>`,`<thead>`,`<th>`,`<tbody>`,`<tr>`, `<td style="text-align:center">` samt `</>`
* Celler kan innehålla htmlkod. T ex `<b></b>` och `<br>`

## Kommentarer
```
#        innanför metedata
[//]: # (utanför metedata)
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

Exempel: `Program_Junior_2011_HT.md`

### Blandade koder på wasask.se

Vissa filer innehåller både utf-8 OCH cp1252.  
Saknar kodinformation: `<meta charset="utf-8">` eller `<meta charset="cp1252">`  
De flesta filer har bara ett enda felaktigt tecken. Dessa läses med `s.decode("utf-8","backslashreplace")` i Python.  
Sedan får man manuellt redigera skräptecknet.
Legacy hanteras genom en fil som innehåller önskade filer: `legacy.txt`
Dessa filer hämtas med pythonprogrammet och lagras under `legacy`, där man kan redigera.
Efter manuell rättning kan orden sökas fram.
Pga att sveltekit klagar på html-syntax, pekas man till wasask.se när man vill en sida.
Då dyker felet upp igen. Det måste alltså rättas på wasask.se.

### Seven Dimensions

* date: yyyy-mm-dd
* age: Knatte Minior Junior Senior Veteran
* typ: Resultat Inbjudan Program Meddelande Utbildning Game Diverse
* team: 1 2 3 4 5 6 7 8 X=10 L=50 Klass
* level: KM DM SM NM EM WM
* time: Blixt=5 Snabb=10-20 Half=45 Lång=90-120
* sex: Female Male Other

Dessa kodas t ex som  
2022-12-10 J R 1 D S _ JGP_finaler_2022.php  
_ anger att dimensionen ej är tillämplig.

(Jag har kodat sex som _ och F. M är ju öppen för alla, vilket F ej är. Ska man göra samma sak med Junior och Senior?)
