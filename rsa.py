def gcd(a,b):
    while(a!=0 and b!=0):
        if a > b : a = a % b
        else: b = b % a
    return a+b

p, q = 3.0,7.0
n = p*q
phi = (p-1)*(q-1)
print("p,q,phi(n) ",p,q,phi)
e = 2.0
while e < phi:
    if gcd(e,phi) == 1:
        break
    else: e+=1

print("public key (e,n) ",e,n)

k = 2
z= k*phi +1
while(z%e != 0):
    k+=1
    z = k*phi +1
d = (1+ k*phi)/e
print("private key ",d)

msg = 19
print("message ",msg)

c = (msg**e)%n
print("ciphertext ",c)

m = (c**d)%n
print("deciphertext ",m)

""" Output:
p,q,phi(n)  3.0 7.0 12.0
public key (e,n)  5.0 21.0
private key  5.0
message  19
ciphertext  10.0
deciphertext  19.0
"""
