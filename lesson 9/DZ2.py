a = [12, 23, 5, 78, 66, 100, 99]
result = []

while len(a) > 0:
    result.append(max(a))
    a.remove(max(a))

string = ''.join([str(x) for x in result])
print(string)

