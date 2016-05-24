#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot:
  #ここに素数判定プログラムを実装してください。

  def generate_hash(self,command,data,hash):
    temp_list_com=[ord(t) for t in len(self["command"])]
    self.command = "".join(str(d) for d in temp_list_com)
    temp_list_dat=[ord(t) for t in len(self["data"])]
    self.data = "".join(str(d) for d in temp_list_dat)

    self.hash=hex(scientificNotation(ans_com)+scientificNotation(ans_dat))
    return self.hash

  # Convert the number into scientific notation with 16 digits after "."
  # If power of e is greater than 20, get the number between "." and "e"
  # Else return the number itself
  def scientificNotation(num):
    dat = "%.16e" % num

    tmp_res1 = dat.split("e+")

    if (int(tmp_res1[1]) > 21):
      tmp_res2 = "".join(str(t) for t in tmp_res1)
      tmp_res3 = tmp_res2.split(".")
      while(tmp_res3[1][0]=="0"):
        result = tmp_res3[1].lsprit("0")
    else:
      result = num
    return result
