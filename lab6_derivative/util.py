from dataclasses import dataclass
from math import *


class Fun:
    def __init__(self, expr):
        self.__expr = expr

    def __call__(self, x, y=None):
        return eval(self.__expr)

    def __str__(self):
        return self.__expr


@dataclass
class Equation:
    dif: Fun
    ex: Fun
    a: float
    b: float
    y0: float


def format_float(x):
    return f'{x:.5f}'
