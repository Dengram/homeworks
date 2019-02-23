text = input().split()
result = []
imax = 0

for j in range(0, len(text)):
    for i in range(0, len(text) - 1):
        if len(text[imax]) < len(text[i]):
            imax = i
            result.append(text[imax])

        print(text)
           

        

        

