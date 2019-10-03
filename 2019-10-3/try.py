word2 ="hello"
word3=""
z=len(word2)-1
for i in range(0,len(word2)):
	word3 = word3+word2[(z-i)-len(word2)]
print (word3)