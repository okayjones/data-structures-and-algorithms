from challenges.breadth_first_graph.breadth_first_graph import Graph

def test_graph_breadth_first_one():
    graph = Graph()
    a = graph.add_node("a")
    actual = graph.breadth_first(a)
    expected = [a]
    assert actual == expected

def test_graph_breadth_first_many():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    e = graph.add_node("e")
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, e)
    actual = graph.breadth_first(a)
    expected = [a, b, c, d, e]
    assert actual == expected