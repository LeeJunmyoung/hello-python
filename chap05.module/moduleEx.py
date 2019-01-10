import math as m 
# import 모듈명 as 약칭
from math import pi,sin 
# from 모듈명 import 메서드 혹은 변수 
print(m.pi)
print(m.sin(10))

print(pi)
print(sin(10))

import random

print(random.random()*500)
print(random.uniform(10,20))
print(random.randrange(0,100,2))
a= [1,2,3,4,5,6,7,8,9]
print(a)

random.shuffle(a)
print(a)

import externalModule
externalModule.println('test')

print()
print("######################")
print()

import os
print(os.name)