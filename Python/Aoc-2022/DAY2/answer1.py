strategy = open("input.txt", "r")
strategies=strategy.read().splitlines()

total= 0

for round in strategies:

    print(round)

    choose = round.split(' ')
    opponent = choose[0]
    me = choose[1]
    
   
    #For Rock
    if me == "X":
        #Opponents choose Scissors then win
        if opponent == "C":
            total+=1+6
        elif opponent == "A":
            total+=1+3
        else:
            total+=1
    #For Paper
    elif me == "Y":
        #Opponents choose Rock then win
        if opponent == "A":
            total+=2+6
        elif opponent == "B":
            total+=2+3
        else:
            total+=2
    #For Scissors
    elif me == "Z":
        #Opponents choose Paper then win
        if opponent == "B":
            total+=3+6
        elif opponent == "C":
            total+=3+3
        else:
            total+=3+0
    print(total)

print('After playing all rounds the total score is:'+ str(total))