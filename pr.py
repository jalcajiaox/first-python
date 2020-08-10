"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
"""
name = input("Enter file:")

handle = open(name)
d=dict()														#abro documento 
for line in handle:
    if not line.startswith("From "): 
        continue
    else:    
        line=line.split()				#Si comienza con from encuentro linea en la posicion 5, analizo del 0 al 2 y sumo key y value en diccionario
        line=line[5]                  
        line=line[0:2]
        d[line]=d.get(line,0)+1

lst=list()        
for value,count in d.items():        #apunto al diccionario y disparo la informacion a la lista con append y for
    lst.append((value,count))

lst.sort()
for value,count in lst:            #finalmente imprimo los valores de la lista en forma de strings
    print (value,count)

