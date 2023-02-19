def sum(a, b):
    return a + b


def get_primes(amount):
    found_primes = []

    current = 2
    while len(found_primes) < amount:
        is_prime = True
        for prime in found_primes:
            if current % prime == 0:
                is_prime = False

        if is_prime:
            found_primes.append(current)
        current += 1  # current = current + 1

    return found_primes


lst = get_primes(1000)
print(lst)
for i in range(5):
    b = 'Hello'
import time

time.sleep(5)
print(b)
