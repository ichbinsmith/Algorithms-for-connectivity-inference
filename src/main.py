import random
from graph import *


#create graphe from edge list, this edges are just tuple(char,char)
#it means Vertex will be created, they don't exist
#same for the Edges
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

#create a compete graphe from existing vertices list : Already created vertices
#do not forget that Graph.Vertex is hashable
def complete_graph_from_verticesList(V):
	g = Graph()

	#adding vertices
	for v in V:
		g.add_vertex(v)

	#create all edges and add them
	for v1 in V:
		for v2 in V:
			if( (v1!=v2) and (g.get_edge(v1, v2) is None) ):
				g.insert_edge(v1,v2)


	return g

'''
	subComplexes genetor
'''
def subComplexesGenerator(vertices, t, p):
	#Error if function doesn't work for the given parameters (t and p)
	if p not in range(1,101):
		raise ValueError('the third parameter must be in range(1,100)')
	if (t<1):
		raise ValueError('the second parameter must be greater than 0')
	subComplexes = {} #Dictionnary Of the subComplexes

	for i in range(1,t+1): #number of subComplexes created == t
		vertex_added = 0
		vertex_for_creation = []

		while(vertex_added<p): #Select p different vertices [random]
			v = random.choice(list(vertices.values()))
			if(v not in vertex_for_creation):
				vertex_for_creation.append(v)
				vertex_added=vertex_added+1

		subComplexes['C'+str(i)] = complete_graph_from_verticesList(vertex_for_creation)


	return subComplexes

def Prim(G):
	result = {}

	mst = []
	bh = set()
	u = G.random_vertex()
	marked = { u }
	for e in G.incident_edges(u):
		bh.add(e)
	while len(marked) < G.vertex_count():
		e = bh.pop()
		a, b = e.endpoints()
		if a in marked and b in marked:
			continue
		mst.append(e)
		x = a if b in marked else b
		marked.add(x)
		for e in G.incident_edges(x):
			if e.opposite(x) not in marked:
				bh.add(e)

	return mst

'''
	Computing method
'''
def compute(subComplexes, k, delta, t):
	win = 0
	fail = 0
	
	for sc in subComplexes.values():
		edgesInG = []
		g = {}
		res = Prim(sc)
		for e in res :
			if(e not in edgesInG):
				edgesInG.append(e)
		
		edgesList=[]
		for e in edgesInG:
			edgesList.append(e.endpointsTag())
		g=graph_from_edgelist(edgesList)
		#edges count < k
		a= True if (g.edge_count()<k) else False
		#max degree < delta
		b= True if (g.max_degree()<delta) else False
		if (a==True and b==True):
			win = win +1
		else:
			fail = fail +1

	return win / t

#Main

if __name__ == '__main__':
	vertices={}
	#create 100 vertices
	for i in range(1,101):
		vertices['V'+str(i)] = Graph.Vertex('V'+str(i))

	#generate subComplexes t,n
	subComplexes = subComplexesGenerator(vertices,3,5) 

	#compute subComplexes, k, delta, t, a
	res = compute(subComplexes,100,3,3)

	print(res)