import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plotting import create_plot
import csv

file_path = 'src\currency.csv'

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

def on_button_click(from_currency, to_currency, currency_sign, currency_sign2, Time_period):
    """Event handler for the button click."""
    print(from_currency.get(), to_currency.get())

def from_currency_changed(event, currency_sign):
    """Event handler for the from_currency combobox."""
    for row in data:
        if row[0] == event.widget.get():
            currency_sign["text"] = row[2]
    

    

def setup_gui():
    root = tk.Tk()
    root.title("Currency exchange rates")

    topbox = tk.Frame(root)
    topbox.pack(pady=10)

    currency_choices = [row[0] for row in data]

    from_currency = ttk.Combobox(topbox)
    from_currency["values"] = currency_choices
    from_currency["state"] = "readonly"  # Prevents the user from typing in the combobox
    from_currency.bind("<<ComboboxSelected>>", lambda event: from_currency_changed(event, currency_sign))
    from_currency.current(0)
    from_currency.pack(side=tk.LEFT)

    to_currency = ttk.Combobox(topbox)
    to_currency["values"] = currency_choices
    to_currency["state"] = "readonly" 
    to_currency.bind("<<ComboboxSelected>>", lambda event: from_currency_changed(event, currency_sign2))
    to_currency.current(1)
    to_currency.pack(side=tk.LEFT)

    button = tk.Button(topbox, text="Get exchange rate")
    button["command"] = lambda: on_button_click(from_currency, to_currency, currency_sign, currency_sign2, Time_period)
    button.pack(side=tk.LEFT)

    bottombox = tk.Frame(root)
    bottombox.pack(pady=10)


    amount = tk.Entry(bottombox)
    amount.pack(side=tk.LEFT)
    amount.insert(0, "1")

    currency_sign = tk.Label(bottombox, text="$")
    currency_sign.pack(side=tk.LEFT)

    equals_sign = tk.Label(bottombox, text="=")
    equals_sign.pack(side=tk.LEFT)

    exchange_rate = tk.Entry(bottombox)
    exchange_rate.pack(side=tk.LEFT)
    exchange_rate['state'] = 'readonly'

    currency_sign2 = tk.Label(bottombox, text="$")
    currency_sign2.pack(side=tk.LEFT)

    Time_period = ttk.Combobox(bottombox)
    Time_period["values"] = ["1 day", "1 week", "1 month", "1 year"]
    Time_period["state"] = "readonly"
    Time_period.current(0)
    Time_period.pack(side=tk.LEFT)

    fig = create_plot()  # Get the plot from the plotting module
    canvas = FigureCanvasTkAgg(fig, master=root)  # Embed the plot in Tkinter
    canvas.draw()
    canvas.get_tk_widget().pack()
    return root
