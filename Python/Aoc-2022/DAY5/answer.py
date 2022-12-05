import string


input = open("input.txt", "r")
instructions=input.read().splitlines()


map = [['Z','J','N','W','P','S'],['G','S','T'],['V','Q','R','L','H'],['V','S','T','D'],['Q','Z','T','D','B','M','J'],['M','W','T','J','D','C','Z','L'],['L','P','M','W','G','T','J'],['N','G','M','T','B','F','Q','H'],['R','D','G','C','P','B','Q','W']]


for instruction in instructions:
    
    instruction = instruction.split(" ")

    quantity = int(instruction[1])
    origin = int(instruction[3])-1
    to = int(instruction[5])-1



    map[to]+=list((map[origin][len(map[origin])-quantity:]))



    map[origin]=map[origin][:len(map[origin])-quantity]
    

last=[]
for column in map:
    last.append(column[len(column)-1])

print(last)
