def isleapyear(year):
    if (year % 400) == 0:
        return  True
    if (year % 100) == 0:
        return False
    if (year % 4) == 0:
        return True
    return False

def daysInMonth(year,month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 9 or month ==11 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            return 28
        else:
            return 30

#proccedure that return true if (year1,month1,day1)before(year2,month2,day2)
def dates_is_before(year1,month1,day1,year2,month2,day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2:
                return True
            if day1 == day2:
                return False

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dates_is_before(year1, month1, day1, year2, month2, day2)
    days = 0
    while dates_is_before(year1,month1,day1,year2,month2,day2):
        year1,month1,day1 = nextDay(year1, month1, day1)
        days = days + 1
    return days

#test procedure:
def test():
    assert daysBetweenDates(2013,1,1,2013,1,1) == 0
    assert daysBetweenDates(2013,1,1,2013,1,2) == 1
    assert daysBetweenDates(2013,1,1,2014,1,1) == 365
    assert daysBetweenDates(2014,1,1,2014,1,1) == 0
    assert nextDay(2013,1,1) == (2013,1,2)
    assert nextDay(2013,4,30) == (2013,5,1)
    assert nextDay(2012,12,31)== (2013,1,1)
    assert isLeapYear(2012) == True
    assert daysBetweenDates(2012,1,1,2013,1,1) == 366
    return  ("Test Finished")

print test()
