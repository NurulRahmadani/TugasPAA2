import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")

    def minKey(self, key, mstSet):
        min_value = sys.maxsize
        min_index = None

        for v in range(self.V):
            if key[v] < min_value and mstSet[v] == False:
                min_value = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

g = Graph(6)
g.graph = [
    [0, 4, 0, 0, 0, 0],
    [4, 0, 2, 0, 0, 0],
    [0, 2, 0, 6, 0, 0],
    [0, 0, 6, 0, 3, 0],
    [0, 0, 0, 3, 0, 8],
    [0, 0, 0, 0, 8, 0],
]

g.primMST()