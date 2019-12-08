import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import interactive


class CustomGraph:
    def __init__(self, _n, _weights=[], _random=True):
        if (_random is True):
            self.konstruktor_random(_n)
        if (_random is False):
            self.konstruktor_zadano(_n, _weights)
    # Konstruktor za random graf --- ima bridove netrivijalne
    # tezine: (i, j), za i < j.

    def konstruktor_random(self, _n):
        self.weights = []
        self.n = _n

        for i in range(0, _n):
            vert = []
            for j in range(0, i+1):
                vert.append(0)
            for j in range(i+1, _n):
                vert.append(random.randint(0, 100))
            self.weights.append(vert)

    # Graf sa zadanim tezinama
    def konstruktor_zadano(self, _n, _weights):
        self.weights = _weights
        self.n = _n

    def skiciraj(self):
        G_rend = nx.MultiDiGraph()
        G_rend.add_nodes_from([i for i in range(0, self.n)])
        pos = nx.circular_layout(G_rend)

        edges = []
        edge_labels = {}

        for i in range(0, self.n):
            for j in range(0, self.n):
                if (self.weights[i][j] > 0):
                    edges.append((i, j))
                    edge_labels[(i, j)] = self.weights[i][j]

        fig = plt.figure(num="Graf")
        ax = fig.add_subplot(111)
        plt.axis("off")

        nx.draw_networkx_nodes(G_rend, pos, node_size=500)

        vert_labels = {i-1: i for i in range(1, self.n + 1)}

        nx.draw_networkx_labels(G_rend, pos, vert_labels, font_size=16)

        nx.draw_networkx_edges(G_rend, pos, edgelist=edges, edge_color='black')

        nx.draw_networkx_edge_labels(G_rend,
                                     pos,
                                     edge_labels,
                                     font_color='black')


if __name__ == "__main__":
    interactive(True)
    G = CustomGraph(3, [[0, 1, 2], [1, 0, 0], [0, 0, 0]], _random=False)
    G.skiciraj()
