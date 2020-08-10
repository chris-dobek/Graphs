"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import collections

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        q.enqueue(starting_vertex)

        seen = set()

        while q.size() > 0:
            current = q.dequeue()

            if current not in seen:
                seen.add(current)
                print(current)

                neighbors = self.get_neighbors(current)

                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        seen = set()

        while s.size() > 0:
            current = s.pop()

            if current not in seen:
                seen.add(current)
                print(current)

                neighbors = self.get_neighbors(current)

                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, seen = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if seen == None:

           seen = set()

        if starting_vertex not in seen:
            seen.add(starting_vertex)
            print(starting_vertex)
            
            neighbors = self.get_neighbors(starting_vertex)

            # Base case is no neighbors:
            if len(neighbors) == 0:
                return seen

            
            for neighbor in neighbors:
                self.dft_recursive(neighbor, seen)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        seen = set()
        path = list()

        path.append(starting_vertex)

        q.enqueue(path)

        while q.size() > 0:
            currentpath = q.dequeue()
            
            currentnode = currentpath[-1]

           
            if currentnode == destination_vertex:
                return currentpath

            
            if currentnode not in seen:

                # Mark it as seen and get its neighbors
                seen.add(currentnode)
                neighbors = self.get_neighbors(currentnode)

                # Now we iterate over it's neighbors
                for neighbor in neighbors:

                    
                    # Every neighbor has the exact previous steps, so we can copy
                    neighborpath = currentpath.copy()
                    # We now add the neighbor to it's new path
                    neighborpath.append(neighbor)
                    # And we enqueue the neighborpath to our queue to continue our traversal
                    q.enqueue(neighborpath)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        path = list()
        seen = set()

        
        path.append(starting_vertex)
        s.push(path)

       
        while s.size() > 0:

            
            currentpath = s.pop()
            
            currentnode = currentpath[-1]

            # if the current node is our destination then return it
            if currentnode == destination_vertex:
                return currentpath

            # If not we have to traverse
            # Go through what we have not seen yet
            if currentnode not in seen:
                # Mark it as seen get it's neighbors
                seen.add(currentnode)
                neighbors = self.get_neighbors(currentnode)

                # Now itereate over neighbors 
                for neighbor in neighbors:
                    # Each neighbor is a new path with the same previous steps so we can give a copy
                    neighborpath = currentpath.copy()
                    neighborpath.append(neighbor)

                    # push the path to the stack
                    s.push(neighborpath)

    def dfs_recursive(self, starting_vertex, destination_vertex, seen = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if seen is None:
            seen = set()
            path = collections.deque([])
            path.append([starting_vertex])

        seen.add(starting_vertex)
        current = path.pop()
        last = current[-1]

        for last in self.get_neighbors(last):
            if last not in seen:
                route = list(current)
                route.append(last)
                path.append(route)
                if last is destination_vertex:
                    return route

        return self.dfs_recursive(last, destination_vertex, seen, path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
