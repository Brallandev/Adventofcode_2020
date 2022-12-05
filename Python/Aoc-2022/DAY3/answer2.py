import operator as op
import string

input = open("input.txt", "r")
ruckbacks=input.read().splitlines()

alphabet=list(string.ascii_lowercase)+list(string.ascii_uppercase)

total=0

for elfnum in range(2, len(ruckbacks),3):
    
    elf1 = list(ruckbacks[elfnum])
    elf2 = list(ruckbacks[elfnum-1])
    elf3 = list(ruckbacks[elfnum-2])

    for item in elf1:
        if op.countOf(elf2,item) >= 1:

           if op.countOf(elf3,item) >= 1:
              total+=(alphabet.index(item))+1
              break



print(total)
