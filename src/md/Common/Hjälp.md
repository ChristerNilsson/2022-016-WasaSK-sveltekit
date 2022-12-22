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
* Förkortningar kan definieras, per post. T ex:
	* `B = https://storage.googleapis.com/bildbanken2/index.html`
	* `T = https://member.schack.se/ShowTournamentServlet`
* Man kan påverka utseendet mha `<style>`
* Postens skapande används som publiceringstidpunkt
* Vill du stå som författare skriver du in detta själv enligt nedan

## Markdown

```c
---                                                          Inleder Metadata. Måste stå först i .md-filen
title:  Lathund till Markdown                                (default: filens namn minus extension)
date:   2022-12-24 15:00                                     (default: filens skapandedatum)
author: Christer Nilsson                                     (default: författare okänd)
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