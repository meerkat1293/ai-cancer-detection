"https://www.python-course.eu/graphs_python.php"
class Graph:
    
    def __init__(self,graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
    
    def verticies(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self,vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self,edge):

        edge= set(edge)
        (vertex1,vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        res = "verticies: "
        for k in self.__graph_dict:
            res += str(k)+" "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res



            