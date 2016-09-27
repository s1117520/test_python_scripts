import numpy as np

data=open('some_data.csv','r')
more_data=open('some_more_data.csv','r')

def loading_data(data):
	lines=data.readlines()
	num_lines=[]
	for i in lines:
	        line=i.split(',')
		this_line_nums=[]
		for j in line:
			num=int(j)
			this_line_nums.append(num)

		num_lines.append(this_line_nums)

	numpy_array=np.asarray(num_lines)
	print numpy_array
	

loading_data(more_data)
loading_data(data)






