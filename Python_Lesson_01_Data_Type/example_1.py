# example_1.py

a = 3
b = 3.14
c = 3.75
d = '3'
e = '3.14'
f = '3.75'
g = 'abc'

print('a', a, type(a))
print('str(a)', str(a),type(str(a)))
print('float(a)', float(a),type(float(a)))
print('\n')

print('b', b, type(b))
print('str(b)', str(b),type(str(b)))
print('int(b)', int(b),type(int(b)))
print('\n')

print('c', c, type(c))
print('str(c)', str(c),type(str(c)))
print('int(c)', int(c),type(int(c)))
print('\n')

print('d', d, type(d))
print('int(d)', int(d),type(int(d)))
print('float(d)', float(d),type(float(d)))
print('\n')

print('e', e, type(e))
try:
    print('int(e)', int(e),type(int(e)))
except Exception as ex:
    print(f"Exception: {ex}")
print('float(e)', float(e),type(float(e)))
print('\n')

print('f', f, type(f))
try:
    print('int(f)', int(f),type(int(f)))
except Exception as ex:
    print(f"Exception: {ex}")
print('float(f)', float(f),type(float(f)))
print('\n')

print('g', g, type(g))

try:
    print('int(g)', int(g),type(int(g)))
except Exception as ex:
    print(f"Exception: {ex}")

try:
    print('float(g)', float(g),type(float(g)))
except Exception as ex:
    print(f"Exception: {ex}")