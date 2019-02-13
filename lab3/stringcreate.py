from subprocess import call
 
s=call('openssl dgst -md5 file0',shell=True)
fi=open('write.txt','w')
fi.write(s)
