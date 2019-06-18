def solution(A):
    # write your code in Python 3.6
    numbers = set(A)
    for i in numbers:
        if A.count(i) % 2 != 0:
            return i