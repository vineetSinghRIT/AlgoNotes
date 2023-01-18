


from collections import defaultdict

def makegraph(node_cnt,connectionList):
    graph=dict()
    for i in range(node_cnt):
        graph[i]=[]
    for conn in connectionList:
        graph[conn[1]].append(conn[0])
        if conn[0] not in graph:
            graph[conn[0]]=[]
    return graph

#def topSort(graph):

def toposort(graph):
    res, found = [], [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(~node)
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack += graph[node]

    # cycle check
    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0

    return res[::-1]

if __name__ == '__main__':
    temp=[[1,0],[2,0],[3,1],[3,2],[7,5],[5,4],[8,5]]
    # 5 is the assumed no of nodes in graph
    graph=makegraph(9,temp)
    print(graph)
    print(toposort(graph))