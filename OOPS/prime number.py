def primes_below(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False

    primes = [i for i in range(n) if sieve[i]]
    return primes


# Find and display primes below 2 million
primes = primes_below(2000000)
print(f"All prime numbers below 2 million:")
print(primes)

# Calculate the sum of all primes
sum_of_primes = sum(primes)
print(f"\nSum of all prime numbers below 2 million: {sum_of_primes}")
