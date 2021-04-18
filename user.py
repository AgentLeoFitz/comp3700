# coding=UTF-8
import group
class user(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  username  (protected)

   

  password  (private)

  """
  def __init__(self, nameIn, passwordIn):
    global username
    global password
    
    username = nameIn
    password = passwordIn

  def getName(self):
    return username
