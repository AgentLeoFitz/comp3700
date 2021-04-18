import game
import group
import user
import threading
from hashlib import sha512
import tkinter as tk
from functools import partial

def createUser(userName,password):
    userName = userName.get()
    password = password.get()
    if userName in userDatabase:
        print("USER ALREADY EXISTS")
        return False
    hashGen = sha512()
    hashGen.update(bytearray(password, encoding ='utf-8'))
    pHash = hashGen.hexdigest()
    userDatabase.update({userName:pHash})
    return True
    
class mainMenu(tk.Frame):
   inButt = None
   newButt = None

   def __init__(self, root):
      tk.Frame.__init__(self, root)
      self.root = root
      root.title("Log In")
      tk.Label(root,text="Username: ").grid(row=0,column=0)
      uname = tk.StringVar()
      unameEntry = tk.Entry(root, textvariable=uname).grid(row=0,column=1)
      
      tk.Label(root,text="Password: ").grid(row=1,column=0)
      pword = tk.StringVar()
      pwordEntry = tk.Entry(root, textvariable=pword).grid(row=1,column=1)
      
      createUserH = partial(createUser,uname,pword)
      
      self.inButt = tk.Button(root, text = 'Login', fg = 'forest green', command = yeet).grid(row=2,column=0)
      self.newButt = tk.Button(root, text = 'Create', fg = 'forest green', command = createUserH).grid(row=2,column=1)
      
      
def main():
    global allGames
    allGames = []
    global userDatabase
    
    userDatabase = dict()
    root = tk.Tk()
    box = mainMenu(root)
    box.mainloop()

if __name__ == "__main__":
    main()
