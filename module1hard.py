grades = [5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
per_student = {}
students1 = sorted(students)
average = [((sum(grades[0])) / len(grades[0])),
           ((sum(grades[1])) / len(grades[1])),
           ((sum(grades[2])) / len(grades[2])),
           ((sum(grades[3])) / len(grades[3])),
           ((sum(grades[4])) / len(grades[4]))]
per_student = zip(students1, average)
print(dict(per_student))

#еще нагуглил решение через for
#for a in range(0, 5):
 #   key = students1[a]
  #  value = average[a]
   # per_student[key] = value
#но пока не очень разобрался, как именно этот цикл работает