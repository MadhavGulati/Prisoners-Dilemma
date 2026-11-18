import random

def play(history=None):
    return random.choice("CD")


# verifying that the output is truly random


# c_num = 0
# d_num = 0
# total = 0

# for n in range(10000000):
#     result = play()
#     if result == "C":
#         c_num += 1
#     elif result == "D":
#         d_num += 1
#     total += 1

# print("c:", c_num)
# print("d:", d_num)
# print("total:", total)
# print("c ratio", c_num/total)

#   example output:
            # c: 5001034
            # d: 4998966
            # total: 10000000
            # c ratio 0.5001034