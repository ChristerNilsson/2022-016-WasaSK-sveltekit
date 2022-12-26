---
macros:
  - $W | http://wasask.se
  - $A | https://member.schack.se/turnering
  - $T | https://member.schack.se/ShowTournamentServlet?id
  - $B | https://storage.googleapis.com/bildbanken2/index.html?query
  - $C | https://chess-results.com

januari:
  header: Januari | Ort | Datum | Anmälan | Resultat
  align: LLCLL
  texts:
    - Rilton Cup & Rilton ELO | Stockholm                        |   2022-12-27<br>2023-01-05 | Anmäl dig här                    | Anmälda
    - Blixt-SM                | Scandic Continental, Stockholm   |<b>2022-12-27<br>2023-01-01</b>| Anmäl_dig här                    | Anmälda
    - Rilton 1800             | Stockholm                        |<b>2023-01-02<br>2023-01-05</b>| Anmäl dig här                    | Anmälda
    - Tjejträffen             | Garbosalen, Katarina Södra Skola | 2023-01-07                 | Anmäl dig här                    |
    - Flick-SM                | Göteborg                         | 2023-01-27 <br> 2023-01-29 | Anmäl dig här                    | Anmälda
    - Juniorlag-DM, Elitserien| Salongerna, Stockholm            | 2023-01-28 <br> 2023-01-29                                  ||
  links:
    - $W/Inbjudan_Rilton_Cup_svenska_2022_2023.pdf|              |                          |$C/Anmeldung.aspx?lan=6&tnr=661619| $C/tnr661619.aspx?lan=6
    - $W/INBJUDAN-Blixt-SM-2023.pdf|                             |                          |$A/3336/anmalan                   | $T=10838
    - $W/Inbjudan_Rilton_Cup_svenska_2022_2023.pdf|              |                          |$C/Anmeldung.aspx?lan=6&tnr=661619| $C/tnr661621.aspx?lan=6&art=0&turdet=YES
    - $W/Inbjudan_Tjejtraffen_2023.pdf|                          |                          |$A/3378/anmalan                   | 
    - $W/flicksm2023.pdf      |                                  |                          |$A/3388/anmalan                   | $T=10912

februari:
  header: Februari | Ort | Datum | Anmälan | Resultat
  align: LLCLL
  texts:
    - Elite Hotels Open - GP   |Växjö                 |2023-02-10 <br> 2023-02-12       |Anmäl dig här|Anmälda
    - Juniorlag-DM, Superettan |Salongerna, Stockholm |<b>2023-02-18 <br> 2023-02-19</b>||
    - Västgöta Open            |Stadshotellet Skara   |2023-02-18 <br> 2023-02-19       |             |Anmälda
    - Trojanska Hästens Vår-JGP|Vallatorpsskolan, Täby|<b>2023-02-25</b>||
    - Sportlovsturneringen     |Salongerna, Stockholm |<b>2023-02-27</b>||
  links:
    - x|||$A/3070/anmalan|$T=10378
    - x
    - x||||$C/tnr710950.aspx?lan=6&art=3&turdet=YES

mars:
  header: Mars | Ort | Datum | Anmälan | Resultat
  align: LLCLL
  texts:
    - Stockholmsmästerskapet             | Salongerna, Stockholm|Startar 2023-03-06      ||
    - Elitseriesammandrag rond 7-9       | Södertälje           |2023-03-10<br>2023-03-12||
    - Tyresö JGG                         | Kumla skola, Tyresö  |<b>2023-03-18</b>       ||
    - Snabbschack-SM,knattar och miniorer| ?                    |<b>2023-03-25</b>       ||
    - Compo Cup                          | Salongerna, Stockholm|2023-03-31<br>2023-04-02||

april:
  header: April | Ort | Datum | Anmälan | Resultat
  align: LLCLL
  texts:
    - Påskturneringen - GP   |Norrköping               |2023-04-07<br>2023-04-10    |Anmäl dig här|Anmälda
    - Påsklovsturneringen    |Salongerna, Stockholm    |<b>2023-04-14</b>           |             |
    - Kadettallsvenskans kval|?                        |**2023-04-22<br>2023-04-23**|             |
    - Wasa JGP               |Salongerna, Stockholm (?)|**2023-04-29<br>2023-04-30**|             |
  links:
    - x|||$A/3071/anmalan|$T=10380

maj:
  header: Maj | Ort | Datum | Anmälan | Resultat
  align: LLCLL
  texts:
    - TePe-Sigeman & Co Chess Tournament|Elite Plaza Hotel, Malmö|2023-05-04<br>2023-05-10    ||
    - Stockholmsmästerskapet i blixt    |Salongerna, Stockholm   |2023-05-06                  ||
    - Skollags-SM                       |?                       |2023-05-06<br>2023-05-07    ||
    - JDM i snabbschack                 |Salongerna, Stockholm   |**2023-05-13<br>2023-05-14**||
    - Deltalift Open - GP               |Tylösand                |2023-05-18<br>2023-05-20    |Anmäl dig här|Anmälda
    - Stockholm Elo Challenge           |Salongerna, Stockholm   |2023-05-17<br>2023-05-21    ||
  links:
    - x
    - x
    - x
    - x
    - x|||$A/3072/anmalan | $A/3072/anmalan

---

Klicka på tävlingens namn för att se Inbjudan.

<TABLE data={januari} {macros} ></TABLE>
<TABLE data={februari} {macros} ></TABLE>
<TABLE data={mars} {macros} ></TABLE>
<TABLE data={april} {macros} ></TABLE>
<TABLE data={maj} {macros} ></TABLE>

<script>
  import TABLE from "$lib/TABLE.svelte"
</script>
