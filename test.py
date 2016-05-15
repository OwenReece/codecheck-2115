#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot():
  #ここに素数判定プログラムを実装してください。

  def generateHash(data):
    temp_data=[]
    for i in range(len(data)):
      temp_data.append(ord(data[i]))

    ans = "".join(str(d) for d in temp_data)
    return ans

  # Convert the number into scientific notation with 16 digits after "."
  # If power of e is greater than 20, get the number between "." and "e"
  # Else return the number itself
  def scientificNotation(num):
    data = "%.16e" % num
    temp_result = data.split("e+")

    if (int(temp_result[1]) > 21):
      result = "".join(temp_result)
    else:
      result = num
    return result

  x = "ladder"
  y = "climbing"

  com = scientificNotation(int(generateHash(x)))
  dat = scientificNotation(int(generateHash(y)))

  comdat=com+dat

  hash = hex(comdat)
  print(hash)
