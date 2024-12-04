from broker import Broker
from protocol import ConsensusProtocol

# params
num_agents = 10
# noise std bi trebalo da bude oko 10% merene vrednosti, ili tkao nesto
true_value = 56
noise_std = 7.0

# inicijalizacija brokera i protokola
broker = Broker(num_agents, true_value, noise_std)
protocol = ConsensusProtocol(broker)

# tesitanje protokola, tolerancija 0.001 kao neki dafault i iteracija 1000
protocol.run(max_iterations=1000, tolerance=1e-3)
protocol.visualize()
