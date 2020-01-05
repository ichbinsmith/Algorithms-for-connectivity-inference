import random
import argparse
from graph import *



# argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--numberOfSubComplexes', help="number Of Sub-Complexes -t in [1...*]",type=int, default=20)
parser.add_argument('-p', '--subComplexesItemsNumber', help="number Of Sub-Complexes items", type=int, default=10)
parser.add_argument('-k', '--maxNumberOfEdges', help="maxNumberOfEdges -k [1...*]", type=int, default=2)
parser.add_argument('-d', '--delta', help="Max degree of the resulting graph", type=int, default=10)
parser.add_argument('-a', '--algo', help="The algo use for simulation 0-first Algo, 1-second algo", type=int, choices=[0, 1], default=0)
parser.add_argument('-n', '--execNumber', help="Number of execution -n in [1...*]", type=int, default=1)
args = parser.parse_args()

def printOptions():
	print("numberOfSubComplexes : ", args.numberOfSubComplexes)
	print("subComplexesItemsNumber : ", args.subComplexesItemsNumber)
	print("maxNumberOfEdges : ", args.maxNumberOfEdges)
	print("delta : ", args.delta)
	print("algo : ", args.algo)
	print("Number of execution : ", args.execNumber)
	print()

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
	Computing method "Algo One"
'''
def computeAlgoOne(subComplexes, k, delta, t):
	win = 0
	
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

	return win

'''
	Compute Algo n time and return proportion of positive result
'''
def computeAlgoOneXtime(n, subComplexes, k, delta, t):
	win = 0
	for i in range(1,n+1):
		win = win + computeAlgoOne(subComplexes, k, delta, t)

	return win/n

def computeAlgoTwo(subComplexes, k, delta, t):
	win = 0
	fail = 0



	return win / t

#Main

if __name__ == '__main__':
	#args
	t=args.numberOfSubComplexes
	p=args.subComplexesItemsNumber
	k=args.maxNumberOfEdges
	d=args.delta
	a=args.algo
	n=args.execNumber
	printOptions()

	#program beginning

	vertices={}
	#create 100 vertices
	for i in range(1,101):
		vertices['V'+str(i)] = Graph.Vertex('V'+str(i))

	#generate subComplexes t,p
	subComplexes = subComplexesGenerator(vertices,t,p) 

	#compute subComplexes, k, delta, t, a
	if(a==0):
		res = computeAlgoOneXtime(n,subComplexes,k,d,t)
		print(res)
	elif(a==1):
		print("second algo is not ready yet")
	

	