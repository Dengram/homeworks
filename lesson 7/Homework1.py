import random
import Homework2

firstName = ['Глеб', 'Никита', 'Даниил']
lastName = ['Булдыгин', 'Ляшевич', 'Бухтояров']
age = [16, 20, 22]
job = ['ресэйлер', 'програмист', 'учитель']
language = ['английский', 'французский', 'китайский']

for i in range(3):
    person = {
        'firstName': firstName[random.randint(0, 2)],
        'lastName': lastName[random.randint(0, 2)],
        'age': age[random.randint(0, 2)],
        'job': job[random.randint(0, 2)],
        'language': language[random.randint(0, 2)],
        'language': [language[random.randint(0, 2)],language[random.randint(0, 2)]]
    }
    Homework2.checkUser(person)
    