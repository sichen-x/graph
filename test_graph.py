from graph import Node
from graph import Graph

def test_empty_node():
    """
    tests creation of empty node
    """
    try:
        Node({})
    except Exception as e:
        assert str(e) == 'input info has more than 1 entry!'
    # create node with empty connection
    try:
        node_b = Node({'A':[]})
    except Exception:
        assert False
    assert node_b.name == 'A'

def test_error_node():
    """
    tests creation of bad node
    Node({'a':'a'})
    have to pass since the test is written to test error
    """
    try:
        node_a = Node({'a':'a'})
    except Exception as e:
        assert str(e) == 'input connected nodes info is not in a list.'

def test_good_node():
    """
    tests creation of good node
    Node({'A':['B','C']})
    """
    node_a = Node({'A':['B','C']})
    assert node_a.name == 'A'
    assert node_a.connections == ['B','C']

def test_node_str():
    """
    test that node representation of string is
    "{'name':['list','of','vertex']}"
    """
    node_a = Node({'name':['list','of','vertex']})
    assert str(node_a) == "{'name':['list','of','vertex']}"

def test_empty_graph():
    """
    tests creation of empty graph
    """
    try:
        graph_a = Graph()
    except Exception:
        assert False
    assert True

def test_graph_with_list():
    """
    tests creation of the graph with a list of nodes
    """
    node_list = []
    node_list.append(Node({'A':['B','C']}))
    node_list.append(Node({'B':['C','D']}))
    node_list.append(Node({'C':['D']}))
    node_list.append(Node({'D':['C']}))
    g = Graph(node_list)
    assert len(g.nodes) != 0

def test_graph_with_list_fail():
    """
    tests creation of the graph with a list
    """
    try:
        node_list = ["slippery list"]
        node_list.append(Node({'A':['B','C']}))
        node_list.append(Node({'B':['C','D']}))
        node_list.append(Node({'C':['D']}))
        node_list.append(Node({'D':['C']}))
        g = Graph(node_list)
    except Exception as e:
        assert str(e) == 'invalid node provided!'

def test_add_to_graph():
    """
    create graph and add nodes in a loop
    """
    node_list = []
    node_list.append(Node({'A':['B','C']}))
    node_list.append(Node({'B':['C','D']}))
    node_list.append(Node({'C':['D']}))
    node_list.append(Node({'D':['C']}))
    g = Graph()
    for node in node_list:
        g.add(node)
    assert len(g.nodes) == len(node_list)

def test_graph_str():
    """
    test string representation of the graphs
    should be
    "[{'A':"['B','C']"}, {'B':['C','D']}, {'C':['D']}]"
    """
    node_list = []
    node_list.append(Node({'A':['B','C']}))
    node_list.append(Node({'B':['C','D']}))
    node_list.append(Node({'C':['D']}))
    g = Graph(node_list)
    assert str(g) == "[{'A':['B','C']},{'B':['C','D']},{'C':['D']}]"

def test_find_path_dfs():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    g = Graph()
    node_1 = Node({'A':['B','C']})
    g.add(node_1)
    node_2 = Node({'B':['C','D']})
    g.add(node_2)
    node_3 = Node({'C':['D']})
    g.add(node_3)
    node_4 = Node({'D':['C']})
    g.add(node_4)
    node_5 = Node({'E':['C']})
    g.add(node_5)

    # zero path between node_1 and node_5
    path_0 = g.find_path_dfs(node_1, node_5)
    assert path_0 == None

    # only one path between node_5 and node_4
    path_1 = g.find_path_dfs(node_5, node_4)
    assert [ node.name for node in path_1 ] == [ node_5.name, node_3.name, node_4.name ]

    # three paths between node_1 and node_3, verify anyone of the three is returned
    path_3 = g.find_path_dfs(node_1, node_3)
    assert [ node.name for node in path_3 ] == [ node_1.name, node_2.name, node_3.name ] or \
        [ node.name for node in path_3 ] == [ node_1.name, node_2.name, node_4.name, node_3.name ] or \
        [ node.name for node in path_3 ] == [ node_1.name, node_3.name ]


def test_find_path_bi():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    assert True

def test_find_all_paths():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    g = Graph()
    node_1 = Node({'A':['B','C']})
    g.add(node_1)
    node_2 = Node({'B':['C','D']})
    g.add(node_2)
    node_3 = Node({'C':['D']})
    g.add(node_3)
    node_4 = Node({'D':['C']})
    g.add(node_4)
    node_5 = Node({'E':['C']})
    g.add(node_5)

    # zero path between node_1 and node_5
    paths_0 = g.find_all_paths(node_1, node_5)
    assert len(paths_0) == 0
    # only one path between node_5 and node_4
    paths_1 = g.find_all_paths(node_5, node_4)
    assert len(paths_1) == 1
    assert [ node.name for node in paths_1[0] ] == [ node_5.name, node_3.name, node_4.name ]
    # three paths between node_1 and node_3, verify all the three paths are returned
    paths_3 = g.find_all_paths(node_1, node_3)
    assert len(paths_3) == 3
    for path in paths_3:
        assert [ node.name for node in path ] == [ node_1.name, node_2.name, node_3.name ] or \
            [ node.name for node in path ] == [ node_1.name, node_2.name, node_4.name, node_3.name ] or \
            [ node.name for node in path ] == [ node_1.name, node_3.name ]


def test_find_shortest_path():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    g = Graph()
    node_1 = Node({'A':['B','C']})
    g.add(node_1)
    node_2 = Node({'B':['C','D']})
    g.add(node_2)
    node_3 = Node({'C':['D']})
    g.add(node_3)
    node_4 = Node({'D':['C']})
    g.add(node_4)
    node_5 = Node({'E':['C']})
    g.add(node_5)

    # zero path between node_1 and node_5
    path_0 = g.find_shortest_path(node_1, node_5)
    assert path_0 == None
    # only one path between node_5 and node_4
    path_1 = g.find_shortest_path(node_5, node_4)
    assert [ node.name for node in path_1 ] == [ node_5.name, node_3.name, node_4.name ]
    # three paths between node_1 and node_3, verify the shortest one is returned
    path_3 = g.find_shortest_path(node_1, node_3)
    assert [ node.name for node in path_3 ] == [ node_1.name, node_3.name ]

def test_has_route():
    """
    you should test with graphs that have 0, 1, 3 paths
    """
    g = Graph()
    node_1 = Node({'A':['B','C']})
    g.add(node_1)
    node_2 = Node({'B':['C','D']})
    g.add(node_2)
    node_3 = Node({'C':['D']})
    g.add(node_3)
    node_4 = Node({'D':['C']})
    g.add(node_4)
    node_5 = Node({'E':['C']})
    g.add(node_5)

    # zero path between node_1 and node_5
    assert g.has_route(node_1, node_5) == False
    # only one path between node_5 and node_4
    assert g.has_route(node_5, node_4) == True
    # three paths between node_1 and node_3,
    assert g.has_route(node_1, node_3) == True