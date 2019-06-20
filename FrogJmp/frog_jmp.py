def solution(X, Y, D):
    div, mod = divmod((Y-X), D)
    if mod != 0:
        div += 1
    return div