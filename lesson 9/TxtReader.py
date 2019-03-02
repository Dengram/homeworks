file = open('person.txt', 'r', encoding = 'utf-8')
person = {}

i = 0
for line in file:
    line = line.replace(',', "")
    line = line.replace('"', "")
    line = line.replace('firstName', "")
    line = line.replace('lastName', "")
    line = line.replace(':', "")
    
    if i == 0:
        person["fistName"] = line
    elif i == 1:
        person["lastName"] = line

    i += 1

print(person)