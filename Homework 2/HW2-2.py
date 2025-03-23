from collections import defaultdict

class Graph():
    def __init__(self):
        self.nodes = defaultdict(list)
    
    def add_children(self, parent, children):
        self.nodes[parent].extend(children)

graph = Graph()

# Define the tree structure
graph.add_children('a', ['b', 'c'])
graph.add_children('b', ['d', 'e'])
graph.add_children('c', ['f', 'h'])
graph.add_children('d', ['i', 'j'])
graph.add_children('f', ['g2', 'k'])
graph.add_children('h', ['l', 'm'])
graph.add_children('m', ['n', 'g2'])

def depth_first_search(graph, start, goal):
    open_list = [start] 
    closed_list = [] 
    
    while open_list:
        x = open_list.pop(0) 
        
        if x == goal:
            closed_list.append(x) 
            return f"Success: Path found to {goal}", closed_list
        
        closed_list.append(x) 
        
        children = graph.nodes[x]

        for child in reversed(children):  
            if child not in closed_list and child not in open_list:
                open_list.insert(0, child) 
    
    return "Goal not Found"

result = depth_first_search(graph, 'a', 'f')
print(result)

    
