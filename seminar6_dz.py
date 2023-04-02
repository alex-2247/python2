from package6.mystery import one_myst
from package6.mystery import myst_serial
from package6.date_check import dchk


print(f'Задача 1:   {one_myst.__doc__}\n')
print(f'Задача 2:   {myst_serial.__doc__}\n')
print(f'Задача 3:   {dchk.__doc__} \n' \
      '    (реализована в виде проверки тестового набора)')
my_choice = int(input("\nВведите номер задачи:  "))


if my_choice == 1:
    print(one_myst('Зимой и летом одним цветом', \
                   ['Елка', 'Ель', 'Елочка'], 3))
elif my_choice == 2:
    myst_serial()
else:
    print("01.01.0001", "  ", dchk("01.01.0001"))
    print("24.02.2022", "  ", dchk("24.02.2022"))
    print("29.02.2020", "  ", dchk("29.02.2020"))   # Високосный
    print("29.02.2023", "  ", dchk("29.02.2023"))   # Не високосный
    print("32.13.0000", "  ", dchk("32.13.0000"))
