"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
 Once 'done' is entered, print out the largest and smallest of the numbers. 
 If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
 Enter 7, 2, bob, 10, and 4 and match the output below.
"""
largest = None #flag
smallest = None #flag
while True: #programa loop infinito hasta que encuentre un break
    inp = input("Enter a number: ")
    if inp == "done" : #termino el programa
    	break
    try: #almaceno valores
        num = int(inp)
    except ValueError: #condiciona a que solo puedo ingresar numeros
        print ("Invalid input")
    else: #ya que no he terminado el programa esto simpre se ejecuta recopilando los valores mayores y menores
        
        if smallest is None: 
            smallest = num
            largest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num

print ("Maximum is", largest) #imprimo valor maximo
print ("Minimum is", smallest) #imprimo valor minimo