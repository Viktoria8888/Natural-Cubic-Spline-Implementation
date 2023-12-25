import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from CubicSpilneFunctions import CreatePolynomials, np
STEP = 0.001
class PointCollectorApp:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Point Collector")

        self.image_path = image_path

        self.spline_points = []
        self.points = []

        self.canvas = tk.Canvas(self.root, width=2000, height=600)
        self.canvas.pack()

        self.load_image()

        self.canvas.bind("<Button-1>", self.on_click)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.add_spline_button = tk.Button(self.root, text="Add Spline", command=self.add_spline)
        self.quit_button.pack()
        self.add_spline_button.pack()

        # Create a Matplotlib figure and embed it in the Tkinter window
        self.fig, self.ax = plt.subplots()
        self.canvas_matplotlib = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_matplotlib.get_tk_widget().pack()

    def add_spline(self):
        self.spline_points.append(self.points.copy())
        self.points = []  # Clear the current points list

        # Plot the spline using Matplotlib
        self.plot_spline()

    def plot_spline(self):
        self.ax.clear()

        for i in range(len(self.spline_points)):
            xs = [p[0] for p in self.spline_points[i]]
            ys = [p[1] for p in self.spline_points[i]]
            n = len(xs) - 1
            ts = [k / n for k in range(0, n + 1)]

            fxs, fys = CreatePolynomials(ts, [xs, ys])

            ts_plot = np.arange(ts[0], ts[-1] + STEP, STEP)
            xs_plot = np.array([fxs(t) for t in ts_plot])
            ys_plot = np.array([fys(t) for t in ts_plot])

            self.ax.plot(xs_plot, ys_plot)

        self.canvas_matplotlib.draw()

    def load_image(self):
        self.image = Image.open(self.image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def on_click(self, event):
        x, y = event.x, event.y
        self.points.append((x, -y))
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="blue")
        print(f"Point added: ({x}, {y})")

image_path = "image1.png"

root = tk.Tk()
app = PointCollectorApp(root, image_path)
root.mainloop()
a = app.spline_points





