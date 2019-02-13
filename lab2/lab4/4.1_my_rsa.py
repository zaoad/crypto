def encrypt(m,n,e):
    c=pow(m,e)%n
    return c
def createD(e,phi):
    g,x,_= egcd(e,phi)
    if g==1:
        return x%phi
def egcd(a,b):
    if a==0:
        return (b,0,1)
    else:
        g,x,y=egcd(b%a,a)
        return g, y-(b/a)*x,x
def decrypt(c,d,n):
    a=pow(c,d)%n
    return a
if __name__ == '__main__':
    p=11
    q=3
    e=5
    n=p*q
    phi=(p-1)*(q-1)
    d=createD(e,phi)
    c=encrypt(10,n,e)
    print(c)
    m=decrypt(c,d,n)
    print(m)
