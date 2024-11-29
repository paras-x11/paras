import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def plot_graph():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 30, 40, 50]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Tkinter window setup
window = tk.Tk()
window.title("Data Visualization with Tkinter")
button = tk.Button(window, text="Plot Graph", command=plot_graph)
button.pack()
window.mainloop()