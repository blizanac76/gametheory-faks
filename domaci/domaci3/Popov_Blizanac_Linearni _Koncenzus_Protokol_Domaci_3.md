# Linearni Koncenzus Protokol: Analiza, Implementacija i Simulacija

## Opis problema

U jednom distributivnom sistemu, više agenata dele i primaju informacije. Svaki od tih agenata ima pristup svom merenju, koje je zagađeno određenim šumom odnosno smetnjom koja remeti u nekoj meri stvarnu vrednost koji treba očitati. Komunikacija agenta sa okolinom se svodi na komunikaciju sa sebi najbližim susedima i svaki agent iterativno podešava svoje estimacije koristeći informacije koje dobija od okoline. Cilj je uspostaviti koncenzus stvarne vrednosti eleminišući efekat šumova i poremećaja koji svaki agent ima koristeći ograničenu komunikaciju.

### Ključni elementi:
- **Stvarna vrednost (true value) $$ V_{\text{true}} $$ **: Stvarna vrednost koju svi estimiraju.
- **Stanje agenta (Agent State) $$ S_i $$ **: U ovom slučaju stanje agenta će biti njegova estimacija.
- **Okolni agenti (Neighbors)**: Svaki agent komunicira samo sa obližnjim susedima.
- **Ažuriranje vrednosti (Consensus Update)**: Način iterativnog ažuriranja agentovog stanja u odnosu na stanja okolnih susednih agenata u cilju nalaženja neke stvarne vrednosti.

---

## Ideja i pristup

Sistem prati linearni koncenzus protokol:
1. Neka svaki agent u početku ima neku estimaciju stvarne vrednosti koja u sebi ima šum.
2. U svakoj iteraciji:
   - Agent će prilagođavati svoje stanje (estimaciju) u odnosu na razliku koju ima sa stanjima susednih agenata (**consensus adjustment**).
   - Mali faktor težine (bias) će omogućiti da se estimirana vrednost približava stvarnoj, smanjujući oscilovanje.
3. Proces se izvršava dokle god se ne izkonvergira stvarnoj vrednosti i greška ne bude manja od tolerancije.

---

## Klasa `Agent` 

**Agent** definiše ponašanje i postojanje jednog agenta. U sebi sadrži implementaciju logike kreiranja novog agenta, ažuriranje vrednosti estimacije i interakciju sa susedima.



#### Update stanja

Svaki agent gleda stanja suseda i svoje stanje menja prema tome, prateći razliku svog i stanja suseda:

$$
S_i \gets S_i + \sum_j W_{ij}(S_j - S_i),
$$
gde je  $W_{ij}$ neki težinski faktor dodat susedu kao uticaj na agenta.

---

#### Update biasa

Malecni bias koji će privlačiti agenta ka stvarnoj vrednosti:

$$
S_i \gets S_i + \alpha (V_{\text{true}} - S_i),
$$
gde upravo $ \alpha $ predstavlja taj bias faktor.

---

#### Update

Konačan update stanja će izgledati ovako:

$$
S_i \gets S_i + \sum_j W_{ij}(S_j - S_i) + \alpha (V_{\text{true}} - S_i).
$$
Implementacija u kodu:

```python
class Agent:
    def __init__(self, agent_id, true_value, noise_std=5.0):
        """
        Inicijalizuje agenta sa:
        - agent_id: ID agenta
        - true_value: stvarna vrednost koja biva estimirana
        - noise_std: sum u vidu standarne devijacije
        - stanje: Inicijalno merenje koje na stvarnu vrednost koju meri senzor dodaje neki sum
        - neighbors`: skup suseda za svakog agenta
        """
        self.id = agent_id
        self.state = true_value + np.random.normal(0, noise_std)  # svaki senzor ima koliko-toliko precizno 			merenje koje je zagadjeno sumom. Pristup nije da se da neka apsolutno random vrednost, nego da 				na pravu dodamo sum 
        self.neighbors = []
        
```

Stanje agenta se ažurira  tako da aktivno prati stanja suseda.

```python
    def update_state(self, weights, neighbor_states, true_value, alpha=0.01):
        """
        Azurira agentsko stanje postujuci protokol.

        - weights: faktor za kontrolu konvergiranja i prihvatanja razlike u odnosu na susede
        - neighbor_states: stanja susednih agenata
        - alpha: bias faktor prema stvarnoj vrednosti (0.01)

        - Agentovo stanje tezi da se izjednaci ili bar nadje na pola sa susedima uz pomoc tezinskog faktora
        """
        consensus_update = sum(weights[i] * (neighbor_states[i] - self.state)
                               for i in range(len(neighbor_states)))
        bias_update = alpha * (true_value - self.state)
        self.state += consensus_update + bias_update

```

---

## Klasa `Broker` 

Ova klasa definiše posrednika, **Broker**-a. Klasa kontroliše agente i njihovu komunikaciju  u samom sistemu. Stvara komunikacijsku mrežu, računa težinske faktore uticaja agenta na druge agente (weight) i vodi računa o ažuriranju stanja agenata. 

### Inicijalizacija

Inicijalizuje sistem koristeči sledeće parametre:
- **num_agents**: Ukupan broj agenata u sistemu
- **true_value**: stvarna vrednost
- **noise_std**: standardna devijacija koja ometa očitavanje senzora (simulira nesavršenost senzora). Tokom testiranja, uzeta je vrednost od oko 10% stvarne vrednosti.

Implementacija u kodu:

```python
class Broker:
    def __init__(self, num_agents, true_value, noise_std=5.0):
        """
        Inicijalizuje brokera sa:
		- num_agents: broj agenata u sistemu
        - true_value: stvarna vrednost koja biva estimirana
        - agents: Instance klase agent, stvarni agenti sa njihovim atributima
        - graph: Random komunikacioni graf, mreza u kojoj agenti komuniciraju
        - conn_matrix: Connection matrica, matrica koja je ixj dimenzija i polje ima vrednost 1 ako izmedju agenta i i agenta j ima direktna veza, i 0 ako nema
        - weights = tezinski faktori
        """
        self.num_agents = num_agents
        self.true_value = true_value
        self.agents = [Agent(i, true_value, noise_std) for i in range(num_agents)]
        self.graph = self._generate_communication_graph()
        self.conn_matrix = nx.to_numpy_array(self.graph)
        self.weights = self._compute_weights()
```

Generisanje grafa komunikacije se obavlja uz pomoć funkcije iz bibliotene networkx `erdos_renyi_graph`. 

Ideja je da graf bude potpuno povezan, odnosno da informacija od jednog agenta može teoretski doći do bilo kog drugog agenta, što bi svakako moralo da bude ispunjeno zbog postojanja Brokera.

```python
def _generate_communication_graph(self):
        """
        Koristi funkciju erdos_renyi_graph() od networkx koji pravi random graf.
        0.4: verovatnoca da postoji veza izmedju 2 cvora.
        seed=X cuva nasumicnost, da mi ne generise novi graf iznova i iznova.
        - posto je cilj implementirati neki oblik DRUS-a svaki agent mora biti povezan sa nekim drugim makar indirektno, odnosno komunikacija je potpuna.
        """
        graph = nx.erdos_renyi_graph(self.num_agents, 0.4, seed=42)
        while not nx.is_connected(graph): #potpuna konekcija
            graph = nx.erdos_renyi_graph(self.num_agents, 0.4, seed=42)
        return graph
```

`_compute_weights` računa težine veze između čvorova koje će uticati posle na to koliko jak uticaj ima sused na agentovo stanje.

---

---

Vrši se **normalizacija**, koju je najlakše objasniti na sledećem promeru:

*Neka je dat neki mali graf sa 4 agenta:*

*Agent 0 -- Agent 1 -- Agent 2
                      |
                Agent 3
Njihova matrica konekcija bi izgledala ovako:*

  ```primer
  [0, 1, 0, 0],  Agent 0 je povezan sa Agentom 1
  [1, 0, 1, 1],  Agent 1 je povezan sa Agentima 0, 2 i 3
  [0, 1, 0, 0],  Agent 2 je povezan sa Agentom 1
  [0, 1, 0, 0],  Agent 3 je povezan sa Agentom 1
  ```



*Sume težina po redovima bi bile:*

    [1],  Suma po redu za Agenta 0
    [3],  Suma po redu za Agenta 1 
    [1],  Suma po redu za Agenta 2
    [1],  Suma po redu za Agenta 3 
*Matricu konekcija podelimo sa sumama težina korenspondirajućim redovima:*

    ```primer
    [0, 1, 0, 0], Agent 0 je pod  jakim uticajem Agent1 1
    [1/3, 0, 1/3, 1/3], Agent 1 je pod jednakim uticajem Agent1 0, 2, and 3
    [0, 1, 0, 0], Agent 2 potpuno pod uticajem Agenta 1
    [0, 1, 0, 0], Agent 3 je potpuno po uticajem Agenta 1
    ```

---

---

```python
def _compute_weights(self):
        """
        Racuna matricu weightsa (tezine) koji se koriste pri komunikaciji
        - Te tezine su takve da im je zbir jedan.
        """
        adj_matrix = self.conn_matrix
        row_sums = adj_matrix.sum(axis=1, keepdims=True)
        return adj_matrix / row_sums  # normalizacija na 1
```

