# 						*Prvi Domaći* 

## Prvi deo: Analiza tržišta u slučaju N kompanija

### 1. Pretpostavka

1. **Funkcija cene**:  
   $$
   p(Q) = b - aQ, \quad \text{gde je } Q = \sum_{i=1}^N q_i
   $$
   -  b \: Maksimum koji neko može da plati
   -  a : Stopa pada cene, neki vid inflacije
   - Q : Ukupan broj proizvedenih proizvoda
   
2. **Funkcija cene svake kompanije**:  
   $$
   c_i(q_i) = c q_i + d
   $$
   gde je $$c$$  cena proizvodnje svakog pojedinačnog proizvoda za svaku $$ i$$  kompaniju, a $$d$$ je neka fiksna cena održavanja

3. **Prihod (Profit) za kompaniju **:  
   $$
   u_i(q_i, Q_{-i}) = q_i \cdot p(Q) - c_i(q_i)
   $$
   Dalje:  
   $$
   u_i(q_i, Q_{-i}) = q_i b - a q_i Q - c q_i - d
   $$

---

### 2. Optimizacija

Da bismo maksimizovali $$u_i$$, radimo izvod po proizvedenoj količini $$ q_i $$ i postavimo ga na 0:

$$
\frac{\partial u_i}{\partial q_i} = b - a Q - a q_i - c = 0
$$

Ubacivanjem dela $$ Q = q_i + Q_{-i} $$:

$$
b - a(q_i + Q_{-i}) - a q_i - c = 0
$$

Dalje:

$$
b - 2a q_i - a Q_{-i} - c = 0
$$

Rešenje za  $$q_i$$:

$$
q_i = \frac{b - c - a Q_{-i}}{2a}
$$

---

### 3. Simetrični slučaj

Iz teksta zadatka, pretpostavimo da sve kompanije imaju istu cenu proizvodnje i istu cenu održavanja, odnosno tržište je jednako i simetrično  za sve učesnike: $$q_i = q $$. Onda:

$$
Q = Nq
$$

Za svaku kompaniju, količina proizvedenog proizvoda postaje:

$$
q = \frac{b - c - a(N-1)q}{2a}
$$

$$
q + \frac{a(N-1)q}{2a} = \frac{b - c}{2a}
$$

$$
q \left( 1 + \frac{N-1}{2} \right) = \frac{b - c}{2a}
$$

$$
q \cdot \frac{N+1}{2} = \frac{b - c}{2aa}
$$

$$
q = \frac{b - c}{a(N+1)}
$$

---

### 4. Konačna cena

#### Ukupan broj proizvoda
$$
Q = Nq = N \cdot \frac{b - c}{a(N+1)} = \frac{N(b - c)}{a(N+1)}
$$

#### Cena
Kad uvrstimo Q u funkciju cene dobija se:

$$
p(Q) = b - aQ
$$

$$
p = b - a \cdot \frac{N(b - c)}{a(N+1)}
$$

Odnosno:

$$
p = b - \frac{N(b - c)}{N+1}
$$

$$
p = \frac{b(N+1) - N(b - c)}{N+1}
$$

$$
p = \frac{b + Nc}{N+1}
$$

---

### 5. Profiti

Profit svake od N kompanija iznosi:

$$
u_i = q_i \cdot p - c_i(q_i)
$$

Uvrštavanjem $$ q_i = \frac{b - c}{a(N+1)} $$ i $$( p = \frac{b + Nc}{N+1} $$:

$$
u_i = \left(\frac{b - c}{a(N+1)}\right) \cdot \frac{b + Nc}{N+1} - \left(c \cdot \frac{b - c}{a(N+1)} + d\right)
$$

Odnosno:

1. Ukupan prihod:
$$
\frac{(b - c)(b + Nc)}{a(N+1)^2}
$$

2. Deo koji se uložio u porizvodnju:
$$
\frac{c(b - c)}{a(N+1)} + d
$$

Na kraju, celokupan profit je:

$$
u_i = \frac{(b - c)(b + Nc)}{a(N+1)^2} - \frac{c(b - c)}{a(N+1)} - d
$$

---

### 6. Zaključak

1. Ako se broj kompanija povećava $$ N \to \infty $$ Cena proizvoda će se približavati ceni proizvodnje, sprečavajući neku od kompanija da preuzme monopol na tržištu, diktira i kontroliše cenu.
2. Za manje $$ N $$, odnosno manji broj kompanija, broj proizvoda će biti manju čime će svaka od kompanija imati veću slobodu u dizanju cene dokle god potražđnja može da je isprati.

---

## Drugi deo: Analiza tržišta u slučaju da jedna kompanija plaća manje



















Petar 'Del Piero' Popov E2 __/2024
Mladen Blizanac E2 87/2024