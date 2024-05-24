from read import graphs, vertex_source

edges = graphs
graph = {}
start = vertex_source
target_distance = 2024

for u, v, w in edges:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))


def dfs(graph, start, target_distance, current_distance, path, path_weights, visited):
    if current_distance == target_distance:
        return path, path_weights
    if current_distance > target_distance:
        return None, None
    
    for neighbor, weight in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            result, result_weights = dfs(graph, neighbor, target_distance, current_distance + weight, path + [neighbor], path_weights + [current_distance + weight], visited)
            if result is not None:
                return result, result_weights
            visited.remove(neighbor)
    
    return None, None

path, path_weights = dfs(graph, start, target_distance, 0, [start], [0], {start})

if path:
    result = "Path: " + " -> ".join(f"{path[i]}({path_weights[i]})" for i in range(len(path)))
else:
    result = "No path found"

print(result)

