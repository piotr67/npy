#!/usr/bin/env python
# -*-coding: utf-8 -*-

def tekst():
	print("Nowy tekst wpisany")


tekst()
tekst()
tekst()
tekst()


def fun(a1, a2):
	args = a1+ " - "+a2
	return args

print fun("nowy", "dwor")



def new(n1, n2 = "ktos"):
	global n
	n3 = n1+" - "+n2
	n = 1
	return n3

print new("moze")
print n


print "nowa funkcja test"
a = 5
def test(x = a):
	return x


a = 9
print test()


a = [6]
def test2(x = a):
	return x


a.append(2)
print test2()


def test3(*x):
	return x

print test3('n', 'bodfrgt', 67, 89, 123456)



def test6(t, **x3):
	return x3


print test6(t='cvfg', we='aswde', fg=78, df=56)


a = [1]
def te(x = a):
	return x

a.append(24)
print te()


def test6():
	return 'abde'

test.a = 1
test.lol = 'omg'

print test6()
print test.__dict__


def test():
	global a
	a = 7
	return True

test()
print a


a = lambda : 'a'
print a()

b = lambda x,y : x+y
print b(3,5)

print "---------------------------"

liczby = [1,2,3,4,5]
def dwa(x):
	return x*2


print map(dwa, liczby)

liczby_n = [1,2,5]
liczby_p = [2,4,6]
print zip(liczby_n, liczby_p)


liczby = [2,2,2,2,2]
def suma(x,y):
	return x+y
print reduce(suma, liczby)


liczby = [1,2,3,4,5]
def parzyste(x):
	if x%2 == 0:
		return True
	else:
		return False

print filter(parzyste, liczby)


print eval('2+2')
print
exec ('for i in range(1,3): print i')