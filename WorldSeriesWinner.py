infile = open('WorldSeriesWinners.txt','r')
infile1 = open('WorldSeriesWinners.txt','r')




output = int(input("Type in a year: "))

if output == 1994:
    print("No World Series")
elif output == 1904:
    print("No World Series")
else:

    #year[counter] = output
    winner = {}

    for line in infile:
        line = line.rstrip("\n")
        if line in winner:
            winner[line] = winner[line] + 1
        else:
            winner[line] = 1
    winner[line]
    #Print the Dictionary:
    #print(winner)

    year = {}

    counter = 1902
    for line in infile1:
        line = line.rstrip("\n")
        #counter += 1
        if counter == 1903:
            counter += 2 
            year[counter] = line
        elif counter == 1993:
            counter += 2 
            year[counter] = line
        else:
            counter += 1
            year[counter] = line
    year[counter] = line

    counter = output
    result = year[counter]
    wins = winner[result]
    print("World Series Champion:",result)
    print("Number of Championships won:", wins)

    #print year dictionary:
    #print(year)