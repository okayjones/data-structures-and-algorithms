from data_structures.graph.graph import Graph


class Graph(Graph):
    def breadth_first(self, vertex):
        nodes = []
        queue = [vertex]

        while queue:
            current = queue.pop()
            nodes.append(current)

            for neighbor in self.get_neighbors(current):
                if neighbor.vertex not in nodes:
                    queue.append(neighbor.vertex)

        return nodes