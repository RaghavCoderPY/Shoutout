from os import system
from sys import platform
# import win32com.client as wincom # For Windows

# speak = wincom.Dispatch("SAPI.SpVoice") # For Windows

l = ["Rahul", "Nishant", "Harry"]
for i in l:
    if platform == "darwin" or platform == "linux":
        system(f"say Shoutout to {i}")
    else:
        # For Windows
        # text = f"shoutout to {i}"
        # speak.Speak(text)
        print(f"Shoutout to {i}")

