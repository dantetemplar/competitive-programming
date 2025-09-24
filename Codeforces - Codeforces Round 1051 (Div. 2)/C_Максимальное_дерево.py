# ruff: noqa: F401
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict

# ----------------  Solution   ---------------- #
from typing import Any, Dict, Hashable, Iterable, List


# graph: Dict[u, Iterable[(v, w)]], где w — вес/метка, которую игнорируем для топосортировки
def _neighbors_list(adj: Iterable[Any]):
    for item in adj:
        yield item[0] if isinstance(item, tuple) else item  # взять только вершину


def topo_dfs_weighted(graph: Dict[Hashable, Iterable[Any]]) -> List[Hashable]:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {}
    order = []

    nodes = set(graph.keys())
    for u, adj in graph.items():
        for v in _neighbors_list(adj):
            nodes.add(v)

    def dfs(u):
        color[u] = GRAY
        for v in _neighbors_list(graph.get(u, ())):
            c = color.get(v, WHITE)
            if c == GRAY:
                raise ValueError("Graph has a cycle (not a DAG)")
            if c == WHITE:
                dfs(v)
        color[u] = BLACK
        order.append(u)

    for u in nodes:
        if color.get(u, WHITE) == WHITE:
            dfs(u)

    order.reverse()
    return order


def solve(n: int, tree: list[tuple[int, int, int, int]]) -> list[int]:
    # u, v - indexes, x, y - x value if p[u] > p[v] else y value. Need to find optimal p, so it will maximize sum of all edges.
    graph = defaultdict(list)
    for u, v, x, y in tree:
        if x > y:
            graph[u].append((v, x))
        else:
            graph[v].append((u, y))

    # topological sorting
    sorting = topo_dfs_weighted(graph)

    answer = [None] * n
    for i, t in enumerate(sorting):
        answer[t - 1] = n - i
    return answer


# ----------------  Input/Output   ---------------- #
def main():
    import sys

    input = lambda: sys.stdin.readline().rstrip()  # noqa
    print = lambda s, end="\n": sys.stdout.write(str(s) + end)  # noqa

    t = int(input())
    for _ in range(t):
        n = int(input())
        tree = []
        for i in range(n - 1):
            u, v, x, y = map(int, input().split())
            tree.append((u, v, x, y))

        res = solve(n, tree)
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()  # Press Ctrl+Alt+B to run test cases
