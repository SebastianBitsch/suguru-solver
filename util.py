import matplotlib.pyplot as plt

def flat_list(l: list) -> list:
    return [item for sublist in l for item in sublist]


def configure_plot(w:int, h:int):
    plt.grid(True, color='black', linestyle='-', linewidth=1)

    plt.tick_params(axis='x', colors=(0,0,0,0))
    plt.tick_params(axis='y', colors=(0,0,0,0))
    
    plt.xticks([x-0.5 for x in list(range(1,w+1))])
    plt.yticks([x-0.5 for x in list(range(1,h+1))])
