# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rJJ9hu4hEef7hq9dqQdMRxD5bbBuSQ7d
"""

heat_tree = 0
while heat_tree < 10:
  heat_tree += 1
  print(f'나무를 {heat_tree}번 찍었습니다')
  if heat_tree == 10:
    print("나무 넘어갑니다")

prompt = """
    1.ADD
    2.DEL
    3.LIST
    4.QUIT
    Enter number:
"""

number = 0
# while number != 4:
while number < 4:
  print(prompt)
  number = int(input())

coffee = 3
while True:  #무한 루프 (Break statement로 빠져나가야함)
  money = int(input("Insert Money: "))
  if not coffee:
    print("커피가 없습니다")
    break

  if money == 300:
    print("커피")
    coffee -= 1
  elif money > 300:
    print(f'{money-300}원 반환 + 커피')
    coffee -= 1
  else:
    print(f'돈이 모자랍니다.')
  
a = 0
while a < 10:
  a += 1
  if a % 2 == 0: continue # 첫번째 줄로 이동
  print(a)
