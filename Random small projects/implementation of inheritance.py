class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print(f"Name: {lastName}, {firstName}")
        print(f"ID: {idNum}")


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = []

        Person.__init__(self, firstName, lastName, idNumber)

    def calculate(self):
        score = ''
        avg = sum(scores) / len(scores)

        if 90 <= avg <= 100:
            score = 'O'

        elif 80 <= avg < 90:
            score = 'E'

        elif 70 <= avg < 80:
            score = 'A'

        elif 55 <= avg < 70:
            score = 'P'

        elif 40 <= avg < 55:
            score = 'D'

        else:
            score = 'T'

        return score


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
num_score = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
