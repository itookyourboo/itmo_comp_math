from dataclasses import dataclass, field


@dataclass
class Result:
    root: float | None = None
    error: float | None = None
    header: list = field(default_factory=list)
    data: list = field(default_factory=list)


LIMIT = 1_000


def horde_method(f, left, right, fix=-1, eps=10e-3):
    res = Result(
        header='№ a b x f(a) f(b) f(x) |a-b|'.split()
    )
    
    x0 = left if fix == -1 else right

    for i in range(1, LIMIT + 1):
        x1 = (left * f(right) - right * f(left)) / (f(right) - f(left))

        res.data.append([
            i, left, right, x1, f(left), f(right), f(x1), abs(left - right)
        ])

        if (
                abs(x1 - x0) <= eps or
                abs(f(x1)) <= eps
        ):
            res.root = x1
            res.error = abs(x1 - x0)
            break

        if f(x1) * f(left) < 0:
            right = x1
        else:
            left = x1

        x0 = x1

    return res


def newton_method(f, df, x0, eps=10e-3):
    res = Result(
        header="№ x_k f(x_k) f'(x_k) x_{k+1} |x_k-x_{k+1}|".split()
    )

    for i in range(1, LIMIT + 1):
        x1 = x0 - f(x0) / df(x0)

        res.data.append([
            i, x0, f(x0), df(x0), x1, abs(x1 - x0)
        ])

        if (
                abs(x1 - x0) <= eps or
                abs(f(x1) / df(x1)) <= eps or
                abs(f(x1)) <= eps
        ):
            res.root = x1
            res.error = abs(x1 - x0)
            break

        x0 = x1

    return res


def simple_iteration_method(f, phi, x0=1, eps=10e-3):
    res = Result(
        header="№ x_k f(x_k) x_{k+1} phi(x_k) |x_k-x_{k+1}|".split()
    )

    for i in range(1, LIMIT + 1):
        x1 = phi(x0)

        res.data.append([
            i, x0, f(x0), x1, phi(x0), abs(x1 - x0)
        ])

        if (
                abs(x1 - x0) <= eps
        ):
            res.root = x1
            res.error = abs(x1 - x0)
            break

        x0 = x1

    return res
