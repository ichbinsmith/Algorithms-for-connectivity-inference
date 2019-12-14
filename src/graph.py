#Smith Djamoura - 14-12-2019

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

        def __init__(self, t, deg=None):
            self._tag = t
            self._degree = 0

        def tag(self):
            return self._tag

        def __hash__(self):
            return hash(id(self)) 

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
        #redefine equal

        def __eq__(self, other):
            return True if self.tag == other.tag else False

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

        def endpointsTag(self):
            return (self._firstVertex.tag(), self._secondVertex.tag())


        def opposite(self, v):
            """
            Return the vertex that is opposite v on this edge
            """
            if not isinstance(v, Graph.Vertex):
                raise TypeError('v must be a Vertex')
            return self._secondVertex if v is self._firstVertex else self._firstVertex

        def __hash__(self):
            return hash( (self._firstVertex,self._secondVertex) )


        def __repr__(self):
            return '({0},{1})'.format(self._firstVertex,self._secondVertex)

        def __str__(self):
            return '({0},{1})'.format(self._firstVertex,self._secondVertex)

        def __eq__(self, other):
            return True if (self._firstVertex == other._firstVertex and self._secondVertex == other._secondVertex) else False

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
        bref = 0
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        for w in self._vertices.keys():
            if v.tag()==w.tag() :
                bref = bref + 1
                break
        if(bref==0):
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
        Return number of edges incident to vertex v in the graph.
        """
        self._validate_vertex(v)
        adj = self._vertices
        return len(adj[v])
    def max_degree(self):
        degrees = [] 
        for v in self._vertices.keys():
            degrees.append(self.degree(v))
        return max(degrees)


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

    def add_vertex(self,v):
        self._vertices[v] = {}


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
        break_cond = 0
        for w in self._vertices.keys():
            if ( (w==u) or (w==v) ):
                w.incDegree()
                break_cond=break_cond+1
            if break_cond == 2 :
                break


    def _print_edge(self,e):
        return '{0}-{1}'.format(e._firstVertex,e._secondVertex)

    def __str__(self):
        result = ""
        for u in self._vertices:
            for v in self._vertices[u]:
                result += self._print_edge(self._vertices[u][v]) + "\n"
        return result

    def print_graph(self):
        printed = set()
        result = ""
        for u in self._vertices:
            for v in self._vertices[u]:
                if( (self.get_edge(u,v) not in printed) and (self.get_edge(v,u) not in printed) ):
                    result += self._print_edge(self._vertices[u][v]) + "\n"
                    printed.add(self.get_edge(u,v))
                    printed.add(self.get_edge(v,u))
        return result
        



