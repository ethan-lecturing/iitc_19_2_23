''' Exercise #8. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################

class Room:
    def __init__(self, floor, number, guests, clean_level, rank, satisfaction=1.0):
        self.floor = floor
        self.number = number
        self.guests = guests
        self.clean_level = clean_level
        self.rank = rank
        self.satisfaction = satisfaction
        self.is_valid()

    def is_valid(self):
        if type(self.clean_level) != int or self.clean_level < 1 or self.clean_level > 10:
            raise TypeError('Clean level is not int')
        if type(self.rank) != int or self.rank < 1 or self.rank > 3:
            raise TypeError('Rank is not int')
        if type(self.satisfaction) != float or self.satisfaction < 1 or self.satisfaction > 5:
            raise TypeError('Satisfaction is not float')

    def __repr__(self):
        guests_str = 'empty'

        if len(self.guests) > 0:
            guests_str = ', '.join(self.guests)
        return f"floor {self.floor}\nnumber {self.number}\n" + guests_str + f'\nclean_level {self.clean_level}'

    def is_occupied(self):
        return len(self.guests) > 0

    def can_clean(self):
        return True  # replace this with your implementation

    def clean(self):
        if self.can_clean():
            self.clean_level = min(10, self.rank + self.clean_level)
        else:
            return 'Room cannot be cleaned'

    def better_than(self, other):
        pass  # replace this with your implementation

    def check_in(self, guests):
        pass  # replace this with your implementation

    def check_out(self):
        pass  # replace this with your implementation

    def move_to(self, other):
        pass  # replace this with your implementation


#########################################
# Question 2 - do not delete this comment
#########################################
class BudgetRoom(Room):
    def __init__(self, floor, number, guests, clean_level,
                 rank=1, satisfaction=1.0, clean_stock=0):
        pass  # replace this with your implementation

    def __repr__(self):
        return ""  # replace this with your implementation

    # Replace this comment with your methods' implementation


class LegacyRoom(Room):
    def __init__(self, floor, number, guests, clean_level,
                 rank=2, satisfaction=1.0,
                 minibar_drinks=2, minibar_snacks=2):
        pass  # replace this with your implementation

    def __repr__(self):
        return ""  # replace this with your implementation

    # Replace this comment with your methods' implementation


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        pass  # replace this with your implementation

    def __repr__(self):
        return ""  # replace this with your implementation

    def check_in(self, guests, rank):
        pass  # replace this with your implementation

    def check_out(self, guest):
        pass  # replace this with your implementation

    def upgrade(self, guest):
        pass  # replace this with your implementation


#########################################
# Question 3 supplement - do not delete this comment
#########################################
def test_hotel():
    rooms = [BudgetRoom(15, 140, [], 5), LegacyRoom(12, 101, ["Ronen", "Shir"], 6),
             BudgetRoom(1, 2, ["Liat"], 7), Room(2, 23, [], 6, 3)]
    h = Hotel("Dan", rooms)
    print(h.upgrade("Liat"))
    print(h.check_out("Ronen"))
    print(h.check_in(["Alice", "Wonder"], 2))
    print(h.check_in(["Alex"], 3))
    print(h)
    print(h.check_in(["Oded", "Shani"], 3))
    print(h.check_in(["Oded", "Shani"], 1))
    print(h.check_out("Liat"))
    print(h.check_out("Liat"))
    print(h)


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    test_hotel()
