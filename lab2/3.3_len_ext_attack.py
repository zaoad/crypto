import pymd5

fi = open("3.3_query.txt","r")
query = fi.readline()
fi.close()

key = "SECRETSS"

print(query)

fi2 = open("3.3_command3.txt","r")
comm3 = fi2.readline()
print(comm3)
token = query[query.index("=")+1:query.index("&")]
message = query[query.index("&")+1:]
h = pymd5.md5()
h.update(key+query)
token = h.hexdigest()
#print(query)
#print(token)
msglen = len(query)


def main():

    keylen = 8
    pad = pymd5.padding((keylen+msglen)*8)
    padlen = len(pad)

    #"Intruder message"
    new_message = query+pad+comm3

    cnt = (keylen+msglen+padlen)*8
    h = pymd5.md5(state=token.decode("hex"),count=cnt)
    h.update(comm3)
    intruder_token = h.hexdigest()

    # "Intruder Message and Token"
    intra_msg = (new_message,intruder_token)
    print(intra_msg)
    fo = open("Solution33.txt", "w")
    fo.write(new_message)
    server_verify(intra_msg)

def  server_verify(message):

    key = "SECRETSS"
    received_query= message[0]
    received_token = message[1]
    h = pymd5.md5()

    h.update(key+received_query)
    new_token = h.hexdigest()

    if(received_token==new_token):
        print("Token Match")

    else:
        print("Token Not Match")

if __name__ == '__main__':
    main()



