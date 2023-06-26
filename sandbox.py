#Элементы списка проиндексированы, и вы можете получить к ним доступ, обратившись к номеру индекса:

           # -6        -5       -4       -3       -2         -1
           # 1         2         3       4        5          6
mylist = ['python', 'shit', 'bambas', 'goy', 'pidoras', 'blyadstvo']
print(mylist[1])

print('='*30)

"""Отрицательное индексирование"""

#Отрицательная индексация означает начало с конца

#-1 относится к последнему элементу, -6 относится к предпоследнему элементу и т. д.

mylist = ['python', 'shit', 'bambas', 'goy', 'pidoras', 'blyadstvo']
print(mylist[-1])

print('='*30)

"""Диапазон индексов"""

#Вы можете указать диапазон индексов, указав, где начинать и где заканчивать диапазон.

#При указании диапазона возвращаемым значением будет новый список с указанными элементами

mylist = ['python', 'shit', 'bambas', 'goy', 'pidoras', 'blyadstvo']
print(mylist[2:5])

print('='*30)

