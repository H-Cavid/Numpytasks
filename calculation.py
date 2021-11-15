def add(a,b):
    return a+b

def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)

def mult3(n):
    return 3*n

if __name__=='__main__':

    n,m=map(int,input('n,m=').split())
    res = gcd(n,m)
    print(res)

##evde anacondani yukle
# pip install numpy
# pip install pandas
# pip install matplotib
# conda insstall numpy 
# jupyter notebook