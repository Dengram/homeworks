import random

class Person:
    firstName = 'Петя'
    lastName = 'Петров'
    age = '17'

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self):
        return 'Имя ' + str(self.firstName) + 'Фамилия ' + str(self.lastName) + 'Возраст ' + str(self.age)

person1 = ('Петя', 'Петров', '17')

fraza1 = 'Програмирование - моё всё'
fraza2 = 'Блин, через 10 минут придёт Вова, а я определения не записал'
fraza3 = 'Не зделаю дз, Вова скажет папе, мне хана'
fraza = random.randomint(fraza1, fraza2, fraza3)

print(person1)
print('Любимые фразы: ' + fraza)

