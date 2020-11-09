import sys
# import time
from decimal import Decimal, ROUND_HALF_UP

from scipy import spatial

# start_time = time.time()

text = []
for line in sys.stdin:
    text.append(line)

# file = open("C:/Users/Ivan Bucic/Desktop/R0", 'r')
# file = open("C:/Users/Ivan Bucic/Desktop/R.in", 'r')
# text = file.readlines()
# file.close()

first_line = text[0].split(' ')
N = int(first_line[0])
M = int(first_line[1])

matrix_item_user = [line.rstrip() for line in text[1:N + 1]]
item_user = []
item_user_norm = []
M1 = []
for line in matrix_item_user:
    line = line.split(' ')
    line_item = [int(item) if item != 'X' else 0 for item in line]
    number = 0
    for item in line_item:
        if item != 0:
            number += 1
    average = sum(line_item) / number
    # line_item_norm = [round(item - average, 3) if item != 0 else 0 for item in line_item]
    line_item_norm = [item - average if item != 0 else 0 for item in line_item]
    item_user.append(line_item)
    M1.append(average)
    item_user_norm.append(line_item_norm)

item_user_trans = list(map(list, zip(*item_user)))
item_user_norm_trans = []
M2 = []
for line_user in item_user_trans:
    number = 0
    for user in line_user:
        if user != 0:
            number += 1
    average = sum(line_user) / number
    line_user_norm = [user - average if user != 0 else 0 for user in line_user]
    M2.append(average)
    item_user_norm_trans.append(line_user_norm)

# print(item_user)
# print(item_user_trans)
# print(item_user_norm)
# print(item_user_norm_trans)
# print(M1)
# print(M2)
# print()

Q = int(text[N + 1])

matrix_query = [line.rstrip() for line in text[N + 2:]]
for line in matrix_query:
    line_query = list(map(int, line.split(' ')))

    # I - redak film, J - stupac korisnik, T - 0: item/item ; 1: user/user
    I, J, T, K = line_query[0], line_query[1], line_query[2], line_query[3]

    # ITEM/ITEM
    if T == 0:
        query_item = item_user_norm[I - 1]
        sim = [1 - spatial.distance.cosine(item_line, query_item) for item_line in item_user_norm]
        user = item_user_trans[J - 1]

        sim_new = [sim[i] for i in range(len(sim)) if user[i] != 0]
        sim_new.sort(reverse=True)
        sim_K = [sim_new[i] for i in range(K) if sim_new[i] > 0]

        user_sim_sum = 0
        sim_sum = 0
        for item_use, item_sim in zip(user, sim):
            if item_use != 0 and item_sim in sim_K:
                user_sim_sum += item_use * item_sim
                sim_sum += item_sim
        r = user_sim_sum / sim_sum
        r = Decimal(Decimal(r).quantize(Decimal('.001'), rounding=ROUND_HALF_UP))
        sys.stdout.write(str(r) + '\n')

    # USER/USER
    elif T == 1:
        query_user = item_user_norm_trans[J - 1]
        sim = [1 - spatial.distance.cosine(user_line, query_user) for user_line in item_user_norm_trans]
        item = item_user[I - 1]

        sim_new = [sim[i] for i in range(len(sim)) if item[i] != 0]
        sim_new.sort(reverse=True)
        sim_K = [sim_new[i] for i in range(K) if sim_new[i] > 0]

        item_sim_sum = 0
        sim_sum = 0
        for user_item, item_sim in zip(item, sim):
            if user_item != 0 and item_sim in sim_K:
                item_sim_sum += user_item * item_sim
                sim_sum += item_sim
        r = item_sim_sum / sim_sum
        r = Decimal(Decimal(r).quantize(Decimal('.001'), rounding=ROUND_HALF_UP))
        sys.stdout.write(str(r) + '\n')

# print("--- %s seconds ---" % (time.time() - start_time))
