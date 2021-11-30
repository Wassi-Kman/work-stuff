# weighted_graph.py
# From Classic Computer Science Problems in Python Chapter 4
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('V') # type of the vertices in the graph


class WeightedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]

    def add_edge_by_indices(self, u: int, v: int, weight: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge) # call superclass version

    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
        return desc


if __name__ == "__main__":
    city_graph2: WeightedGraph[str] = WeightedGraph(["Nairobi", "Thika", "Naivasha", "Meru", "Embu", "Emali", "Kisumu", "Nakuru", "Malindi", "Mombasa", "Lamu", "Garissa", "Kiambu", "Isiolo", "Eldoret"])

    city_graph2.add_edge_by_vertices("Nairobi", "Emali", 1737)
    city_graph2.add_edge_by_vertices("Nairobi", "Thika", 678)
    city_graph2.add_edge_by_vertices("Thika", "Meru", 386)
    city_graph2.add_edge_by_vertices("Thika", "Naivasha", 348)
    city_graph2.add_edge_by_vertices("Naivasha", "Meru", 50)
    city_graph2.add_edge_by_vertices("Naivasha", "Embu", 357)
    city_graph2.add_edge_by_vertices("Meru", "Embu", 307)
    city_graph2.add_edge_by_vertices("Meru", "Emali", 1704)
    city_graph2.add_edge_by_vertices("Embu", "Lamu", 887)
    city_graph2.add_edge_by_vertices("Embu", "Garissa", 1015)
    city_graph2.add_edge_by_vertices("Lamu", "Emali", 805)
    city_graph2.add_edge_by_vertices("Lamu", "Malindi", 721)
    city_graph2.add_edge_by_vertices("Lamu", "Garissa", 225)
    city_graph2.add_edge_by_vertices("Garissa", "Malindi", 702)
    city_graph2.add_edge_by_vertices("Garissa", "Mombasa", 968)
    city_graph2.add_edge_by_vertices("Malindi", "Emali", 588)
    city_graph2.add_edge_by_vertices("Malindi", "Eldoret", 543)
    city_graph2.add_edge_by_vertices("Malindi", "Mombasa", 604)
    city_graph2.add_edge_by_vertices("Mombasa", "Eldoret", 923)
    city_graph2.add_edge_by_vertices("Emali", "Kiambu", 238)
    city_graph2.add_edge_by_vertices("Kiambu", "Kisumu", 613)
    city_graph2.add_edge_by_vertices("Kiambu", "Eldoret", 396)
    city_graph2.add_edge_by_vertices("Kiambu", "Nakuru", 482)
    city_graph2.add_edge_by_vertices("Kisumu", "Nakuru", 190)
    city_graph2.add_edge_by_vertices("Nakuru", "Isiolo", 81)
    city_graph2.add_edge_by_vertices("Isiolo", "Eldoret", 123)

    print(city_graph2)
