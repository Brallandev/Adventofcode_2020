input = open("input.txt", "r")
assigments=input.read().splitlines()

total=0
for pair in assigments:
    
    elf1=pair.split(",")[0]
    elf2=pair.split(",")[1]

    elf1_min=int(elf1.split("-")[0])
    elf1_max=int(elf1.split("-")[1])


    elf2_min=int(elf2.split("-")[0])
    elf2_max=int(elf2.split("-")[1])

    if elf1_min <= elf2_min and elf1_max >= elf2_max:
        total+=1
        continue
    elif elf2_min <= elf1_min and elf2_max >= elf1_max:
        total+=1
        continue
  
print(total)