#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot(object):
  #ここに素数判定プログラムを実装してください。

  def generateHash(self):
    temp_list_com=[ord(t) for t in len(self["command"])]
    ans_com = "".join(str(d) for d in temp_list_com)
    temp_list_dat=[ord(t) for t in len(self["data"])]
    ans_dat = "".join(str(d) for d in temp_list_dat)
    
    ans=scientificNotation(ans_com)+scientificNotation(ans_dat)
    return hex(ans)
    
  # Convert the number into scientific notation with 16 digits after "."
  # If power of e is greater than 20, get the number between "." and "e"
  # Else return the number itself
  def scientificNotation(num):
    dat = "%.16e" % num

    tmp_res1 = dat.split("e+")

    if (int(tmp_result1[1]) > 21):
      tmp_res2 = "".join(str(t) for t in tmp_res1)
      tmp_res3 = tmp_res2.split(".")
      result = tmp_res3[1]
    else:
      result = num
    return result
