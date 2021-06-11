
import copy
from functools import lru_cache


def sorted_list_merger(list_one, list_two):
    final = []
    while not ((len(list_one) == 0) and (len(list_two) == 0)):
        if len(list_one) == 0 and len(list_two) > 0:
            temp_var = list_two.pop(0)
        elif len(list_one) > 0 and len(list_two) == 0:
            temp_var = list_one.pop(0)
        else:
            if list_one[0] < list_two[0]:
                temp_var = list_one.pop(0)
            else:
                temp_var = list_two.pop(0)
        final.append(temp_var)
        print(final)
    return final


# sorted_list_merger([1, 2, 3, 4, 5],
#                    [0, 1, 4, 5, 6])

def power_set(flowers):
    fragrances = []
    fragrances.append([])

    for flower in flowers:
        fragrance = copy.deepcopy(fragrances)
        for item in fragrance:
            item.append(flower)
        fragrances = fragrances + fragrance

    print(fragrances)


# power_set([1, 2, 3, 4])


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


# g = fibonacci(5)

cached_value = {}


def fibonacci_cached(n):

    if n in cached_value:
        return cached_value[n]
    if n <= 2:
        value = n
    else:
        value = fibonacci_cached(n - 1) + fibonacci_cached(n - 2)
    cached_value[n] = value
    return value


# master fibonacci_cached

@lru_cache(maxsize=1000)
def alpha_fibonacci(n):
    if type(n) != int or n < 1:
        raise TypeError("n must be a positive integer")
    if n <= 2:
        return 1
    else:
        return alpha_fibonacci(n-1) + alpha_fibonacci(n - 2)


# for n in range(1, 51):
#     print(alpha_fibonacci(n))


def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[len(word) - 1]:
        return False
    else:
        return palindrome(word[1:-1])


# word = palindrome('racecar')

# print(word)

# recursive power set
# TODO not working
def recursive_power_set(flowers):
    frangrances = copy.deepcopy(flowers)

    for flower in flowers:
        frangrances = frangrances.remove(flower)
        frangrances = frangrances + recursive_power_set(frangrances)
        frangrances = frangrances.append(flower)
    return frangrances


# a = recursive_power_set([1, 2])


