class MyGraph:

    def __init__(self, n_nodes, n_edges):
        self.n_nodes = n_nodes
        self.n_edges = n_edges

        self.graph = [[] for i in range(n_nodes + 1)]
        self.cycles = [[] for i in range(n_nodes + 1)]
        self.n_cycles = 0

        self.visited = [False for i in range(n_nodes + 1)]

        # arrays required to color the
        # graph, store the parent of node
        self.color = [0] * (n_nodes + 1)
        self.par = [0] * (n_nodes + 1)

        # mark with unique numbers
        self.mark = [0] * (n_edges + 1)

    def add_edge(self, start_node, end_node):
        self.graph[start_node].append(end_node)
        self.graph[end_node].append(start_node)

    def is_connected(self, start=1):
        if start >= self.n_nodes:
            return True

        # the rest is a connect graph
        if not self.is_connected(start + 1):
            return False

        # start node connect with the rest
        for i in range(1, self.n_nodes + 1):
            if start in self.graph[i]:
                return True

        return False

    def dfs_cycle(self, u, p,
                  color: list,
                  mark: list,
                  par: list):
        # already (completely) visited vertex.
        if color[u] == 2:
            return

        # seen vertex, but was not
        # completely visited -> cycle detected.
        # backtrack based on parents to
        # find the complete cycle.
        if color[u] == 1:
            self.n_cycles += 1
            cur = p
            mark[cur] = self.n_cycles

            # backtrack the vertex which are
            # in the current cycle thats found
            while cur != u:
                cur = par[cur]
                mark[cur] = self.n_cycles

            return

        par[u] = p

        # partially visited.
        color[u] = 1

        # simple dfs on graph
        for v in self.graph[u]:

            # if it has not been visited previously
            if v == par[u]:
                continue
            self.dfs_cycle(v, u, color, mark, par)

        # completely visited.
        color[u] = 2

    def calc_circles(self):

        # call DFS to mark the cycles
        self.dfs_cycle(1, 0, self.color, self.mark, self.par)

        for i in range(1, self.n_edges + 1):
            if self.mark[i] != 0:
                self.cycles[self.mark[i]].append(i)

        return self.cycles

    def n_spanningtree(self):
        if not self.is_connected():
            return 0

        n = 1
        for i in range(1, self.n_cycles + 1):
            n *= len(self.cycles[i])
        return n

    # Function to print the cycles
    def print_circles(self):
        # print all the vertex with same cycle
        for i in range(1, self.n_cycles + 1):

            # Print the i-th cycle
            print("Cycle Number %d:" % i, end=" ")
            for x in self.cycles[i]:
                print(x, end=" ")
            print()

    def load_from_runtime(self):
        n_remain_edges = self.n_edges
        while n_remain_edges > 0:
            node1, node2 = input().split(" ")
            node1 = int(node1)
            node2 = int(node2)
            self.add_edge(node1, node2)
            n_remain_edges -= 1


def test():
    g = MyGraph(13, 14)
    # add edges
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 6)
    g.add_edge(4, 7)
    g.add_edge(5, 6)
    g.add_edge(3, 5)
    g.add_edge(7, 8)
    g.add_edge(6, 10)
    g.add_edge(5, 9)
    g.add_edge(10, 11)
    g.add_edge(11, 12)
    g.add_edge(11, 13)
    g.add_edge(12, 13)

    g.calc_circles()
    g.print_circles()
    print(g.is_connected())
    print(g.n_spanningtree())


def test_cases():
    g = MyGraph(0, 0)
    # g.calc_circles()
    # assert g.n_spanningtree() == 0

    g = MyGraph(1, 0)
    g.calc_circles()
    assert g.n_spanningtree() == 1

    g = MyGraph(2, 1)
    g.add_edge(1, 2)
    g.calc_circles()
    assert g.n_spanningtree() == 1

    g = MyGraph(3, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.calc_circles()
    assert g.n_spanningtree() == 1

    g = MyGraph(3, 3)
    # add edges
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(1, 3)

    g.calc_circles()
    assert g.n_spanningtree() == 3

    g = MyGraph(5, 6)
    # add edges
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(1, 3)

    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(3, 5)

    g.calc_circles()
    print(g.n_cycles)
    g.print_circles()
    print(g.n_spanningtree())
    assert g.n_spanningtree() == 9


def main():
    id_case = 1
    try:
        n_remain_cases = int(input())
    except:
        n_remain_cases = 0

    while n_remain_cases > 0:
        n_nodes, n_edges = input().split(" ")
        n_nodes = int(n_nodes)
        n_edges = int(n_edges)

        g = MyGraph(n_nodes, n_edges)
        g.load_from_runtime()
        g.calc_circles()

        print("Case {}: {}".format(id_case, g.n_spanningtree()))
        id_case += 1
        n_remain_cases -= 1


# Driver Code
if __name__ == "__main__":
    # main()
    test_cases()
