from data_structures.graph.graph import Graph, Vertex, Edge


def test_add_vertex_pass():
    expected = "a"
    vertex = Vertex(expected)
    actual = vertex.value
    assert actual == expected


def test_add_vertex_fail():
    expected = "a"
    vertex = Vertex("b")
    actual = vertex.value
    assert actual != expected


def test_add_edge():
    vertex_a = Vertex("a")
    vertex_b = Vertex("b")


def test_add_node():
    graph = Graph()
    expected = "a"
    actual = graph.add_node(expected).value
    assert expected == actual


def test_add_edge_true():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a, b)
    assert True


def test_graph_size_pass():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a, b)
    assert len(graph._adjacency_list) == 2


def test_graph_size_fail():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a, b)
    assert len(graph._adjacency_list) != 3


def test_graph_nodes_empty():
    graph = Graph()
    actual = graph.get_nodes()
    expected = None
    assert actual == expected


def test_graph_nodes_list():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    actual = graph.get_nodes()
    expected = [a, b]
    assert actual == expected


def test_graph_neighbors():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    edge_ab = graph.add_edge(a, b)
    edge_ac = graph.add_edge(a, c)
    actual = graph.get_neighbors(a)
    expected = [edge_ab, edge_ac]
    assert actual == expected


def test_graph_neighbors_one_node_one_edge():
    graph = Graph()
    a = graph.add_node("a")
    edge_a = graph.add_edge(a, a)
    actual = graph.get_neighbors(a)
    expected = [edge_a]
    assert actual == expected