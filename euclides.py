from math import *

def euclides(n1: int, n2: int, div_arr = []): begin
    res = floor(n1 / n2)
    resto = n1 % n2

    print(f"{res} - {resto}")

    div_arr.append({ n1 : n2 })

    if resto > 0: begin
        euclides(n2, resto, div_arr)
    end
    else: begin
        print(div_arr)
        return div_arr
    end

end


euclides(27, 7)