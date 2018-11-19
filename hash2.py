user_id = input("enter user name: ")
pass_word = input("enter password: ")

def my_hash(user_id,pass_word):
    flag = 1
    fp = open("passwd.txt",'r')
    for line in fp:
        user, salt, password, hashi = line.split()
        if user != user_id:
            continue
        else:
            flag = 0;i = 0; digest = ''
            s = pass_word+salt
            print("salt+password:", s)
            blocks= []
            while(i<len(s)):
                blocks.append(s[i:i+4])
                i+=4
            for i1 in blocks:
                sum1=0
                for i2 in i1:
                    sum1+=ord(i2)
                sum1 = sum1%93
                digest += chr(sum1+33)
            print(digest,hashi)
            if hashi == digest:
                print("user_id and password are correct authentication success")
            else:
                print("user_id and password mismatch authentication failed")
    if flag:
        print("user_id and password doesn exist")
my_hash(user_id, pass_word)


"""Output:
enter user name: user1
enter password: helloworld12
salt+password: helloworld12E1F53135E559C253
Rt=X3OD Rt=X3OD
user_id and password are correct authentication success
"""
