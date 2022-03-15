import postfix

def testnonoperator():
    ret = postfix.postfix("1234")
    assert ret == 1

def testonly_operents():
    ret = postfix.postfix("/*-+*-/-/-+")
    assert ret == "invalid expression"

def testmore_operents():
    ret = postfix.postfix("123/*-+*-/-/-+")
    assert ret == "invalid expression"

def test_normalcalculation():
    ret = postfix.postfix("12345+-*/")
    assert ret == 12

