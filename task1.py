##edwin ng'era
import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
       
belowFive = [i for i in ourList if i<5]
print(ourList)
print(belowFive)
