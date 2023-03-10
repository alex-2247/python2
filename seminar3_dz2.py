'''✔ В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку.'''

# str1 = "qqq www eee rrr qqq eee rrr eee ttt"
str0 = "List, список является самой часто используемой коллекцией в Python. " + \
"Прежде чем говорить о списках, я напомню, что такое массив в информатике. " + \
"Массив - это непрерывная область в оперативной памяти компьютера, поделённая " + \
"на ячейки одинакового размера хранящие данные одного типа. Массивы могут быть " + \
"статическими, то есть размер массива нельзя изменить, и динамическими, когда " + \
"размер массива изменяется при добавлении или удалении элементов. Один из " + \
"самых больших плюсов в работе с массивами — это доступ к любой из его ячеек " + \
"за константное время. Массив — упорядоченный набор элементов, каждый из которых " + \
"хранит одно значение, идентифицируемое с помощью одного или нескольких индексов. В " + \
" простейшем случае массив имеет постоянную длину и хранит единицы данных одного " + \
"и того же типа, а в качестве индексов выступают целые числа. В информатике, " + \
"список (англ. list) — это абстрактный тип данных, представляющий собой " + \
"упорядоченный набор значений, в котором некоторое значение может встречаться " + \
"более одного раза. Экземпляр списка является компьютерной реализацией " + \
"математического понятия конечной последовательности. Экземпляры значений, " + \
"находящихся в списке, называются элементами списка (англ. item, entry либо " + \
"element); если значение встречается несколько раз, каждое вхождение считается " + \
"отдельным элементом."
str1 = str0.lower().replace('.', '').replace(',', '')\
    .replace('(', '').replace(')', '').replace('—', '').replace(';', '')
list1 = str1.split()
my_dict = {}

for item in list1:
    my_dict.setdefault(item, 0)
    my_dict[item] = my_dict[item] + 1

# Чтобы отсортировать словарь (а без этого задача не решается), пришлось
# гуглить и применять функционал, выходящий за рамки этого урока - а именно
# лямбда-функцию. Другие способы еще более далекие, или требуют импорта.
sort_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
result_list = sort_list[:10]

for item in result_list:
    print(f'Слово "{item[0]}" встречается в тексте {item[1]} раза')
