import hashlib
import sys
# import time

# start_time = time.time()


def hammingDistance(string1, string2):
    difference = 0
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            difference += 1

    return difference


def hamming_distance(string1, string2):
    return sum(c1 != c2 for c1, c2 in zip(string1, string2))


def countDifference(text_lines, i, k):
    diff_count = 0
    line = text_lines[i]
    for line2 in lines:
        if hammingDistance(line2, line) <= k:
            diff_count += 1
    return diff_count


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


# line = "fakultet elektrotehnike i racunarstva"
# simh = simHash(line)
# print(simh)
# print(hex(int(simh, 2))[2:])

# text = []
# for sys_line in sys.stdin:
#     text.append(sys_line)
# text = [line for line in sys.stdin]
file = open("C:/Users/Ivan Bucic/Desktop/test2/R.in", 'r')
text = file.readlines()
file.close()
N = int(text[0])
Q = N + 2

lines = [simHash(line.rstrip()) for line in text[1:N + 1]]
ques = [line.rstrip() for line in text[Q:]]
# print("--- %s seconds ---" % (time.time() - start_time))

for Q in ques:
    flags = Q.split(' ')
    L = int(flags[0])  # [0, N-1]
    K = int(flags[1])  # [0, 31]

    # count = countDifference(lines, int(flags[0]), int(flags[1]))
    count = countDifference(lines, L, K) - 1
    sys.stdout.write(str(count) + '\n')

# print("--- %s seconds ---" % (time.time() - start_time))
