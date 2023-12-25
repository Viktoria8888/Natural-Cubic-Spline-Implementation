import matplotlib.pyplot as plt
from CubicSpilneFunctions import CreatePolynomials, np

import tkinter as tk
from PIL import Image, ImageTk

class PointCollectorApp:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Point Collector")

        self.image_path = image_path
        self.points = []

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.load_image()

        self.canvas.bind("<Button-1>", self.on_click)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack()

    def load_image(self):
        self.image = Image.open(self.image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def on_click(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")
        print(f"Point added: ({x}, {y})")


image_path = "image.png"

root = tk.Tk()
app = PointCollectorApp(root, image_path)
root.mainloop()


a = app.points
xs = [p[0] for p in a]
ys = [p[1] for p in a]
n = len(xs)-1
ts = [k/n for k in range(0, n+1)]

import matplotlib.pyplot as plt

STEP = 0.001

def plot_NIFS3_zad6(ts, xs, ys, step=STEP):
    fxs, fys = CreatePolynomials(ts, [xs, ys])

    ts_plot = np.arange(ts[0], ts[-1] + step, step)
    xs_plot = np.array([fxs(t) for t in ts_plot])
    ys_plot = np.array([fys(t) for t in ts_plot])

    plt.plot(xs_plot, ys_plot)
    plt.show()
plot_NIFS3_zad6(ts, xs, ys, 0.001)
