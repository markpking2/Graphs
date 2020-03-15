import sys
sys.path.insert(0, '../graph/')
from graph import Graph
from util import Queue



class Ancestor_Graph(Graph):
    def bfs_oldest(self, starting_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        longest_path = [starting_vertex]
        while queue.size() > 0:
            current_path = queue.dequeue()
            if len(current_path) > len(longest_path) or len(current_path) == len(longest_path) and current_path[-1] < longest_path[-1]:
                longest_path = current_path
            for vertex in self.get_neighbors(current_path[-1]):
                queue.enqueue([*current_path, vertex])
        return longest_path[-1] if longest_path[-1] != starting_vertex else -1


def earliest_ancestor(ancestors, starting_node):
    graph = Ancestor_Graph()
    for vertex in set([v for adj in ancestors for v in adj]):
        graph.add_vertex(vertex)
    # inverse of original directed graph
    for adj in ancestors:
        graph.add_edge(adj[1], adj[0])
    return graph.bfs_oldest(starting_node)
