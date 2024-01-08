"""
Project 6: The Shortest Path Algorithm
"""


my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

my_graph_2 = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    """
    Find the shortest possible path from a source node to all other nodes in a weighted graph.

    Args:
        graph (dict): A weighted graph represented as a dictionary, where the keys are the nodes 
        and the values are lists of tuples representing the neighboring nodes 
        and their distances.
        
        start: The starting node or source node from which to find the shortest paths.
        
        target (optional): The target node to find the shortest path to. 
        If not provided, the function will find the shortest paths to all other nodes in the graph.

    Returns:
        tuple: A tuple containing two dictionaries:
            - distances (dict): A dictionary that maps each node to its shortest distance from the starting node.
            - paths (dict): A dictionary that maps each node to its shortest path from the starting node.
    """
    # create list of unvisited nodes
    unvisited = list(graph)
    distances = {node : 0 if node == start else float('inf') for node in graph} # keep track of shortest distance between starting node and other nodes
    paths = {node: [] for node in graph} 
    paths[start].append(start) # add starting node to own paths list
    
    while unvisited:
        # define current node to visit
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    # add current node path to neighbor node path
                    paths[node].extend(paths[current])
                # append neighbor node to its path
                paths[node].append(node)
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    
    for node in targets_to_print:
        if node == start:
            continue
        print(f"\n{start}-{node} distance: {distances[node]}\nPath: {' -> '.join(paths[node])}")
    
    return distances, paths


shortest_path(my_graph, 'A', 'C')