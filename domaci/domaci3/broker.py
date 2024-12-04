import numpy as np
import networkx as nx
from agent import Agent

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
    
    def _compute_weights(self):
        """
        Racuna matricu weightsa (tezine) koji se koriste pri komunikaciji
        - Te tezine su takve da im je zbir jedan. Primer u dokumentaciji
        """
        adj_matrix = self.conn_matrix
        row_sums = adj_matrix.sum(axis=1, keepdims=True)
        return adj_matrix / row_sums  # normalizacija na 1

    def get_neighbor_states(self, agent_id):
        """
        Vraca state susednih agenata
        """
        neighbors = list(self.graph.neighbors(agent_id))
        return [self.agents[neighbor].state for neighbor in neighbors], neighbors

    def update_agents(self):
        """
        - 1 iteracija updatea SVIm agentima.
        - Poziva se dok sistem ne izkonvergira
        - Za svakog agenta nadje susede, nadje korespondirajuce tezine, i izvrsi update na osnovu ta 2 parametra.
        - Sacuva nova stanja, koja ce posle novim pozivanjem updateovati
        """
        new_states = []
        for agent in self.agents:
            neighbor_states, neighbors = self.get_neighbor_states(agent.id)
            weights = [self.weights[agent.id, neighbor] for neighbor in neighbors]
            agent.update_state(weights, neighbor_states)
            new_states.append(agent.state)
        return new_states
    
    def check_convergence(self, tolerance=1e-3):
        """
        Provera da li je izvrsena konvergencija, da li je kraj.
        - Pravi listu stateova
        - Gleda da li je i najneprecizniji agent dovoljno blizu pravoj vrednosti, po aps vrednosti
        - Kada razlika kadne ispod tolerancije gg 
        """
        states = [agent.state for agent in self.agents]
        return np.max(np.abs(np.array(states) - self.true_value)) < tolerance

    def __repr__(self):
        return f"Broker(num_agents={self.num_agents}, agents={self.agents})"
