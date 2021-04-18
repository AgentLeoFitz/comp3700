# coding=UTF-8
from group import *

class game(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   
  name   (protected)
  genre  (protected)

  """
  def __init__(self, nameIn, genreIn):
    global name
    global genre
    global players
    name = nameIn
    genre = genreIn
    players = []
    
  def start(self):
    """
     

    @return bool :
    @author
    """
    pass

  def addPlayers(self, playerList):
    """
     

    @param list playerList : 
    @return bool :
    @author
    """
    players.add(playerList)

  def endGame(self):
    """
    

    @return bool :
    @author
    """
    pass


