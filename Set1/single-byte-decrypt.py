def single_byte_decrypt(string):
    """
       MISSING DESCRIPTION
    """
    valid = '0123456789abcdef'
    all_valid = []
    good_chars = 'abcdefghijklmnopqrstuvwxyz'
    good_chars = good_chars.upper() + '0123456789,.?! @#$%^&*()_-=+'

    for i in valid:
        for j in valid:
            all_valid.append(i+j)
    finals = []

    for c in all_valid:
        result = xor(c, string[0])
        dec = int(result,16)
        if (dec >= 97 and dec <= 122) or (dec >= 65 and dec <= 90):
            temp = repeating_key_xor(string, c).decode("hex")
            space = temp.split(' ')
            if len(space) > 3:
                finals.append([temp,c])
    if len(finals) == 0:
        return None, None
    if len(finals) > 1:
        print "WARNING!!"
    return finals[0]
