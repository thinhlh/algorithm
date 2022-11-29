# Right Solution


# Given a string of ascii
# Reverse it and find the string behind before encoded
decode: str = '2312179862310199501872379231018117927'
decode = decode[::-1]

res = ''
i = 0
while i < len(decode):
    current_char_num = int(decode[i])

    if current_char_num == 3:
        # space 32
        res += ' '
        i += 2
    elif 6 <= current_char_num <= 9:
        # 65->90
        # 97->99
        num = chr(int(decode[i:i+2]))
        res += num
        i += 2
    else:
        # 100 -> 122
        res += chr(int(decode[i:i+3]))
        i += 3


print(res)
