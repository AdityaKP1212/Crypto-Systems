data = "1000100100111000"
seed = int("1100",2)
def my_hash_function(block, hashkey):
    return block ^ hashkey

def my_hash(blocks, seed):
    flag = 1;index = 0
    while(index<4):
        if flag:
            digest = my_hash_function(int(blocks[index],2),seed)
            flag = 0
        else:
            digest = my_hash_function(int(blocks[index],2),digest)
        index += 1
    return digest
l = data
intl = [l[:4],l[4:8],l[8:12],l[12:]]
intl1 = ['0'+l[1:4],l[4:8],l[8:12],l[12:]]

digest = my_hash(intl, seed)
print("message: {0}, digest: {1:06b}, seed sent: {2:04b} ".format(int(data,2),digest,seed))

digest1 = my_hash(intl ,seed)
print("message recieved correctly digest is: {0:06b}".format(digest1))
digest2= my_hash(intl1 , seed)
print("message wrongly recieved digest is: {0:06b}".format(digest2))


""" Output:
message: 35128, digest: 000110, seed sent: 1100
message recieved correctly digest is: 000110
message wrongly recieved digest is: 001110
"""
