import datetime

currentDate = datetime.date.today()

print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

print(currentDate.strftime('%d %b, %Y'))

print(currentDate.strftime('Event on %A, %B %d year %Y'))

birthday = input("Birthday dd/mm/yyyy\n")
birthdate = datetime.datetime.strptime(birthday, "%d/%m/%Y").date() #input format is 01 jan, 1990

difference =  currentDate-birthdate
print(difference.days)

currentTime = datetime.datetime.now()
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)
print(datetime.datetime.strftime(currentTime, "%H:%M"))