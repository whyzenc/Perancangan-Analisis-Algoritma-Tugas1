#NAMA  : WHENNY ZENICA
#NIM   : 23343022
#PRODI : INFORMATIKA
#PROGRAM : Prim Algorithm

import heapq

class PrimGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def displayMST(self, mst):
        print("Edge \tWeight")
        total_cost = 0
        for start, end, weight in mst:
            print(f"{chr(65 + start)} - {chr(65 + end)} \t {weight}")
            total_cost += weight
        print("Total Cost:", total_cost)

    def findMST(self):
        mst = []
        included = [False] * self.vertices
        priority_queue = [(0, 0, -1)]  # (weight, current node, parent node)

        while priority_queue and len(mst) < self.vertices - 1:
            weight, current, parent = heapq.heappop(priority_queue)

            if included[current]:
                continue

            included[current] = True

            if parent != -1:
                mst.append((parent, current, weight))

            for neighbor in range(self.vertices):
                edge_weight = self.adj_matrix[current][neighbor]
                if edge_weight > 0 and not included[neighbor]:
                    heapq.heappush(priority_queue, (edge_weight, neighbor, current))

        if len(mst) == self.vertices - 1:
            self.displayMST(mst)
        else:
            print("Graph is not connected; MST cannot be formed.")

if __name__ == '__main__':
    graph = PrimGraph(6)  # Graph with 6 vertices (A-F)
    
    graph.adj_matrix = [[0, 3, 0, 0, 6, 5],  # A
                         [3, 0, 1, 0, 0, 4],  # B
                         [0, 1, 0, 6, 0, 4],  # C
                         [0, 0, 6, 0, 8, 5],  # D
                         [6, 0, 0, 8, 0, 2],  # E
                         [5, 4, 4, 5, 2, 0]]  # F

    graph.findMST()