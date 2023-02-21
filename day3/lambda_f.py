import random



lst = [random.randint(1, 10) for i in range(20)]
print(lst)
lst2= list(map(lambda x: x * 2, lst))
print(lst2)
