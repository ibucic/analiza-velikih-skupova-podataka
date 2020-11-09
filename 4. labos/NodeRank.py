import sys
import time
from decimal import Decimal, ROUND_HALF_UP

start_time = time.time()

text = []
for line in sys.stdin:
    text.append(line)

# file = open("C:/Users/Ivan Bucic/Desktop/btest2/R.in", 'r')
# text = file.readlines()
# file.close()

first_line = text[0].split(' ')
n = int(first_line[0])
beta = float(first_line[1])
r = (1 - beta) / n

node_matrix = [[r for _ in range(n)] for _ in range(100)]
node_matrix.insert(0, [1 / n for _ in range(n)])

nodes_string = [line.rstrip().split(' ') for line in text[1:n + 1]]
nodes_list = [[int(line) for line in lines] for lines in nodes_string]
# print(nodes_list)

for i in range(100):
    for j in range(n):
        for node in nodes_list[j]:
            node_matrix[i + 1][node] += beta * node_matrix[i][j] / len(nodes_list[j])

# print(node_matrix)
# print("--- %s seconds ---" % (time.time() - start_time))

Q = int(text[n + 1])
query_string = [line.rstrip().split(' ') for line in text[n + 2:]]
query_list = [[int(query) for query in querys] for querys in query_string]
# print(query_list)

for querys in query_list:
    node, i = querys[0], querys[1]
    result = Decimal(Decimal(node_matrix[i][node]).quantize(Decimal('.0000000001'), rounding=ROUND_HALF_UP))
    sys.stdout.write(str(result) + '\n')

# print("--- %s seconds ---" % (time.time() - start_time))
