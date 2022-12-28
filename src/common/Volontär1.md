# Översätta arkiverade websidor till Markdown.

[Input](http://wasask.se/lag_speldatum_ht2022-vt2023.ulenkar.php)

Output:
```c
---
A : https://member.schack.se/turnering
B : https://storage.googleapis.com/bildbanken2/index.html?query=
T : https://member.schack.se/ShowTournamentServlet?id=
---

<div>

### Lag-DM

Lag        |Serie                 |1                     |                     2|                     3|                     4|                     5|Lagledare    |Telefon
         :-|                    :-|                    :-|                    :-|                    :-|                    :-|                    :-|           :-|-
Wasa SK    |[Elitserien]({T}10508)|[19/09]({B}2022-09-19)|[17/10]({B}2022-10-17)|[14/11]({B}2022-11-14)|[12/12]({B}2022-12-12)|[30/01]({B}2023-01-30)|Birger Wenzel|076 - 123 45 67
Wasa SK II |[Division 1]({T}10509)|[26/09]({B}2022-09-26)|[24/10]({B}2022-10-24)|[21/11]({B}2022-11-21)|[19/12]({B}2022-12-19)|[06/02]({B}2023-02-06)|Karl-Gustav Sjölund|073 - 645 34 07
Wasa SK III|[Division 2]({T}10510)|[03/10]({B}2022-10-03)|[31/10]({B}2022-10-31)|[28/11]({B}2022-11-28)|[16/01]({B}2023-01-16)|[13/02]({B}2023-02-13)|Birger Wenzel|076 - 123 45 67
Wasa SK IV |[Division 3]({T}10511)|[10/10]({B}2022-10-10)|[07/11]({B}2022-11-07)|[05/12]({B}2022-12-05)|[23/01]({B}2023-01-23)|[20/02]({B}2023-02-20)|Birger Wenzel|076 - 123 45 67
Wasa SK V  |[Division 4]({T}10512)|[10/10]({B}2022-10-10)|[07/11]({B}2022-11-07)|[05/12]({B}2022-12-05)|[23/01]({B}2023-01-23)|[20/02]({B}2023-02-20)|Birger Wenzel|076 - 123 45 67
Wasa SK VI |[Division 5]({T}10513)|[03/10]({B}2022-10-03)|[31/10]({B}2022-10-31)|[28/11]({B}2022-11-28)|[16/01]({B}2023-01-16)|[13/02]({B}2023-02-13)|Birger Wenzel|076 - 123 45 67

### Allsvenskan

|Lag|Serie|1|2|3|4|5|6|7|Lagled|Tel|
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|-|
|Wasa SK II |[DIV II:3]({T}10430)|[23-10]({B}2022-10-23)|[13-11]({B}2022-11-13)|[04-12]({B}2022-12-04)|[15-01]({B}2023-01-15)|[05-02]({B}2023-02-05)|[05-03]({B}2023-03-05)|[19-03]({B}2023-03-19)|Birger Wenzel|076 - 123 45 67|
|Wasa SK III|[DIV II:3]({T}10430)|[23-10]({B}2022-10-23)|[13-11]({B}2022-11-13)|[04-12]({B}2022-12-04)|[15-01]({B}2023-01-15)|[05-02]({B}2023-02-05)|[05-03]({B}2023-03-05)|[19-03]({B}2023-03-19)|Niclas Hedin|073 - 645 34 07|

[Inbjudan](https://www.wasask.se/Inbjudan_Lag_DM_2022_2023.pdf)
[Tävlingsbestämmelser](https://www.wasask.se/Tavlingsbestammelser_Lag_DM_2022_2023.pdf)

</div>

<style>
	table {border-collapse: collapse}
	table thead th {
		background-color: #000;
		color: #ff0;
		font-size: 13px;
		border: 1px solid #555;
	}
	table tbody td {border: 1px solid #555;}
	table tbody tr {background-color: #eee;}
	table tbody tr:nth-child(odd) {background-color: #fff;}	
	div {background: #FFC200}	
</style>

```

## Färdigt [resultat](http://localhost:5174/post/Datum_f%C3%B6r_Wasas_lagmatcher_HT_2022_och_VT_2023.md)

![alt](/images/Volontär1.JPG)

[Tutorial](https://www.markdowntutorial.com)

[Try it!](https://mdsvex.com/playground)
