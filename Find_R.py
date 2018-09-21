def find_r(s):
    sub = "r"
    i = 0
    t = len(s)
    while i < len(s):
        if sub:
            r = s.count(sub, 0, t)
        return r
    
    i += 1


print(find_r('''Welcome to the LearnPython.org interactive Python tutorial.

Whether you are an experienced programmer or not, this website is intended for everyone who wishes to learn the Python programming language.

You are welcome to join our group on Facebook for questions, discussions and updates.

Just click on the chapter you wish to begin from, and follow the instructions. Good luck!'''))
