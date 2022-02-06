def improve(update,close,guess= 1):
    while not close(guess):
        guess =update(guess);
    return guess
def approx_eq(x,y,tol = 1e-3):
    return abs(x-y) < tol

def average(x,y):
    return(x+y)/2

def _sqrt(a):
    def sqrt_update(x):
        return average(x,a/x)
    def sqrt_close(x):
        return approx_eq(x*x,a)   
    return improve(sqrt_update,sqrt_close)

from math import sqrt

def sqrt_test(x):
    assert approx_eq(sqrt(x),_sqrt(x)),'shit!'
    
for i in range(1,100):
    sqrt_test(i)