COOPERATE = 0
DEFECT = 1

def strategy_player1(history_p1, history_p2):

    if len(history_p2) == 0:  
        return COOPERATE
    else:
        return history_p2[-1]  