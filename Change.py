def change(p):

   print("please Add The Name")
   inp =input()
   if inp == "" :
        i = 0
        while i < 4:
           print("please Add The Name")
           input() 
           i = i + 1
        return "You Have Exxeded The Number Of Trails"   
   else:
        p.append(inp)
        convert_string = ' '.join(p)
        return convert_string


print(change(["mina"]))
