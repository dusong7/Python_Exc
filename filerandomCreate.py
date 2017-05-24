import random

table = "1234567890"
for i in range(100):
  list = random.sample(table,10)
  print("".join(list))
