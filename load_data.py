import numpy as np

data=open('some_data.csv','r')

lines=data.readlines()

line1=lines[0].split(',')

print line1

line_nums=[]
line_string=[]

#for i in line1:
#	num=int(i)
#	print num
#	line_nums.append(num)
#	line_string.append(i)


#print line_nums
#print line_string

for j in lines:
	split_line=j.split(',')
	this_line_nums=[]
	for k in split_line:
		num=int(k)
		this_line_nums.append(num)

	line_nums.append(this_line_nums)

print line_nums

median=np.median(line_nums[0])
print median
mean=np.mean(line_nums[1])
print mean

numpy_array=np.asarray(line_nums[0])

print line_nums[0]

print numpy_array



