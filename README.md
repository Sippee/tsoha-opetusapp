# tsoha-opetusapp

## Opetussovellus
Sovelluksen avulla voidaan järjestää verkkokursseja, joissa on tekstimateriaalia ja automaattisesti tarkastettavia tehtäviä. Jokainen käyttäjä on opettaja tai opiskelija.

### Sovelluksen ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Opiskelija näkee listan kursseista ja voi liittyä kurssille.
- Opiskelija voi lukea kurssin tekstimateriaalia sekä ratkoa kurssin tehtäviä.
- Opiskelija pystyy näkemään tilaston, mitkä kurssin tehtävät hän on ratkonut.
- Opettaja pystyy luomaan uuden kurssin, muuttamaan olemassa olevaa kurssia ja poistamaan kurssin.
- Opettaja pystyy lisäämään kurssille tekstimateriaalia ja tehtäviä. Tehtävä voi olla ainakin monivalinta tai tekstikenttä, johon tulee kirjoittaa oikea vastaus.
- Opettaja pystyy näkemään kurssistaan tilaston, keitä opiskelijoita on kurssilla ja mitkä kurssin tehtävät kukin on ratkonut.

## Käynnistysohjeet
Kloonaa repositorio
```bash
git clone https://github.com/Sippee/CSB-project1
```

Luo tiedosto .env, johon lisätään
```bash
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```

Luo virtuaaliympäristö
```bash
python3 -m venv venv
```
Aktivoi virtuaaliympäristö
```bash
source venv/bin/activate
```
Jos edellinen ei toimi
```bash
. venv/scripts/activate
```

Lataa riippuvuudet
```bash
pip install -r requirements.txt
```

Alusta tietokanta
```bash
psql < schema.sql
```
tai (oma käyttäjä, tietokanta ja .sql tiedoston sijainti pathin kanssa)
```bash
psql -U username -d myDataBase -a -f myInsertFile
```

Käynnistä sovellus, osoite: http://127.0.0.1:5000/
```bash
flask run
```
