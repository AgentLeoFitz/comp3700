import game
import group
import user
from hashlib import sha512

allGames = []
userDatabase = dict()

def createUser(userName,password)
    hashGen = sha512()
    hashGen.update(password)
    hash = hashGen.hexdigest()
    userDatabase.update({userName,hash})
