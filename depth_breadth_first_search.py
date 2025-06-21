from collections import deque
from typing import Dict, Hashable, List, Set

class SimpleGraph:
    def __init__(self):
        self.adj: Dict[Hashable, List[Hashable]] = {}

    def add_node(self, node: Hashable):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u: Hashable, v: Hashable):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append(v)

    def get_neighbors(self, node: Hashable) -> List[Hashable]:
        return self.adj.get(node, [])

    def get_nodes(self) -> List[Hashable]:
        return list(self.adj.keys())

def dfs_traverse(graph: SimpleGraph, start_node: Hashable) -> List[Hashable]:
    if start_node not in graph.get_nodes():
        print(f"Start node {start_node} not found in graph")
        return []

    visited: Set[Hashable] = set()
    stack: List[Hashable] = [start_node]
    dfs_order: List[Hashable] = []

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            dfs_order.append(current_node)

            neighbors = graph.get_neighbors(current_node)
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

    return dfs_order

def bfs_traverse(graph: SimpleGraph, start_node: Hashable) -> List[Hashable]:

    if start_node not in graph.get_nodes():
        print(f"Start node {start_node} not found in graph")
        return []

    visited: Set[Hashable] = set()
    queue: deque[Hashable] = deque([start_node])
    visited.add(start_node)
    bfs_order: List[Hashable] = []

    while queue:
        current_node = queue.popleft()
        bfs_order.append(current_node)

        for neighbor in graph.get_neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_order

if __name__ == "__main__":
    # Create a sample graph:
    # A -- > B -- > D
    # |      |      |
    # v      v      v
    # C -- > E < -- F

    graph = SimpleGraph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 'E') # Added edge D->E
    graph.add_edge('F', 'E') # Added edge F->E
    graph.add_node('G') # Add an isolated node

    print("Graph nodes:", graph.get_nodes())
    print("Graph adjacency list:", graph.adj)

    print("\n--- Traversal Examples ---")

    start_node = 'A'
    print(f"Starting traversal from node: {start_node}")

    dfs_result = dfs_traverse(graph, start_node)
    print(f"DFS Traversal Order: {dfs_result}")
    # Expected DFS order starting from A (depends on neighbor order):
    # e.g., ['A', 'C', 'E', 'F', 'B', 'D'] or ['A', 'B', 'D', 'E', 'C', 'F'] etc.

    bfs_result = bfs_traverse(graph, start_node)
    print(f"BFS Traversal Order: {bfs_result}")
    # Expected BFS order starting from A (depends on neighbor order):
    # e.g., ['A', 'B', 'C', 'D', 'E', 'F'] or ['A', 'C', 'B', 'E', 'D', 'F'] etc.
    # Level 0: A
    # Level 1: B, C
    # Level 2: D, E (reachable from B, C), F (reachable from F, but F is not reachable from A)
    # Let's re-evaluate BFS reachable from A:
    # Level 0: A
    # Level 1: B, C
    # Level 2: D (from B), E (from B, C)
    # So, reachable nodes from A are A, B, C, D, E. F and G are not reachable.
    # A valid BFS order would be ['A', 'B', 'C', 'D', 'E'] or ['A', 'C', 'B', 'D', 'E'] etc.

    print("\n--- Example with unreachable nodes ---")
    start_node_f = 'F'
    print(f"Starting traversal from node: {start_node_f}")
    dfs_result_f = dfs_traverse(graph, start_node_f)
    print(f"DFS Traversal Order: {dfs_result_f}") # Expected: ['F', 'E']
    bfs_result_f = bfs_traverse(graph, start_node_f)
    print(f"BFS Traversal Order: {bfs_result_f}") # Expected: ['F', 'E']

    print("\n--- Example with non-existent start node ---")
    start_node_invalid = 'Z'
    print(f"Starting traversal from node: {start_node_invalid}")
    dfs_result_invalid = dfs_traverse(graph, start_node_invalid)
    print(f"DFS Traversal Order: {dfs_result_invalid}") # Expected: []
    bfs_result_invalid = bfs_traverse(graph, start_node_invalid)
    print(f"BFS Traversal Order: {bfs_result_invalid}") # Expected: []
