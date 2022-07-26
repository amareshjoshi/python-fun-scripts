#!/usr/bin/env python3

from datetime import datetime



# find all of the prime factors of a range of numbers
center = 100 * 1000 * 1000 * 1000
size = 10
beg = center - (size // 2)
end = center + (size // 2)

print("Begin at:", datetime.now().strftime("%H:%M:%S"))
print("===================================")

for n in range(beg, end+1):
  print("start time for ", n, " = ", datetime.now().strftime("%H:%M and %S.%f seconds"))
  print("n = ", n)
  primes = []
  while n > 1:
    # look for the first prime divisor (the first divisor will always be prime)
    for i in range(2, n+1):
      # when you find it
      if n % i == 0:
        # add it to the primes array
        primes.append(i)
        # reduce n by that amount (since we know that i is a divisor of n)
        n = n // i
        break
  print("prime factors = ", primes)
  print("=============================================")
print("all done!")
