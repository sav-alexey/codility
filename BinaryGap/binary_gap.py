def solution(N):
    cache = 0
    gaps = []
    bin_str = str(bin(N))[2:]
    for num in bin_str:
        if num == '0':
            cache += 1
        else:
            gaps.append(cache)
            cache = 0
    return max(gaps)