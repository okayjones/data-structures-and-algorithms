from data_structures.graph.graph import Graph


class Graph(Graph):
    def breadth_first(self, vertex):
        nodes = []
        breadth = []
        visited = set()

        breadth.append(vertex)
        visited.add(vertex)

        while breadth:
            front = breadth.pop()
            nodes.append(front)

            for child in self.get_neighbors(front):
                if child.vertex not in visited:
                    visited.add(child.vertex)
                    breadth.append(child.vertex)

        return nodes