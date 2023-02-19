class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.validate()

    def validate(self):
        if self.day > 30 or self.day < 1:
            raise ValueError('The day is invalid')
        elif self.month > 12 or self.month < 1:
            raise ValueError('The month is invalid')

    # Returns True if self is later than other,
    # otherwise false
    def older_than(self, other):
        other_tup = (other.year, other.month, other.day)
        self_tup = (self.year, self.month, self.day)
        return self_tup < other_tup

    def increment_days(self, days):
        initial_days = self.year * 365 + self.month * 30 + self.day
        new_days = initial_days + days
        self.year = new_days // 365
        new_days = new_days % 365
        self.month = new_days // 30
        self.day = new_days % 30

    def convert_to_days(self):
        return self.year * 365 + self.month * 30 + self.day

    def __add__(self, other):
        d3 = Date(self.day, self.month, self.year)
        d3.increment_days(other.convert_to_days())
        return d3

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


d1 = Date(15, 2, 1995)
d2 = Date(1, 1, 2)
print(d1 + d2)
# d1.increment_days(365 * 3)
# print(d1)
