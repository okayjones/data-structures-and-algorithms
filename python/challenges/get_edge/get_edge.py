from data_structures.graph.graph import Graph


def get_edge(graph, route):
    if graph.get_nodes() == None or route == None:
        return False, 0

    total_weight = 0

    for idx, city in enumerate(route):
        connections = graph.get_neighbors(city)
        next_city = route[idx + 1] if idx + 1 < len(route) else None

        if next_city == None:
            break

        elif next_city not in [e.vertex for e in connections]:
            return False, 0

        next_city_weight = sum([e.weight for e in connections if e.vertex == next_city])
        total_weight += next_city_weight

    return True, total_weight
