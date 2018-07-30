from py2neo import Graph, Node
import networkx as nx 
graph = Graph(password = "rosebay")
hunter = Node("Person", name="hunterni", address= "kupondole")
graph.create(hunter)
query = '''
        MATCH(n) RETURN n
        '''
query2 = '''
        CALL apoc.help("dijkstra")
        '''
data = graph.run(query)
strin = graph.run(query2)
for d in data:
    print(d)