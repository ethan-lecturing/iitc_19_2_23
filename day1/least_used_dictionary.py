class LeastUsedDictionary:
    def __init__(self, maximal_amount):
        self.maximal_amount = maximal_amount
        self.inner_dict = {}
        self.counts = {}

    def get(self, key):
        self.counts[key] += 1
        return self.inner_dict[key]

    def set(self, key, value):
        if len(self.inner_dict) >= self.maximal_amount:
            min_key = ''
            min_value = 1000000
            for key, count in self.counts.items():
                if count < min_value:
                    min_value = count
                    min_key = key
            del self.counts[min_key]
        self.inner_dict[key] = value
        self.counts[key] = 0

    def __len__(self):
        return len(self.inner_dict)

    def __str__(self):
        return str(self.inner_dict)


d = LeastUsedDictionary(10)
d.set('Hello', 5)
d.set('bli bla', 444)
d['hello'] = 5
print(len(d))
print(d)
