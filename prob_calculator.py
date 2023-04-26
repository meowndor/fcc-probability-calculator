import random
import copy
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.contents_all = []
        for colors in kwargs:
            for counts in range(kwargs[colors]):
                self.contents.append(colors)
                self.contents_all.append(colors)

    def draw(self, num_balls):

        if num_balls > len(self.contents):
            return (self.contents)

        else:
            draws = []
            for _ in range(num_balls):
                draws.append(self.contents.pop(
                    random.randint(0, len(self.contents)-1)))

            return (draws)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probs = 0

    for i in range(num_experiments):
        hat.contents_copy = hat.contents_all.copy()
        hat_draw = hat.draw(num_balls_drawn)
        drawn = {x: hat_draw.count(x) for x in set(hat_draw)}
        hat.contents = hat.contents_copy

        for key, value in expected_balls.items():
            if key not in drawn or drawn[key] < value:
                break
            else:
                probs += 1
                break
    return probs/num_experiments
