import sys
import itertools
import time

start_time = time.time()

text = []
for sys_line in sys.stdin:
    text.append(sys_line)

# file = open("C:/Users/Ivan Bucic/Desktop/test2/R.in", 'r')
# text = file.readlines()
# file.close()

basket_number = int(text[0])
s = float(text[1])
step = s * basket_number
case_number = int(text[2])

baskets = [basket.rstrip() for basket in text[3:basket_number + 3]]

items = {}
for basket in baskets:
    basket = list(map(int, basket.split(' ')))
    for item in basket:
        items[item] = items[item] + 1 if item in items.keys() else 1
# print("--- %s seconds ---" % (time.time() - start_time))

cases = {}
for basket in baskets:
    basket = list(map(int, basket.split(' ')))
    for item1, item2 in itertools.combinations(basket, 2):
        if items[item1] >= step and items[item2] >= step:
            k = ((item1 * len(items)) + item2) % case_number
            cases[k] = cases[k] + 1 if k in cases.keys() else 1
# print("--- %s seconds ---" % (time.time() - start_time))

pairs = {}
for basket in baskets:
    basket = list(map(int, basket.split(' ')))
    for item1, item2 in itertools.combinations(basket, 2):
        if items[item1] >= step and items[item2] >= step:
            k = ((item1 * len(items)) + item2) % case_number
            if cases[k] >= step:
                pairs[(item1, item2)] = pairs[(item1, item2)] + 1 if (item1, item2) in pairs.keys() else 1

m = 0
for i in items:
    if items[i] >= step:
        m += 1
A = m * (m - 1) / 2
sys.stdout.write(str(int(A)) + '\n')

# counter = 0
# for item1, item2 in pairs.items():
#     counter += 1
# sys.stdout.write(str(counter) + '\n')

sys.stdout.write(str(len(pairs.values())) + '\n')

for i in sorted(pairs, key=pairs.get, reverse=True):
    sys.stdout.write(str(pairs[i]) + '\n')

# print("--- %s seconds ---" % (time.time() - start_time))
