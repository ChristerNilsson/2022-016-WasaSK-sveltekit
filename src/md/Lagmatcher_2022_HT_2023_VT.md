---
date : 2022-07-01
attr : SPLDL_
W : https:/www.wasask.se

macros:
  - $T|https://member.schack.se/ShowTournamentServlet?id
  - $E|https://bildbanken.schack.se/?query=Vy-Lag-DM Elitserien
  - $X|https://bildbanken.schack.se/?query=Vy-Lag-DM Division_
  - $Y|https://bildbanken.schack.se/?query=DIV
  - $S|https://bildbanken.schack.se/?query=Stockholmsserien

LagDM:
  header: Lag-DM|Serie|1|2|3|4|5|Lagledare|Telefon
  align:  LLCCCCCLL
  texts:
    - Wasa I  |Elitserien|<b>19 sep</b>|17 okt|14 nov|12 dec|30 jan|Birger Wentzel     |076-701 27 26
    - Wasa II |Division 1|26 sep|24 okt|21 nov|19 dec|06 feb|Karl-Gustav Sjölund|073-645 34 07
    - Wasa III|Division 2|03 okt|31 okt|28 nov|16 jan|13 feb|Birger Wentzel     |076-701 27 26
    - Wasa IV |Division 3|10 okt|07 nov|05 dec|23 jan|20 feb|Birger Wentzel     |076-701 27 26
    - Wasa V  |Division 4|10 okt|07 nov|05 dec|23 jan|20 feb|Birger Wentzel     |076-701 27 26
    - Wasa VI |Division 5|03 okt|31 okt|28 nov|16 jan|13 feb|Birger Wentzel     |076-701 27 26
  links:
    - x|$T=10508|$E  2022-09-19|$E  2022-10-17|$E  2022-11-14|$E  2022-12-12|||
    - x|$T=10509|$X1 2022-09-26|$X1 2022-10-24|$X1 2022-11-21|$X1 2022-12-19|||
    - x|$T=10510|$X2 2022-10-03|$X2 2022-10-31|$X2 2022-11-28||||
    - x|$T=10511|$X3 2022-10-10|$X3 2022-11-07|$X3 2022-12-05||||
    - x|$T=10512|$X4 2022-10-10|$X4 2022-11-07|$X4 2022-12-05||||
    - x|$T=10513|$X5 2022-10-03|$X5 2022-10-31|$X5 2022-11-28||||

Elitserien:
  header: Elitserien|Serie|1|2|3|4|5|6|7|8|9|Lagledare|Telefon
  texts:
    - Wasa I|Elitserien|14 okt|15 okt|16 okt|21 jan|22 jan|25 feb|12 mar|13 mar|14 mar|Birger Wentzel|076-701 27 26
  links:
    - x|$T=10421

Allsvenskan:
  header: Allsvenskan|Serie|1|2|3|4|5|6|7|Lagledare|Telefon
  texts:
    - Wasa II |Div II:3 |23 okt|13 nov|04 dec|15 jan|05 feb|05 mar|19 mar|Birger Wenzel    |076-701 27 26
    - Wasa III|Div II:3 |23 okt|13 nov|04 dec|15 jan|05 feb|05 mar|19 mar|Niclas Hedin     |073-345 16 54
    - Wasa IV |Div III:3|23 okt|13 nov|04 dec|      |05 feb|      |19 mar|Majkel Kokocinski|076-052 60 05
  links:
    - x|$T=10430|$XII  2022-10-23|$XII  2022-11-13|$XII  2022-12-04|$XII 2023-01-15|$XII  2023-02-05|$XII 2023-03-05|$XII  2023-03-19||
    - x|$T=10430|$XII  2022-10-23|$XII  2022-11-13|$XII  2022-12-04|$XII 2023-01-15|$XII  2023-02-05|$XII 2023-03-05|$XII  2023-03-19||
    - x|$T=10438|$XIII 2022-10-23|$XIII 2022-11-13|$XIII 2022-12-04|               |$XIII 2023-02-05|               |$XIII 2023-03-19||

Stockholmsserien:
  header: Stockholmsserien|Serie|1|2|3|4|5|6|7|8|Lagledare|Telefon
  texts:
    - Wasa V|Division 5|23 okt|13 nov|04 dec|15 jan|05 feb|05 mar|19 mar|frirond|David Douhan|
  links:
    - x|$T=10726|$S 2022-10-23|$S 2022-11-13|$S 2022-12-04|$S 2023-01-15|$S 2023-02-05|$S 2023-03-05|$S 2023-03-19
---

<TABLE data={LagDM} {macros} />
<TABLE data={Elitserien} {macros} />
<TABLE data={Allsvenskan} {macros} />
<TABLE data={Stockholmsserien} {macros} />

[Inbjudan]({W}/Inbjudan_Lag_DM_2022_2023.pdf)
[Tävlingsbestämmelser]({W}/Tavlingsbestammelser_Lag_DM_2022_2023.pdf)

<script>
  import TABLE from "$lib/TABLE.svelte"
</script>
