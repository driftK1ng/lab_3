from model import Model
from view import View

if __name__ == "__main__":
    model_size = 10
    empty_percent = 10
    others_count = 2
    iterations_count = 100000

    model = Model(others_count=others_count, iterations_count=iterations_count)

    model.fill(model_size, empty_percent)

    view = View(model)

    view.show_graph()
