p = 41
q = 3
n = p*q
e = 3
r = (p-1) * (q-1)
M = 99
print("Message: " + str(M))


encrypted_msg = (M ** e) % n
print("Encrypted Message: " + str(encrypted_msg))

def egcd(a, b):
	if a==0:
		return (b, 0, 1)
	g, y, x = egcd(b%a, a)
	return (g, x-(b/a) * y, y)

def mulinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		print('No modular inverse')
	return x%m 


d = mulinv(e, r)
print("D" + str(d))


decrypted_msg = (encrypted_msg ** d) % n
print("Decrypted Message: " + str(decrypted_msg))


