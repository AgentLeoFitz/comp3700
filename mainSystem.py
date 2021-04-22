import game
import group
import user
import threading
from hashlib import sha512
import tkinter as tk
from functools import partial


def createUser(userName, password):
    if userName in pwordDatabase:
        print("USER ALREADY EXISTS")
        return False
    hashGen = sha512()
    hashGen.update(bytearray(str(password), encoding='utf-8'))
    pHash = hashGen.hexdigest()
    pwordDatabase.update({userName: pHash})
    userDatabase.update({userName: user.__init__(userName, password)})
    return True


def logIn(userName, password):
    if userName in pwordDatabase:
        hashGen = sha512()
        hashGen.update(bytearray(password, encoding='utf-8'))
        pHash = hashGen.hexdigest()
        if pHash == pwordDatabase[userName]:
            return userDatabase[userName]
    return None


class dash(tk.Frame):
    def __init__(self, root, owner):
        tk.Frame.__init__(self, root)
        self.root = root
        root.title(owner.getName())


class mainMenu(tk.Frame):
    global pwordEntry
    global unameEntry

    def launchMenu(self):
        currentUser = logIn(self.unameEntry.get(), self.pwordEntry.get())
        newDash = dash(self, currentUser)

    def makeUser(self):
        createUser(self.unameEntry, self.pwordEntry)

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        root.title("Log In")
        tk.Label(root, text="Username: ").grid(row=0, column=0)
        username = tk.Entry(root).grid(row=0, column=1)
        self.unameEntry = username

        tk.Label(root, text="Password: ").grid(row=1, column=0)
        password = tk.Entry(root).grid(row=1, column=1)
        self.pwordEntry = password

        inButt = tk.Button(root, text='Login', fg='forest green', command=self.launchMenu).grid(row=2, column=0)
        newButt = tk.Button(root, text='Create', fg='red', command=self.makeUser).grid(row=2, column=1)


def main():
    global allGames
    allGames = []
    global pwordDatabase
    global userDatabase

    pwordDatabase = dict()
    userDatabase = dict()
    root = tk.Tk()
    box = mainMenu(root)
    box.mainloop()


if __name__ == "__main__":
    main()
