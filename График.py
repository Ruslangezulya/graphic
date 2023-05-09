from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

def plot_graph():

    x = float(x_entry.get())
    y = float(y_entry.get())
    z = float(z_entry.get())

    
    dem = cbook.get_sample_data('jacksboro_fault_dem.npz', np_load=True)
    elevation = dem['elevation']
    nrows, ncols = elevation.shape
    x_values = np.linspace(dem['xmin'], dem['xmax'], ncols)
    y_values = np.linspace(dem['ymin'], dem['ymax'], nrows)
    x_values, y_values = np.meshgrid(x_values, y_values)

    region = np.s_[x:x+50, y:y+50]
    


    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

    ls = LightSource(270, 45)
    # To use a custom hillshading mode, override the built-in shading and pass
    # in the rgb colors of the shaded surface calculated from "shade".
    rgb = ls.shade(elevation, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
    surf = ax.plot_surface(x_values, y_values, elevation, rstride=1, cstride=1, facecolors=rgb,
                           linewidth=0, antialiased=False, shade=False)

    plt.show()


root = tk.Tk()
root.title("График")
root.geometry("300x200")
root.configure(bg='MediumAquaMarine')
x_label = tk.Label(root, text="Введите X:")
x_label.pack()
x_entry = tk.Entry(root)
x_entry.pack()

y_label = tk.Label(root, text="Введите Y:")
y_label.pack()
y_entry = tk.Entry(root)
y_entry.pack()

z_label = tk.Label(root, text="Введите Z:")
z_label.pack()
z_entry = tk.Entry(root)
z_entry.pack()

submit_button = tk.Button(root, text="Построить", command=plot_graph)
submit_button.pack()
made_by_label = tk.Label(root, text="(c) Гезуля Руслан, 2023 г.")
made_by_label.pack(side=tk.BOTTOM)
root.mainloop()