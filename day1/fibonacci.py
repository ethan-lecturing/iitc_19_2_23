def fibonacci(amount):
    lst = [0, 1]
    for i in range(amount - 2):
        lst.append(lst[-1] + lst[-2])
    return lst[:amount]


print(fibonacci(1)  )
