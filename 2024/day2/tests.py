from challenge import get_safety, safe_reports, safe_reports2

example_data = [[int(y) for y in x.split(' ')] for x in open('example.txt').read().split('\n')]

def test_get_safety():
    assert get_safety("7 6 4 2 1".split()) == True
    assert get_safety("1 2 7 8 9".split()) == False
    assert get_safety("9 7 6 2 1".split()) == False
    assert get_safety("1 3 2 4 5".split()) == False
    assert get_safety("8 6 4 4 1".split()) == False
    assert get_safety("1 3 6 7 9".split()) == True

def test_safe_reports():
    assert safe_reports(example_data) == 2

def test_safe_reports2():
    assert safe_reports2(example_data) == 4