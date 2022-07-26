#/usr/local/bin/python3

#
# qs - quicksort
def qs(a):
  print("a = ", a)
  if a == []:
    return a
  else:
    pivot = a[0]
    left = []
    right = []
    for n in range(1, len(a)):
      if a[n] < pivot:
        left.append(a[n])
      else:
        right.append(a[n])
    print("left, pivot, right = ", left, pivot, right)
    return qs(left) + [pivot] + qs(right)
  

a = [2,2,2,2, 4, 4, 4, 1, 5, 2, 2, 2, 5]


print("==========================================================")
print("beg = ", a)
print("end   = ", qs(a))





