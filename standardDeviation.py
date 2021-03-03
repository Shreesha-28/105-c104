import math

import csv
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#mean
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total += int(x)
    mean=total/n
    return mean

#squaring and geting the values
squared_list=[]
for number in data:
    a=(int(number)-mean(data))**2
    squared_list.append(a)
#getting sum
sum=0
for i in squared_list:
    sum+=i
    
#dividing the sum by n-1 values
result=sum/(len(data)-1)

#getting the square root to get the standard deviation
sd=math.sqrt(result)

print(sd)