names= ('Anil', 'Amol', 'Aditya', 'Avi', 'Alka')
print(names)


names = list(names)
names.remove('Avi')
print(names)

names = tuple(names)


names_append_one = names + ('Zulu',)
print(names_append_one)
