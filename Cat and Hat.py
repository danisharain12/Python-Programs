# Return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
# Note: str contains only lowercase English alphabets
----------------------------------------------------------------------------------------------------------------------------------------------

def cat_hat(str):
    if str.count('cat') == str.count('hat'):
        return True
    else:
        return False
