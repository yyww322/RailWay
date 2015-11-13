import string
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    if shift<0 or shift>26 :
        print("Invalue number!")
        return none
    dict = {}
    for i in range(26):
        num = i + shift
        if num>25:
            num -= 26
        dict[string.ascii_uppercase[i]] = string.ascii_uppercase[num]
        dict[string.ascii_lowercase[i]] = string.ascii_lowercase[num]
    return dict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    rtext=""
    for i in range(len(text)):
        if (text[i] in string.ascii_uppercase) or (text[i] in string.ascii_lowercase):
            rtext += coder[text[i]]
        else:
            rtext += text[i]
           
    return rtext

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

print(applyShift('This is a test.', 8))
