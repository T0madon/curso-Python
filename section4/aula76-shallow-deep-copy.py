# Para um dicionário n alterar o outro, utilizamos um método da lib copy, o deepcopy
import copy

d1 = {
    'c1': 1,
    'c2': 2,

}
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'] = 9999999

print(d1)