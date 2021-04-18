import game
import group
import user
import threading
from hashlib import sha512
import tkinter as tk

def createUser(userName,password):
    if userName in userDatabase:
        print("USER ALREADY EXISTS")
        return False
    hashGen = sha512()
    hashGen.update(bytearray(password, encoding ='utf-8'))
    pHash = hashGen.hexdigest()
    userDatabase.update({userName:pHash})
    return True

def yeet():
    print("YEEET!")
    
class mainMenu(tk.Frame):
   goButt = None
   newButt = None
   def __init__(self, root):
      tk.Frame.__init__(self, root)
      self.root = root
      root.title("Log In")
      self.inButt = tk.Button(root, text = 'Login', fg = 'forest green', command = yeet).place(relx = .5, rely = .5, anchor = 'center')
      
def main():
    global allGames
    allGames = []
    global userDatabase
    
    userDatabase = dict()
    createUser("user","secure")
    root = tk.Tk()
    box = mainMenu(root)
    box.mainloop()

if __name__ == "__main__":
    main()
