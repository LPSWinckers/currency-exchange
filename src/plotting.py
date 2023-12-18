import matplotlib.pyplot as plt

def create_plot():
    fig, ax = plt.subplots()
    ax.set_xlabel("Date")
    ax.set_ylabel("Exchange rate")
    return fig  
