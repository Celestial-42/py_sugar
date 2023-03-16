from functools import partial


def a_v1(x1, x2):
  return x1.b + x2.c


def a_v2(x1, x2, x3):
  return x1.e + x2.f + x3.g

class D(object):
def __init__(self):
  self.b = 1
  self.c = 2
  self.e = 3
  self.f = 4
  self.g = 5


d1 = D()
d2 = D()
d3 = D()

d1.d = partial(a_v1, d1, d2)
print(d1.d())
d2.c = 9
print(d1.d())

d3.d = partial(a_v2, d1, d2, d3)
print(d3.d())
d3.g = 23
print(d3.d())

print(d1.d())

d2.d = a_v1
print(d2.d(d2, d3))
