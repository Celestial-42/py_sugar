class C:pass

c = C()

def F(o, n, f):
  _t = type(o)
  _t = type(_t.__name__, (_t,), {})
  setattr(_t, n, f)
  o.__class__ = _t

F(c, 'say', lambda self:print('hello'))

c.say()
