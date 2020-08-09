"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
hand = open(fname)              #abro el documento

lst = list()         #creo lista

for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])    #detecto donde estan los correos y los a;ado a la lista

counts = dict()       #creo un diccionario
for word in lst:
    counts[word] = counts.get(word,0) + 1        #empiezo a contar los correos y los a;ado al diccionario key y value
bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:           #asigno  los valores key y value mas altos encontrados en variables
        bigcount = count
        bigword = word

print (bigword,bigcount)