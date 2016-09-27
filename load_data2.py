import numpy as np

data=open('some_data.csv','r')

lines=data.readlines()

line_nums=[]

for i in lines:
	line_split=i.split(',')
	this_line_nums=[]
	for j in line_split:
		num=int(j)
		this_line_nums.append(num)

	line_nums.append(this_line_nums)

print line_nums

array_numpy=np.asarray(line_nums[:])

print array_numpy

	
