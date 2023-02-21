import random



lst = [random.randint(1, 10) for i in range(20)]
new_lst = []
print(lst)
print(list(map(lambda x: x * 2, lst)))
