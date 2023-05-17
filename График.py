from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

def plot_graph():

    x1 = float(x1_entry.get())
    x2 = float(x2_entry.get())
    x3 = float(x3_entry.get())
    y1 = float(y1_entry.get())
    y2 = float(y2_entry.get())
    y3 = float(y3_entry.get())
    z1 = float(z1_entry.get())
    z2 = float(z2_entry.get())
    z3 = float(z3_entry.get())

    x_values = np.array([[x1, x2, x3], [y1, y2, y3], [z1, z2, z3]])
    
    dem = cbook.get_sample_data('jacksboro_fault_dem.npz', np_load=True)
    elevation = dem['elevation']
    nrows, ncols = elevation.shape
    x_coords = np.linspace(dem['xmin'], dem['xmax'], ncols)
    y_coords = np.linspace(dem['ymin'], dem['ymax'], nrows)
    x_coords, y_coords = np.meshgrid(x_coords, y_coords)

    region = np.s_[x1:x1+50, y1:y1+50]
    
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

    ls = LightSource(270, 45)
    rgb = ls.shade(elevation, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
    
    surf = ax.plot_surface(x_coords, y_coords, elevation, rstride=1, cstride=1, facecolors=rgb,
                           linewidth=0, antialiased=False, shade=False)
    
    ax.scatter(x_values[0], x_values[1], x_values[2], color='red', s=50)
    
    plt.show()


root = tk.Tk()
root.title("График")
root.geometry("700x600")
root.configure(bg='MediumAquaMarine')

x1_label = tk.Label(root, text="Введите X1:")
x1_label.pack()
x1_entry = tk.Entry(root)
x1_entry.pack()

x2_label = tk.Label(root, text="Введите X2:")
x2_label.pack()
x2_entry = tk.Entry(root)
x2_entry.pack()

x3_label = tk.Label(root, text="Введите X3:")
x3_label.pack()
x3_entry = tk.Entry(root)
x3_entry.pack()

y1_label = tk.Label(root, text="Введите Y1:")
y1_label.pack()
y1_entry = tk.Entry(root)
y1_entry.pack()

y2_label = tk.Label(root, text="Введите Y2:")
y2_label.pack()
y2_entry = tk.Entry(root)
y2_entry.pack()

y3_label = tk.Label(root, text="Введите Y3:")
y3_label.pack()
y3_entry = tk.Entry(root)
y3_entry.pack()

z1_label = tk.Label(root, text="Введите Z1:")
z1_label.pack()
z1_entry = tk.Entry(root)
z1_entry.pack()

z2_label = tk.Label(root, text="Введите Z2:")
z2_label.pack()
z2_entry = tk.Entry(root)
z2_entry.pack()

z3_label = tk.Label(root, text="Введите Z3:")
z3_label.pack()
z3_entry = tk.Entry(root)
z3_entry.pack()

submit_button = tk.Button(root, text="Построить", command=plot_graph)
submit_button.pack()

made_by_label = tk.Label(root, text="(c) Гезуля Руслан, 2023 г.")
made_by_label.pack(side=tk.BOTTOM)

root.mainloop()