def change_capital_to_small(s):
    char = 0
    while char < len(s):
        if s[char] == s[char].upper():
            char = char + 1
    return char

print change_capital_to_small("Mina Remon")
