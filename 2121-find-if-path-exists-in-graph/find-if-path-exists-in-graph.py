class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = deque([source])
        visited = set()
        while queue:
            current_vertex = queue.popleft()
            if current_vertex == destination:
                return True
            visited.add(current_vertex)
            for neighbor in graph[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

        
        return False
            