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
    uTemp = user.user(userName, password)
    userDatabase.update({userName:uTemp})
    return True


def logIn(userName, password):
    if userName in userDatabase:
        hashGen = sha512()
        hashGen.update(bytearray(password, encoding='utf-8'))
        pHash = hashGen.hexdigest()
        if pHash == pwordDatabase[userName]:
            return userDatabase[userName]
        else:
            return None


class dash(tk.Frame):

    def createDash(groupName):
        group = group.__init__(groupName)
        tk.Frame.__init__(self, parentWin.root)
        self.root = tk.Tk()
        self.root.title(owner.getName())
        tk.Label(self.root,text="Admin Menu").grid(row=0, column=0)
        tk.Label(self.root, text="Player: ").grid(row=1, column=0)
        tk.Label(self.root, text="Privacy: ").grid(row=2, column=0)
        tk.Label(self.root, text="Genre: ").grid(row=3, column=0)
        tk.Label(self.root, text="Join Code: ").grid(row=4, column=0)
        tk.Label(self.root, text="Language: ").grid(row=5, column=0)
        tk.Label(self.root, text="Region: ").grid(row=6, column=0)
        player = tk.Entry(self.root)
        player.grid(row=1, column=1)
        privacy = tk.Entry(self.root)
        privacy.grid(row=2, column=1)
        genre = tk.Entry(self.root)
        genre.grid(row=3, column=1)
        joinCode = tk.Entry(self.root)
        joinCode.grid(row=4, column=1)
        language = tk.Entry(self.root)
        language.grid(row=5, column=1)
        region = tk.Entry(self.root)
        region.grid(row=1, column=1)
        inButt = tk.Button(self.root, text="Set Attributes", fg="forest green", command=group.setAttributes(player,privacy,genre,joinCode,language,region)).grid(row=2, column=0)

    def joinDash(groupName):
        return 0

    def __init__(self, parentWin, owner):
        tk.Frame.__init__(self, parentWin.root)
        self.root = tk.Tk()
        self.root.title(owner.getName())
        tk.Label(self.root,text="Group Menu").grid(row=0, column=0)
        tk.Label(self.root, text="Group Name: ").grid(row=1, column=0)
        groupName = tk.Entry(self.root)
        groupName.grid(row=1, column=1)
        inButt = tk.Button(self.root, text="Create Group", fg="forest green", command=self.createDash(str(groupName))).grid(row=2, column=0)
        newButt = tk.Button(self.root, text="Join Group", fg="red", command=self.joinDash(str(groupName))).grid(row=2, column=1)
        self.mainloop()



class mainMenu(tk.Frame):
    global pwordEntry
    global unameEntry

    def launchMenu(self):
        currentUser = logIn(self.unameEntry.get(), self.pwordEntry.get())
        newDash = dash(self, currentUser)

    def makeUser(self):
        createUser(self.unameEntry.get(), self.pwordEntry.get())

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        root.title("Log In")
        tk.Label(root, text="Username: ").grid(row=0, column=0)
        self.unameEntry = tk.Entry(root)
        self.unameEntry.grid(row=0, column=1)

        tk.Label(root, text="Password: ").grid(row=1, column=0)
        self.pwordEntry = tk.Entry(root)
        self.pwordEntry.grid(row=1, column=1)
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
