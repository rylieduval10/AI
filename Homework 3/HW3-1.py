from collections import deque

class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n, time_of_day):
        H = {}

        for node in self.adjacency_list:
            if '41st' in node or '43rd' in node or '44th' in node or '45th' in node or '46th' in node or '47th' in node or '48th' in node:
                H[node] = 2
            else:
                H[node] = 1

        
        if 2 <= time_of_day <= 7:
            for node in H:
                if '42nd' in node:
                    H[node] = 6
                elif '_11' in node or '_10' in node or '_9' in node or '_8' in node:
                    H[node] = 4
                elif '_12' in node:
                    H[node] = 8
    

        return H[n]

    def a_star_algorithm(self, start_node, stop_node, time_of_day):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v, time_of_day) < g[n] + self.h(n, time_of_day):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    
adjacency_list = {
    #12th Ave
    '48th_12': [('48th_11', 3.5), ('47th_12', 1)],
    '47th_12': [('47th_11', 3.5), ('46th_12', 1), ('48th_12', 1)],
    '46th_12': [('46th_11', 3.5), ('45th_12', 1), ('47th_12', 1)],
    '45th_12': [('45th_11', 3.5), ('44th_12', 1), ('46th_12', 1)],
    '44th_12': [('44th_11', 3.5), ('43rd_12', 1), ('45th_12', 1)],
    '43rd_12': [('43rd_11', 3.5), ('42nd_12', 1), ('44th_12', 1)],
    '42nd_12': [('42nd_11', 3.5), ('41st_12', 1), ('43rd_12', 1)],
    '41st_12': [('41st_11', 3.5), ('42nd_12', 1)],
    #11th Ave
    '48th_11': [('48th_10', 3.5), ('48th_12', 3.5),('47th_11', 1)],
    '47th_11': [('47th_10', 3.5), ('47th_12', 3.5),('46th_11', 1), ('48th_11', 1)], 
    '46th_11': [('46th_10', 3.5), ('46th_12', 3.5),('45th_11', 1), ('47th_11', 1)], 
    '45th_11': [('45th_10', 3.5), ('45th_12', 3.5),('44th_11', 1), ('46th_11', 1)], 
    '44th_11': [('44th_10', 3.5), ('44th_12', 3.5),('43rd_11', 1), ('45th_11', 1)], 
    '43rd_11': [('43rd_10', 3.5), ('43rd_12', 3.5),('42nd_11', 1), ('44th_11', 1)], 
    '42nd_11': [('42nd_10', 3.5), ('42nd_12', 3.5),('41st_11', 1), ('43rd_11', 1)], 
    '41st_11': [('41st_10', 3.5), ('41st_12', 3.5), ('42nd_11', 1)], 

    #10th Ave
    '48th_10': [('48th_9', 3.5), ('48th_11', 3.5),('47th_10', 1)],
    '47th_10': [('47th_9', 3.5), ('47th_11', 3.5),('46th_10', 1), ('48th_10', 1)], 
    '46th_10': [('46th_9', 3.5), ('46th_11', 3.5),('45th_10', 1), ('47th_10', 1)], 
    '45th_10': [('45th_9', 3.5), ('45th_11', 3.5),('44th_10', 1), ('46th_10', 1)], 
    '44th_10': [('44th_9', 3.5), ('44th_11', 3.5),('43rd_10', 1), ('45th_10', 1)], 
    '43rd_10': [('43rd_9', 3.5), ('43rd_11', 3.5),('42nd_10', 1), ('44th_10', 1)], 
    '42nd_10': [('42nd_9', 3.5), ('42nd_11', 3.5),('41st_10', 1), ('43rd_10', 1)], 
    '41st_10': [('41st_9', 3.5), ('41st_11', 3.5), ('42nd_10', 1)], 

    #9th Ave
    '48th_9': [('48th_8', 3.5), ('48th_10', 3.5),('47th_9', 1)],
    '47th_9': [('47th_8', 3.5), ('47th_10', 3.5),('46th_9', 1), ('48th_9', 1)], 
    '46th_9': [('46th_8', 3.5), ('46th_10', 3.5),('45th_9', 1), ('47th_9', 1)], 
    '45th_9': [('45th_8', 3.5), ('45th_10', 3.5),('44th_9', 1), ('46th_9', 1)], 
    '44th_9': [('44th_8', 3.5), ('44th_10', 3.5),('43rd_9', 1), ('45th_9', 1)], 
    '43rd_9': [('43rd_8', 3.5), ('43rd_10', 3.5),('42nd_9', 1), ('44th_9', 1)], 
    '42nd_9': [('42nd_8', 3.5), ('42nd_10', 3.5),('41st_9', 1), ('43rd_9', 1)], 
    '41st_9': [('41st_8', 3.5), ('41st_10', 3.5), ('42nd_9', 1)], 

    #8th Ave
    '48th_8': [('48th_9', 3.5), ('47th_8', 1)],
    '47th_8': [('47th_9', 3.5), ('46th_8', 1), ('48th_8', 1)],
    '46th_8': [('46th_9', 3.5), ('45th_8', 1), ('47th_8', 1)],
    '45th_8': [('45th_9', 3.5), ('44th_8', 1), ('46th_8', 1)],
    '44th_8': [('44th_9', 3.5), ('43rd_8', 1), ('45th_8', 1)],
    '43rd_8': [('43rd_9', 3.5), ('42nd_8', 1), ('44th_8', 1)],
    '42nd_8': [('42nd_9', 3.5), ('41st_8', 1), ('43rd_8', 1)],
    '41st_8': [('41st_9', 3.5), ('42nd_8', 1)],


}   
graph1 = Graph(adjacency_list)

start_node = '42nd_8'
stop_node = '46th_12'  

# Create a graph instance
graph1 = Graph(adjacency_list)

path_at_1pm = graph1.a_star_algorithm(start_node, stop_node, 1) 
path_at_4pm = graph1.a_star_algorithm(start_node, stop_node, 4) 





