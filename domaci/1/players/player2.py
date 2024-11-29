import random
COOPERATE = 0
DEFECT = 1
prom = 1
def strategy_player2(history_p1, history_p2):
    import random
    prom = random.choice([0, 1])
    if prom ==1:
        return COOPERATE 
    else:
        return DEFECT
  

    