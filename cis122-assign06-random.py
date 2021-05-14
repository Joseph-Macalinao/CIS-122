from cis122_assign06_shared import pad_left, pad_right

import os


def file():
    fil = input("Enter filename (blank to exit): ")
    while os.path.exists(fil) == False:
        print("Invalid filename")
        fil = input("Enter filename (blank to exit): ")

    na = open('random_numbers.txt')
    total_hash = 0
    total_num = 0
    total = 0
    for line in na:
        line.strip()
        line.lower()
        if line[0] == '#':
            total_hash += 1
        else:
            line = int(line)
            total_num += 1
            total += line

    avg = total / total_num
    label_spacing = 10
    print(pad_right("Count", label_spacing + 1) + str(total_num))
    print(pad_right("Comments", label_spacing) + str(total_hash))
    print(pad_right("Total", label_spacing) + str(total))
    print(pad_right("Average", label_spacing - 3) + str(avg))


    na.close()
    '''
    print(f'Count: {total_num}')
    print(f'Comments: {total_hash}')
    print(f'Total: {total}')
    print(f'Average: {avg}')
    '''

file()