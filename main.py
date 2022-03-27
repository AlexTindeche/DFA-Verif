def read_dfa(dfa, states):
    fin = open("dfa.txt")
    # global dfa, states
    nodeNr = int(fin.readline().strip())
    edgeNr = int(fin.readline().strip())
    finalStates = int(fin.readline().strip())
    for i in range(nodeNr):
        states[i] = 0
    for i in range(finalStates):
        final = int(fin.readline().strip())
        states[final] = 1
    for i in range(edgeNr):
        fromNode = int(fin.readline().strip())
        toNode = int(fin.readline().strip())
        onEdge = fin.readline().strip()
        if fromNode not in dfa:
            dfa[fromNode] = [(toNode, onEdge)]
        else:
            dfa[fromNode].append((toNode, onEdge))

    return [dfa, states]


def verify_dfa(node, word, states, dfa, done):
    # global states, dfa, done
    # if word == []:
    if not word:
        if states[node] == 1:
            print(".ACCEPTED.")
            # done = 1
            return 1
        else:
            return 0
    else:
        for edge in dfa[node]:
            if edge[1] == word[0]:
                if done == 0:
                    path.append(edge[0])
                    done = verify_dfa(edge[0], word[1:], states, dfa, done)
                else:
                    return 1

    return done


if __name__ == '__main__':
    dfa = {}
    states = {}
    done = 0

    (dfa, states) = read_dfa(dfa, states)
    print(dfa)
    print(states)

    word = list(input("Word to verify: "))
    # path = []
    # path.append(0)
    path = [0]

    done = verify_dfa(0, word, states, dfa, done)
    if done == 0:
        print(".NOT ACCEPTED.")
    else:
        print(path)
