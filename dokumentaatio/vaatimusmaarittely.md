# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on 2D- peli nimeltä LabRat. Pelihahmo on rotta, jota ohjataan labyrintin sisällä olevaa juustoa kohti. Pelin voittaa, kun rotta saa juuston. Pelin häviää, jos astuu rotanloukkuun. Pelaajan on mahdollista selvittää labyrinttejä. Tämän lisäksi pelaaja voi suunnitella ja tallentaa labyrinttejä tietokantaan muiden pelaajien selvitettäväksi.

Pelissä on seuraavat objektit:
* Rotta
* Seinä
* Lattia
* Juusto
* Loukku

## Toiminnallisuudet
* Labyrinttitietokanta.
* Labrojen suunnittelutyökalu.
* Labrojen selvittäminen ja pelien voittaminen/häviäminen.
* Main Menu -näkymä , mistä valitaan suunnitella tai selvittää labra.
* Lab Selection Menu -näkymä, mistä valitaan labra selvitettäväksi.
* Game Over Menu -näkymä, mistä valitaan sulkea peli tai mennä alkuun.
* Lab Size Menu -näkymä, mistä valitaan suunniteltavan labran koko.
* Navigoiminen näkymien välillä.

## Käyttäjät

Sovelluksessa ei ole kirjautumismahdollisuutta. Labyrinttejä luodaan ja selvitetään kirjautumatta.

## Käyttöliittymä

Alkuperäinen käyttöliittymäluonnos:

![LabRat-käyttöliittymäluonnos](kuvat/LabRat_kayttis.jpg)

Pelin käyttöliittymä näyttää ensin pelaajalle Main Menu -näkymän. Tästä pelaaja voi siirtyä nuolinäppäimillä joko selvittämään labyrinttia (Solve) tai suunnittelemaan labyrinttia (Create).

Solve: Valitsemalla Solve pelaaja siirtyy Lab Selection Menu -näkymään, mistä valitaan pelattavaksi labyrintti nimen perustella. Näkymän jokainen "sivu" näyttää kolme labyrinttivaihtoehtoa kerrallaan. Pelaaja voi selata vaihtoehtoja ja valita mieleisensä nuolinäppäimillä.

Valitessa labyrintin siirtyy pelinäkymään, missä rottaa liikutellaan labrassa nuolinäppäimillä. Pelin voittaa, jos rotta osuu juustoon. Pelin häviää, jos rotta osuu loukkuun.

Pelin päättyessä siirrytään Game Over Menu -näkymään, missä pelaaja voi valita nuolinäppäimilä palata alkunäkymään (Play again) tai sulkea pelin (Quit).

Create: Valitsemalla Create pelaaja siirtyy labyrinttien suunnittelutyökalun näkymään, missä pelaaja voi syöttää tarvittavia tietoja peliin. Tekstikenttään "Name your lab" kirjoitetaan labyrintin nimi. Place -valikosta valitaan asetettava objekti (floor, wall, trap, cheese tai rat). x - ja y-kenttiin syötetään objektin koordinaatit ja klikataan nappia "Place element!". Lopuksi klikataan nappia "Finished!" tallettamaan labyrintti tietokantaan.

Kun suunnittelutyökalu suljetaan, palataan alkunäkymään. Nyt jos pelaaja navigoi Lab Selection Menu -näkymään, löytyy juuri talletettu labyrintti sieltä.

## Käyttökokemus

Sovelluksessa tulisi olla helppo navigoida eri näkymien välillä. Sovelluksen kieli on englanti.

## Jatkokehitysideat

* tutorial -vaihtoehto alkunäkymään
* monipuolisempia labyrinttejä (esimerkiksi pyöröovet, liikuteltavat laatikot...)
* mahdollisuus käyttäjän luomiseen ja selvitettyjen labyrinttien tarkastelemiseen
* ajastetut pelit
* labyrintteihin jako vaikeustasoihin
* scoreboard
* satunnaisesti generoidut labyrintit
