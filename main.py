my_dist = {'Nikolas': 2000, 'Denis': 2001}
print('Dist: ', my_dist) # диктовать

print('Existing value: ', my_dist['Nikolas']) # Существующая стоимость
print('Not existing value: ', my_dist.get('Kamila')) # Не существующее значение
my_dist.update({'Anton': 2002,
              'Alex': 1999})
print('Deleted value: ', my_dist['Alex']) # Удалённое значение
my_dist.pop('Anton')
print("Modified dictionary: ", my_dist)# Модифицированный словарь

print()
my_set_ = {1,2,1,2,3,1,"Яблоко","Стул","Яблоко"} # Набор.
print('Set: ', my_set_)

list_= 1, 7, "Картофель"
my_set_.update(list_)
print("Modified set: ", my_set_)# Модифицированный набор
