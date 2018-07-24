from py2neo import Graph, Node
import networkx as nx 
graph = Graph(password = "rosebay")
hunter = Node("Person", name="hunterni", address= "kupondole")
graph.create(hunter)
query = '''
        MATCH(n) RETURN n
        '''
data = graph.run(query)
for d in data:
    print(d)