import programs

def test_emptyString():
     ret=programs.paragraph('')
     assert ret==0
def test_alphanumeric():
     ret=programs.alphanumeric('!@#$%^')
     assert ret ==False
def test_numbercharectors():
     ret=programs.numbercharectors('shamil123')
     assert ret==9
def test_emptywords():
     ret=programs.emptywords('word')
     assert ret==None
def test_numberword():
     ret=programs.numberword('how are you')
     assert ret==2
def test_emptysentence():
     ret=programs.emptysentence('hope you are doing well')
     assert ret==None
def test_sentence():
     ret=programs.sentences('i how are you? hope you are doing well. please be careful!')
     assert ret==3