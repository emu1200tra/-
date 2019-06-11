# -*- coding: utf-8 -*-

# problem No.1-A
def p1_A(string):
  tmp = ""
  for i in range(len(string)-1, -1, -1):
    tmp+=string[i]
  return tmp

# problm No.1-B
def p1_B(string):
  tmp = string.split(' ')
  for i in range(len(tmp)):
    tmp[i] = p1_A(tmp[i])
  return ' '.join(tmp)

# problem No.2
def p2(num):
  record = 0
  for i in range(1, num+1):
    if i % 3 != 0 and i % 5 != 0:
      record += 1
    elif i % 3 == 0 and i % 5 == 0:
      record += 1
  return record

# problem No.3
'''
  拿標示為混和的袋子，此袋子不可能是混和，所以一定是鉛筆袋或原子筆袋，
  若拿出是鉛筆，表示此袋子應是鉛筆袋，剩下原子筆袋跟混和袋，
  因為標示原子筆袋不可能裝原子筆，所以標示原子筆袋是混和袋，而標示混和袋是原子筆袋；
  若從標示混和的袋子拿出是原子筆，則此袋是原子筆袋，而剩下鉛筆袋跟混和袋，
  因為標示鉛筆袋不可能裝鉛筆，所以標示鉛筆袋是混和袋，而標示混和袋是鉛筆袋。

'''

# problem No.4
'''
  在同乘以一個常數的情況下，越大的數字乘上一個常數後會增長的越快，因此原本是300*3跟退還後的270*3，常數是3，原本300跟270差30，
  乘上常數放大後會差90元，但服務生只吞佔60，所以就會發生30元的落差，故不應直接用乘法列式，
  正確來看應是300*3-60-90=750的想法才合理。
'''


tmp = p1_A("junyiacademy")
print tmp
tmp = p1_B("flipped class room is important")
print tmp
tmp = p2(15)
print tmp

