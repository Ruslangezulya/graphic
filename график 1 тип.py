import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import tkinter as tk

def plot_graph():
    x1 = float(entry_x1.get())
    x2 = float(entry_x2.get())
    x3 = float(entry_x3.get())
    y1 = float(entry_y1.get())
    y2 = float(entry_y2.get())
    y3 = float(entry_y3.get())
    z1 = float(entry_z1.get())
    z2 = float(entry_z2.get())
    z3 = float(entry_z3.get())

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt((X-x1)**2 + (Y-y1)**2) + np.sqrt((X-x2)**2 + (Y-y2)**2) + np.sqrt((X-x3)**2 + (Y-y3)**2)
    Z = z1*np.exp(-R**2) + z2*np.exp(-(R-3)**2/4) + z3*np.exp(-(R-5)**2/4)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=cm.Blues)

    ax.set(xticklabels=[],
           yticklabels=[],
           zticklabels=[])

    plt.show()


root = tk.Tk()
root.title("График")
root.geometry("700x600")
root.configure(bg='MediumAquaMarine')


label_x1 = tk.Label(root, text="X1:")
label_x1.grid(row=0, column=0)
entry_x1 = tk.Entry(root)
entry_x1.grid(row=0, column=1)

label_x2 = tk.Label(root, text="X2:")
label_x2.grid(row=1, column=0)
entry_x2 = tk.Entry(root)
entry_x2.grid(row=1, column=1)

label_x3 = tk.Label(root, text="X3:")
label_x3.grid(row=2, column=0)
entry_x3 = tk.Entry(root)
entry_x3.grid(row=2, column=1)

label_y1 = tk.Label(root, text="Y1:")
label_y1.grid(row=3, column=0)
entry_y1 = tk.Entry(root)
entry_y1.grid(row=3, column=1)

label_y2 = tk.Label(root, text="Y2:")
label_y2.grid(row=4, column=0)
entry_y2 = tk.Entry(root)
entry_y2.grid(row=4, column=1)

label_y3 = tk.Label(root, text="Y3:")
label_y3.grid(row=5, column=0)
entry_y3 = tk.Entry(root)
entry_y3.grid(row=5, column=1)

label_z1 = tk.Label(root, text="Z1:")
label_z1.grid(row=6, column=0)
entry_z1 = tk.Entry(root)
entry_z1.grid(row=6, column=1)

label_z2 = tk.Label(root, text="Z2:")
label_z2.grid(row=7, column=0)
entry_z2 = tk.Entry(root)
entry_z2.grid(row=7, column=1)

label_z3 = tk.Label(root, text="Z3:")
label_z3.grid(row=8, column=0)
entry_z3 = tk.Entry(root)
entry_z3.grid(row=8, column=1)

button_plot = tk.Button(root, text="Построить", command=plot_graph)
button_plot.grid(row=9, column=0, columnspan=2)

made_by_label = tk.Label(root, text="(c) Гезуля Руслан, 2023 г.")
made_by_label.pack(side=tk.BOTTOM)

root.mainloop()