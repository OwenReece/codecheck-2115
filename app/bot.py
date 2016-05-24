class Bot(object):
  def __init__(self,dic={}):
    self.dic = dic
  def generate_hash(self):
    self.command=self.dic["command"]
    self.data=self.dic["data"]
    temp_list_com=[ord(t) for t in self.command]
    tmp_com = "".join(str(d) for d in temp_list_com)
    temp_list_dat=[ord(t) for t in self.data]
    tmp_data = "".join(str(d) for d in temp_list_dat)

    tmp_hash=hex(int(int(scientificNotation(int(tmp_com)))+int(scientificNotation(int(tmp_data)))))
    self.hash=tmp_hash.lstrip("0").lstrip("x")
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
      tmp_res3[1] = tmp_res3[1].lstrip("0")
    return tmp_res3[1]
  else:
    return tmp_res1
