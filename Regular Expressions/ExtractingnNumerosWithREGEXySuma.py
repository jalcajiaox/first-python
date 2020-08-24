import re
fname=input("Enter file name: ")
fhand=open(fname)
sum_list=[]
for line in fhand:
	if line=="":       #foldear las lineas espacio hueco
		continue
	x=re.findall('[0-9]+' ,line)        #agarrar todos los numeros y agruparlos en lista
	sum_list+=x
sum_num_list=[]
for i in sum_list:                                      #sumar y que reconozca los string numero como numero
	y=int(i)
	sum_num_list.append(y)
print(sum_num_list)
print(sum(sum_num_list))
