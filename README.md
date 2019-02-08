#sotkuri

With this python application you are able to mess up google's ad targeting algorithms.
Your internet behaviour is tracked in every page, where there is google adsense 
and google's cookies that you will download on the first page load.

This app uses urlit.db database file, which includes 18380 urls from 1375 different categories.
The sotkuri.py python console application picks a random category (from scratch.csv), and then opens all urls
in said category with google chrome (there's 5-20 of them) and after waiting for 7
seconds the app kills the browser. The app repeats this cycle for 20 times, but you are 
able to modify this by changing the value of the 'maara' variable.

Upon page load the browser downloads cookies from all opened pages, and therefore google thinks
that you are interested in said category (for example audi, home decoration).
Basically you can spoof google algorithms with fake data.

You must log in to chrome with your google account.

The urls in urlit.db are the first urls from a google search with an entry of 'category name',
for example 'toyota'.

You can view your google ad setting in adssettings.google.com

-----------------------------------------------------------------------------------------------------

Tällä python sovelluksella voit sekoittaa googlen algoritmit, syöttämällä random dataa googlelle.
urlit.db tietokantaan on ladattu 18380 linkkiä 1375 kategoriasta. Python skripti hakee satunnaisella
indeksillä kategorian ja avaa 5-20 välilehteä kyseisestä aiheesta. Ohjelma sulkee välilehdet 
automaattisesti 7 sekunnin kuluttua, ja hakee uuden kategorian. Tässä ajassa kerkeää ladata evästeet
kyseisen kategorian sivustoilta => googlelle menee tieto että pidät kyseisestä kategoriasta (esim. audi)

Huom! Jatkuva 20 välilehden latailu voi vaatia tietokoneelta sekä netiltä tehoa.
Huom! Kirjaudu chromeen google-tunnuksillasi.

Scratch.csv sisältää googlen algoritmin 1375 kategoriaa. Tästä on siivottu pois maita ja kaupunkeja
koskevat kategoriat (esim. Etelä-Afrikka ja New York). Älä kuitenkaan tee muutoksia tähän tiedostoon,
sillä sotkuri.py käyttää tätä tiedostoa, ja sitä on käytetty tietokannan rakentamiseen. Katsoa saa
mutta ei koskea.

Jos saat urlit.db tiedoston auki, voit tarkastella eri kategorioiden sisältämiä linkkejä. Ne ovat google-haun
ensimmäiset hakutulokset hakusanalla (esim. Home Improvement).

Voit tarkastella omia mainosten personontejasi osoitteessa adssettings.google.com 

Tällä sovelluksella voit sekoittaa ne.

----------------------------------------------------------------------------------------------------

Jonni Uusi-Hakimo 
17.1.2019
