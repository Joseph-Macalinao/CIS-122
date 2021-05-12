from cis122_assign06_shared import pad_left, pad_right


def file():
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
    print(f'Count: {total_num}')
    print(f'Comments: {total_hash}')
    print(f'Total: {total}')
    print(f'Average: {avg}')
    na.close()
file()