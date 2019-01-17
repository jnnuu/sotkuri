#sotkuri

Tällä python sovelluksella voit sekoittaa googlen algoritmit, syöttämällä random dataa googlelle.
urlit.db tietokantaan on ladattu 18000 linkkiä 1375 kategoriasta. Python skripti hakee satunnaisella
indeksillä kategorian ja avaa 5-20 välilehteä kyseisestä aiheesta. Ohjelma sulkee välilehdet 
automaattisesti 7 sekunnin kuluttua, ja hakee uuden kategorian. Tässä ajassa kerkeää ladata evästeet
kyseisen kategorian sivustoilta => googlelle menee tieto että pidät kyseisestä kategoriasta (esim. audi)

Huom! Jatkuva 20 välilehden latailu voi vaatia tietokoneelta sekä netiltä tehoa.
Huom! Kirjaudu chromeen google-tunnuksillasi.

Scratch.csv sisältää googlen algoritmin 1374 kategoriaa. Tästä on siivottu pois maita ja kaupunkeja
koskevat kategoriat (esim. Etelä-Afrikka ja New York). Älä kuitenkaan tee muutoksia tähän tiedostoon,
sillä sotkuri.py käyttää tätä tiedostoa, ja sitä on käytetty tietokannan rakentamiseen. Katsoa saa
mutta ei koskea.

Jos saat urlit.db tiedoston auki, voit tarkastella eri kategorioiden sisältämiä linkkejä. Ne ovat google-haun
ensimmäiset hakutulokset hakusanalla (esim. Home Improvement).

Voit tarkastella omia mainosten personontejasi osoitteessa adssettings.google.com
Tällä sovelluksella voit sekoittaa mainosten räätälöintitapoja.

Jonni Uusi-Hakimo 
17.1.2019
