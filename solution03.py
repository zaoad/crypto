import codecs

from Crypto.Cipher import AES
def getiv():
    iv =''
    for i in range(0 , 32):
        iv +='0'
    iv = codecs.decode(iv, 'hex')
    return iv

def solutioncipher(weak_cipher):


    #print(iv)
    iv=getiv()
    key = ''
    for i in range(0, 62):
        key+='0'
    for i in range(0 , 16):
        tmp = key+'0'
        tmp +=hex(i)[2:]
        #print(tmp)
        tmp = codecs.decode(tmp, 'hex')
       # print(tmp)
        aes = AES.new(tmp, AES.MODE_CBC, iv)
        plaintext = aes.decrypt(week_cipher)
        #print(plaintext)
    for i in range(16 , 32):
        tmp = key
        tmp +=hex(i)[2:]
        #print(tmp)
        tmp = codecs.decode(tmp, 'hex')
       # print(tmp)
        aes = AES.new(tmp, AES.MODE_CBC, iv)
        plaintext = aes.decrypt(week_cipher)
       # print(plaintext)

    key = ''
    for i in range(0, 62):
        key += '0'
    key = key + hex(30)[2:]
    key = codecs.decode(key, 'hex')
    aes = AES.new(key, AES.MODE_CBC,iv)
    plaintext = aes.decrypt(week_cipher)
    #print(plaintext)

    return key

if __name__ == '__main__':
    week_cipher1 = open('aes_weak_ciphertext.hex', 'r')
    week_cipher = week_cipher1.read()
    week_cipher = codecs.decode(week_cipher, 'hex')
    key =solutioncipher(week_cipher)
    outfile = open('solution03.hex', 'w')
    key = key.decode('utf-8')
    outfile.write(key)
