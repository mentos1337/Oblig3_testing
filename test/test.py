from Kalender import isLeapYear

def test_is_divisible_by_4_but_not_100():
    assert isLeapYear(1240) == True

def test_is_divisible_by_400():
    assert isLeapYear(400) == True

def test_is_divisible_by_4_or_400():
    assert isLeapYear(2000) == True

def test_is_not_divisible_by_4():
    assert isLeapYear(2111) == False

def test_is_divisible_by_100_not_div_by_400():
    assert isLeapYear(100) == False

def test_is_not_a_leap_year():
    assert isLeapYear(1700) == False
