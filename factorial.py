import sys
import math
from sys import setrecursionlimit
from decimal import Decimal, getcontext

setrecursionlimit(1000000)


def get_input_sen():
    try:
        n_remain_cases = int(input())
    except:
        n_remain_cases = 0

    inputs = []
    while n_remain_cases > 0:
        n_integer, n_prime = input().split(" ")
        n_integer = int(n_integer)
        n_prime = int(n_prime)
        inputs.append((n_integer, n_prime))
        n_remain_cases -= 1
    return inputs


# Utility function to do modular
def __gcd(a, b):
    if (b == 0):
        return a
    else:
        return __gcd(b, a % b)

    # To compute x^y under modulo m


def power(x, y, m):
    if (y == 0):
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m

    return p if (y % 2 == 0) else (x * p) % m


# Function to find modular inverse
# of a under modulo p using Fermat's
# method. Assumption: p is prime
def modInverse(a, p):
    return power(a, p - 2, p)


# Returns n! % p using
# Wilson's Theorem
def modFact(n, p):
    # n! % p is 0 if n >= p
    if (p <= n):
        return 0

    # Initialize result as (p-1)!
    # which is -1 or (p-1)
    res = (p - 1)

    # Multiply modulo inverse of
    # all numbers from (n+1) to p
    for i in range(n + 1, p):
        res = (res * modInverse(i, p)) % p
    return res


def calc_answer(n_integer, n_prime):
    if n_integer == 1:
        return 1
    if n_integer % n_prime == 0:
        return 0
    return n_integer * calc_answer(n_integer - 1, n_prime) % n_prime


def calc_answer_flat(n, p):
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % p
    return res


def calc_answer2(n_integer, n_prime):
    if n_integer > n_prime:
        return 0

    if n_integer == 1:
        return 1

    if n_integer == 2:
        return 2 % n_prime

    return ((n_integer * (n_integer - 1) % n_prime) * calc_answer2(n_integer - 2, n_prime)) % n_prime


def calc_answer3(n, p):
    if n == 1:
        return 1
    if n % p == 0:
        return 0
    if n // p == 0:
        return n * calc_answer3(n - 1, p) % p
    return calc_answer3(n // p, p)


def calc_answer_core(list_n, i, p):
    if list_n[i] > p:
        return 0

    if list_n[i] == 1:
        return 1

    if list_n[i] == 2:
        return 2 % p

    res = 1
    while res < p and i < len(list_n):
        res *= list_n[i]
        i += 1

    left = res % p

    if i < len(list_n):
        right = calc_answer_core(list_n, i, p)
    else:
        right = 1

    return (left * right) % p


def calc_answer4(n_integer, n_prime):
    list_n = list(range(n_integer, 0, -1))
    return calc_answer_core(list_n, 0, n_prime)


def process(inputs):
    res = []
    for n_integer, n_prime in inputs:
        res.append(calc_answer4(n_integer, n_prime))
    return res


def print_result(res):
    for r in res:
        print(r)


def print_true(inputs):
    print("true: ")
    for n, p in inputs:
        print(math.factorial(n) % p)
    print("-----")


if __name__ == "__main__":
    inputs = get_input_sen()
    #inputs = [(2, 5), (5, 11), (21, 71), (8, 97), (96, 97)]
    # print_true(inputs)

    res = process(inputs)
    print_result(res)
