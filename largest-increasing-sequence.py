
a = [1, 2, 1, 4, 5, 1, 1, 101, 102, 103, 104, 105, 1, 2, 3, 4, 6, 7, 10]
largest = []
temp = []

print("********************************************************************************")
print("starting array = ", a)

# add the zeroth (first) number manually
temp.append(a[0])


# go down the list
for n in range(1, len(a)):
  # current number > end of temp, append it to temp
  if a[n] > temp[-1]:
    temp.append(a[n])
  # if it is smaller
  else:
    # compare len(temp) witn len(largest)
    # if temp is bigger, replace largest
    if len(temp) > len(largest):
      largest = temp
    # since we've hit a smaller number we also need to rest temp to the current number   
    temp = [a[n]]

  print("====================================")
  print("step n  = ", n)
  print("(sub) a[n] = ", a[n])
  print("(sub) largest   -> ", largest)
  print("(sub)    temp   -> ", temp)
#
# at the end if the last temp is longer than largest, replace largest
if len(temp) > len(largest):
  largest = temp  

print("largest increasing sequence = ", largest)
