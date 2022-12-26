import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.red = kwargs.get('red', 0)
        self.green = kwargs.get('green', 0)
        self.blue = kwargs.get('blue', 0)
        self.yellow = kwargs.get('yellow', 0)
        self.orange = kwargs.get('orange', 0)
        self.black = kwargs.get('black', 0)
        self.pink = kwargs.get('pink', 0)
        self.striped = kwargs.get('striped', 0)

        self.contents = []
        for colors in kwargs:
            for counts in range(kwargs[colors]):
                self.contents.append(colors)

    def draw(self, numbers):
        drawn_balls = []
        for _ in range(numbers):
            drawn_balls.append(
                self.contents[random.randint(0, len(self.contents)-1)])
        # remove drawn balls in self.contents
        for i in drawn_balls:
            self.contents.remove(i)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # for i in range(num_experiments):
    hat.draw(num_balls_drawn)
