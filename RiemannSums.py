import numpy as np
import math

class Leftpoint:
    def __init__(self, upper, lower, rectangles):
        self.upper = upper
        self.lower = lower
        self.rec = rectangles

        self.d = (upper - lower)/rectangles

    def lapprox(self):
        val = 0
        fval = 0

        for x in np.arange(self.lower, self.upper, self.d):
            # f(x)
            func = x**3 + 6*x**2 + x -5
            val += func
        fval = val * self.d

        # rounds it to n decimal place
        return round(fval, 2)

class Rightpoint(Leftpoint):
    def __init__(self, upper, lower, rectangles):
        super().__init__(upper, lower, rectangles)

        self.lower += self.d
        self.upper += 0.001

    def rapprox(self):
        return self.lapprox()


if __name__ == '__main__':
    print(Leftpoint(2, -4, 10).lapprox())
    print(Rightpoint(2, -4, 10).rapprox())








