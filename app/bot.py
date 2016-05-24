#!/usr/#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nose.tools import assert_equal

class Bot(object):
  def __init__(self,dic={}):
    self.dic = dic
  def generate_hash(self):
    temp_list_com=[ord(t) for t in self.dic["command"]]
    self.command = "".join(str(d) for d in temp_list_com)
    temp_list_dat=[ord(t) for t in self.dic["data"]]
    self.data = "".join(str(d) for d in temp_list_dat)

    self.hash=hex(scientificNotation(ans_com)+scientificNotation(ans_dat))
    return self.hash

  # Convert the number into scientific notation with 16 digits after "."
  # If power of e is greater than 20, get the number between "." and "e"
  # Else return the number itself

def scientificNotation(num):
  dat = "%.16e" % num

  tmp_res1 = dat.split("e+")

  if (tmp_res1[1] > 21):
    tmp_res2 = "".join(str(t) for t in tmp_res1)
    tmp_res3 = tmp_res2.split(".")
    while(tmp_res3[1][0]=="0"):
      result = tmp_res3[1].lstrip("0")
    return result
  else:
    result = num
    return result
