#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot():
  #ここに素数判定プログラムを実装してください。

  def generateHash(self):
    temp_data=[]
    for i in range(len(self)):
      temp_data.append(ord(self[i]))

    ans = "".join(str(d) for d in temp_data)
    return ans

  # Convert the number into scientific notation with 16 digits after "."
  # If power of e is greater than 20, get the number between "." and "e"
  # Else return the number itself
  def scientificNotation(self,num):
    data = "%.16e" % num

    temp_result1 = data.split("e+")

    if (int(temp_result1[1]) > 21):
      temp_result2 = "".join(str(t) for t in temp_result1)
      temp_result3 = temp_result2.split(".")
      result = "".join(str(t) for t in temp_result3)
    else:
      result = num
    return result

  x = str(input("hash1 : "))
  y = str(input("hash2 : "))

  com = scientificNotation(int(generateHash(x)))
  dat = scientificNotation(int(generateHash(y)))

  comdat=int(com)+int(dat)

  hash = hex(comdat)
  print(hash)
