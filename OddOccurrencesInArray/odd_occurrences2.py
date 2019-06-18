def solution(A):
    # write your code in Python 3.6
    dictionary = {}
    for i in A:
        if not dictionary.pop(i, None):
            dictionary.update([(i, 1)])
    return dictionary.popitem()[0]