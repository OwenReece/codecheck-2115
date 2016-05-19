#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot():
  # Please write your code here.

  def generate_hash(self):

  # Convert the number into scientific notation with 16 digits after "."
  # If power of e is greater than 20, get the number between "." and "e"
  # Else return the number itself
  def scientificNotation(self, num):
    data = "%.16e" % num
    result = data if (int(data.split("e+")[1]) > 20) else num
    return result
  
