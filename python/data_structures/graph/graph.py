class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start, end, weight=1):
        if start not in self._adjacency_list:
            raise KeyError("Start Vertex not in Graph")
        if end not in self._adjacency_list:
            raise KeyError("End Vertex not in Graph")

        edge = Edge(end, weight)
        adjacencies = self._adjacency_list[start]
        adjacencies.append(edge)
        return edge

    def get_nodes(self):
        return list(self._adjacency_list) or None

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def size(self):
        return len(self.self_adjacency_list)

    def __str__(self):
        return str(self._adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return f"({self.vertex}, {self.weight})"