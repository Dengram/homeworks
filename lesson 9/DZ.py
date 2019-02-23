my_file = open('some.txt', 'w')
a = [input()]
while a[len(a) - 1] != 'выход':
    a.append(input()) 
else:
    string = '\n'.join([str(x) for x in a])
    print(string)
my_file.write(string)
my_file.close()
