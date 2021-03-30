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
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    actual = graph.breadth_first(a)
    expected = [a, c, b]
    assert actual == expected