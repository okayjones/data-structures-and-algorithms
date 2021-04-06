from data_structures.graph.graph import Graph


class Graph(Graph):
    def depth_first(self, vertex):
        nodes, stack = [vertex], [vertex]

        while stack:
            top = stack[-1]
            neighbors = self.get_neighbors(top)
            unvisited = [nb.vertex for nb in neighbors if nb.vertex not in nodes]
            if unvisited:
                next_visit = unvisited[0]
                nodes.append(next_visit)
                stack.append(next_visit)
            else:
                stack.pop()

        return nodes