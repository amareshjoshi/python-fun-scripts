
import string

# for i in range(1, 13):
#   z = i // 3
#   x = i / 3
#   if (i * (i //3)) == (i * (i / 3)):
#     print(i)
# exit(0)

def fizzbuzz(n):
  # print("fizbuzz from 1 to", n)
  for i in range(1, n+1):
    fizz = buzz = False
    # if (i * (i // 3)) == (i * (i / 3)):
    #   fizz = True
    # if (i * (i // 5)) == (i * (i / 5)):
    #   buzz = True
    if i % 3 == 0:
      fizz = True
    if i % 5 == 0:
      buzz = True

    fizzbuzz = fizz & buzz
    if fizzbuzz:
      print("FizzBuzz")
    elif fizz:
      print("Fizz")
    elif buzz:
      print("Buzz")
    else:
      print(i)

# 1,000,000,000
#fizzbuzz(100000000)
fizzbuzz(30)
