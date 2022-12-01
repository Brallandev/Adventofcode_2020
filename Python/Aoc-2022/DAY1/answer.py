with open('input.txt') as file:
    elfs_calories = file.readlines()


max = 0
total = 0
totals=[]

for record in elfs_calories:
    if record == '\n':

        if total > max:
            max = total

        totals.append(total)
        total = 0
        continue
    
    else:
        total += int(record)
        

totals.sort(reverse=True)

#Answer for part 1
print(totals[0])

#Answer for part 2
print(totals[0]+totals[1]+totals[2])
