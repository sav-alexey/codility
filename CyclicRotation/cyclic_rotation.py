from collections import deque


def solution(A, K):
    dq = deque(A)
    for i in range(1, K+1):
        cache = dq.pop()
        dq.appendleft(cache)
    return list(dq)