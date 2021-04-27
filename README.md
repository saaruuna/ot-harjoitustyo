# LabRat-pelisovellus

LabRat on 2D-pelisovellus. Pelihahmona on rotta, jota ohjataan labyrintissa juustoa kohti ja vältellään rotanloukkuja. Käyttäjä voi selvittää labyrinttejä sekä tallentaa suunnittelemiaan labyrintteja pelin tietokantaan muiden pelaajien selvitettäväksi.

Tällä hetkellä koossa on pelin runko. Pelin voi käynnistää, rottaa voi liikuttaa lattialla (ei seinien läpi) ja juuston saadessaan voi voittaa pelin. Osuessa rotanloukkuun ei tapahdu mitään.

## Käyttöohjeet

1. Asenna riippuvuudet komennolla `<poetry install>`.
2. Käynnistä peli komennolla `<poetry run invoke start>` tai `<python3 -m poetry run invoke start>`.
3. Liikuttele rottaa labyrintissa nuolinäppäimillä.  
4. Peli loppuu, kun rotta saa juuston.

## Testien suorittaminen

Projektin testit voi suorittaa komennolla `<poetry run invoke test>` tai `<python3 -m poetry run invoke test>`. Kattavuusraportin voi generoida komennolla `<poetry run invoke coverage-report>` tai `<python3 -m poetry run invoke coverage-report>`.

## Dokumentaatio

[Määrittelydokumentti](https://github.com/saaruuna/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/saaruuna/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/saaruuna/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## TODO

* käyttöliittymään mahdollisuus luoda ja tallentaa labyrintteja tietokantaan
