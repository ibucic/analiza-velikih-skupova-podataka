import hashlib
import sys
# import time

# start_time = time.time()


def hash2int(def_zone, def_hash_line):
    return int(''.join(def_hash_line[16 * def_zone:16 * def_zone + 16]))


def hammingDistance(string1, string2):
    difference = 0
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            difference += 1

    return difference


def simHash(line):
    sh = [i - i for i in range(128)]
    words = line.split(' ')
    for word in words:
        hash_list = list((bin(int(hashlib.md5(word.encode('utf-8')).hexdigest(), 16))[2:]).zfill(128))
        # h = hashlib.md5(word.encode('utf-8'))
        # hexadecimal = h.hexdigest()
        # decimal = int(hexadecimal, 16)
        # binary = bin(decimal)
        # hash_list = list(binary)

        # for i in range(0, len(hash_list)):
        #     sh[i] = sh[i] + 1 if hash_list[i] == '1' else sh[i] - 1
        sh = [sh[i] + 1 if hash_list[i] == '1' else sh[i] - 1 for i in range(0, len(hash_list))]

    # sh2 = [0] * length
    # for i in range(0, len(sh)):
    #     sh2[i] = 1 if sh[i] >= 0 else 0
    # sh2 = [1 if sh[i] >= 0 else 0 for i in range(0, len(sh))]
    # sh2_string = ''.join(str(i) for i in sh2)

    # return ''.join(str(i) for i in sh2)
    return ''.join(str(i) for i in [1 if sh[i] >= 0 else 0 for i in range(0, len(sh))])


text = []
for sys_line in sys.stdin:
    text.append(sys_line)
# file = open("C:/Users/Ivan Bucic/Desktop/lab1B_primjer/test0/R.in", 'r')
# file = open("C:/Users/Ivan Bucic/Desktop/lab1B_primjer/test2/R.in", 'r')
# text = file.readlines()
# file.close()
N = int(text[0])
Q = N + 2

lines = [simHash(line.rstrip()) for line in text[1:N + 1]]
queries = [line.rstrip() for line in text[Q:]]
# print("--- %s seconds ---" % (time.time() - start_time))

candidates = {}
b = 8

for zone in range(b):
    cases = {}
    length = 16 * zone
    for current_id in range(0, N):
        hash_line = lines[current_id]
        # hash_slice = hash_line[length:length + 16]
        # hash_string = ''.join(hash_slice)
        # hash_int = int(hash_string)
        # value = int(''.join(hash_line[length:length + 16]))
        value = hash2int(zone, hash_line)

        text_case = set()
        if value in cases:
            text_case = cases.get(value)
            for text_id in text_case:
                if current_id not in candidates:
                    candidates[current_id] = []
                if text_id not in candidates:
                    candidates[text_id] = []
                candidates[current_id].append(text_id)
                candidates[text_id].append(current_id)
        else:
            text_case = set()
        text_case.add(current_id)
        cases[value] = text_case

for line in queries:

    flags = line.split(' ')
    L = int(flags[0])  # [0, N-1]
    K = int(flags[1])  # [0, 31]

    count = 0
    counted = []
    line = lines[L]
    if L >= len(candidates):
        count = 0
    else:
        for line2 in candidates[L]:
            if hammingDistance(lines[line2], line) <= K:
                if line2 not in counted:
                    counted.append(line2)
                    count += 1
    sys.stdout.write(str(count) + '\n')

# print("--- %s seconds ---" % (time.time() - start_time))
