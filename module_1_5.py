immutable_var = 1, 2, 3, 4, "Raoof", True
print(immutable_var)

# immutable_var[2] = 7
# print(immutable_var) #Ошибка TypeError: 'tuple' object does not support item assignment говорит о невозможности переназначения элементов

mutable_list = [5, 8, 13, 21, 34]
mutable_list[4] = 'vote' # меняем 34 на vote
print(mutable_list)