
N = 1000

def calculate_b(n):
    b = int(n ** 0.5)
    prime_nums = [2]
    for num in range(3, b + 1, 2):
        is_prime = True
        for divisor in prime_nums:
            if divisor > num ** 0.5:
                break
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    return prime_nums

primes_in_b = calculate_b(N)
primes_in_c = []

start = int(N ** 0.5) + 1
if start % 2 == 0:
    start += 1

for num in range(start, N + 1):
    is_prime = True
    for prime_from_b in primes_in_b:
        if prime_from_b > num ** 0.5:
            break
        if num % prime_from_b == 0:
            is_prime = False
            break
    if is_prime:
        primes_in_c.append(num)

all_primes = primes_in_b + primes_in_c

print(f'Prime numbers up to {N}:')
for i in range(0, len(all_primes), 10):
    for prime in all_primes[i:min(i + 10, len(all_primes))]:
        print(str(prime).zfill(3), end=', ')
    print()
