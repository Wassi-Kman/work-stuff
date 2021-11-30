# mst.py
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
from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

V = TypeVar('V') # type of the vertices in the graph
WeightedPath = List[WeightedEdge] # type alias for paths


def total_weight(wp: WeightedPath) -> float:
    return sum([e.weight for e in wp])


def mst(wg: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:
    if start > (wg.vertex_count - 1) or start < 0:
        return None
    result: WeightedPath = [] # holds the final MST
    pq: PriorityQueue[WeightedEdge] = PriorityQueue()
    visited: List[bool] = [False] * wg.vertex_count # where we've been

    def visit(index: int):
        visited[index] = True # mark as visited
        for edge in wg.edges_for_index(index):
            # add all edges coming from here to pq
            if not visited[edge.v]:
                pq.push(edge)

    visit(start) # the first vertex is where everything begins

    while not pq.empty: # keep going while there are edges to process
        edge = pq.pop()
        if visited[edge.v]:
            continue # don't ever revisit
        # this is the current smallest, so add it to solution
        result.append(edge)
        visit(edge.v) # visit where this connects

    return result


def print_weighted_path(wg: WeightedGraph, wp: WeightedPath) -> None:
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} {edge.weight}> {wg.vertex_at(edge.v)}")
    print(f"Total Weight: {total_weight(wp)}")


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

    result: Optional[WeightedPath] = mst(city_graph2)
    if result is None:
        print("No solution found!")
    else:
        print_weighted_path(city_graph2, result)
