import pytest
from challenges.get_edge.get_edge import get_edge
from data_structures.graph.graph import Graph


def test_empty_graph():
    graph = Graph()
    cities = []
    actual_connected, actual_weight = get_edge(graph, cities)
    expected_connected, expected_weight = False, 0
    assert actual_connected == expected_connected
    assert actual_weight == expected_weight


def test_one_connection_true(flights):
    graph = flights["graph"]
    route = [flights["metroville"], flights["pandora"]]
    actual = get_edge(graph, route)
    expected = (True, 82)
    assert actual == expected


def test_two_connection_true(flights):
    graph = flights["graph"]
    route = [flights["arendelle"], flights["monstropolis"], flights["naboo"]]
    actual = get_edge(graph, route)
    expected = (True, 115)
    assert actual == expected


def test_one_connection_false(flights):
    graph = flights["graph"]
    route = [flights["naboo"], flights["pandora"]]
    actual = get_edge(graph, route)
    expected = (False, 0)


def test_two_connection_false(flights):
    graph = flights["graph"]
    route = [flights["narnia"], flights["arendelle"], flights["naboo"]]
    actual = get_edge(graph, route)
    expected = (False, 0)
    assert actual == expected


@pytest.fixture
def flights():
    graph = Graph()
    pandora = graph.add_node("pandora")
    narnia = graph.add_node("narnia")
    arendelle = graph.add_node("arendelle")
    metroville = graph.add_node("metroville")
    monstropolis = graph.add_node("monstropolis")
    naboo = graph.add_node("naboo")
    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(narnia, metroville, 37)
    graph.add_edge(narnia, naboo, 250)
    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(arendelle, pandora, 150)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(arendelle, monstropolis, 42)
    graph.add_edge(monstropolis, arendelle, 42)
    graph.add_edge(monstropolis, metroville, 105)
    graph.add_edge(monstropolis, naboo, 73)
    graph.add_edge(naboo, monstropolis, 73)
    graph.add_edge(naboo, metroville, 26)
    graph.add_edge(naboo, narnia, 250)
    return {
        "graph": graph,
        "pandora": pandora,
        "narnia": narnia,
        "arendelle": arendelle,
        "metroville": metroville,
        "monstropolis": monstropolis,
        "naboo": naboo,
    }
