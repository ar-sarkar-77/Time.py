import time

time0=(time.strftime('%H:%M:%S'))
print("Time is:",time0)

time1=int(time.strftime('%H'))

time2=int(time.strftime('%M'))

time3=int(time.strftime('%S'))

a=str(input("Enter your name:"))

if (6<=time1<=11 and 0<=time2<=59 and 0<=time3<=59):
    print("Good Morning!",a)

elif (12<=time1<=14 and 0<=time2<=59 and 0<=time3<=59):
    print("Good Noon!",a)

elif (15<=time1<=18 and 0<=time2<=59 and 0<=time3<=59):
    print("Good Afternoon!",a)

elif (19<=time1<=20 and 0<=time2<=59 and 0<=time3<=59):
    print("Good Evening!",a)

else:
    print("Good Night!",a)