import csv

with open('Height-Weight.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

#to pop the titles out of the list
file_data.pop(0)

#sorting data to get the height of the ppl which is in first position
new_data=[]

for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

n=len(new_data)
new_data.sort()

#using floor division to get the nearest whole number
if n%2==0:
    #getting the first number
    median1=float(new_data[n//2])
    #getting the second number
    median2=float(new_data[n//2-1])
    #getting the mean of those numbers
    median=median1+median2
else:
    median=new_data[n//2]

print("median is: "+str(median))