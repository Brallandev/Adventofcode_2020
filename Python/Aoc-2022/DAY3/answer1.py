import operator as op
import string

input = open("input.txt", "r")
ruckbacks=input.read().splitlines()

alphabet=list(string.ascii_lowercase)+list(string.ascii_uppercase)

total=0

for ruckback in ruckbacks:
    compartment1 = ruckback[:len(ruckback)//2]
    compartment2 = ruckback[len(ruckback)//2:]
    
    items1 = list(compartment1)
    items2 = list(compartment2)


    for item in items1:
        if op.countOf(items2,item) >= 1:
           total+=(alphabet.index(item))+1
           break

print(total)