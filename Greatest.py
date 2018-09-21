def sort(p):
    list_sort = p.sort()
    return (p)

def max_value(c):
     sort_list = sort(c)
     return max(c,default = 0)

def greatest(d):
    i = 0
    sort_list = sort(d)
    result = max_value(d)
    while i < len(d):
        if sort_list:
            return result
        else:
            return all(d)
    i = i + 1

    

def test():
    assert sort([4,23,1]) == [1,4,23],"Not Sorted"
    assert max_value([4,23,1]) == 23,"Not Max Value"
    assert greatest([4,23,1]) == 23 ,"Not THe Greatest"
    assert greatest([]) == 0 ,"Not THe Greatest"
    


print (greatest([4,23,1]))
print (greatest([]))
print (test())





