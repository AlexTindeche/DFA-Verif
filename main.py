dfa = {}

def read_dfa():
    nodeNr = int(input("Number of nodes: "))
    edgeNr = int(input("Number of edges: "))
    for i in range(edgeNr):
        fromNode = int(input("From: "))
        toNode = int(input("To: "))
        onEdge = input("With: ")
        if fromNode not in dfa:
            dfa[fromNode] = [(toNode, onEdge)]
        else:
            dfa[fromNode].append((toNode, onEdge))

### main ###
read_dfa()
print(dfa)