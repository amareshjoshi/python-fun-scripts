memo = {};

def fib1(n):
    # in memo
    if n in memo:
      return memo[n]
    else:
      # not in memo
      if n < 2:
        return 1
      else:
        f = fib1(n-1) + fib1(n-2)
        memo[n] = f
        return f

def fib2(a, b, n):
    if a < 2:
      return n
    else:
      fib2(b, n, a+n)


for i in range(10):
  print(i , fib1(i))

for i in range(10):
  print(i , fib2(1, 1, 1))

1 1 1
1 1 2
1 2 3
2 3 5
3 5 8
5 8 11
