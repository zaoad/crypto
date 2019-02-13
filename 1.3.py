from Crypto.Cipher import AES
import codecs
def convertbit(i):
    s=""
    for a in range(1,251):
        s=s+'0'
    b=bin((i))[2:]
    




if __name__ == '__main__':
    cipher=open('aes_weak_ciphertext.hex','r')
    iv=open('aes_iv.hex','r')
    key=open('aes_key.hex','r')
    cipher_data=cipher.read()
    iv_data=iv.read()
    key_data=key.read()
    cipher_data=codecs.decode(cipher_data,'hex')
    iv_data=codecs.decode(iv_data,'hex')
    key_data=codecs.decode(key_data,'hex')
    ci=AES.new(key_data,AES.MODE_CBC,iv_data)
    out=ci.decrypt(cipher_data)
    out=out.decode('utf-8')
    output=open('solution02.txt','w')
    output.write(out)



