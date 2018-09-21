def change(p):
    i = 0
    new_list = []
    while i < len(p):
        if p[i] == "r":
            new_list = p[i].replace("r", "z")
        i = i + 1
    return new_list


print(change(['mina', 'shaker']))
