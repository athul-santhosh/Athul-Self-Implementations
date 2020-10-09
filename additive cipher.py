# additive cipher 

def additive_cipher(s,key):
	m = []
	# plain text to alpha values
	for i in s:
		c = ord(i) - ord('a')
		if c == -65:
			m.append(" ")
		else:
			m.append(c)
	print(m)
	result = []
	for i in m:
		if i == " ":
			result.append(" ")
		else:
			cipher = (int(i) + key) % 26
			#print(("( {} + 20 ) % 26 = {}").format(i,cipher)) 
			result.append(cipher)
	print(result)
	final_result = ""
	for i in result:
		if i == " ":
			final_result += " "
		else:
			final_result += chr(i+ord("a"))
	print(final_result)

 


additive_cipher("this is an exercise",20)