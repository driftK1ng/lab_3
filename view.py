import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation
from model import Model

class View():
    def __init__(self, model: Model):
        self.model = model
        self.cmap = mcolors.ListedColormap(["blue", "white", "red"])
        self.fig, (self.ax_static, self.ax_dynamic) = plt.subplots(1, 2, figsize=(10,5))
        self.im_dynamic = self.ax_dynamic.imshow(self.model.get_box(), cmap=self.cmap, interpolation="nearest")
        self.im_static = self.ax_static.imshow(self.model.get_box().copy(), cmap=self.cmap, interpolation="nearest")

    def show_graph(self):
        ani = FuncAnimation(self.fig, self.update, frames=self.model.get_iterations_count(), interval = 0.1, blit=False)
        plt.title("test")
        plt.show()

    def update(self, frame):
        self.model.iteration()
        self.im_dynamic.set_array(self.model.get_box())