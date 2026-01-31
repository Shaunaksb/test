def permute(chars, i, length):
    if i==length:
        print("".join(chars))
    else:
        for j in range(i,length):
            chars[i], chars[j] = chars[j], chars[i]
            permute(chars, i+1, length)
            chars[i], chars[j] = chars[j], chars[i] 

s="abc"
chars=list(s)
length = len(s)
permute(chars, 0, length)