import sys
import time

dead_ends = []


def find_nearest_black_node(visited_nodes, open_nodes, black_nodes, matrix, dead_end_nodes, distance):
    if distance > 10 or len(open_nodes) == 0:
        return -1, -1

    visited_nodes = open_nodes + visited_nodes
    visited_nodes.sort()
    next_nodes = []
    for node in open_nodes:
        if black_nodes[node] == 0:
            return node, distance
        add_nodes = [nd for nd in matrix[node] if nd not in visited_nodes and nd not in dead_end_nodes]
        next_nodes = next_nodes + add_nodes
    next_nodes.sort()
    return find_nearest_black_node(visited_nodes, next_nodes, black_nodes, matrix, dead_end_nodes, distance + 1)


start_time = time.time()

text = []
for line in sys.stdin:
    text.append(line)

# file = open("C:/Users/Ivan Bucic/Desktop/btest2/R.in", 'r')
# text = file.readlines()
# file.close()

first_line = text[0].split(' ')
n = int(first_line[0])
e = int(first_line[1])
e_float = float(first_line[1])

node_list = [int(node) for node in text[1:n + 1]]

index_list = {}
for i in range(n):
    index_list[i] = []
for query in text[n + 1:]:
    query_line = query.rstrip().split(' ')
    node1, node2 = int(query_line[0]), int(query_line[1])
    index_list[node1].append(node2)
    index_list[node2].append(node1)
for node in index_list:
    index_list[node].sort()
# print(index_list)

distance_list = [-1 if node == 0 else 0 for node in node_list]
# print(distance_list)

for node in range(n):
    b, dist = find_nearest_black_node([], [node], distance_list, index_list, dead_ends, 0)
    if b == -1 and dist == -1:
        dead_ends.append(node)
    sys.stdout.write(str(b) + ' ' + str(dist) + '\n')

# print("--- %s seconds ---" % (time.time() - start_time))
