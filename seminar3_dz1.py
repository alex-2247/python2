'''✔ Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.'''

my_list = [1, 2, 3, 5, 2, 13, 1, 13, 4, 2]
res_list = []

for item in my_list:
    if my_list.count(item) > 1 and item not in res_list:
        res_list.append(item)

print(res_list)
