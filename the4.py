def iscup(tree):
    if type(tree[1]) == int:
        return True
    else:
        return False


def ischild(tree, x):
    if type(tree[-1]) != int and x == tree[0]:
        return True
    else:
        for i in range(1, len(tree)):
            if type(tree[-1]) != int and ischild(tree[i], x):
                return True
            elif type(tree[-1]) != int and tree[i][0] == x:
                return True
        return False


def maxtime(q):
    flatlist = [0]
    while q:
        first = q[0]
        q = q[1:]
        if type(first) == list:
            q += first
        elif type(first) == int and flatlist[-1] != first:
            flatlist += [first]
    return max(flatlist)


def ischild_multi(tree, taps):
    for i in taps:
        if not ischild(tree, i):
            return False
    return True


def ancestor(tree, taps, time):
    if time == maxtime(tree) and ischild_multi(tree, taps):
        return tree[0]
    else:
        for i in range(1, len(tree)):
            if type(tree[i][1]) != int and ancestor(tree[i], taps, time) is not None:
                return ancestor(tree[i], taps, time)


def aztec(x, a):
    if iscup(x):
        a[x[1] - 1] += x[:-1:]
    else:
        for i in range(1, len(x)):
            aztec(x[i], a)
    return a


def only_taps(tree):
    t = []
    maxt = maxtime(tree)
    while len(t) != maxt:
        t.append([])
    return aztec(tree, t)


def comb(x):
    a = [x]
    if len(x) > 1:
        for b in a:
            for i in range(len(b)):
                c = b[:i] + b[i + 1:]
                if c not in a and len(c) > 1:
                    a.append(c)
    return a


def chalchiuhtlicue(tree):
    otaps = only_taps(tree)
    total_time = len(otaps)
    for i in range(0, total_time):
        if len(otaps[i]) > 1:
            for c in comb(otaps[i]):
                if ancestor(tree, c, i + 1) is not None and (ancestor(tree, c, i + 1) not in otaps[i]):
                    sil = c[:]
                    otaps[i] += [ancestor(tree, c, i + 1)]
                    for s in sil:
                        otaps[i].remove(s)
    return otaps
