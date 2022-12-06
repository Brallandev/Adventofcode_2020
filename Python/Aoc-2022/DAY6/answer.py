with open('input.txt') as file:
    downstream = file.read()

#how many distinct characters has start-of-message marker
extend_marker=14

for i in range(0,len(downstream)):

    possible_marker = set(downstream[i:i+extend_marker])
    
    if len(possible_marker) == extend_marker:
        print(i+extend_marker)
        break