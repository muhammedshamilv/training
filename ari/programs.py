import math

def alphanumeric(p):
     if not p.isalnum():
       return False

def numbercharacters(p):
     acc=0
     for i in p:
          acc+=1
     return acc

def emptywords(p):
     if " " not in p:
          return None

def numberword(p):
     acc=0
     for i in p:
          if i ==' ':
               acc+=1
     return acc

def emptysentence(p):
     if "." or "!" or"?" not in p:
          return None    

def sentences(p):
     acc=0
     for i in p:
          if i == '!' or i == '?' or i == '.':
               acc+=1
     return acc

def ari_calculation(p):
    indexValue=math.ceil(4.71*(numbercharectors(p)/numberword(p))+0.5*(numberword(p)/sentences(p))-21.43)
    index={
          1:"5-6 Kindergarten",
          2:"6-7 First Grade",
          3:"7-8 Second Grade",
          4:"8-9 Third Grade",
          5:"9-10 Fourth Grade",
          6:"10-11 Fifth Grade",
          7:"11-12 Sixth Grade",
          8:"12-13 Seventh Grad",
          9:"13-14 Eighth Grade",
          10:'14-15 Ninth Grade',
          11:'15-16 Tenth Grade',
          12:'16-17 Eleventh Grade',
          13:'17-18 Twelfth Grade',
          14:'18-22 College student'
          }
    return index[indexValue]
