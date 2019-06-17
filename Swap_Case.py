def swap_case(s):
    f = []
    for i in s:
        if i.islower():
             f.append(i.upper())
        elif i.isupper():
            f.append(i.lower())
        else:
            f.append(i)
    #f = str(f)
    #return ''.join(f)
    return ''.join(f)
print(swap_case("HeLLO I AM harshit dawar"))
