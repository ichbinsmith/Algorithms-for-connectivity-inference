import random

class Graph:
    """
    Representation of a simple graph
    """

    #-------------------------Vertex class -------------------------
    class Vertex:
        """
        vertex structure for a graph
        """
        __slots__ = '_tag' , '_degree'

        def __init__(self, t):
            self._tag = t
            self._degree = 0

        def tag(self):
            return self._tag

        def degree(self):
            return self._degree

        def incDegree(self):
            self._degree = self._degree + 1

        def decDegree(self):
            self._degree = self._degree - 1

        def __str__(self):
            return str(self._tag)

        def __repr__(self):
            return str(self._tag)

    #------------------------- Edge class -------------------------
    class Edge:
        """
        unweight edge structure for a graph
        """
        __slots__ = '_firstVertex', '_secondVertex'

        def __init__(self, u, v):
        
            self._firstVertex = u
            self._secondVertex = v

        def endpoints(self):
            return (self._firstVertex, self._secondVertex)

        def opposite(self, v):
            """
            Return the vertex that is opposite v on this edge
            """
            if not isinstance(v, Graph.Vertex):
                raise TypeError('v must be a Vertex')
            return self._secondVertex if v is self._firstVertex else self._firstVertex


        def __repr__(self):
            return '({0},{1})'.format(self._firstVertex,self._secondVertex)

        def __str__(self):
            return '({0},{1})'.format(self._firstVertex,self._secondVertex)

    #------------------------- Graph methods -------------------------
    
    def __init__(self):
        """
        Create an empty graph (undirected)
        """
        self._vertices = {}
        

    def _validate_vertex(self, v):
        """
        Verify that v is a Vertex of this graph
        """
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._vertices:
            raise ValueError('Vertex does not belong to this graph.')

    def get_vertex(self,tag):
        """
        Return the first vertex having the given tag.
        This is only a convenience method to grab a vertex
        after the graph has been constructed. You should not
        use it in graph algorithms.
        """
        for v in self._vertices.keys():
            if v.tag() == tag:
                return v
        return None

    def random_vertex(self):
        '''
        Return a vertex from the graph picked randomly
        (this is useful for Prim algorithm)
        '''
        return random.choice(list(self._vertices.keys()))

    def vertex_count(self):
        """
        Return the number of vertices in the graph
        """
        return len(self._vertices)

    def vertices(self):
        """
        Return an iteration of all vertices of the graph
        """
        return self._vertices.keys()

    def edge_count(self):
        """
        Return the number of edges in the graph
        """
        total = sum(len(self._vertices[v]) for v in self._vertices)
        return total // 2

    def edges(self):
        """
        Return a set of all edges of the graph
        """
        result = set()
        for secondary_map in self._vertices.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """
        Return the edge from u to v, or None if not adjacent
        """
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._vertices[u].get(v)

    def degree(self, v):   
        """
        Return number of (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to count incoming edges
        """
        self._validate_vertex(v)
        adj = self._vertices
        return len(adj[v])

    def adjacents(self, v):
        """
        Return an iteration of all adjacents vertices of vertex v
        """
        return self._vertices[v].keys()

    def incident_edges(self, v):   
        """
        Return an iteration of all incident edges to vertex v in the graph.
        """
        self._validate_vertex(v)
        adj = self._vertices
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, t=None):
        """
        Insert and return a new Vertex with tag t
        """
        v = self.Vertex(t)
        self._vertices[v] = {}
        return v

    def insert_edge(self, u, v):
        """
        Insert and return a new Edge from u to v.
        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent
        """
        if self.get_edge(u, v) is not None:
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v)
        self._vertices[u][v] = e

        #inc these vertices degree
        int break_cond = 0
        for w in self._vertices.keys()
            if ( (w==u) or (w==v) ):
                w.incDegree()
                break_cond++
            if break_cond = 2 :
                break


    def _print_edge(self,e):
        return '{0}-{1}'.format(e._firstVertex,e._secondVertex)

    def __str__(self):
        result = ""
        for u in self._vertices:
            for v in self._vertices[u]:
                result += self._print_edge(self._vertices[u][v]) + "\n"
        return result


def graph_from_edgelist(E):
    """
    Make a graph instance based on a sequence of edge tuples.
    Edges are in form (origin,destination) .
    Vertex set is presume to be those
    incident to at least one edge. Vertex labels are assumed to be hashable
    """
    g = Graph()
    V = set()
    
    #adding the vertices to V
    for e in E:
        V.add(e[0])
        V.add(e[1])

    #Inserting vertices to the graph
    verts = {}
    for v in V:
        verts[v] = g.insert_vertex(v)

    #inserting Edges to the graph
    for e in E:
        src = e[0]
        dest = e[1]
        g.insert_edge(verts[src],verts[dest])

    return g
