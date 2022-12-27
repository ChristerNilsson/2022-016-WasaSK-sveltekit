_av Christer Nilsson_

## Motiv

* Sökbara poster
* Enklare redigering
* Anpassad för mobiler

## Hjälp till läsare

* Sökning sker alltid från början av varje ord
* Menyn fungerar som en katalogstruktur
	* `Upp` innebär att man går upp till en högre nivå

## Hjälp till redigerare

* Enklare redigering mha [MarkDown](https://mdsvex.com/playground)
	* Man kan fortfarande skriva `HTML` för delar av poster, även hela poster
* Förkortningar kan definieras, per post. Två varianter existerar:
	* `$T|https://member.schack.se/ShowTournamentServlet?id`
		* `$T=12345`
	* `T : https://member.schack.se/ShowTournamentServlet?id`
		* `{T}=12345`
* Man kan påverka utseendet mha `<style>`
* Postens skapande används som publiceringstidpunkt

## Markdown

```c
---                                                          Inleder Metadata. Måste stå först i .md-filen
T:      https://member.schack.se/ShowTournamentServlet?id=   Förkortning
---                                                          Avslutar Metadata. Metadata-sektionen visas inte.

{T}12345           Användning av metadata

#                  Mycket stor rubrik
##                 Stor rubrik
###                Lagom stor rubrik
####               Lagom liten rubrik
#####              Liten rubrik
######             Mycket liten rubrik

   text        text      Normal stil
  *text*      _text_     Fet stil
 **text**    __text__    Kursiv stil
***text***  ___text___   Fet och kursiv stil

*                  Punktlista
1                  Sifferlista

---                Horisontell linje

[Text](https:...)  Länk
![alt](bild.jpg)   Bild

|Namn           |Prenumeranter|   Tabellhuvud
|:-             |           -:|   Vänsterjusterad och högerjusterad kolumn
|Hikaru Nakamura|1470k|           Mellanslag kan utelämnas
Anna Cramling   | 221k            Yttre lodstreck (|) kan utelämnas
```

## TABLE

```
---
macros:
  - $W | http://wasask.se
  - $A | https://member.schack.se/turnering
  - $T | https://member.schack.se/ShowTournamentServlet?id
  - $C | https://chess-results.com

januari:
  header: Januari | Ort | Datum | Anmälan | Resultat
  align: LLCLL
  texts:
    - Rilton Cup & Rilton ELO | Stockholm                        |   2022-12-27<br>2023-01-05    | Anmäl dig här                    | Anmälda
    - Blixt-SM                | Scandic Continental, Stockholm   |<b>2022-12-27<br>2023-01-01</b>| Anmäl_dig här                    | Anmälda
  links:
    - $W/Inbjudan_Rilton_Cup_svenska_2022_2023.pdf|              |                               |$C/Anmeldung.aspx?lan=6&tnr=661619| $C/tnr661619.aspx?lan=6
    - $W/INBJUDAN-Blixt-SM-2023.pdf|                             |                               |$A/3336/anmalan                   | $T=10838
---

<TABLE data={januari} {macros} ></TABLE>
<TABLE data={februari} {macros} ></TABLE>

<script>
  import TABLE from "$lib/TABLE.svelte"
</script>
```

[Resultatet](/post/2023/Inbjudningar_2023_VT.md)