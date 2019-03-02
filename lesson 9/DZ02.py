import random
import DZ03

firstName = ['Пётр', 'Леонид', 'Максим']
lastName = ['Одинцов', 'Петров', 'Смирнов']
age = [16, 20, 22]

for i in range(1):
    person = {
    'firstName': firstName[random.randint(0, 2)],
    'lastName': lastName[random.randint(0, 2)],
    'age': age[random.randint(0, 2)]
    }
    DZ03.infoPerson(person)
    