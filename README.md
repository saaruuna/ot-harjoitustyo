# LabRat-pelisovellus

LabRat on 2D-pelisovellus. Pelihahmona on rotta, jota ohjataan labyrintissa juustoa kohti ja vältellään rotanloukkuja. Käyttäjä voi selvittää labyrinttejä sekä tallentaa suunnittelemiaan labyrintteja pelin tietokantaan muiden pelaajien selvitettäväksi.

Tällä hetkellä koossa on pelin runko, tietokanta ja hieman käyttöliittymää. Pelin voi käynnistää, ja alkuvalikosta voi valita yhden labyrintin pelattavaksi. Rottaa voi liikuttaa lattialla, juuston saadessaan voi voittaa pelin ja osuessa rotanloukkuun hävitä. Tämän jälkeen voi sulkea sovelluksen tai navigoida alkuun. Tehtävänä on vielä labyrinttivalikko ja käyttöliittymä labyrinttien suunnittelemiseen.

## Käyttöohjeet

1. Asenna riippuvuudet komennolla `<poetry install>`.
2. Käynnistä peli komennolla `<poetry run invoke start>` tai `<python3 -m poetry run invoke start>`.
3. Voit navigoida sovelluksessa nuolinäppäimillä.

## Testien suorittaminen

Projektin testit voi suorittaa komennolla `<poetry run invoke test>` tai `<python3 -m poetry run invoke test>`. Kattavuusraportin voi generoida komennolla `<poetry run invoke coverage-report>` tai `<python3 -m poetry run invoke coverage-report>`.

## Dokumentaatio

[Määrittelydokumentti](https://github.com/saaruuna/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/saaruuna/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/saaruuna/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## TODO

* käyttöliittymään mahdollisuus luoda ja tallentaa labyrintteja tietokantaan
