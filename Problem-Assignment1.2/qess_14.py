def testgen(index):
Weekdays=  ['sun','mon','tue','wedn','thu','fri','sat']
yield Weekdays[index]
yield Weekdays[index+1]
day = testgen(0)
print (next(day)), next(day)