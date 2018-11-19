import random
data = int("100010010011",2)
round1_key = 3
def permut(left, right):
    return right<<6 | left

def split(data):
    return (data>>6, data & int("111111",2))

def foo(key, rdata):
    round1_key = key % 6
    rdata = '{0:06b}'.format(rdata)
    return int(rdata[-round1_key:]+rdata[:-round1_key], 2)

print("init data : ", data)
l,r = split(data)
newr = foo(round1_key,r)
newl = int('{0:06b}'.format(newr ^ l), 2)
nextdata = permut(newl, r)
print("data sent : ",nextdata)

redata = nextdata
print("data recieved : ", redata)
rel, rer = split(redata)
swapdata = permut(rel, rer)
newrel, newrer = split(swapdata)
intr = foo(round1_key , newrer)
finall = int('{0:06b}'.format(newrel ^ intr) ,2)
finalr = newrer
finaldata = finall<<6 | finalr
print("finaldata : ", finaldata)


""" Output:
init data :  2195
data sent :  1272
data recieved :  1272
finaldata :  2195
"""
