map={}
def createmap():
    global map
    map['0'] = '0001'
    map['1'] = '0010'
    map['2'] = '0011'
    map['3'] = '0100'
if __name__ == '__main__':

    first=open('input1.txt','r')
    second=open('input1.1.txt','r')
    first_data=first.read()
    second_data=second.read()
    print(first_data)
    print(second_data)







