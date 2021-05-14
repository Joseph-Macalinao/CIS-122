def pig_latin(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if string[0] not in vowel:
        if string[1] not in vowel:
            return string[2:] + (string[0] + string[1]) + 'ay'
        elif string[1] in vowel:
            return string[1:] + string[0] + 'ay'
    elif string[0] in vowel:
        return string + 'way'

def pig_sentence(sent):
    sentence = ''
    for word in sent.split():
        sentence += pig_latin(word) + ' '
    return sentence


print(pig_sentence('shamrock farms'))