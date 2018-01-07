from collections import namedtuple

n = int(input().strip())
student = namedtuple('student', input().split())

students = []
for i in range(n):
    students.append(student(*input().split()))

sum = 0
for student in students:
    sum += int(student.MARKS)

print("{:.2f}".format(sum/n))
