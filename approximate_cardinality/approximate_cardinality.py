import random
import string

def cardinality(array):
    max_leading_zeroes = 0
    for a in array:
        binary = bin(abs(hash(a)))
        i = len(binary)-1
        while binary[i] == '0':
            i -= 1
        leading_zeroes = len(binary)-1 - i
        if leading_zeroes > max_leading_zeroes:
            max_leading_zeroes = leading_zeroes
    print("Exact distinct elements: {}".format(len(set(array))))
    print("Approx. distinct elements: {}".format(2**max_leading_zeroes))

# -----------------------------------------------
nums = [1, 2, 2, 3, 3, 3, 4, 5]
cardinality(nums)
print()

lower_bound = random.randint(0, 10000)
upper_bound = random.randint(lower_bound, lower_bound + 10000)
nums = [random.randint(lower_bound, upper_bound) for i in range(10)]
cardinality(nums)
print()


strings = []
for i in range(10000):
    chars = random.choices(string.ascii_uppercase + string.digits, k=10)
    s = ''.join(chars)
    strings.append(s)
cardinality(strings)