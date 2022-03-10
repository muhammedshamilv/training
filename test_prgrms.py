import prgrms
def testSame():
    ret=prgrms.freq("aaa")
    assert ret == {"a":3}

def testMultiple():
    ret=prgrms.freq("aaabbc")
    assert ret == {"a":3,"b":2,"c":1}

def testempty():
    ret=prgrms.freq("")
    assert ret == {}

def testPanagramnot():
    assert not prgrms.panagram("qwertyuioplkjhgfdsazxcvbn")
    
def testPanagram():
    assert prgrms.panagram("qwertyuioplkjhgfdsazxcvbnm")
    
def test_average_postive():
    ret = prgrms.average([1,2,3,4,5])
    assert ret == 3

def test_average_negative():
    ret = prgrms.average([-1,-2,-3,-4,-5])
    assert ret == -3

def test_average_negative_positive():
    ret = prgrms.average([-1,2,3,4,-5])
    assert ret == 3

def test_average_none():
    ret = prgrms.average([])
    assert ret == None