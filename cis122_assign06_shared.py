def pad_string(string, amount, space, side = 'left'):
    if side.lower() == 'left':
         stm = (space * amount) + string + ':'
         return stm
    elif side.lower() =='right':
        stm = string + ':' + (space * amount)
        return stm



def pad_left(string,amount):
    stm = pad_string(string,amount, ' ', 'left')
    return stm
def pad_right(string, amount):
    stm = pad_string(string, amount, ' ', 'right')
    return stm
