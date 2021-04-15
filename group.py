# coding=UTF-8
from game import *
from user import *

class group(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  adminList  (private)

   

  memberList  (private)

   

  banList  (private)

   

  groupName  (protected)

   

  games  (protected)

   

  waitList  (private)

  """
  def __init__(self, nameIn):
      adminList = []
      memberList = []
      banList = []
      groupName = nameIn
      games = []
      waitList = []
      
  def _launchGame(self, gameToLaunch):
    """
     

    @param game gameToLaunch : 
    @return bool :
    @author
    """
    pass

  def _banPlayer(self, badPerson):
    """
     

    @param user badPerson : 
    @return bool :
    @author
    """
    if badPerson in memberList:
        memberList.remove(badPerson)
        banList.add(badPerson)
        return true
    else:
        return false

  def _addPlayer(self, player):
    """
     

    @param user player : 
    @return bool :
    @author
    """
    if player in waitlist:
        memberList.add(player)
        return true
    else:
        return false
    pass



