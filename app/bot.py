#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Bot():
  #ここに素数判定プログラムを実装してください。

  def generateHash(command,data):
	for i in range(0,len(command)):
      temp_com[i] = ord(command[i]);
    for j in range(0,len(data)):
      temp_dat[j] = ord(data[j]);
    
    com = "".join(temp_com);
    dat = "".join(temp_data);
    scientificNotation(com);
    scientificNotation(dat);
    com_dat = com+dat;
    return result;
  
  # Convert the number into scientific notation with 16 digits after "."
  # If power of e is greater than 20, get the number between "." and "e"
  # Else return the number itself
  def scientificNotation(num):
    data = "%.16e" % num
    temp_result = data.split("e+");
    
    if (int(temp_result[1]) > 21):
      result = "".join(temp_result);
    else 
      result = num;
    return result;

x="ladder";
y="climbing";

print(x);
print(y);
a = generateHash(x,y):
  
hash = hex(a);
print(hash);