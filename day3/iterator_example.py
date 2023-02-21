class MyNumbers:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def bla(self):
        print('woho')

    def __next__(self):
        self.count += 1  # self.count = self.count +1
        if self.count >= 15:
            raise StopIteration()
        return self.count


# class List:
#     def __init__(self):
#         self.lst = []
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current == len(self.lst) - 1:
#             return 5
#         self.current += 1
#         return self.lst[self.current]


# def for_loop(iterable):
#     iterator = iter(iterable)
#     while True:
#         next(iterator)

m = MyNumbers()


