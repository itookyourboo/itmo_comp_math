from dataclasses import dataclass, field


@dataclass
class Result:
    iteration: int
    solved: bool
    roots: list[float] = field(default_factory=list)
    errors: list[float] = field(default_factory=list)


LIMIT = 1_000


def system_simple_iteration_method(xs, x0=None, eps=1e-3):
    n = len(xs)
    if x0 is None:
        x0 = [1] * n
    x1 = x0[:]
    err = [0] * n

    for i in range(1, LIMIT + 1):
        converges = True
        for j in range(n):
            x1[j] = xs[j](*x0)
            err[j] = abs(x1[j] - x0[j])
            if err[j] > eps:
                converges = False

        if converges:
            return Result(i, True, x1, err)

        x0 = x1[:]

    return Result(i, False, [0] * n, [0] * n)
