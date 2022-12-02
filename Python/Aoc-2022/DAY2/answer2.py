strategy = open("input.txt", "r")
strategies=strategy.read().splitlines()

total= 0

for round in strategies:

    print(round)

    choose = round.split(' ')
    opponent = choose[0]
    secret = choose[1]
    
    #Loose
    if secret == "X":
        #Opponents choose Scissors then win
        if opponent == "C":
            total+=2
        elif opponent == "A":
            total+=3
        else:
            total+=1
    #Draw
    elif secret == "Y":
        #Opponents choose Rock then win
        if opponent == "A":
            total+=3+1
        elif opponent == "B":
            total+=3+2
        else:
            total+=3+3
    #Win
    elif secret == "Z":
        #Opponents choose Paper then win
        if opponent == "B":
            total+=6+3
        elif opponent == "C":
            total+=6+1
        else:
            total+=6+2
    print(total)

print('After playing all rounds the total score is:'+ str(total))