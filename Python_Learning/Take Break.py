import time
import webbrowser
def Takebreak():
    i = 0
    print("This Program Started On" + time.ctime())
    while i < 3:
        time.sleep(60)
        webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
        i = i + 1
Takebreak()
