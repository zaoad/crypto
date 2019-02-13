if __name__ == '__main__':

    cipher=open('sub_ciphertext.txt','r')
    key=open('sub_key.txt')
    cipher_data=cipher.read()
    key_data=key.read()
    print(cipher_data)
    print(key_data)
    s=""
    for i in cipher_data:
        if i==" ":
            s=s+" "
        elif i<'A':
            s=s+i
        else:
            for j in range(0,len(key_data)):
                if i==key_data[j]:
                    c=chr(65+j)
                    s=s+c
    out=open('solution01.txt','w')
    out.write(s)






