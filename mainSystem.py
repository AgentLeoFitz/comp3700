import game
import group
import user
from hashlib import sha512

def main():
    global allGames
    allGames = []
    global userDatabase
    userDatabase = dict()
    createUser("user","secure")

def createUser(userName,password):
    if userName in userDatabase:
        print("USER ALREADY EXISTS")
        return False
    hashGen = sha512()
    hashGen.update(password)
    hash = hashGen.hexdigest()
    userDatabase.update({userName,hash})
    return True
