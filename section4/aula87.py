lista = ['a', 1, 1.1, True, [0,1,2], (1,2), 
         {0,1}, {'Nome': 'João'},
         ]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item,set))

    if isinstance(item, str):
        item.upper()
        print(item)

    if isinstance(item, (int,float)):
        print(item, item *2)