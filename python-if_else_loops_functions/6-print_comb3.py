#!/usr/bin/python3
print(", ".join("{:d}{:d}{:d}".format(i, j, k)
      for i in range(10)
      for j in range(i + 1, 10)
      for k in range(j + 1, 10)))
