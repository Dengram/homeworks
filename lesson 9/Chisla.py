Chisla = []
allDone = True

while allDone:
    
    consoleInput = input()
    
    if not consoleInput.lstrip("-").isnumeric():
        break

    Chisla.append(int(consoleInput))
    for i in Chisla:
        if  Chisla[len(Chisla) - 1] < 0:
            Chisla[len(Chisla) - 1] = -1
        elif  Chisla[len(Chisla) - 1] > 0:
            Chisla[len(Chisla) - 1] = 1
        elif Chisla[len(Chisla) - 1] == 0:
            Chisla[len(Chisla) - 1] = 0
print(Chisla)


        
            