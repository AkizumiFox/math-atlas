"""Small DAG utilities for the atlas (stdlib only).

A graph is a dict mapping each node to the set of its direct prerequisites
(`preds`). Edges point from prerequisite to dependent: p -> n when p in preds[n].
"""
from collections import defaultdict, deque


def successors(preds):
    succ = defaultdict(set)
    for n, ps in preds.items():
        succ.setdefault(n, set())
        for p in ps:
            succ[p].add(n)
    return succ


def find_cycle(preds):
    """Return one cycle as a list of nodes [a, b, ..., a], or None."""
    WHITE, GREY, BLACK = 0, 1, 2
    colour = defaultdict(int)
    stack = []

    def visit(n):
        colour[n] = GREY
        stack.append(n)
        for p in sorted(preds.get(n, ())):
            if colour[p] == GREY:
                return stack[stack.index(p):] + [p]
            if colour[p] == WHITE:
                found = visit(p)
                if found:
                    return found
        stack.pop()
        colour[n] = BLACK
        return None

    for n in sorted(preds):
        if colour[n] == WHITE:
            found = visit(n)
            if found:
                return found
    return None


def topo_order(preds, key=None):
    """Kahn's algorithm; ties broken by `key` (default: node name). Raises on a cycle."""
    key = key or (lambda n: n)
    nodes = set(preds) | {p for ps in preds.values() for p in ps}
    indeg = {n: len(preds.get(n, ())) for n in nodes}
    succ = successors({n: preds.get(n, set()) for n in nodes})
    ready = sorted((n for n in nodes if indeg[n] == 0), key=key)
    out = []
    while ready:
        n = ready.pop(0)
        out.append(n)
        for m in succ[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                ready.append(m)
        ready.sort(key=key)
    if len(out) != len(nodes):
        raise ValueError(f"cycle: {find_cycle(preds)}")
    return out


def ancestors(preds, start):
    """All nodes reachable backwards from `start` (iterable), excluding nothing."""
    seen = set()
    todo = deque(start)
    while todo:
        n = todo.popleft()
        if n in seen:
            continue
        seen.add(n)
        todo.extend(preds.get(n, ()))
    return seen


def descendants(preds, start):
    return ancestors(successors(preds), start)


def longest_paths(preds):
    """height[n] = number of nodes on the longest path ending at n; and a witness path."""
    height, back = {}, {}
    for n in topo_order(preds):
        best = None
        for p in preds.get(n, ()):
            if best is None or (height[p], p) > (height[best], best):
                best = p
        height[n] = 1 + (height[best] if best else 0)
        back[n] = best
    return height, back


def path_to(back, n):
    out = []
    while n:
        out.append(n)
        n = back[n]
    return out[::-1]


def transitive_reduction(preds):
    """Drop p -> n whenever n is reachable from p by a longer path. For display only."""
    red = {}
    for n, ps in preds.items():
        keep = set(ps)
        for p in ps:
            if any(p in ancestors(preds, [q]) for q in ps - {p}):
                keep.discard(p)
        red[n] = keep
    return red
