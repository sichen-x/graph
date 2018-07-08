from copy import deepcopy

class Node:
    """
    class constructor should take one argument:
    dictionary with a name of the node as a key and a list of nodes it is connected to as value.
    For example
        >> Node({'A':['B','C']})

    Note 1,
      that the node may not have any connections, thus empty list is a legal dictionary value.
    >> Node({'A':[]})

    Note 2,
      any other input to the node should result in an error.
    """

    def __init__(self, info={}):
        if type(info) != dict:
            raise Exception('input info is not a dictionary!')
        elif len(info) != 1:
            raise Exception('input info has more than 1 entry!')
        else:
            for key in info: # this loop only iterates for one time
                if key == '':
                    raise Exception('input node name is empty!')
                else:
                    self.name = key
                if type(info[key]) != list:
                    raise Exception('input connected nodes info is not in a list.')
                else:
                   self.connections = info[key]

    def __str__(self):
        """
        returns string representation
        >> {node:[vertex, vertex]}
        """
        out_str = "{'" + self.name + "':["
        for connection in self.connections:
            out_str += ("'" + connection + "'" + ",")
        out_str = out_str.rstrip(',')
        out_str += ']}'
        return out_str



class Graph:
    def __init__(self, list_of_nodes=None):
        """
        The constructor accepts a list of valid nodes, if no list is given, the graph is instantiated empty.
        """
        if list_of_nodes and type(list_of_nodes) != list:
            raise Exception('nodes provided are not in a list!')
        self.nodes = dict()
        if list_of_nodes != None:
            for node in list_of_nodes:
                if type(node) == Node:
                    self.nodes[node.name] = node.connections
                else:
                    raise Exception('invalid node provided!')
        self.paths = []

    def add(self, node):
        """
        adds the node to the graph
        """
        self.nodes[node.name] = node.connections

    def delete(self, node):
        """
        deletes given node from the graph
        """
        for key in node:
            if key in self.nodes:
                del self.nodes[key]

    def find_path_dfs(self, start_node, end_node):
        """
        return one path between start and end
        search is performed Depth-First
        """
        visited = dict()
        for node in self.nodes: visited[node] = False
        path = []
        del self.paths[:]
        self.dfs_search(start_node, end_node, visited, path)
        if len(self.paths) > 0:
            return self.paths[0]
        else:
            return None

    def find_path_bi(self, start_node, end_node):
        """
        *******
        7/6/2018 17:02:32 L:
        this is extra credit assignment
        *******
        return one path between start and end
        search is performed Bidirectional
        [Node 1, Node 2, Node 3]
        """
        pass

    def find_all_paths(self, start_node, end_node):
        """
        returns a list with all paths between start and end, the list
        is empty if no path is found. Use traversal method of your choice.
        """
        visited = dict()
        for node_name in self.nodes: visited[node_name] = False
        path = []
        del self.paths[:]
        self.dfs_search(start_node, end_node, visited, path)
        return self.paths

    def dfs_search(self, start, end, visited, path):
        visited[start.name] = True
        path.append(start)
        if start.name == end.name:
            self.paths.append(deepcopy(path))
        else:
            for i in self.nodes[start.name]:
                if visited[i] == False:
                    self.dfs_search(Node({i:self.nodes[i]}), end, visited, path)
        path.pop()
        visited[start.name]= False

    def find_shortest_path(self, start_node, end_node):
        """
        returns the shortest path between start and end, or None if no path was found.
        """
        all_paths = self.find_all_paths(start_node, end_node)
        if len(all_paths) > 0:
            shortest_path = all_paths[0]
            for path in all_paths:
                shortest_path = path if len(path) < len(shortest_path) else shortest_path
            return shortest_path
        else:
            return None


    def has_route(self, start_node, end_node):
        """
        design an algorithm to return True if there is at least one path between
        start_node and end_node, otherwise returns False
        """
        return len(self.find_all_paths(start_node, end_node)) > 0

    def print_path(self, path):
        """
        Given the path 'A' to 'B' to 'C', print the path in following format:
        'A'->'B'->'C'
        The node names have to come in order

        path is defined as
        [Node({'A',['B']}), Node({'B',['C','D']}), Node({'C',['E','F']})]
        """
        if path == None:
            print('None')
        else:
            output_str = ''
            for node in path:
                output_str += ("'" + node.name + "'" + "->")
            output_str = output_str.rstrip("->")
            print(output_str)

    def __str__(self):
        """
        returns a list representation with each node
        >> [{'A':['B','C']},{'D':['B','C']},{'B':['C','E']}]
        """
        out_str = '['
        for key in self.nodes:
            node = Node({key: self.nodes[key]})
            out_str += (str(node) + ',')
        out_str = out_str.rstrip(',')
        out_str += ']'
        return out_str

# test
if __name__ == '__main__':
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
    paths = g.find_all_paths(node_1, node_3)
    for path in paths:
        g.print_path(path)
    paths = g.find_all_paths(node_1, node_4)
    for path in paths:
        g.print_path(path)
    print(g.has_route(node_1, node_4))
    print(g.has_route(node_1, node_5))
    g.print_path(g.find_shortest_path(node_1, node_3))
    g.print_path(g.find_path_dfs(node_1, node_3))
    print(str(g))
    print(str(node_1))
    g.print_path(g.find_path_dfs(node_1, node_5))
