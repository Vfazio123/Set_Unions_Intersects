'''
Vincent Fazio
Discrete Structures
02/14/20
Assignment 2
   This program takes two inputs, and figures the intersect, union, disjoint, and Cartesian Project of them.
   It also displayes the Cardinality of the Sets that are in use.
   
NOTE: In order to run the program you must include the file names during compiling. 
   
      EX: python3 Sets_Union_Disjoint_etc.py FileA.txt FileB.txt FileC.txt   
 
     This is because the files are read in through CLI
         
      ALSO Set() = empty set, this this result when an intersect is performed and there are no matches.

'''
from sys import argv
from itertools import product

with open(argv[1], 'r') as file:
   Afile = "".join(line.rstrip() for line in file)       #Takes file input, creates a list of strings
   Afile = Afile.split(", ")                             #Splits them at ', ' meaning no ',' and ' '
   Acount = len(Afile)                                   #Finds cardinality of the set(#of elements)
   Afile = {*(Afile)}                                    #Turn into set
with open(argv[2], 'r') as file:
   Bfile = "".join(line.rstrip() for line in file)
   Bfile = Bfile.split(", ")
   Bcount = len(Bfile)
   Bfile = {*(Bfile)}
with open(argv[3], 'r') as file:
   Cfile = "".join(line.rstrip() for line in file)
   Cfile = Cfile.split(", ")
   Ccount = len(Cfile)
   Cfile = {*(Cfile)}
   
print("\nA:",Afile)
print("B:",Bfile)
print("C:",Cfile)

print("\nOperations: union, intersect, product")
print("\nExample: A union B")
exp = input("Enter Two of the Three Sets Seperated by an operation\n>")


#Spliting User Input
for i in range(2):
   Nexp = exp.split()

#Displaying Cardinality
print("\nCardinality of Set A:", Acount)
print("Cardinality of Set B:", Bcount)
print("Cardinality of Set C:", Ccount)
print("")

productset = []

#Unions and Intersections, all possible combinations
if ((Nexp[0] == 'A' and Nexp[2] == 'B') or (Nexp[0] == 'B' and Nexp[2] == 'A')) and (Nexp[1] == 'union'):
   print(Afile | Bfile)
elif(Nexp[1] == 'intersect') and ((Nexp[0] == 'A' and Nexp[2] == 'B') or (Nexp[0] == 'B' and Nexp[2] == 'A')):
   print(Afile & Bfile)
elif(Nexp[1] == 'product') and ((Nexp[0] == 'A' and Nexp[2] == 'B') or (Nexp[0] == 'B' and Nexp[2] == 'A')):
   for p in product(Afile, Bfile):
      productset.append(p)
   print(set(productset))

if ((Nexp[0] == 'A') and (Nexp[1] == 'union') and (Nexp[2] == 'A')):
   print(Afile | Afile)
elif(Nexp[1] == 'intersect') and (Nexp[0] == 'A') and (Nexp[2] == 'A'):
   print(Afile & Afile)
elif(Nexp[1] == 'product') and ((Nexp[0] == 'A') and (Nexp[2] == 'A')):
   for p in product(Afile, Afile):
      productset.append(p)
   print(set(productset))

if ((Nexp[0] == 'A' and Nexp[2] == 'C') or (Nexp[0] == 'C' and Nexp[2] == 'A')) and (Nexp[1] == 'union'):   
   print(Afile | Cfile)   
elif ((Nexp[1] == 'intersect') and ((Nexp[0] == 'A' and Nexp[2] == 'C') or (Nexp[0] == 'C' and Nexp[2] == 'A'))):
   print(Afile & Cfile)
elif ((Nexp[1] == 'product') and ((Nexp[0] == 'A' and Nexp[2] == 'C') or (Nexp[0] == 'C' and Nexp[2] == 'A'))):
   for p in product(Afile, Cfile):
      productset.append(p)
   print(set(productset))

if ((Nexp[1] == 'union') and ((Nexp[0] == 'B' and Nexp[2] == 'C') or (Nexp[0] == 'C' and Nexp[2] == 'B'))):
   print(Bfile | Cfile)
elif ((Nexp[1] == 'intersect') and ((Nexp[0] == 'B' and Nexp[2] == 'C') or (Nexp[0] == 'C' and Nexp[2] == 'B'))): 
   print(Bfile & Cfile)
elif ((Nexp[1] == 'product') and ((Nexp[0] == 'B' and Nexp[2] == 'C') or (Nexp[0] == 'C' and Nexp[2] == 'B'))):
   for p in product(Bfile, Cfile):
      productset.append(p)
   print("d",set(productset))


if ((Nexp[1] == 'union') and (Nexp[2] == 'B') and (Nexp[0] == 'B')):
   print(Bfile | Bfile)
elif ((Nexp[1] == 'intersect') and (Nexp[0] == 'B') and (Nexp[2] == 'B')):
   print(Bfile & Bfile)
elif (Nexp[1] == 'product') and ((Nexp[0] == 'B') and (Nexp[2] == 'B')):
   for p in product(Bfile, Bfile):
      productset.append(p)
   print(set(productset))   


if ((Nexp[1] == 'union') and (Nexp[0] == 'C') and (Nexp[2] == 'C')):
   print(Cfile | Cfile)
elif ((Nexp[1] == 'intersect') and (Nexp[0] == 'C') and (Nexp[2] == 'C')):
   print(Cfile & Cfile)
elif (Nexp[1] == 'product') and ((Nexp[0] == 'C') and (Nexp[2] == 'C')):
   for p in product(Cfile, Cfile):
      productset.append(p)
   print(set(productset))  
