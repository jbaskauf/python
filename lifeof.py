title = 'The Meaning of Life'
author = 'William Shakespeare'
def pi():
	return 3.141592
def addten(X):
	return X+10
def square(Y):
	return Y*Y
def expo(Z):
	return Z**Z
def sub():
    numbers = adder()
    return numbers[0]-numbers[1]

composer = 7
genre=10
def adder():
    A = input('Give me the first number:')
    B = input('Give me the second number:')
    return([int(A),int(B)])
    
def compint():
    P = input('initial amount=:')
    r = input('anual rate of interest (decimal)=')
    n = input('number of times compounded per year=')
    t = input('number of year(s)=')
    return(['final amount=', float(P)*(1+float(r)/float(n))**(float(n)*float(t))])
