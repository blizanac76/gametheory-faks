from broker import Broker
import matplotlib.pyplot as plt
import numpy as np

class ConsensusProtocol:
    def __init__(self, broker):
        """
        Inicijalizacija koncenzusa sa brokerom posreduje agente
        """
        self.broker = broker
        self.iteration = 0
        self.history = []  # Store state histories for visualization
    
    def run(self, max_iterations=1000, tolerance=1e-3):
        """
        Protokol se obavlja dok se ne izkonvergira ili dok se ne urad 1000 iteracija.
        """
        while self.iteration < max_iterations:
            self.history.append([agent.state for agent in self.broker.agents])
            # update agenata novim vrednostima
            for agent in self.broker.agents:
                neighbor_states, neighbors = self.broker.get_neighbor_states(agent.id)
                weights = [self.broker.weights[agent.id, neighbor] for neighbor in neighbors]
                agent.update_state(weights, neighbor_states, self.broker.true_value)
            self.iteration += 1
            if self.broker.check_convergence(tolerance):
                print(f"Consensus reached at iteration {self.iteration}")
                break
    
    def visualize(self):
        """
        Prikaz, plotovanje
        """
        self.history = np.array(self.history)
        plt.figure(figsize=(10, 6))
        #Ovde sam stavio limit na 50 x osu, da vidim koliko brzo udju u to 'mirno' stanje u pocetnik fazama. par stotina iteracija treba da 
        # bude dovoljno blizu stvarne vrednosti
        plt.xlim([0,50])
        for agent_id in range(self.broker.num_agents):
            plt.plot(self.history[:, agent_id], label=f"Agent {agent_id}")
        plt.axhline(self.broker.true_value, color='red', linestyle='--', label="PRAVA vrednost")
        plt.title("Protokol koncenzus")
        plt.xlabel("Iteracija")
        plt.ylabel("Agent state")
        plt.legend()
        plt.show()
