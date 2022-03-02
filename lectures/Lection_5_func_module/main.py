from math import log, cos

# from mymath.equations import dichotomy
# from mymath.linalg import gaussian_elimination
from mymath import *
from mymath.linalg import *
from mymath.constants import pi

def f(x):
    assert x != 0, 'Аргумент не может быть равен нулю'
    return 1.2 - log(x) - 4 * cos(2 * x)


# 2x1 + 2x2 - 1x3 = 5
# 0x1 - 2x2 - 1x3 = -7
# 0x1 + 0x2 + 5x3 = 15

if __name__ == "__main__":
    root = equations.dichotomy(f, 1, 4, 1e-5)

    print("Корень равен: {}".format(root),
          "Значение функции: {}".format(f(root)),
          sep="\n")

    roots = gaussian_elimination([[2, 2, -1], [0, -2, -1], [0, 0, 5]],
                                 [[5], [-7], [15]])
    print(roots)
    print(pi)