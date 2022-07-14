# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YXIKBX_WPK-8xsL1UH-UMh2YHrD_VgX4
"""
def add(a, b):
  return a+b

def sub(a, b):
  return a-b

print(f'3+4={add(3, 4)}, 3-3={sub(3, 3)}')

# 함수 1 (입, 출)
rtn_add = add(3, 4)
print(rtn_add)

# 함수 2 (입x, 출)
def add_5_6():
  return 5+6
rtn_add56 = add_5_6()
print(rtn_add56)

# 함수 3 (입, 출x)
def mul(a, b):
  print(a * b)
rtn_mul = mul(33, 44)
print(f'return value is "{rtn_mul}"')

# 함수 4 (입x, 출x)
import math
def print_PI():
  print(math.pi)
rtn_pi = print_PI()
print(f'return print_PI function is "{rtn_pi}"')

# 함수 호출 시 파라미터 지정 가능
mul(a=2, b=3), mul(b=3, a=2), mul(a=33, b=23)

# 함수 호출 파라미터 갯수가 정해지지 않았을때.
def add_many(*args):
  result = 0
  for i in args:
    result += i
  return result

rtn_val = []
rtn_val.append(add_many(1,2,3,4,5))
rtn_val.append(add_many(1,2,3,4))
rtn_val.append(add_many(1,2,3))
print(rtn_val)

val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tmp = add_many(*val)
print(f'tmp = {tmp}')

def add_mul(choice, *args):
  if choice == "add":
    result = 0
    for i in args:
      result += i
  elif choice == "mul":
    result = 1
    for i in args:
      result *= i
  return result

print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5))

# 키워드 파라미터
def func_kwargs(**kwargs):
  print(kwargs)

func_kwargs(a=1, b=3) # 딕셔너리타입으로 반환

# dictionary 자료형 복습?
# dict_val = {'a': 1, 'b': 3}
# for item in dict_val: # key-value 쌍에서 key만 item에 넘겨줌
# for items in dict_val.items():
#   print(items)  # dict.items() ==> 튜플로 반환 (a,1)
# print(dict_val.items())

def myFunc(**kwargs):
  for item in kwargs.items():
    print(item)

myFunc(x=100, y=200, z='abc')

# 함수 리턴 값
def add_and_mul(a, b):
  return (a+b), (a*b)

print("result=%d,%d" % add_and_mul(2, 4))
print(f'{add_and_mul(2,4)}')
result = add_and_mul(2, 4)
a, b = add_and_mul(2, 4)
print(f'{a} {b}')
print(result, a, b)

# 함수 초기 값
def say_myself(name, age, dept="AI-Engineering"):
  print(f'나의 이름은 {name} 입니다.')
  print(f'나이는 {age} 입니다.')
  print(f'학과는 {dept}')

say_myself('김동규', 25)

# 함수의 범위
a = 1
def vartest(a):
  a = a + 1

vartest(a)
print(a)

def vartest1(inner_var):
  inner_var = inner_var + 1

vartest1(3)
# print(inner_var)

# global
aa = 1
def globaltest(a):
  global aa
  aa = a + 1

globaltest(3)
print(aa)

#C 매크로함수 #define MUL(a, b)  a+b
#lambda
add = lambda a, b: a + b
result = add(3, 4)
print(result)


