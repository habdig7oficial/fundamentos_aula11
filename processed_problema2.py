from string import ascii_lowercase as ascii_letters 

correspondency = {} 
for letter, i in zip(ascii_letters, range(len(ascii_letters))): 
	correspondency[letter] = i 
	print(f"{letter} - {i}") 


correspondency[" "] = len(ascii_letters) 

print(correspondency) 


def to_cypher(x, a, b, n): 
	return ((a * x + b) % n) 


def to_text(c, a, b, n): 
	return ((a * (c - b)) % n) 



def encrypt(msg: str, a: int, b: int, chartype ): 
	cypher_arr = [] 
	cyphertext = [] 
	for i in msg: 
		print(chartype[i]) 
		cypher_letter = to_cypher(chartype[i], a, b, len(chartype)) 
		cypher_arr.append(cypher_letter) 
		print("----") 
		cyphertext.append(list(chartype.keys())[list(chartype.values()).index(cypher_letter)]) 


	return "".join(cyphertext) 


def decrypt(cypher, a, b, chartype ): 
	char_arr = [] 
	text = [] 
	for i in cypher: 
		char = to_text(chartype[i], a, b, len(chartype)) 
		char_arr.append(char) 
		text.append(list(chartype.keys())[list(chartype.values()).index(char)]) 

	print(text) 
	return "".join(text) 



teste = encrypt("hoje", a = 7, b = 3, chartype = correspondency) 
print(teste) 

#inversa da classe mod n 
teste2 = decrypt(teste, a = 4, b = 3, chartype = correspondency) 

print(teste2) 
