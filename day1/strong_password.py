import random
import string


def get_password(amount):
    all_letters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return ''.join([all_letters[random.randint(0, len(all_letters) - 1)] for i in range(amount)])

print(get_password(10))
# lst = [random.randint(1,10) for i in range(10)]
#
# lst = []
# for i in range(10):
#     lst.append(random.randint(1, 10))
#
