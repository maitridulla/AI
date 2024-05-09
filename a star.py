class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {
            'a': 11,
            'b': 6,
            'c': 99,
            'd': 1,
            'e': 7
        }
        return H.get(n, float('inf'))  # Use get() to handle missing keys gracefully

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])

        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found:', reconst_path)
                print('Heuristic values:', [self.h(node) for node in reconst_path])
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

# Take input for adjacency list
adjac_lis = {}
nodes = input("Enter nodes separated by spaces: ").split()
for node in nodes:
    neighbors = input(f"Enter neighbors for node {node} (format: neighbor1 weight1 neighbor2 weight2 ...): ").split()
    adjac_lis[node] = [(neighbors[i], int(neighbors[i+1])) for i in range(0, len(neighbors), 2)]

# Create graph with user-provided adjacency list
graph = Graph(adjac_lis)

# Take input for start and stop nodes
start_node = input("Enter start node: ")
stop_node = input("Enter stop node: ")

# Call A* algorithm with user-provided nodes
graph.a_star_algorithm(start_node, stop_node)
