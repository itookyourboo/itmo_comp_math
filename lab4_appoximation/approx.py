import math
import numpy as np
from dataclasses import dataclass


@dataclass
class Result:
    coefficients: iter
    dispersion: float
    deviation: float
    confidence: float
    function: callable
    function_str: str
    pearson: float | None = None

    def __lt__(self, other):
        return self.deviation < other.deviation

    def __le__(self, other):
        return self.deviation == other.deviation


def msr(ps, ys, num):
    return (np.sum((ps - ys) ** 2) / num) ** 0.5


def confidence(ps, ys, num):
    return 1 - np.sum((ys - ps) ** 2) / (np.sum(ps ** 2) - np.sum(ps) ** 2 / num)


def get_linspace(xs, ys):
    xs = np.array(xs)
    ys = np.array(ys)
    return xs, ys, len(xs)


def approx_lin(xs, ys):
    xs, ys, num = get_linspace(xs, ys)
    SX, SXX, SY, SXY = np.sum(xs), np.sum(xs ** 2), np.sum(ys), np.sum(xs * ys)

    a, b = np.linalg.solve(
        np.array([[SXX, SX], [SX, num]]),
        np.array([SXY, SY])
    )

    ps = a * xs + b
    S = np.sum((ps - ys) ** 2)

    x0, y0 = np.mean(xs), np.mean(ys)
    r = np.sum((xs - x0) * (ys - y0)) / (np.sum((xs - x0) ** 2) * np.sum((ys - y0) ** 2)) ** 0.5

    return Result(
        coefficients=(a, b),
        dispersion=float(S),
        deviation=msr(ps, ys, num),
        pearson=r,
        confidence=confidence(ps, ys, num),
        function=lambda x: a * x + b,
        function_str=f'{a:.3f}x + {b:.3f}'
    )


def approx_quad(xs, ys):
    xs, ys, num = get_linspace(xs, ys)

    pf = np.polyfit(xs, ys, 2)
    ps = np.poly1d(pf)(xs)

    S = np.sum((ps - ys) ** 2)

    return Result(
        coefficients=pf,
        dispersion=float(S),
        deviation=msr(ps, ys, num),
        confidence=confidence(ps, ys, num),
        function=lambda x: pf[0] * x ** 2 + pf[1] * x + pf[2],
        function_str=f'{pf[0]:.3f}x^2 + {pf[1]:.3f}x + {pf[2]:.3f}'
    )


def approx_cube(xs, ys):
    xs, ys, num = get_linspace(xs, ys)

    pf = np.polyfit(xs, ys, 3)
    ps = np.poly1d(pf)(xs)

    S = np.sum((ps - ys) ** 2)

    return Result(
        coefficients=pf,
        dispersion=float(S),
        deviation=msr(ps, ys, num),
        confidence=confidence(ps, ys, num),
        function=lambda x: pf[0] * x ** 3 + pf[1] * x ** 2 + pf[2] * x + pf[3],
        function_str=f'{pf[0]:.3f}x^3 + {pf[1]:.3f}x^2 + {pf[2]:.3f}x + {pf[3]:.3f}'
    )


def approx_pow(xs, ys):
    xs, ys, num = get_linspace(xs, ys)

    XS, YS = np.log(xs), np.log(ys)
    A, B = np.polyfit(XS, YS, 1)[:]
    a, b = math.exp(A), B
    ps = a * xs ** b

    S = np.sum((ps - ys) ** 2)

    return Result(
        coefficients=(a, b),
        dispersion=float(S),
        deviation=msr(ps, ys, num),
        confidence=confidence(ps, ys, num),
        function=lambda x: a * math.pow(x, b),
        function_str=f'{a:.3f}x^{b:.3f}'
    )


def approx_exp(xs, ys):
    xs, ys, num = get_linspace(xs, ys)

    YS = np.log(ys)
    A, B = np.polyfit(xs, YS, 1)[:]
    a, b = math.exp(A), B
    ps = a * np.exp(b * xs)

    S = np.sum((ps - ys) ** 2)

    return Result(
        coefficients=(a, b),
        dispersion=float(S),
        deviation=msr(ps, ys, num),
        confidence=confidence(ps, ys, num),
        function=lambda x: a * math.exp(b * x),
        function_str=f'{a:.3f}e^{b:.3f}x'
    )


class LnException(Exception):
    pass


def approx_log(xs, ys):
    xs, ys, num = get_linspace(xs, ys)
    if xs[xs < 0]:
        raise LnException('x must be positive for ln log approximation')

    XS = np.log(xs)
    A, B = np.polyfit(XS, ys, 1)[:]
    a, b = A, B
    ps = a * np.log(xs) + b

    S = np.sum((ps - ys) ** 2)

    return Result(
        coefficients=(a, b),
        dispersion=float(S),
        deviation=msr(ps, ys, num),
        confidence=confidence(ps, ys, num),
        function=lambda x: a * math.log(x) + b,
        function_str=f'{a:.3f}ln(x) + {b:.3f}'
    )
