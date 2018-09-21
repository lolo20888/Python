def sort(p):
    i = 0
    while i < len(p):
        if p[i] > p[i+1]:
            p = [p[i + 1] , p[i], p[i + 2]]
            return p
print sort([5,8,6])
