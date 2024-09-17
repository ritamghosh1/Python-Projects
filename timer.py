import time
timestamp =int( time.strftime("%H"))
print(timestamp)
timestamp2 = time.strftime("%H:%M:%S")
print("Now the time is",timestamp2)
if(timestamp<=10):
     print("Good Morning sir . Hope you have a great day")
elif(timestamp<=17):
     print("Good Afternoon sir . Wish you had a great day")
elif(timestamp<=21):
     print("Good Evening sir . Have a great night")
else: print("Good Night sir . All the best for Tommorow")
