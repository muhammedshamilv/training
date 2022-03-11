def paragraph(p):
    if bool(p) == False:
        return 0

def alphanumeric(p):
     if not p.isalnum():
       return False

def numbercharectors(p):
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