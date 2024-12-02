data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

s = str(data_structure)
total = 0
if '35' in s:
    total += int('35')
s = s.replace('35','')
if 'Urban2' in s:
    s = s.replace('Urban2', 'Urban1')
for i in s:
    if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        total += 1
    if i in '123456789':
        total += int(i)
print(total)
