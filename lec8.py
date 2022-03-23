'''
lecture 8
'''

def my_function(a,b=0):
    print(a)
    print(b)
    
    result = a + b 
    return result
    
print(my_function(b=1, a=2))

#ex1 cal abs values

def cal_abs(a):
    if a >=0:
        return a
    if a <0:
        return -a
        
print(cal_abs(0))

