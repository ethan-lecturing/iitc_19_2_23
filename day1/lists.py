found_primes = []
amount = 100

current = 2
while len(found_primes) < amount:
    is_prime = True
    for prime in found_primes:
        if current % prime == 0:
            is_prime = False

    if is_prime:
        found_primes.append(current)
    current += 1  # current = current + 1

print(found_primes)
