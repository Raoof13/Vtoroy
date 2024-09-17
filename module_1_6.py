#Словари
my_dict = {'Илья': 2003, 'Максим': 1999, 'Сергей': 2000}
print(my_dict)

print(my_dict['Сергей']) #По существующему ключу

print(my_dict.get('Фёдор')) # По отсутствующему ключу: 1 вариант
print(my_dict.get('Фёдор', 'Нет в списке')) # 2 вариант

my_dict['Евгений'] = 1977
my_dict['Александр'] = 1974
print(my_dict)

print(my_dict.pop('Илья'))

print(my_dict)

#Множества
my_set = {10, 15, 5, 10, 5, 4, 5, 10, 5, 'Утра', True}
print(my_set)

print(my_set.add(1))
print(my_set.add('Соседи'))
print(my_set.discard('Утра'))

print(my_set)