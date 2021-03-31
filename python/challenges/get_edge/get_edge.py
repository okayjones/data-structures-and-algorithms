from data_structures.graph.graph import Graph


def get_edge(graph, route):

    # exit immeditaely if either are empty
    if graph.get_nodes() == None or route == None:
        return False, 0

    total_weight = 0

    # iterate through route
    for index, city in enumerate(route):
        # Connected_edges is a list of Edges (self.vertex, self.weight)
        connected_cities = graph.get_neighbors(city)
        route_cities = [city.vertex for city in connected_cities]
        next_city = route[index + 1] if index + 1 < len(route) else None
        # if end of list, break
        if not next_city:
            break
        # next city isn't in the list, return false
        if next_city not in route_cities:
            return False, 0
        # find city in neighbors list and add weight
        for connection in connected_cities:
            if connection.vertex == next_city:
                total_weight += connection.weight
        
    return True, total_weight 