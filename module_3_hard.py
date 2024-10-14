def calculate_structure_sum(data_structure):
    summa = 0
    if data_structure == []:
        return summa
    if isinstance(data_structure, str):
        summa += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
    elif isinstance(data_structure, dict):
        summa += calculate_structure_sum({*data_structure.items()})
    elif isinstance(data_structure, (tuple, list, set)):
        for i in data_structure:
            summa += calculate_structure_sum(i)
    return summa

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
