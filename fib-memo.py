
import string

def fizzbuzz(n):
  print("fizbuzz from 1 to", n)
  for i in range(1, n+1):
    out = ""
    if i % 3 == 0:
      out += "fizz"
    if i % 5 == 0:
      out += "buzz"
    if out == "":
      print(i)
    else:
      print(out)

# 1,000,000,000
#fizzbuzz(1000000)
#exit(0)



def fib_naif(n):
  if n <= 1:
    return 1
  else:
    f = fib_naif(n-1) + fib_naif(n-2)
    return f

memo = {}
def fib_memo(n):
  if n in memo:
    return memo[n]
  if n <= 1:
    return 1
  else:
    f = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = f
    return f

def memoize(f):
    memo = {}
    def foo(x):
        if x not in memo:
            memo[x] = f(x)
        else:
          return memo[x]
    return foo

bar = memoize(fib_naif)

start = 50
stop = 60

for i in range(start, stop):
 print("memoize(fib_naif)", i, bar(i))

for i in range(start, stop):
  print("fib_memo", i, fib_memo(i))

# for i in range(start, stop):
#  print("fib_naif", i, fib_naif(i))

exit(0)

for i in range(100, 110):
  print("fib_memo", i, fib_memo(i))

for i in range(100, 110):
  print("fib_naif", i, fib_naif(i))



