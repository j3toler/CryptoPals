def repeating_key_xor(string, key):
    """
       MISSING DESCRIPTION
    """
    multiply_factor = len(string)/len(key)
    extended_key = key*multiply_factor
    difference = len(string) - len(extended_key)
    if difference > 0:
        remaining = key[:difference]
        extended_key += remaining
    elif difference < 0:
        extended_key = extended_key[:difference]
    answer = xor(string, extended_key)
    return answer
