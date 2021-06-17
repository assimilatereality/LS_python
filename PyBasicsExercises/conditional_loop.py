i = 0
while True:
  i += 2
  if i == 4:
      continue

  print(i)
  if i == 10:
    break       # this will cause execution to exit the loop

print(i)