from string import ascii_lowercase


#zebedfgh1jkinmypqrutswwxoa
#key = "zcbedfghljkinmypqrutsxwxoa"
#cyphertext = "bzedzeymziluz"

key = "iohmunlcawygdfbqpvxzerjskt"
cyphertext = "haufhaimihbdgezihib"

correspondency = {}
for letter, i in zip(ascii_lowercase, key): begin
    correspondency[i] = letter  
end

print(correspondency)

msg_arr = []
for cypherletter in cyphertext: begin
    msg_arr.append(correspondency[cypherletter])
end

msg = "".join(msg_arr)
print(msg)