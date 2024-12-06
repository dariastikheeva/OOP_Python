import math


class Vertex:
    __count = 0

    def __init__(self, name=None):
        Vertex.__count += 1
        self.name = name if name is not None else str(Vertex.__count)
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        if self._v2 not in self._v1._links:
            self._v1._links.append(self._v2)
        if self._v1 not in self._v2._links:
            self._v2._links.append(self._v1)
        self._dist = dist

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist
    @dist.setter
    def dist(self, value):
        self._dist = value

    def __eq__(self, other):
        return self.v1 in (other.v1, other.v2) and self.v2 in (other.v1, other.v2)


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def get_vertex(self, name):
        for vertex in self._vertex:
            if vertex.name == name:
                return vertex

    def get_dist_vertex(self, from_v, to_v):
        if from_v == to_v:
            return 0
        for link in self._links:
            if (from_v == link._v1 or from_v == link._v2) and (
                to_v == link._v1 or to_v == link._v2
            ):
                return link._dist
        return math.inf

    def get_link(self, v1, v2):
        for link in self._links:
            if isinstance(link, Link):
                if Link(v1, v2) == link:
                    return link
            if isinstance(link, LinkMetro):
                if LinkMetro(v1, v2, self.get_dist_vertex(v1, v2)) == link:
                    return link

    def next_vertex(self, viewed, lenght_path):
        min = -1
        max = math.inf
        for key, value in lenght_path.items():
            if value < max and key not in viewed:
                max = value
                min = key
        return min

    def find_path(self, start_v, stop_v):
        matrix = self.create_matrix()
        optimal_link = [0] * len(self._vertex)
        viewed_vertex = set()  # Просмотренные вершины
        path = ()  # Кортеж результирующий с наименованием вершин и связями между ними
        lenght_path = {v.name: math.inf for v in self._vertex}
        v = start_v.name
        viewed_vertex.add(v)
        lenght_path[v] = 0
        while v != -1:
            for ind, val in enumerate(matrix[v]):
                if str(ind + 1) not in viewed_vertex:
                    w = lenght_path[v] + val
                    if w < lenght_path[str(ind + 1)]:
                        lenght_path[str(ind + 1)] = w
                        optimal_link[ind] = v
            v = self.next_vertex(viewed_vertex, lenght_path)
            if v != -1:
                viewed_vertex.add(v)

        start = start_v.name
        end = stop_v.name
        P = [int(end)]
        while end != start:
            end = optimal_link[P[-1] - 1]
            P.append(int(end))
        res_P = P[::-1]
        path = [self.get_vertex(str(name)) for name in res_P]
        weight = [
            self.get_link(
                self.get_vertex(str(res_P[i - 1])), self.get_vertex(str(res_P[i]))
            )
            for i in range(1, len(res_P))
        ]
        return (path, weight)

    def create_matrix(self):
        len_matrix = len(self._vertex)
        matrix = {v.name: [math.inf] * len_matrix for v in self._vertex}

        for i, v in enumerate(self._vertex):
            for ind, to_v in enumerate(self._vertex):
                dist = self.get_dist_vertex(v, to_v)
                matrix[v.name][ind] = dist
                dist = 0
        return matrix


class Station(Vertex):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def __eq__(self, other):
        if isinstance(other, Station):
            return True if self.name == other.name else False


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)
