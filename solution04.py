freq_count= {}
cipher=''
tot_count_c = 0


def solution4(ciphertext):
    global cipher
    global tot_count_c
    cipher = open('substitution_ciphertext.txt' , 'r')
    cipher = cipher.read()
    cipher = cipher.lower()
    global freq_count
    for i in range(97, 123):
        freq_count[chr(i)] = 0
    for i in range(0, len(cipher)-1):
        if cipher[i] !=' ':
            tot_count_c +=1
            freq_count[cipher[i]] +=1


    key , text= get_key()
    return key , text


def get_key():
    global freq_count
    mn = 123123123123.000
    exp_text=''
    key_value = 0
    for i in range(0 , 26):
        chi_value, plain_text = do_decryption2(i)
#        print(i , chi_value, plain_text, cipher)
        mn = min(chi_value, mn)
        if mn == chi_value:
            exp_text = plain_text
            key_value = i
#    print(key_value, mn, exp_text)
    return key_value, exp_text


def do_decryption2(shift_len):
    chi_value = do_chi_square_calculation2(shift_len)
    plain_text = ''
    for i in range(0, len(cipher) - 1):
        if cipher[i] != ' ':
            plain_text += reverse_shifted_chr(cipher[i], shift_len)
        else:
            plain_text += cipher[i]
    return chi_value, plain_text


def reverse_shifted_chr(init_chr, sl):
    got = ord(init_chr)
    # print(got)
    got -= sl
    got -= 97
    got += 26
    got %=26
    got += 97
    # print(got)
    return chr(got)


def shifted_chr(init_chr, sl):
    # print('heerere ', init_chr, sl)
    got = ord(init_chr)
    # print(got)
    got += sl
    got -=97
    got %=26
    got += 97
    # print(got)
    return chr(got)


def do_chi_square_calculation2(sl):
    global tot_count_c
    probability = get_probabilityability()
    sum = 0.0
    for i in range(0, 26):
        exp_val = tot_count_c*probability[chr(i+97)]
        tmp = freq_count[shifted_chr(chr(i+97) , sl)] - exp_val
        tmp = tmp*tmp
        sum += tmp/exp_val
    return sum


def get_probabilityability():
    probability = {}
    probability['A'] = 8.167
    probability['B'] = 1.492
    probability['C'] = 2.782
    probability['D'] = 4.253
    probability['E'] = 12.702
    probability['F'] = 2.228
    probability['G'] = 2.015
    probability['H'] = 6.094
    probability['I'] = 6.996
    probability['J'] = 0.153
    probability['K'] = 0.772
    probability['L'] = 4.025
    probability['M'] = 2.406
    probability['N'] = 6.749
    probability['O'] = 7.507
    probability['P'] = 1.929
    probability['Q'] = 0.095
    probability['R'] = 5.987
    probability['S'] = 6.327
    probability['T'] = 9.056
    probability['U'] = 2.758
    probability['V'] = 0.978
    probability['W'] = 2.360
    probability['X'] = 0.150
    probability['Y'] = 1.974
    probability['Z'] = 0.074
    probability['a'] = 8.167
    probability['b'] = 1.492
    probability['c'] = 2.782
    probability['d'] = 4.253
    probability['e'] = 12.702
    probability['f'] = 2.228
    probability['g'] = 2.015
    probability['h'] = 6.094
    probability['i'] = 6.996
    probability['j'] = 0.153
    probability['k'] = 0.772
    probability['l'] = 4.025
    probability['m'] = 2.406
    probability['n'] = 6.749
    probability['o'] = 7.507
    probability['p'] = 1.929
    probability['q'] = 0.095
    probability['r'] = 5.987
    probability['s'] = 6.327
    probability['t'] = 9.056
    probability['u'] = 2.758
    probability['v'] = 0.978
    probability['w'] = 2.360
    probability['x'] = 0.150
    probability['y'] = 1.974
    probability['z'] = 0.074
    return probability


if __name__ == '__main__':
    #print(shifted_chr('a', 26))
    cipher = open('substitution_ciphertext.txt', 'r')
    cipher = cipher.read()
    cipher = cipher.lower()
    key , plaintext = solution4(cipher)
    print('key: ', key)
    print('text: ', plaintext)
    outfile = open('solution04.txt' ,'w')
    outfile.write('key:')
    outfile.write(str(key))
    outfile.write('\n')
    outfile.write('plaintext: ')
    outfile.write(plaintext)
