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

#getting the mean
n=len(new_data)
total=0
for x in new_data:
    total+=x
mean=total/n

print("mean is: "+str(mean))