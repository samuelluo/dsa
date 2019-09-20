import random
import string
import time


def cardinality(array):
    start_time = time.time()
    exact = len(set(array))
    end_time = time.time()
    time_elapsed = end_time - start_time
    print("{} | Exact distinct elements: {}".format(time_elapsed, exact))

    start_time = time.time()
    max_leading_zeroes = 0
    for a in array:
        binary = bin(abs(hash(a)))
        i = len(binary)-1
        while binary[i] == '0':
            i -= 1
        leading_zeroes = len(binary)-1 - i
        if leading_zeroes > max_leading_zeroes:
            max_leading_zeroes = leading_zeroes
    end_time = time.time()
    time_elapsed = end_time - start_time
    approx = 2**max_leading_zeroes
    print("{} | Approx. distinct elements: {}".format(time_elapsed, approx))


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 3, 3, 4, 5]
    cardinality(nums)
    print('')

    lower_bound = random.randint(0, 10000)
    upper_bound = random.randint(lower_bound, lower_bound + 10000)
    nums = [random.randint(lower_bound, upper_bound) for i in range(10)]
    cardinality(nums)
    print('')

    strings = []
    for i in range(1000000):
        chars = random.choices(string.ascii_uppercase + string.digits, k=10)
        s = ''.join(chars)
        strings.append(s)
    cardinality(strings)
