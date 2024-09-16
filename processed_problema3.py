from string import ascii_lowercase 


#zebedfgh1jkinmypqrutswwxoa 
#key = "zcbedfghljkinmypqrutsxwxoa" 
#cyphertext = "bzedzeymziluz" 

key = "iohmunlcawygdfbqpvxzerjskt" 
cyphertext = "haufhaimihbdgezihib" 

correspondency = {} 
for letter, i in zip(ascii_lowercase, key): 
	correspondency[i] = letter 


print(correspondency) 

msg_arr = [] 
for cypherletter in cyphertext: 
	msg_arr.append(correspondency[cypherletter]) 


msg = "".join(msg_arr) 
print(msg) 
