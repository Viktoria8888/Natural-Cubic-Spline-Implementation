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

if __name__ == "__main__":
    image_path = "image1.png"

    root = tk.Tk()
    app = PointCollectorApp(root, image_path)
    root.mainloop()

    # Access collected points after the GUI is closed
    print("Collected Points:", app.points)
