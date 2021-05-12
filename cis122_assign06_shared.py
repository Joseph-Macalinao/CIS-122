def pad_string(string, amount, space, side = 'left'):
    if side.lower() == 'left':
         print((space * amount) + string + ':')
    elif side.lower() =='right':
        print(string + ':' + (space * amount))



def pad_left(string,amount):
    pad_string(string,amount, ' ', 'left')

def pad_right(string, amount):
    pad_string(string, amount, ' ', 'right')

pad_right('count', 10)
