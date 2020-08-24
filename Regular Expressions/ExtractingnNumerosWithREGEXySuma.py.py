import re
fname=input("Enter file name: ")
fhand=open(fname)
sum_list=[]
for line in fhand:
	if line=="":
		continue
	x=re.findall('[0-9]+' ,line)
	sum_list+=x
sum_num_list=[]
for i in sum_list:
	y=int(i)
	sum_num_list.append(y)
print(sum_num_list)
print(sum(sum_num_list))
