# Wasa SK

## URL

Följande entry points finns:

URL|Beskrivning
-|-
/                            | Visar hundra senaste posterna, med senaste först.
/post                        | Visar posternas rubriker
/post/Medlemskap_i_Wasa.md   | Visar en .md-post
/post/Medlemskap_i_Wasa.html | Visar en .html-post
/query                       | Visa alla sökbara ord
/query/ett_eller_flera_ord   | Visar funna posters rubriker

Sökningen visar en kombination av OCH samt ELLER. Poster med flera träffar kommer före poster med färre träffar.

## JSON
```
{"menu":
{"Hem":"/post",
"Medlemskap":"Medlemskap_i_Wasa.md",
"Alla ord":"/query",
...
"md":
{"Välkommen_till_Wasa_SK.md":["2022-12-17 09:10:40",
" alla allsvenska alt antal at att av barn barnen bedriver berömda bli bottom broar buss"],
...
```

## md
Innehåller .md filer

## html
Kan bara nås via menyn i nuläget. Problemet är att md processas till html, men att släppa igenom html oförändrat är knepigt.  
Att döpa om html-filerna till .md fungerar ej eftersom de inte blir godkända.

## Inspiration

https://joshcollinsworth.com/blog/build-static-sveltekit-markdown-blog

## images

Lite knepigt att hitta hur man gör.
```
![alt](/images/Volontär1.JPG)
```

/ pekar på static-katalogen

Preview i VS Code fungerar ej. Kan ev gåatt installera en annan md-viewer.
