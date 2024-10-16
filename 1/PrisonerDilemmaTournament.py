import numpy as np
import matplotlib.pyplot as plt
import random
from players.player1 import strategy_player1
from players.player2 import strategy_player2
from players.player3 import strategy_player3
from players.player4 import strategy_player4

COOPERATE = 0
DEFECT = 1

broj_igraca = 4

players = {
    1: strategy_player1,
    2: strategy_player2,
    3: strategy_player3,
    4: strategy_player4
}

payoff_matrix = {
    (COOPERATE, COOPERATE): (3, 3),  
    (COOPERATE, DEFECT): (0, 5),     
    (DEFECT, COOPERATE): (5, 0),    
    (DEFECT, DEFECT): (1, 1)         
}

rounds = 150
choices_p1 = []
choices_p2 = []
payoffs_p1 = []
payoffs_p2 = []

player_ids = [1, 2, 3, 4]
random.shuffle(player_ids)

player1 = player_ids[0]
player2 = player_ids[1]

player3 = player_ids[2]
player4 = player_ids[3]

#np.random.seed(42)  # zadrzava iste random brojeve i sledeci put kad se pokrene - --debug
def play_match(player1_strategy, player2_strategy, rounds=100):
    history_p1 = []  
    history_p2 = []  
    payoffs_p1 = []
    payoffs_p2 = []

    for _ in range(rounds):
        choice_p1 = player1_strategy(history_p1, history_p2)
        choice_p2 = player2_strategy(history_p2, history_p1)

        history_p1.append(choice_p1)
        history_p2.append(choice_p2)

        payoff_p1, payoff_p2 = payoff_matrix[(choice_p1, choice_p2)]
        payoffs_p1.append(payoff_p1)
        payoffs_p2.append(payoff_p2)

    total_payoff_p1 = sum(payoffs_p1)
    total_payoff_p2 = sum(payoffs_p2)
    
    return total_payoff_p1, total_payoff_p2

print(f"Prvi mec: igrac {player1} vs igrac {player2}")
print(f"drugi mec: igrac {player3} vs igrac {player4}")

payoff_1, payoff_2 = play_match(players[player1], players[player2])
payoff_3, payoff_4 = play_match(players[player3], players[player4])

winner1 = player1 if payoff_1 > payoff_2 else player2
winner2 = player3 if payoff_3 > payoff_4 else player4

print(f"pobednik meca 1: igrac {winner1}")
print(f"pobednik meca 2: igrac {winner2}")

print(f"finale je: igrac {winner1} vs igrac {winner2}")
final_payoff_1, final_payoff_2 = play_match(players[winner1], players[winner2])

tournament_winner = winner1 if final_payoff_1 > final_payoff_2 else winner2
print(f"pobednik je: igrac {tournament_winner}")

# plt.figure(figsize=(10, 6))


# plt.plot(odluke_1, label="Igrac 1 (0 = saradjuje, 1 = sebican)", color='blue', marker='o', linestyle='-')
# plt.plot(odluke_2, label="igrac 2 (0 = saradjuje, 1 = sebican)", color='red', marker='x', linestyle='--')
# plt.title("graf1")
# plt.xlabel("partija")
# plt.ylabel("odluka")
# plt.yticks([COOPERATE, DEFECT], ["saradjuje", "izdaje"])
# plt.legend()

# plt.grid(True)
# plt.show()
# plt.figure(figsize=(10, 6))

# skupljenadobit1 = np.cumsum(zbir_1)
# skupljenadobit2 = np.cumsum(zbir_2)

# ukupnadobit_p1 = sum(skupljenadobit1)
# ukupnadobit_p2 = sum(skupljenadobit2)

# plt.plot(skupljenadobit1, label="igrac 1 ukupna dobit", color='blue', linestyle='-')
# plt.plot(skupljenadobit2, label="igrac 2 ukupna dobit", color='red', linestyle='--')

# plt.title("dobit na broj rundi")
# plt.xlabel("runda")
# plt.ylabel("ukupna dobit do te runde")
# plt.legend()
# plt.grid(True)
# plt.show()



# print("igrac 1 dobiti: ", skupljenadobit1, "\n\n", " igrac 2 dobiti: ", skupljenadobit2)
# print("igrac 1 ukupna dobit: ", ukupnadobit_p1, "\n\n", " igrac 2 ukupna dobit: ", ukupnadobit_p2)