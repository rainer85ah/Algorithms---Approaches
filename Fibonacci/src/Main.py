import numpy as np
"""
Algorithm: Fibonacci. Approaches: Recursion, Tail, Recursion, Iterative, Dynamic.
"""


def fibonacci_iterative(n):
    """
    iterative approach.
    :param n: Integer
    :return: Integer: Fibonacci number of the input n.
    """
    ant, next, result = 0, 1, 0
    for i in range(n-1):
        result = ant + next
        ant = next
        next = result

    return result

# print fibonacci_iterative(5)


def fibonacci_recursion(n):
    """
    Recursion approach. Multiple case Recursion. Complexity: O(2^N)
    :param n: Integer
    :return: Integer: Fibonacci number of the input n.
    """
    if n in [0, 1]:
        return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

#  print fibonacci_recursion(5)


def fibonacci_tail_recursion(n):
    """
    Tail Recursion approach. Multiple case Recursion. Complexity: O(2^N)
    :param n: Integer
    :return: Integer: Fibonacci number of the input n.
    """
    if n in [0, 1]:
        return n
    return fibonacci_tail_recursion_aux(n, 1, 0, 1, 0)


def fibonacci_tail_recursion_aux(n, i, prev, next, result):
    if i == n:
        return result
    else:
        return fibonacci_tail_recursion_aux(n, i+1, next, prev+next, prev+next)

# print fibonacci_tail_recursion(5)

store_dict = dict()
store_dict[0] = 0
store_dict[1] = 1


def fibonacci_dynamic(n):
    """
    Dynamic Programming approach.
    :param n: Integer
    :return: Integer: Fibonacci number of the input n.
    """
    if n in [0, 1]:
        return store_dict[n]

    if (n-1) not in store_dict.keys():
        store_dict[n-1] = fibonacci_dynamic(n-1)

    store_dict[n] = store_dict[n-1] + store_dict[n-2]
    return store_dict[n]

print fibonacci_dynamic(5)

np.save('../output/fibonacci_999_numbers.npy', store_dict)
store_dict = np.load('../output/fibonacci_999_numbers.npy').item()
store_dict = dict(store_dict)
print store_dict.keys(), store_dict.values()
