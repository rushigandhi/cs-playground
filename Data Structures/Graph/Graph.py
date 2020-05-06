# Graph Node class that stores a value and list of all edges to/from it
class Node():
    def __init__(self, value):
        self.value = value
        self.edges = []


# Graph Edge class that stores a value, a source node, and a destination node
class Edge():
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


# Graph class implementation
class Graph():

    # initialize graph with nodes and edges
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    # insert_node to graph by appending to the nodes list
    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    # insert_edge to graph
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None

        # find the source node and destination node in graph
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node

        # if not found, create the source node and/or destination node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)

        # create a new edge from the new_edge_val, source node, and destination node
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    # return the greatest node value
    def get_max_index(self):
        maxIndex = -1
        for node in self.nodes:
            maxIndex = max(maxIndex, node.value)
        return maxIndex

    # return the edge list for this graoh
    def get_edge_list(self):
        edge_list = []

        # create a list containing a (edge value, source node value, destination node value) tuple for all edges
        for edge in self.edges:
            edge_list.append(
                (edge.value, edge.node_from.value, edge.node_to.value))
        return edge_list

    # return the adjacency list for this graph
    def get_adjacency_list(self):

        # get the max index and None fill the adj_list
        max_index = self.get_max_index()
        adj_list = [None] * (max_index + 1)

        # for all edges create a list at the index of the source node and store a list with all its
        # destination nodes with their respective edge strengths
        for edge in self.edges:
            if adj_list[edge.node_from.value]:
                adj_list[edge.node_from.value].append(
                    (edge.node_to.value, edge.value))
            else:
                adj_list[edge.node_from.value] = [
                    (edge.node_to.value, edge.value)]
        return adj_list

    # return the adjacency matrix for this graph
    def get_adjacency_matrix(self):

        # get max index and zero fill the matrix
        max_index = self.get_max_index()
        adj_mtx = [[0 for i in range(max_index + 1)]
                   for j in range(max_index + 1)]

        # for all edges, store the edge strength at the [from][to] location
        for edge in self.edges:
            adj_mtx[edge.node_from.value][edge.node_to.value] = edge.value

        return adj_mtx
