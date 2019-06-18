def find_unpaired(dictionary):
    for key, value in dictionary.items():
        if value %2 != 0:
            return key

def solution(A):
    # write your code in Python 3.6
    keys = set(A)
    dictionary = dict.fromkeys(keys, 0)
    for idx, num in enumerate(A):
        dictionary[num] += 1
    return find_unpaired(dictionary)