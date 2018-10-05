def xor(hex1, hex2):
    """
       MISSING DESCRIPTION
    """
    answer = hex(int(hex1,16) ^ int(hex2,16))
    answer = answer.replace('L', '').replace('0x', '')
    answer = answer.zfill(len(hex1))
    return answer
