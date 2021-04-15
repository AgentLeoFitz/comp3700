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
    pass



