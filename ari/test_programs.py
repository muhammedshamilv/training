import programs

def test_numbercharectors():
     ret=programs.numbercharectors('shamil123')
     assert ret==9

def test_numberword():
     ret=programs.numberword('how are you')
     assert ret==2

def test_sentence():
     ret=programs.sentences('i how are you? hope you are doing well. please be careful!')
     assert ret==3
