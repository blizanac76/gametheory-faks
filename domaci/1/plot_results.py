import matplotlib.pyplot as plt
import numpy as np

#PrisonerDilemma.py plot
def plot_match_results(odluke_1, odluke_2, zbir_1, zbir_2, rounds):

    
    #plt.figure(figsize=(12, 8))
    plt.figure(figsize=(10, 6))
    plt.plot(odluke_1, label="Igrač 1 (0 = saradjuje, 1 = izdaje)", color='blue', marker='o', linestyle='-')
    plt.plot(odluke_2, label="Igrač 2 (0 = saradjuje, 1 = izdaje)", color='red', marker='x', linestyle='--')
    plt.title("Odluke tokom partija")
    plt.xlabel("Partija")
    plt.ylabel("Odluka")
    plt.yticks([0, 1], ["Saradjuje", "Izdaje"])
    plt.legend()
    plt.grid(True)
    plt.show()

    
    plt.figure(figsize=(10, 6))
    #skupljena_dobit_1 = np.sum(zbir_1)
    skupljena_dobit_1 = np.cumsum(zbir_1)
    skupljena_dobit_2 = np.cumsum(zbir_2)

    plt.plot(skupljena_dobit_1, label="Igrač 1 ukupna dobit", color='blue', linestyle='-')
    plt.plot(skupljena_dobit_2, label="Igrač 2 ukupna dobit", color='red', linestyle='--')

    plt.title("Ukupna dobit tokom rundi")
    plt.xlabel("Runda")
    plt.ylabel("Ukupna dobit")
    plt.legend()
    plt.grid(True)
    plt.show()

  
    print(f"Igrač 1 ukupna dobit: {sum(skupljena_dobit_1)}")
    print(f"Igrač 2 ukupna dobit: {sum(skupljena_dobit_2)}")
