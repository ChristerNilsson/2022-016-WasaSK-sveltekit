---
W : https:/www.wasask.se

LagDM:
  header: Lag|Serie|1|2|3|4|5|Lagledare|Telefon
  align:  LLCCCCCLL
  texts: >
    Wasa_I__|Elitserien|19/09|17/10|14/11|12/12|30/01|$B|076-701_27_26
    Wasa_II_|Division_1|26/09|24/10|21/11|19/12|06/02|$S|073-645_34_07
    Wasa_III|Division_2|03/10|31/10|28/11|16/01|13/02|$B|076-701_27_26
    Wasa_IV_|Division_3|10/10|07/11|05/12|23/01|20/02|$B|076-701_27_26
    Wasa_V__|Division_4|10/10|07/11|05/12|23/01|20/02|$B|076-701_27_26
    Wasa_VI_|Division_5|03/10|31/10|28/11|16/01|13/02|$B|076-701_27_26
  links: >
    x|$T=10508|$E__2022-09-19|$E__2022-10-17|$E__2022-11-14|$E__2022-12-12|x|x|x
    x|$T=10509|$X1_2022-09-26|$X1_2022-10-24|$X1_2022-11-21|$X1_2022-12-19|x|x|x
    x|$T=10510|$X2_2022-10-03|$X2_2022-10-31|$X2_2022-11-28|x|x|x|x
    x|$T=10511|$X3_2022-10-10|$X3_2022-11-07|$X3_2022-12-05|x|x|x|x
    x|$T=10512|$X4_2022-10-10|$X4_2022-11-07|$X4_2022-12-05|x|x|x|x
    x|$T=10513|$X5_2022-10-03|$X5_2022-10-31|$X5_2022-11-28|x|x|x|x
  macros: >
    $T|https://member.schack.se/ShowTournamentServlet?id
    $E|https://bildbanken.schack.se/?query=Vy-Lag-DM%20%5FElitserien
    $X|https://bildbanken.schack.se/?query=Vy-Lag-DM%20%5FDivision%20
    $B|Birger%20Wentzel
    $S|Karl-Gustav%20Sjölund

Elitserien:
  header: Lag|Serie|1|2|3|4|5|6|7|8|9|Lagledare|Telefon
  texts: Wasa_I|Elitserien|14/10|15/10|16/10|21/01|22/01|25/02|12/03|13/03|14/03|$B|076-701_27_26
  links: x|$T=10421|x|x|x|x|x|x|x|x|x|x|x
  macros: >
    $B|Birger%20Wentzel
    $T|https://member.schack.se/ShowTournamentServlet?id

Allsvenskan:
  header: Lag|Serie|1|2|3|4|5|6|7|Lagledare|Telefon
  texts: >
    Wasa_II_|Div_II:3_|23/10|13/11|04/12|15/01|05/02|05/03|19/03|Birger_Wenzel____|076-701_27_26
    Wasa_III|Div_II:3_|23/10|13/11|04/12|15/01|05/02|05/03|19/03|Niclas_Hedin_____|073-345_16_54
    Wasa_IV_|Div_III:3|23/10|13/11|04/12|x____|05/02|x____|19/03|Majkel_Kokocinski|076-052_60_05
  links: >
    x|$T=10430|$XII__2022-10-23|$XII__2022-11-13|$XII__2022-12-04|$XII__2023-01-15|$XII__2023-02-05|$XII__2023-03-05|$XII__2023-03-19|x|x
    x|$T=10430|$XII__2022-10-23|$XII__2022-11-13|$XII__2022-12-04|$XII__2023-01-15|$XII__2023-02-05|$XII__2023-03-05|$XII__2023-03-19|x|x
    x|$T=10438|$XIII_2022-10-23|$XIII_2022-11-13|$XIII_2022-12-04|x|$XIII_2023-02-05|x|$XIII_2023-03-19|x|x
  macros: >
    $T|https://member.schack.se/ShowTournamentServlet?id
    $X|https://bildbanken.schack.se/?query=DIV

Stockholmsserien:
  header: Lag|Serie|1|2|3|4|5|6|7|8|Lagledare|Telefon
  texts: Wasa_V|Division_5|23/10|13/11|04/12|15/01|05/02|05/03|19/03|frirond|David_Douhan|okänd
  links: x|$T=10726|$X_2022-10-23|$X_2022-11-13|$X_2022-12-04|$X_2023-01-15|$X_2023-02-05|$X_2023-03-05|$X_2023-03-19|x|x
  macros: >
    $T|https://member.schack.se/ShowTournamentServlet?id
    $X|https://bildbanken.schack.se/?query=Stockholmsserien
---

## Lag-DM
<TABLE data={LagDM} />

## Allsvenskan
<TABLE data={Elitserien} />
<TABLE data={Allsvenskan} />

## Stockholmsserien
<TABLE data={Stockholmsserien} />

[Inbjudan]({W}/Inbjudan_Lag_DM_2022_2023.pdf)
[Tävlingsbestämmelser]({W}/Tavlingsbestammelser_Lag_DM_2022_2023.pdf)

<script>
  import TABLE from "$lib/TABLE.svelte"
</script>
