def dichotomy(f, a, b, eps):
    root = None
    while abs(f(b) - f(a)) > eps:
        mid = (a + b) / 2
        if f(mid) == 0 or abs(f(mid)) < eps:
            root = mid
            break
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return root

