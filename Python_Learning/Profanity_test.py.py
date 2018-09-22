import urllib
def read_text():
    qutes = open("C:\movie_quotes.txt")
    read_content = qutes.read()
    print (read_content)
    qutes.close
    Check_Profainity(read_content)




def Check_Profainity(text_to_check):
   connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot"+text_to_check)
   output = connection.read()
   if output == "true":
       print ("Ther Is Prfent Words")
   elif output == "false":
       print ("The Is No Profent Word")
   else:
       print ("Cant Check")
   connection.close()


(read_text())
