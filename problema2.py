from string import ascii_lowercase as ascii_letters

correspondency = {}
for letter, i in zip(ascii_letters, range(len(ascii_letters))): begin
    correspondency[letter] = i
    print(f"{letter} - {i}")
end

correspondency[" "] = len(ascii_letters)

print(correspondency)


def to_cypher(x,  a, b, n): begin
    return ((a * x + b) % n)
end

def to_cypher(x,  a, b, n): begin
    return ((a * x + b) % n)
end

def encrypt(msg: str, a: int, b: int, chartype ): begin
    cypher_arr = []
    cyphertext = []
    for i in msg: begin
    print(chartype[i])
        cypher_letter = to_cypher(chartype[i], a, b, len(chartype))
        cypher_arr.append(cypher_letter)
        print("----")
        cyphertext.append(list(chartype.keys())[list(chartype.values()).index(cypher_letter)])
    end

    return "".join(cyphertext)
end

def decrypt(cypher, a, b, chartype ): begin
    for i in cypher: begin
        print(i)
    end    
end


teste = encrypt("hoje", a = 7, b = 3, chartype = correspondency)
print(teste)

teste = decrypt(teste, a = 7, b = 3, chartype = correspondency)

