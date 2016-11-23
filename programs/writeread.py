fp=open('text.txt','r')
for l in fp:
  print l,
fp.close()

fp = open('text.txt','w')
while True:
    text = raw_input('Enter text (end with blank):')
    if len(text)==0:
        break
    else:
        fp.write(text+'\n')
fp.close()


nfile='doesnotexist.txt'
fp=open(nfile,'r')
try:
    fp=open(nfile,'r')
except:
    print'Cannot open',nfile,'for reading. Does not exist'


    

fp=open('tempfile.txt','w')
# for i=
fp.close()