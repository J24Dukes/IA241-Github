'''
lec8
'''

def my_function(a,b):
    
    result = a + b
    
    
    print(a)
    print(b)
    return result
    
print (my_function(b=1,a=2))


#ex 1


def cal_abs(a):
    
    if type(a) is str:
        return "Wrong data type"
    
    elif a>=0:
        return a
    
    else:
        return -a
        
print (cal_abs('hi'))

#ex2

def cal_sigma(n,m):
    
    result = 0
    
    for i in range(n,m+1):
        
        result = result + i
    
    return (result)
    
print(cal_sigma(1,999))


def cal_pi(n,m):
    
    result = 1
    
    for i in range(n,m+1):
        
        result = result * i
        
    return result
    
print (cal_pi(1,5))

#ex3

def cal_f(m):
    
    if m ==0:
        return 1
    
    else:
        return m * cal_f(m-1)

print (cal_f(5))


def cal_p(n,m):
    
    return (cal_f(m)/cal_f(m-n))
    
print (cal_p(3,5))